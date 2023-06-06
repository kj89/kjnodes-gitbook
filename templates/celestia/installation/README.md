---
description: Setting up your validator node has never been so easy. Get your validator running in minutes by following step by step instructions.
---

# Installation

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/${PROJECT_NAME}.png" alt=""><figcaption></figcaption></figure>

**Chain ID**: ${CHAIN_ID} | **Latest Version Tag**: ${LATEST_VERSION_TAG} | **Custom Port**: ${CHAIN_PORT}

### Setup validator name

{% hint style='info' %}
Replace **YOUR_MONIKER_GOES_HERE** with your validator name
{% endhint %}

```bash
MONIKER="YOUR_MONIKER_GOES_HERE"
```

### Install dependencies

#### Update system and install build tools

```bash
sudo apt -q update
sudo apt -qy install curl git jq lz4 build-essential
sudo apt -qy upgrade
```

#### Install Go

```bash
sudo rm -rf /usr/local/go
curl -Ls https://go.dev/dl/go${GO_VERSION}.linux-amd64.tar.gz | sudo tar -xzf - -C /usr/local
eval $(echo 'export PATH=$PATH:/usr/local/go/bin' | sudo tee /etc/profile.d/golang.sh)
eval $(echo 'export PATH=$PATH:$HOME/go/bin' | tee -a $HOME/.profile)
```

### Download and build binaries

```bash
# Clone project repository
cd $HOME
rm -rf ${GIT_DIR}
git clone ${GIT_URL}
cd ${GIT_DIR}
git checkout ${LATEST_VERSION_TAG}

# Build binaries
make build

# Prepare binaries for Cosmovisor
mkdir -p $HOME/${CHAIN_DIR}/cosmovisor/genesis/bin
mv ${CHAIN_BINARY_SRC} $HOME/${CHAIN_DIR}/cosmovisor/genesis/bin/
rm -rf build

# Create application symlinks
sudo ln -s $HOME/${CHAIN_DIR}/cosmovisor/genesis $HOME/${CHAIN_DIR}/cosmovisor/current -f
sudo ln -s $HOME/${CHAIN_DIR}/cosmovisor/current/bin/${CHAIN_APP} /usr/local/bin/${CHAIN_APP} -f
```

### Install Cosmovisor and create a service

```bash
# Download and install Cosmovisor
go install cosmossdk.io/tools/cosmovisor/cmd/cosmovisor@v${COSMOVISOR_VERSION}

# Create service
sudo tee /etc/systemd/system/${CHAIN_APP}.service > /dev/null << EOF
[Unit]
Description=${CHAIN_NAME} node service
After=network-online.target

[Service]
User=$USER
ExecStart=$(which cosmovisor) run start
Restart=on-failure
RestartSec=10
LimitNOFILE=65535
Environment="DAEMON_HOME=$HOME/${CHAIN_DIR}"
Environment="DAEMON_NAME=${CHAIN_APP}"
Environment="UNSAFE_SKIP_BACKUP=true"
Environment="PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:$HOME/${CHAIN_DIR}/cosmovisor/current/bin"

[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable ${CHAIN_APP}
```

### Initialize the node

```bash
# Set node configuration
${CHAIN_APP} config chain-id ${CHAIN_ID}
${CHAIN_APP} config keyring-backend ${KEYRING_BACKEND}
${CHAIN_APP} config node tcp://localhost:${CHAIN_PORT}57

# Initialize the node
${CHAIN_APP} init $MONIKER --chain-id ${CHAIN_ID}

# Download genesis and addrbook
curl -Ls https://snapshots.kjnodes.com/${CHAIN_NAME}/genesis.json > $HOME/${CHAIN_DIR}/config/genesis.json
curl -Ls https://snapshots.kjnodes.com/${CHAIN_NAME}/addrbook.json > $HOME/${CHAIN_DIR}/config/addrbook.json

# Add seeds
sed -i -e "s|^seeds *=.*|seeds = \"${CHAIN_TENDERSEED_PEER}@${CHAIN_NAME}.rpc.kjnodes.com:${CHAIN_PORT}59\"|" $HOME/${CHAIN_DIR}/config/config.toml

# Set minimum gas price
sed -i -e "s|^minimum-gas-prices *=.*|minimum-gas-prices = \"${MIN_GAS_PRICE}\"|" $HOME/${CHAIN_DIR}/config/app.toml

# Set pruning
sed -i \
  -e 's|^pruning *=.*|pruning = "nothing"|' \
  -e 's|^pruning-keep-recent *=.*|pruning-keep-recent = "100"|' \
  -e 's|^pruning-keep-every *=.*|pruning-keep-every = "0"|' \
  -e 's|^pruning-interval *=.*|pruning-interval = "19"|' \
  $HOME/${CHAIN_DIR}/config/app.toml

# Set custom ports
sed -i -e "s%^proxy_app = \"tcp://127.0.0.1:26658\"%proxy_app = \"tcp://127.0.0.1:${CHAIN_PORT}58\"%; s%^laddr = \"tcp://127.0.0.1:26657\"%laddr = \"tcp://127.0.0.1:${CHAIN_PORT}57\"%; s%^pprof_laddr = \"localhost:6060\"%pprof_laddr = \"localhost:${CHAIN_PORT}60\"%; s%^laddr = \"tcp://0.0.0.0:26656\"%laddr = \"tcp://0.0.0.0:${CHAIN_PORT}56\"%; s%^prometheus_listen_addr = \":26660\"%prometheus_listen_addr = \":${CHAIN_PORT}66\"%" $HOME/${CHAIN_DIR}/config/config.toml
sed -i -e "s%^address = \"tcp://0.0.0.0:1317\"%address = \"tcp://0.0.0.0:${CHAIN_PORT}17\"%; s%^address = \":8080\"%address = \":${CHAIN_PORT}80\"%; s%^address = \"0.0.0.0:9090\"%address = \"0.0.0.0:${CHAIN_PORT}90\"%; s%^address = \"0.0.0.0:9091\"%address = \"0.0.0.0:${CHAIN_PORT}91\"%; s%:8545%:${CHAIN_PORT}45%; s%:8546%:${CHAIN_PORT}46%; s%:6065%:${CHAIN_PORT}65%" $HOME/${CHAIN_DIR}/config/app.toml
```

