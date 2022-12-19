---
description: Setting up your validator node has never been so easy. Get your validator running in minutes by following step by step instructions.
---

# Installation

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/osmosis.png" width="150" alt=""><figcaption></figcaption></figure>

**Chain ID**: osmosis-1 | **Latest Version Tag**: v13.1.0 | **Custom Port**: 29

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
rm -rf osmosis
git clone https://github.com/osmosis-labs/osmosis.git
cd osmosis

# Build binaries
git checkout v13.1.0
make build
mkdir -p $HOME/.osmosisd/cosmovisor/genesis/bin
mv build/osmosisd $HOME/.osmosisd/cosmovisor/genesis/bin/
rm -rf build
```

### Install Cosmovisor and create a service

```bash
# Download and install Cosmovisor
go install github.com/cosmos/cosmos-sdk/cosmovisor/cmd/cosmovisor@1.4.0

# Create service
sudo tee /etc/systemd/system/osmosisd.service > /dev/null << EOF
[Unit]
Description=osmosis node service
After=network-online.target
[Service]
User=$USER
ExecStart=/usr/bin/cosmovisor run start
Restart=on-failure
RestartSec=10
LimitNOFILE=65535
Environment="DAEMON_HOME=$HOME/.osmosisd"
Environment="DAEMON_NAME=osmosisd"
Environment="UNSAFE_SKIP_BACKUP=true"
[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable osmosisd

# Create application symlinks
ln -s $HOME/.osmosisd/cosmovisor/genesis $HOME/.osmosisd/cosmovisor/current
sudo ln -s $HOME/.osmosisd/cosmovisor/current/bin/osmosisd /usr/local/bin/osmosisd
```

### Initialize the node

```bash
# Set node configuration
osmosisd config chain-id osmosis-1
osmosisd config keyring-backend file
osmosisd config node tcp://localhost:29657

# Initialize the node
osmosisd init $MONIKER --chain-id osmosis-1

# Download genesis and addrbook
curl -Ls https://snapshots.kjnodes.com/osmosis/genesis.json > $HOME/.osmosisd/config/genesis.json
curl -Ls https://snapshots.kjnodes.com/osmosis/addrbook.json > $HOME/.osmosisd/config/addrbook.json

# Add seeds
sed -i -e "s|^seeds *=.*|seeds = \"400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@osmosis.rpc.kjnodes.com:29659\"|" $HOME/.osmosisd/config/config.toml

# Set minimum gas price
sed -i -e "s|^minimum-gas-prices *=.*|minimum-gas-prices = \"0uosmo\"|" $HOME/.osmosisd/config/app.toml

# Set pruning
sed -i -e "s|^pruning *=.*|pruning = \"custom\"|" $HOME/.osmosisd/config/app.toml
sed -i -e "s|^pruning-keep-recent *=.*|pruning-keep-recent = \"100\"|" $HOME/.osmosisd/config/app.toml
sed -i -e "s|^pruning-keep-every *=.*|pruning-keep-every = \"0\"|" $HOME/.osmosisd/config/app.toml
sed -i -e "s|^pruning-interval *=.*|pruning-interval = \"19\"|" $HOME/.osmosisd/config/app.toml

# Set custom ports
sed -i.bak -e "s%^proxy_app = \"tcp://127.0.0.1:26658\"%proxy_app = \"tcp://127.0.0.1:29658\"%; s%^laddr = \"tcp://127.0.0.1:26657\"%laddr = \"tcp://127.0.0.1:29657\"%; s%^pprof_laddr = \"localhost:6060\"%pprof_laddr = \"localhost:29060\"%; s%^laddr = \"tcp://0.0.0.0:26656\"%laddr = \"tcp://0.0.0.0:29656\"%; s%^prometheus_listen_addr = \":26660\"%prometheus_listen_addr = \":29660\"%" $HOME/.osmosisd/config/config.toml
sed -i.bak -e "s%^address = \"tcp://0.0.0.0:1317\"%address = \"tcp://0.0.0.0:29317\"%; s%^address = \":8080\"%address = \":29080\"%; s%^address = \"0.0.0.0:9090\"%address = \"0.0.0.0:29090\"%; s%^address = \"0.0.0.0:9091\"%address = \"0.0.0.0:29091\"%; s%^address = \"0.0.0.0:8545\"%address = \"0.0.0.0:29545\"%; s%^ws-address = \"0.0.0.0:8546\"%ws-address = \"0.0.0.0:29546\"%" $HOME/.osmosisd/config/app.toml
```

### Download latest chain snapshot

```bash
curl -L https://snapshots.kjnodes.com/osmosis/snapshot_latest.tar.lz4 | lz4 -dc - | tar -xf - -C $HOME/.osmosisd
```

### Start service and check the logs

```bash
sudo systemctl start osmosisd && journalctl -u osmosisd -f --no-hostname -o cat
```
