---
description: Setting up your validator node has never been so easy. Get your validator running in minutes by following step by step instructions.
---

# Installation

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/${PROJECT_NAME}.png" width="150" alt=""><figcaption></figcaption></figure>

**Chain ID**: ${CHAIN_ID} | **Latest Version Tag**: ${LATEST_VERSION_TAG} | **Custom Port**: ${CHAIN_PORT}

### Setup validator name

{% hint style='info' %}
Replace **YOUR_MONIKER_GOES_HERE** with your validator name
{% endhint %}

```bash
MONIKER="YOUR_MONIKER_GOES_HERE"
```

### Install dependencies

#### Add package repository for Node.js

```bash
curl -Ls https://deb.nodesource.com/setup_16.x | sudo bash
```

#### Add package repository for Yarn

```bash
curl -Ls https://dl.yarnpkg.com/debian/pubkey.gpg | gpg --dearmor | sudo tee /usr/share/keyrings/yarnkey.gpg >/dev/null
echo "deb [signed-by=/usr/share/keyrings/yarnkey.gpg] https://dl.yarnpkg.com/debian stable main" | sudo tee /etc/apt/sources.list.d/yarn.list
```

#### Update system and install build tools

```bash
sudo apt -q update
sudo apt -qy install curl git jq lz4 build-essential nodejs=16.* yarn
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
rm -rf ${LATEST_VERSION_TAG}
git clone ${GIT_URL} ${LATEST_VERSION_TAG}
cd ${LATEST_VERSION_TAG}
git checkout ${LATEST_VERSION_TAG}

# Install and build Agoric Javascript packages
yarn install && yarn build

# Install and build Agoric Cosmos SDK support
(cd packages/cosmic-swingset && make)

# Prepare binaries for Cosmovisor
mkdir -p $HOME/${CHAIN_DIR}/cosmovisor/genesis/bin
ln -s $HOME/${LATEST_VERSION_TAG}/packages/cosmic-swingset/bin/ag-chain-cosmos $HOME/${CHAIN_DIR}/cosmovisor/genesis/bin/ag-chain-cosmos
ln -s $HOME/${LATEST_VERSION_TAG}/packages/cosmic-swingset/bin/ag-nchainz $HOME/${CHAIN_DIR}/cosmovisor/genesis/bin/ag-nchainz
cp golang/cosmos/build/agd $HOME/${CHAIN_DIR}/cosmovisor/genesis/bin/
cp golang/cosmos/build/ag-cosmos-helper $HOME/${CHAIN_DIR}/cosmovisor/genesis/bin/

# Create application symlinks
ln -s $HOME/${CHAIN_DIR}/cosmovisor/genesis $HOME/${CHAIN_DIR}/cosmovisor/current
sudo ln -s $HOME/${CHAIN_DIR}/cosmovisor/current/bin/${CHAIN_APP} /usr/local/bin/${CHAIN_APP}
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
Environment="PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:$HOME/.agoric/cosmovisor/current/bin"

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
${CHAIN_APP} config node tcp://localhost:${CHAIN_PORT}657

# Initialize the node
${CHAIN_APP} init $MONIKER --chain-id ${CHAIN_ID}

# Download genesis and addrbook
curl -Ls https://snapshots.kjnodes.com/${CHAIN_NAME}/genesis.json > $HOME/${CHAIN_DIR}/config/genesis.json
curl -Ls https://snapshots.kjnodes.com/${CHAIN_NAME}/addrbook.json > $HOME/${CHAIN_DIR}/config/addrbook.json

# Add seeds
sed -i -e "s|^seeds *=.*|seeds = \"${CHAIN_TENDERSEED_PEER}@${CHAIN_NAME}.rpc.kjnodes.com:${CHAIN_PORT}659\"|" $HOME/${CHAIN_DIR}/config/config.toml

# Set minimum gas price
sed -i -e "s|^minimum-gas-prices *=.*|minimum-gas-prices = \"${MIN_GAS_PRICE}\"|" $HOME/${CHAIN_DIR}/config/app.toml

# Set pruning
sed -i \
  -e 's|^pruning *=.*|pruning = "custom"|' \
  -e 's|^pruning-keep-recent *=.*|pruning-keep-recent = "100"|' \
  -e 's|^pruning-keep-every *=.*|pruning-keep-every = "0"|' \
  -e 's|^pruning-interval *=.*|pruning-interval = "19"|' \
  $HOME/${CHAIN_DIR}/config/app.toml

# Set custom ports
sed -i -e "s%^proxy_app = \"tcp://127.0.0.1:26658\"%proxy_app = \"tcp://127.0.0.1:${CHAIN_PORT}658\"%; s%^laddr = \"tcp://127.0.0.1:26657\"%laddr = \"tcp://127.0.0.1:${CHAIN_PORT}657\"%; s%^pprof_laddr = \"localhost:6060\"%pprof_laddr = \"localhost:${CHAIN_PORT}060\"%; s%^laddr = \"tcp://0.0.0.0:26656\"%laddr = \"tcp://0.0.0.0:${CHAIN_PORT}656\"%; s%^prometheus_listen_addr = \":26660\"%prometheus_listen_addr = \":${CHAIN_PORT}660\"%" $HOME/${CHAIN_DIR}/config/config.toml
sed -i -e "s%^address = \"tcp://0.0.0.0:1317\"%address = \"tcp://0.0.0.0:${CHAIN_PORT}317\"%; s%^address = \":8080\"%address = \":${CHAIN_PORT}080\"%; s%^address = \"0.0.0.0:9090\"%address = \"0.0.0.0:${CHAIN_PORT}090\"%; s%^address = \"0.0.0.0:9091\"%address = \"0.0.0.0:${CHAIN_PORT}091\"%; s%^address = \"0.0.0.0:8545\"%address = \"0.0.0.0:${CHAIN_PORT}545\"%; s%^ws-address = \"0.0.0.0:8546\"%ws-address = \"0.0.0.0:${CHAIN_PORT}546\"%" $HOME/${CHAIN_DIR}/config/app.toml
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
