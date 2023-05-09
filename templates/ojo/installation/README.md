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
  -e 's|^pruning *=.*|pruning = "custom"|' \
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

# Set up Price Feeder
{% hint style="warning" %}
To run pricefeeder you validator should be in active set. Otherwise price feeder will not vote on periods.
{% endhint %}

### Install the pricefeeder binary and create directory for pricefeeder configuration 
```bash
cd $HOME && rm price-feeder -rf
git clone https://github.com/ojo-network/price-feeder
cd price-feeder
git checkout v0.1.1
make build
sudo mv ./build/price-feeder /usr/local/bin
rm $HOME/.ojo-price-feeder -rf
mkdir $HOME/.ojo-price-feeder
mv price-feeder.example.toml $HOME/.ojo-price-feeder/config.toml
```

### Check price-feeder version
```bash
price-feeder version
# version: HEAD-5d46ed438d33d7904c0d947ebc6a3dd48ce0de59
# commit: 5d46ed438d33d7904c0d947ebc6a3dd48ce0de59
```

### Create new wallet for pricefeeder and save `24 word mnemonic phrase`
```bash
ojod keys add pricefeeder-wallet --keyring-backend os
```

### Export keyring password
```
 export KEYRING_PASSWORD="PRICE_FEEDER_KEY_PASSWORD_GOES_HERE"
```

### Set up variables
```
export KEYRING="os"
export LISTEN_PORT=7172
export RPC_PORT=${CHAIN_PORT}57
export GRPC_PORT=${CHAIN_PORT}90
export VALIDATOR_ADDRESS=$(ojod keys show wallet --bech val -a)
export MAIN_WALLET_ADDRESS=$(ojod keys show wallet -a)
export PRICEFEEDER_ADDRESS=$(echo -e $KEYRING_PASSWORD | ojod keys show pricefeeder-wallet --keyring-backend os -a)
```

### Fund the pricefeeder-wallet with some testnet tokens.
{% hint style="info" %}
In order to make pricefeeder work, it needs some tokens to pay for transaction fees
{% endhint %}

This command will send `1 OJO` to `pricefeeder-wallet` from you main `wallet`
```
ojod tx bank send wallet $PRICEFEEDER_ADDRESS 1000000uojo --from wallet --chain-id ojo-devnet --gas-adjustment 1.4 --gas auto --gas-prices 0uojo -y
```

Check the balance
```
ojod q bank balances $PRICEFEEDER_ADDRESS
```

### Delegate pricefeeder responsibility

{% hint style="info" %}
As a validator, if you'd like another account to post prices on your behalf (i.e. you don't want your validator mnemonic sending txs), you can delegate pricefeeder responsibilities to another address.
{% endhint %}

```bash
ojod tx oracle delegate-feed-consent $MAIN_WALLET_ADDRESS $PRICEFEEDER_ADDRESS --from wallet --gas-adjustment 1.4 --gas auto --gas-prices 0uojo -y
```

Check linked pricefeeder address
```
ojod q oracle feeder-delegation $VALIDATOR_ADDRESS
```

### Set pricefeeder configuration values
```
sed -i "s/^listen_addr *=.*/listen_addr = \"0.0.0.0:${LISTEN_PORT}\"/;\
s/^address *=.*/address = \"$PRICEFEEDER_ADDRESS\"/;\
s/^chain_id *=.*/chain_id = \"${CHAIN_ID}\"/;\
s/^validator *=.*/validator = \"$VALIDATOR_ADDRESS\"/;\
s/^backend *=.*/backend = \"$KEYRING\"/;\
s|^dir *=.*|dir = \"$HOME/${CHAIN_DIR}\"|;\
s|^grpc_endpoint *=.*|grpc_endpoint = \"localhost:${GRPC_PORT}\"|;\
s|^tmrpc_endpoint *=.*|tmrpc_endpoint = \"http://localhost:${RPC_PORT}\"|;\
s|^global-labels *=.*|global-labels = [[\"chain_id\", \"${CHAIN_ID}\"]]|;\
s|^service-name *=.*|service-name = \"ojo-price-feeder\"|;" $HOME/.ojo-price-feeder/config.toml
```

### Setup the systemd service
```bash
sudo tee /etc/systemd/system/ojo-price-feeder.service > /dev/null <<EOF
[Unit]
Description=Ojo Price Feeder
After=network-online.target

[Service]
User=$USER
ExecStart=$(which price-feeder) $HOME/.ojo-price-feeder/config.toml
Restart=on-failure
RestartSec=30
LimitNOFILE=65535
Environment="PRICE_FEEDER_PASS=$KEYRING_PASSWORD"

[Install]
WantedBy=multi-user.target
EOF
```

### Register and start the systemd service
```bash
sudo systemctl daemon-reload
sudo systemctl enable ojo-price-feeder
sudo systemctl restart ojo-price-feeder
```

### View pricefeeder logs
```bash
journalctl -fu ojo-price-feeder -o cat
```

Successfull Log examples:
```
10:30AM INF broadcasting vote exchange_rates=ATOM:11.449658317452328488,BNB:286.505174071110084991,CRO:0.069718618570227407,DAI:0.999872679370903845,ETH:1552.960176513619371601,IST:1.013970239583170325,OSMO:0.826831324620249729,UMEE:0.007902144939292575,USDC:0.999873169363824893,USDT:0.999851633546200939,WBTC:22001.354045277520185398,stATOM:12.378471944671440576,stOSMO:0.869546768297473244 feeder=ojo1akr5mgltsde7lke3cgxwf2pcug3rnyfy67dl6p module=oracle validator=ojovaloper1mfasrshu4k0wlksvgjyvahe7hz67sw4z0pst3f
10:30AM INF successfully broadcasted tx module=oracle_client tx_code=0 tx_hash=354B62AC58F370F6E866F019A7C14E93E456F6A1355AFE92B915DABCF4C89C86 tx_height=0
10:30AM INF broadcasting pre-vote feeder=ojo1akr5mgltsde7lke3cgxwf2pcug3rnyfy67dl6p hash=9fefb35d3499ce13339c37b65e5fa79b898c1d09 module=oracle validator=ojovaloper1mfasrshu4k0wlksvgjyvahe7hz67sw4z0pst3f
10:30AM INF successfully broadcasted tx module=oracle_client tx_code=0 tx_hash=8E918F16931972681A5CC8C1E0F3E082561D8899DD672D5FA6D943FC81E8179A tx_height=0
10:31AM INF skipping until next voting period current_vote_period=64750 module=oracle previous_vote_period=64750 vote_period=5
10:31AM INF skipping until next voting period current_vote_period=64750 module=oracle previous_vote_period=64750 vote_period=5
```

Also you can check that your pricefeeder-wallet is doing transactions on chain at [Chain Explorer](https://explorer.kjnodes.com/ojo-testnet)
<figure><img src="https://i.ibb.co/748MW95/pricefeeder-transactions.png" alt=""><figcaption><p>Price Feeder Transactions</p></figcaption></figure>

### Useful commands
Check current voting windows progress
```
ojod q oracle slash-window
```

Check missed oracle votes per slashing window
```
ojod q oracle miss-counter $VALIDATOR_ADDRESS
```

Special thanks to `mzonder#5844` and `zoia queen#7436`