### Download latest chain snapshot

```bash
curl -L https://snapshots.kjnodes.com/${CHAIN_NAME}/snapshot_latest.tar.lz4 | tar -Ilz4 -xf - -C $HOME/${CHAIN_DIR}
[[ -f $HOME/${CHAIN_DIR}/data/upgrade-info.json ]] && cp $HOME/${CHAIN_DIR}/data/upgrade-info.json $HOME/${CHAIN_DIR}/cosmovisor/genesis/upgrade-info.json
```

### Start service and check the logs

```bash
sudo systemctl start ${CHAIN_APP} && sudo journalctl -u ${CHAIN_APP} -f --no-hostname -o cat
```

# Install Bridge Node

### Download and build binaries
```bash
cd $HOME 
rm -rf celestia-node 
git clone https://github.com/celestiaorg/celestia-node.git 
cd celestia-node
git checkout v0.10.4
make build
sudo mv build/celestia /usr/local/bin
make cel-key
sudo mv cel-key /usr/local/bin
```

### Add Bridge wallet

#### Generate new wallet

```bash
cel-key add bridge-wallet --node.type bridge --p2p.network blockspacerace
```

#### Recover existing wallet
```bash
cel-key add bridge-wallet --node.type bridge --p2p.network blockspacerace --recover
```

### Fund the wallet with testnet tokens
{% hint style='info' %}
Once you start the Bridge Node, a wallet key will be generated for you. You will need to fund that address with Testnet tokens to pay for PayForBlob transactions
{% endhint %}

### Initialize Bridge node
```bash
celestia bridge init \
  --keyring.accname bridge-wallet \
  --core.ip http://localhost \
  --core.rpc.port ${CHAIN_PORT}57 \
  --core.grpc.port ${CHAIN_PORT}90 \
  --p2p.network blockspacerace \
  --rpc.port ${CHAIN_PORT}58 \
  --gateway.port ${CHAIN_PORT}59
```

### Create service
```bash
sudo tee /etc/systemd/system/celestia-bridge.service > /dev/null << EOF
[Unit]
Description=Celestia Bridge Node service
After=network-online.target

[Service]
User=$USER
ExecStart=$(which celestia) bridge start \\
--keyring.accname bridge-wallet \\
--core.ip http://localhost \\
--core.rpc.port ${CHAIN_PORT}57 \\
--core.grpc.port ${CHAIN_PORT}90 \\
--p2p.network blockspacerace \\
--rpc.port ${CHAIN_PORT}58 \\
--gateway.port ${CHAIN_PORT}59 \\
--metrics.tls=false \\
--metrics \\
--metrics.endpoint otel.celestia.tools:4318 
Restart=on-failure
RestartSec=10
LimitNOFILE=65535

[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable celestia-bridge
```

### Start Bridge node
```bash
systemctl restart celestia-bridge
```

### Check Bridge node logs
```bash
journalctl -fu celestia-bridge -o cat
```

## Useful commands

### Get Bridge Node ID
```bash
AUTH_TOKEN=$(celestia bridge auth admin --p2p.network blockspacerace)
curl -s -X POST -H "Authorization: Bearer $AUTH_TOKEN" -H 'Content-Type: application/json' -d '{"jsonrpc":"2.0","id":0,"method":"p2p.Info","params":[]}' http://localhost:${CHAIN_PORT}58 | jq -r .result.ID
```

### Get Bridge node key
```bash
cel-key show bridge-wallet --node.type bridge --p2p.network blockspacerace -a | tail -1
```

