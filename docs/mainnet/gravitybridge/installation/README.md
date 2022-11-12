---
description: Setting up your validator node has never been so easy. Get your validator running in minutes by following step by step instructions.
---

# Installation

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/gravitybridge.png" width="150" alt=""><figcaption></figcaption></figure>

**Chain ID**: gravity-bridge-3 | **Latest Version Tag**: pleiades | **Custom Port**: 26

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
mkdir gravity-bin && cd gravity-bin
wget -O gravityd https://github.com/Gravity-Bridge/Gravity-Bridge/releases/download/v1.7.2/gravity-linux-amd64
wget -O gbt https://github.com/Gravity-Bridge/Gravity-Bridge/releases/download/v1.7.2/gbt
chmod +x *
sudo mv * /usr/bin/
```

### Create a service

```bash
sudo tee /etc/systemd/system/gravityd.service > /dev/null << EOF
[Unit]
Description=gravitybridge node service
After=network-online.target

[Service]
User=$USER
ExecStart=$(which gravityd) start --home $HOME/.gravity
Restart=on-failure
RestartSec=3
LimitNOFILE=65535

[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable gravityd
```

### Initialize the node

```bash
gravityd init $MONIKER --chain-id gravity-bridge-3
curl -Ls https://snapshots.kjnodes.com/gravitybridge/genesis.json > $HOME/.gravity/config/genesis.json
curl -Ls https://snapshots.kjnodes.com/gravitybridge/addrbook.json > $HOME/.gravity/config/addrbook.json
sed -i -e "s|^seeds *=.*|seeds = \"400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@gravitybridge.rpc.kjnodes.com:26659\"|" $HOME/.gravity/config/config.toml
sed -i -e "s|^minimum-gas-prices *=.*|minimum-gas-prices = \"0ugraviton\"|" $HOME/.gravity/config/app.toml
sed -i -e "s|^pruning *=.*|pruning = \"custom\"|" $HOME/.gravity/config/app.toml
sed -i -e "s|^pruning-keep-recent *=.*|pruning-keep-recent = \"100\"|" $HOME/.gravity/config/app.toml
sed -i -e "s|^pruning-keep-every *=.*|pruning-keep-every = \"0\"|" $HOME/.gravity/config/app.toml
sed -i -e "s|^pruning-interval *=.*|pruning-interval = \"19\"|" $HOME/.gravity/config/app.toml

sed -i.bak -e "s%^proxy_app = \"tcp://127.0.0.1:26658\"%proxy_app = \"tcp://127.0.0.1:26658\"%; s%^laddr = \"tcp://127.0.0.1:26657\"%laddr = \"tcp://127.0.0.1:26657\"%; s%^pprof_laddr = \"localhost:6060\"%pprof_laddr = \"localhost:26060\"%; s%^laddr = \"tcp://0.0.0.0:26656\"%laddr = \"tcp://0.0.0.0:26656\"%; s%^prometheus_listen_addr = \":26660\"%prometheus_listen_addr = \":26660\"%" $HOME/.gravity/config/config.toml
sed -i.bak -e "s%^address = \"tcp://0.0.0.0:1317\"%address = \"tcp://0.0.0.0:26317\"%; s%^address = \":8080\"%address = \":26080\"%; s%^address = \"0.0.0.0:9090\"%address = \"0.0.0.0:26090\"%; s%^address = \"0.0.0.0:9091\"%address = \"0.0.0.0:26091\"%; s%^address = \"0.0.0.0:8545\"%address = \"0.0.0.0:26545\"%; s%^ws-address = \"0.0.0.0:8546\"%ws-address = \"0.0.0.0:26546\"%" $HOME/.gravity/config/app.toml
```

### Download latest chain snapshot

```bash
curl -L https://snapshots.kjnodes.com/gravitybridge/snapshot_latest.tar.lz4 | lz4 -dc - | tar -xf - -C $HOME/.gravity
```

### Start service and check the logs

```bash
sudo systemctl start gravityd && journalctl -u gravityd -f --no-hostname -o cat
```
