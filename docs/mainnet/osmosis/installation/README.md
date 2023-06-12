---
description: Setting up your validator node has never been so easy. Get your validator running in minutes by following step by step instructions.
---

# Installation

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/osmosis.png" alt=""><figcaption></figcaption></figure>

**Chain ID**: osmosis-1 | **Latest Version Tag**: v15.0.0 | **Custom Port**: 129

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
curl -Ls https://go.dev/dl/go1.19.10.linux-amd64.tar.gz | sudo tar -xzf - -C /usr/local
eval $(echo 'export PATH=$PATH:/usr/local/go/bin' | sudo tee /etc/profile.d/golang.sh)
eval $(echo 'export PATH=$PATH:$HOME/go/bin' | tee -a $HOME/.profile)
```

### Download and build binaries

```bash
# Clone project repository
cd $HOME
rm -rf osmosis
git clone https://github.com/osmosis-labs/osmosis.git
cd osmosis
git checkout v15.0.0

# Build binaries
make build

# Prepare binaries for Cosmovisor
mkdir -p $HOME/.osmosisd/cosmovisor/genesis/bin
mv build/osmosisd $HOME/.osmosisd/cosmovisor/genesis/bin/
rm -rf build

# Create application symlinks
sudo ln -s $HOME/.osmosisd/cosmovisor/genesis $HOME/.osmosisd/cosmovisor/current -f
sudo ln -s $HOME/.osmosisd/cosmovisor/current/bin/osmosisd /usr/local/bin/osmosisd -f
```

### Install Cosmovisor and create a service

```bash
# Download and install Cosmovisor
go install cosmossdk.io/tools/cosmovisor/cmd/cosmovisor@v1.4.0

# Create service
sudo tee /etc/systemd/system/osmosisd.service > /dev/null << EOF
[Unit]
Description=osmosis node service
After=network-online.target

[Service]
User=$USER
ExecStart=$(which cosmovisor) run start
Restart=on-failure
RestartSec=10
LimitNOFILE=65535
Environment="DAEMON_HOME=$HOME/.osmosisd"
Environment="DAEMON_NAME=osmosisd"
Environment="UNSAFE_SKIP_BACKUP=true"
Environment="PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:$HOME/.osmosisd/cosmovisor/current/bin"

[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable osmosisd
```

### Initialize the node

```bash
# Set node configuration
osmosisd config chain-id osmosis-1
osmosisd config keyring-backend file
osmosisd config node tcp://localhost:12957

# Initialize the node
osmosisd init $MONIKER --chain-id osmosis-1

# Download genesis and addrbook
curl -Ls https://snapshots.kjnodes.com/osmosis/genesis.json > $HOME/.osmosisd/config/genesis.json
curl -Ls https://snapshots.kjnodes.com/osmosis/addrbook.json > $HOME/.osmosisd/config/addrbook.json

# Add seeds
sed -i -e "s|^seeds *=.*|seeds = \"400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@osmosis.rpc.kjnodes.com:12959\"|" $HOME/.osmosisd/config/config.toml

# Set minimum gas price
sed -i -e "s|^minimum-gas-prices *=.*|minimum-gas-prices = \"0.0025uosmo\"|" $HOME/.osmosisd/config/app.toml

# Set pruning
sed -i \
  -e 's|^pruning *=.*|pruning = "custom"|' \
  -e 's|^pruning-keep-recent *=.*|pruning-keep-recent = "100"|' \
  -e 's|^pruning-keep-every *=.*|pruning-keep-every = "0"|' \
  -e 's|^pruning-interval *=.*|pruning-interval = "19"|' \
  $HOME/.osmosisd/config/app.toml

# Set custom ports
sed -i -e "s%^proxy_app = \"tcp://127.0.0.1:26658\"%proxy_app = \"tcp://127.0.0.1:12958\"%; s%^laddr = \"tcp://127.0.0.1:26657\"%laddr = \"tcp://127.0.0.1:12957\"%; s%^pprof_laddr = \"localhost:6060\"%pprof_laddr = \"localhost:12960\"%; s%^laddr = \"tcp://0.0.0.0:26656\"%laddr = \"tcp://0.0.0.0:12956\"%; s%^prometheus_listen_addr = \":26660\"%prometheus_listen_addr = \":12966\"%" $HOME/.osmosisd/config/config.toml
sed -i -e "s%^address = \"tcp://0.0.0.0:1317\"%address = \"tcp://0.0.0.0:12917\"%; s%^address = \":8080\"%address = \":12980\"%; s%^address = \"0.0.0.0:9090\"%address = \"0.0.0.0:12990\"%; s%^address = \"0.0.0.0:9091\"%address = \"0.0.0.0:12991\"%; s%:8545%:12945%; s%:8546%:12946%; s%:6065%:12965%" $HOME/.osmosisd/config/app.toml
```

### Download latest chain snapshot

```bash
curl -L https://snapshots.kjnodes.com/osmosis/snapshot_latest.tar.lz4 | tar -Ilz4 -xf - -C $HOME/.osmosisd
[[ -f $HOME/.osmosisd/data/upgrade-info.json ]] && cp $HOME/.osmosisd/data/upgrade-info.json $HOME/.osmosisd/cosmovisor/genesis/upgrade-info.json
```

### Start service and check the logs

```bash
sudo systemctl start osmosisd && sudo journalctl -u osmosisd -f --no-hostname -o cat
```
