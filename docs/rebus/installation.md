---
description: >-
  This page contain instructions that will help you to setup a node. For the
  installation we use Ubuntu 20.04
---

# Installation

### Setup validator name
```bash
MONIKER="YOUR_MONIKER_GOES_HERE"
CUSTOM_PORT=YOUR_CUSTOM_PORT_GOES_HERE
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
rm -rf rebus.core
git clone https://github.com/rebuschain/rebus.core.git
cd rebus.core

# Compile genesis version v0.1.0
git checkout v0.1.0
make build
mkdir -p $HOME/.rebusd/cosmovisor/genesis/bin
mv build/rebusd $HOME/.rebusd/cosmovisor/genesis/bin/
rm build -rf

# Compile latest version v0.2.0
git checkout v0.2.0
make build
mkdir -p $HOME/.rebusd/cosmovisor/upgrades/v0.2.0/bin
mv build/rebusd $HOME/.rebusd/cosmovisor/upgrades/v0.2.0/bin/
rm build -rf
```

### Install Cosmovisor and create a service

```bash
curl -Ls https://github.com/cosmos/cosmos-sdk/releases/download/cosmovisor%2Fv1.3.0/cosmovisor-v1.3.0-linux-amd64.tar.gz | tar xz
chmod 755 cosmovisor
sudo mv cosmovisor /usr/bin/cosmovisor

sudo tee /etc/systemd/system/rebusd.service > /dev/null << EOF
[Unit]
Description=rebus node service
After=network-online.target
[Service]
User=$USER
ExecStart=/usr/bin/cosmovisor run start
Restart=on-failure
RestartSec=10
LimitNOFILE=65535
Environment="DAEMON_HOME=$HOME/.rebusd"
Environment="DAEMON_NAME=rebusd"
Environment="UNSAFE_SKIP_BACKUP=true"
[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable rebusd
```

### Initialize the node

```bash
ln -s $HOME/.rebusd/cosmovisor/upgrades/v0.2.0 $HOME/.rebusd/cosmovisor/current
sudo ln -s $HOME/.rebusd/cosmovisor/current/bin/rebusd /usr/local/bin/rebusd
rebusd config chain-id reb_1111-1
rebusd init $MONIKER --chain-id reb_1111-1
curl -Ls https://snapshots.kjnodes.com/rebus/genesis.json > $HOME/.rebusd/config/genesis.json
sed -i -e "s|^seeds *=.*|seeds = \"400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@rebus.rpc.kjnodes.com:21659\"|" $HOME/.rebusd/config/config.toml
tee $HOME/.rebusd/data/priv_validator_state.json > /dev/null << EOF
{
  "height": "0",
  "round": 0,
  "step": 0
}
EOF
sed -i -e "s|^minimum-gas-prices *=.*|minimum-gas-prices = \"0arebus\"|" $HOME/.rebusd/config/app.toml
sed -i -e "s|^pruning *=.*|pruning = \"custom\"|" $HOME/.rebusd/config/app.toml
sed -i -e "s|^pruning-keep-recent *=.*|pruning-keep-recent = \"5\"|" $HOME/.rebusd/config/app.toml
sed -i -e "s|^pruning-keep-every *=.*|pruning-keep-every = \"0\"|" $HOME/.rebusd/config/app.toml
sed -i -e "s|^pruning-interval *=.*|pruning-interval = \"1000\"|" $HOME/.rebusd/config/app.toml

sed -i.bak -e "s%^proxy_app = \"tcp://127.0.0.1:26658\"%proxy_app = \"tcp://127.0.0.1:${CUSTOM_PORT}658\"%; s%^laddr = \"tcp://127.0.0.1:26657\"%laddr = \"tcp://127.0.0.1:${CUSTOM_PORT}657\"%; s%^pprof_laddr = \"localhost:6060\"%pprof_laddr = \"localhost:${CUSTOM_PORT}060\"%; s%^laddr = \"tcp://0.0.0.0:26656\"%laddr = \"tcp://0.0.0.0:${CUSTOM_PORT}656\"%; s%^prometheus_listen_addr = \":26660\"%prometheus_listen_addr = \":${CUSTOM_PORT}660\"%" $HOME/.nibid/config/config.toml
sed -i.bak -e "s%^address = \"tcp://0.0.0.0:1317\"%address = \"tcp://0.0.0.0:${CUSTOM_PORT}317\"%; s%^address = \":8080\"%address = \":${CUSTOM_PORT}080\"%; s%^address = \"0.0.0.0:9090\"%address = \"0.0.0.0:${CUSTOM_PORT}090\"%; s%^address = \"0.0.0.0:9091\"%address = \"0.0.0.0:${CUSTOM_PORT}091\"%; s%^address = \"0.0.0.0:8545\"%address = \"0.0.0.0:${CUSTOM_PORT}545\"%; s%^ws-address = \"0.0.0.0:8546\"%ws-address = \"0.0.0.0:${CUSTOM_PORT}546\"%" $HOME/.nibid/config/app.toml
```

### Download latest chain snapshot

```bash
curl -L https://snapshots.kjnodes.com/rebus/snapshot_latest.tar.lz4 | lz4 -dc - | tar -xf - -C $HOME/.rebusd
```

### Start service and check the logs

```bash
sudo systemctl start rebusd && journalctl -u rebusd -f --no-hostname -o cat
```
