---
description: >-
  This page contain instructions that will help you to setup a node. For the
  installation we use Ubuntu 20.04
---

# Installation

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
rm -rf stride
git clone https://github.com/Stride-Labs/stride.git
cd stride

# Compile genesis version v1.0.2
git checkout v1.0.2
make build
mkdir -p $HOME/.stride/cosmovisor/genesis/bin
mv build/strided $HOME/.stride/cosmovisor/genesis/bin/
rm build -rf

# Compile latest version v2.0.3
git checkout v2.0.3
make build
mkdir -p $HOME/.stride/cosmovisor/upgrades/v2.0.3/bin
mv build/strided $HOME/.stride/cosmovisor/upgrades/v2.0.3/bin/
rm build -rf
```

### Install Cosmovisor and create a service

```bash
curl -Ls https://github.com/cosmos/cosmos-sdk/releases/download/cosmovisor%2Fv1.3.0/cosmovisor-v1.3.0-linux-amd64.tar.gz | tar xz
chmod 755 cosmovisor
sudo mv cosmovisor /usr/bin/cosmovisor

sudo tee /etc/systemd/system/strided.service > /dev/null << EOF
[Unit]
Description=stride node service
After=network-online.target
[Service]
User=$USER
ExecStart=/usr/bin/cosmovisor run start
Restart=on-failure
RestartSec=10
LimitNOFILE=65535
Environment="DAEMON_HOME=$HOME/.stride"
Environment="DAEMON_NAME=strided"
Environment="UNSAFE_SKIP_BACKUP=true"
[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable strided
```

### Initialize the node

```bash
ln -s $HOME/.stride/cosmovisor/upgrades/v2.0.3 $HOME/.stride/cosmovisor/current
sudo ln -s $HOME/.stride/cosmovisor/current/bin/strided /usr/local/bin/strided
strided config chain-id stride-1
strided init $MONIKER --chain-id stride-1
curl -Ls https://snapshots.kjnodes.com/stride/genesis.json > $HOME/.stride/config/genesis.json
sed -i -e "s|^seeds *=.*|seeds = \"400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@stride.rpc.kjnodes.com:16659\"|" $HOME/.stride/config/config.toml
tee $HOME/.stride/data/priv_validator_state.json > /dev/null << EOF
{
  "height": "0",
  "round": 0,
  "step": 0
}
EOF
sed -i -e "s|^minimum-gas-prices *=.*|minimum-gas-prices = \"0ustrd\"|" $HOME/.stride/config/app.toml
sed -i -e "s|^pruning *=.*|pruning = \"custom\"|" $HOME/.stride/config/app.toml
sed -i -e "s|^pruning-keep-recent *=.*|pruning-keep-recent = \"5\"|" $HOME/.stride/config/app.toml
sed -i -e "s|^pruning-keep-every *=.*|pruning-keep-every = \"0\"|" $HOME/.stride/config/app.toml
sed -i -e "s|^pruning-interval *=.*|pruning-interval = \"1000\"|" $HOME/.stride/config/app.toml

sed -i.bak -e "s%^proxy_app = \"tcp://127.0.0.1:26658\"%proxy_app = \"tcp://127.0.0.1:16658\"%; s%^laddr = \"tcp://127.0.0.1:26657\"%laddr = \"tcp://127.0.0.1:16657\"%; s%^pprof_laddr = \"localhost:6060\"%pprof_laddr = \"localhost:16060\"%; s%^laddr = \"tcp://0.0.0.0:26656\"%laddr = \"tcp://0.0.0.0:16656\"%; s%^prometheus_listen_addr = \":26660\"%prometheus_listen_addr = \":16660\"%" $HOME/.nibid/config/config.toml
sed -i.bak -e "s%^address = \"tcp://0.0.0.0:1317\"%address = \"tcp://0.0.0.0:16317\"%; s%^address = \":8080\"%address = \":16080\"%; s%^address = \"0.0.0.0:9090\"%address = \"0.0.0.0:16090\"%; s%^address = \"0.0.0.0:9091\"%address = \"0.0.0.0:16091\"%; s%^address = \"0.0.0.0:8545\"%address = \"0.0.0.0:16545\"%; s%^ws-address = \"0.0.0.0:8546\"%ws-address = \"0.0.0.0:16546\"%" $HOME/.nibid/config/app.toml
```

### Download latest chain snapshot

```bash
curl -L https://snapshots.kjnodes.com/stride/snapshot_latest.tar.lz4 | lz4 -dc - | tar -xf - -C $HOME/.stride
```

### Start service and check the logs

```bash
sudo systemctl start strided && journalctl -u strided -f --no-hostname -o cat
```
