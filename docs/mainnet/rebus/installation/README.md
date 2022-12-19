---
description: Setting up your validator node has never been so easy. Get your validator running in minutes by following step by step instructions.
---

# Installation

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/rebus.png" width="150" alt=""><figcaption></figcaption></figure>

**Chain ID**: reb_1111-1 | **Latest Version Tag**: v0.2.0 | **Custom Port**: 21

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
sudo apt update
sudo apt install curl git jq lz4 build-essential -y
```

#### Install GO

```bash
sudo rm -rf /usr/local/go
sudo curl -Ls https://golang.org/dl/go1.19.4.linux-amd64.tar.gz | sudo tar -C /usr/local -xz
tee -a $HOME/.profile > /dev/null << EOF
export PATH=$PATH:/usr/local/go/bin:$HOME/go/bin
EOF
source $HOME/.profile
```

### Download and build binaries

```bash
# Clone project repository
cd $HOME
rm -rf rebus.core
git clone https://github.com/rebuschain/rebus.core.git
cd rebus.core

# Build binaries
git checkout v0.2.0
make build
mkdir -p $HOME/.rebusd/cosmovisor/genesis/bin
mv build/rebusd $HOME/.rebusd/cosmovisor/genesis/bin/
rm -rf build
```

### Install Cosmovisor and create a service

```bash
# Download and install Cosmovisor
go install cosmossdk.io/tools/cosmovisor/cmd/cosmovisor@v1.4.0

# Create service
sudo tee /etc/systemd/system/rebusd.service > /dev/null << EOF
[Unit]
Description=rebus node service
After=network-online.target
[Service]
User=$USER
ExecStart=$(which cosmovisor) run start
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

# Create application symlinks
ln -s $HOME/.rebusd/cosmovisor/genesis $HOME/.rebusd/cosmovisor/current
sudo ln -s $HOME/.rebusd/cosmovisor/current/bin/rebusd /usr/local/bin/rebusd
```

### Initialize the node

```bash
# Set node configuration
rebusd config chain-id reb_1111-1
rebusd config keyring-backend file
rebusd config node tcp://localhost:21657

# Initialize the node
rebusd init $MONIKER --chain-id reb_1111-1

# Download genesis and addrbook
curl -Ls https://snapshots.kjnodes.com/rebus/genesis.json > $HOME/.rebusd/config/genesis.json
curl -Ls https://snapshots.kjnodes.com/rebus/addrbook.json > $HOME/.rebusd/config/addrbook.json

# Add seeds
sed -i -e "s|^seeds *=.*|seeds = \"400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@rebus.rpc.kjnodes.com:21659\"|" $HOME/.rebusd/config/config.toml

# Set minimum gas price
sed -i -e "s|^minimum-gas-prices *=.*|minimum-gas-prices = \"0arebus\"|" $HOME/.rebusd/config/app.toml

# Set pruning
sed -i -e "s|^pruning *=.*|pruning = \"custom\"|" $HOME/.rebusd/config/app.toml
sed -i -e "s|^pruning-keep-recent *=.*|pruning-keep-recent = \"100\"|" $HOME/.rebusd/config/app.toml
sed -i -e "s|^pruning-keep-every *=.*|pruning-keep-every = \"0\"|" $HOME/.rebusd/config/app.toml
sed -i -e "s|^pruning-interval *=.*|pruning-interval = \"19\"|" $HOME/.rebusd/config/app.toml

# Set custom ports
sed -i.bak -e "s%^proxy_app = \"tcp://127.0.0.1:26658\"%proxy_app = \"tcp://127.0.0.1:21658\"%; s%^laddr = \"tcp://127.0.0.1:26657\"%laddr = \"tcp://127.0.0.1:21657\"%; s%^pprof_laddr = \"localhost:6060\"%pprof_laddr = \"localhost:21060\"%; s%^laddr = \"tcp://0.0.0.0:26656\"%laddr = \"tcp://0.0.0.0:21656\"%; s%^prometheus_listen_addr = \":26660\"%prometheus_listen_addr = \":21660\"%" $HOME/.rebusd/config/config.toml
sed -i.bak -e "s%^address = \"tcp://0.0.0.0:1317\"%address = \"tcp://0.0.0.0:21317\"%; s%^address = \":8080\"%address = \":21080\"%; s%^address = \"0.0.0.0:9090\"%address = \"0.0.0.0:21090\"%; s%^address = \"0.0.0.0:9091\"%address = \"0.0.0.0:21091\"%; s%^address = \"0.0.0.0:8545\"%address = \"0.0.0.0:21545\"%; s%^ws-address = \"0.0.0.0:8546\"%ws-address = \"0.0.0.0:21546\"%" $HOME/.rebusd/config/app.toml
```

### Download latest chain snapshot

```bash
curl -L https://snapshots.kjnodes.com/rebus/snapshot_latest.tar.lz4 | lz4 -dc - | tar -xf - -C $HOME/.rebusd
```

### Start service and check the logs

```bash
sudo systemctl start rebusd && journalctl -u rebusd -f --no-hostname -o cat
```