### Check Bridge node wallet balance
```bash
celestia-appd q bank balances $(cel-key show bridge-wallet --node.type bridge --p2p.network blockspacerace -a | tail -1)
```

# Upgrade Bridge Node

### Stop Bridge node
```
sudo systemctl stop celestia-bridge
```

### Download and build binaries
```bash
cd $HOME 
rm -rf celestia-node 
git clone https://github.com/celestiaorg/celestia-node.git 
cd celestia-node
git checkout v0.10.4
make build
sudo mv build/celestia /usr/local/bin
make cel-key
sudo mv cel-key /usr/local/bin
```

### Check Bridge node version
```
celestia version
```

### Node upgrade
To upgrade Celestia Bridge node you have two options

#### (OPTION 1) Soft upgrade
{% hint style="info" %}
This option will only update attributes of configuration files without deleting any data.
{% endhint %}

Update configuration file
```
celestia bridge config-update --p2p.network blockspacerace
```

#### (OPTION 2) Hard upgrade
{% hint style="warning" %}
This option will clear data store and re-initialize the node. Keys will not be deleted.
{% endhint %}

Clear data store and remove configuration file
```
celestia bridge unsafe-reset-store --p2p.network blockspacerace
rm -rf $HOME/.celestia-bridge-blockspacerace-0/config.toml
```

Initialize Bridge node
```
celestia bridge init \
  --keyring.accname bridge-wallet \
  --core.ip localhost \
  --core.rpc.port ${CHAIN_PORT}57 \
  --core.grpc.port ${CHAIN_PORT}90 \
  --p2p.network blockspacerace \
  --rpc.port ${CHAIN_PORT}58 \
  --gateway.port ${CHAIN_PORT}59
```

### Start Bridge node
```
sudo systemctl start celestia-bridge
```

### Check Bridge node logs
```bash
journalctl -fu celestia-bridge -o cat
```

# Install Orchestrator

### Download and build binaries
```bash
cd $HOME 
rm -rf orchestrator-relayer
git clone https://github.com/celestiaorg/orchestrator-relayer.git
cd orchestrator-relayer
git checkout v0.2.0-app-v0.13.2-beta 
make build
sudo mv build/qgb /usr/local/bin
```

### Initialize Orchestrator node
```bash
qgb orchestrator init
```

### Add Orchestrator EVM wallet
The EVM private key needs to correspond to the EVM address provided when creating the validator.

#### Import EVM wallet private key
```bash
qgb orchestrator keys evm import ecdsa <private key in hex format>
```

### Create service
```bash
sudo tee /etc/systemd/system/celestia-orchestrator.service > /dev/null << EOF
[Unit]
Description=Celestia Orchestrator service
After=network-online.target

[Service]
User=$USER
ExecStart=$(which qgb) orchestrator start \\
--celes-grpc <GRPC_ENDPOINT> \\
--celes-rpc <RPC_ENDPOINT> \\
--evm-address <EVM_ADDRESS> \\
--evm-passphrase <EVM_PASSPHRASE> \\
--p2p-bootstrappers /dns/bootstr-incent-1.celestia.tools/tcp/30000/p2p/12D3KooWSGZ2LXW2soQFHgU82uLfN7pNW5gMMkTnu1fhMXG43TvP
Restart=on-failure
RestartSec=10
LimitNOFILE=65535

[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable celestia-orchestrator
```

Example of service execution command
```
ExecStart=$(which qgb) orchestrator start \\
--celes-grpc localhost:12090 \\
--celes-rpc http://localhost:12057 \\
--evm-address 0x0bd244CcD11892232G990a7b7F37F68042952f42 \\
--evm-passphrase mypassphrasegoeshere \\
--p2p-bootstrappers /dns/bootstr-incent-1.celestia.tools/tcp/30000/p2p/12D3KooWSGZ2LXW2soQFHgU82uLfN7pNW5gMMkTnu1fhMXG43TvP
```

{% hint style="info" %}
Before running the orchestrator, make sure to have the indexing enabled on your RPC node. If the indexer was just activated, then, by default, it will not have the previous transactions indexed. 
And, if you run the orchestrator at the same time, it will try to create the commitments and will fail as the transactions are not indexed.
{% endhint %}

### Start Orchestrator node
```bash
systemctl restart celestia-orchestrator
```

### Check Bridge node logs
```bash
journalctl -fu celestia-orchestrator -o cat
```

## Useful commands

### View validator details
Check the `evm_address` field if it has an address that you want to use to sign attestations.
```bash
celestia-appd q staking validator $(celestia-appd keys show wallet --bech val -a)
```

### Change validator evm_address
```
celestia-appd tx staking edit-validator --evm-address=<NEW_EVM_ADDRESS> --from=wallet --chain-id blockspacerace-0 --gas-adjustment 1.4 --gas auto --gas-prices 0.005utia -y
```
