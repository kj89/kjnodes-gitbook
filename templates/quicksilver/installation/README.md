---
description: Setting up your validator node has never been so easy. Get your validator running in minutes by following step by step instructions.
---

# Installation

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/${PROJECT_NAME}.png" width="150" alt=""><figcaption></figcaption></figure>

**Chain ID**: ${CHAIN_ID} | **Latest Binary Version**: ${LATEST_VERSION_NAME} | **Custom Port**: ${CHAIN_PORT}

### Setup validator name

```bash
MONIKER="YOUR_MONIKER_GOES_HERE"
```

### Install dependencies

#### Update system and install build tools

```bash
sudo apt update
sudo apt install curl git jq lz4 build-essential -y
```

#### Install GO

```bash
sudo rm -rf /usr/local/go
sudo curl -Ls https://go.dev/dl/go1.19.linux-amd64.tar.gz | sudo tar -C /usr/local -xz
tee -a $HOME/.profile > /dev/null << EOF
export PATH=$PATH:/usr/local/go/bin
EOF
source $HOME/.profile
```

### Download and build binaries

```bash
cd $HOME
sudo wget -O /usr/bin/quicksilverd https://github.com/ingenuity-build/testnets/releases/download/v0.10.0/quicksilverd-v0.10.1-amd64
chmod +x /usr/bin/quicksilverd
```

### Create a service

```bash
sudo tee /etc/systemd/system/${CHAIN_APP}.service > /dev/null << EOF
[Unit]
Description=${CHAIN_NAME} node service
After=network-online.target

[Service]
User=$USER
ExecStart=$(which ${CHAIN_APP}) start --home $HOME/${CHAIN_DIR}
Restart=on-failure
RestartSec=3
LimitNOFILE=65535

[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable ${CHAIN_APP}
```

### Initialize the node

```bash
${CHAIN_APP} config chain-id ${CHAIN_ID}
${CHAIN_APP} config keyring-backend ${KEYRING_BACKEND}
${CHAIN_APP} config node tcp://localhost:${CHAIN_PORT}657
${CHAIN_APP} init $MONIKER --chain-id ${CHAIN_ID}
curl -Ls https://snapshots.kjnodes.com/${CHAIN_NAME}/genesis.json > $HOME/${CHAIN_DIR}/config/genesis.json
curl -Ls https://snapshots.kjnodes.com/${CHAIN_NAME}/addrbook.json > $HOME/${CHAIN_DIR}/config/addrbook.json
sed -i -e "s|^seeds *=.*|seeds = \"${CHAIN_TENDERSEED_PEER}@${CHAIN_NAME}.rpc.kjnodes.com:${CHAIN_PORT}659\"|" $HOME/${CHAIN_DIR}/config/config.toml
sed -i -e "s|^minimum-gas-prices *=.*|minimum-gas-prices = \"${MIN_GAS_PRICE}\"|" $HOME/${CHAIN_DIR}/config/app.toml
sed -i -e "s|^pruning *=.*|pruning = \"custom\"|" $HOME/${CHAIN_DIR}/config/app.toml
sed -i -e "s|^pruning-keep-recent *=.*|pruning-keep-recent = \"100\"|" $HOME/${CHAIN_DIR}/config/app.toml
sed -i -e "s|^pruning-keep-every *=.*|pruning-keep-every = \"0\"|" $HOME/${CHAIN_DIR}/config/app.toml
sed -i -e "s|^pruning-interval *=.*|pruning-interval = \"19\"|" $HOME/${CHAIN_DIR}/config/app.toml

sed -i.bak -e "s%^proxy_app = \"tcp://127.0.0.1:26658\"%proxy_app = \"tcp://127.0.0.1:${CHAIN_PORT}658\"%; s%^laddr = \"tcp://127.0.0.1:26657\"%laddr = \"tcp://127.0.0.1:${CHAIN_PORT}657\"%; s%^pprof_laddr = \"localhost:6060\"%pprof_laddr = \"localhost:${CHAIN_PORT}060\"%; s%^laddr = \"tcp://0.0.0.0:26656\"%laddr = \"tcp://0.0.0.0:${CHAIN_PORT}656\"%; s%^prometheus_listen_addr = \":26660\"%prometheus_listen_addr = \":${CHAIN_PORT}660\"%" $HOME/${CHAIN_DIR}/config/config.toml
sed -i.bak -e "s%^address = \"tcp://0.0.0.0:1317\"%address = \"tcp://0.0.0.0:${CHAIN_PORT}317\"%; s%^address = \":8080\"%address = \":${CHAIN_PORT}080\"%; s%^address = \"0.0.0.0:9090\"%address = \"0.0.0.0:${CHAIN_PORT}090\"%; s%^address = \"0.0.0.0:9091\"%address = \"0.0.0.0:${CHAIN_PORT}091\"%; s%^address = \"0.0.0.0:8545\"%address = \"0.0.0.0:${CHAIN_PORT}545\"%; s%^ws-address = \"0.0.0.0:8546\"%ws-address = \"0.0.0.0:${CHAIN_PORT}546\"%" $HOME/${CHAIN_DIR}/config/app.toml
```

### Download latest chain snapshot

```bash
curl -L https://snapshots.kjnodes.com/${CHAIN_NAME}/snapshot_latest.tar.lz4 | lz4 -dc - | tar -xf - -C $HOME/${CHAIN_DIR}
```

### Start service and check the logs

```bash
sudo systemctl start ${CHAIN_APP} && journalctl -u ${CHAIN_APP} -f --no-hostname -o cat
```