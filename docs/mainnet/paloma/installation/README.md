---
description: Setting up your validator node has never been so easy. Get your validator running in minutes by following step by step instructions.
---

# Installation

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/paloma.png" alt=""><figcaption></figcaption></figure>

**Chain ID**: messenger | **Latest Version Tag**: v1.1.0 | **Custom Port**: 110

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
rm -rf paloma
git clone https://github.com/palomachain/paloma.git
cd paloma
git checkout v1.1.0

# Fix version handling: https://github.com/palomachain/paloma/commit/d0f1746754041cd39d2dbd96cd8dd44f5e6ba2c5
sed -i -r -e 's/^  VERSION := \$\(shell git describe --exact-match 2>\/dev\/null\)$/  VERSION := $(shell git describe --exact-match --tags 2>\/dev\/null | sed '"'"'s\/^v\/\/'"'"')/' Makefile

# Build binaries
make build

# Prepare binaries for Cosmovisor
mkdir -p $HOME/.paloma/cosmovisor/genesis/bin
mv build/palomad $HOME/.paloma/cosmovisor/genesis/bin/
rm -rf build

# Create application symlinks
sudo ln -s $HOME/.paloma/cosmovisor/genesis $HOME/.paloma/cosmovisor/current -f
sudo ln -s $HOME/.paloma/cosmovisor/current/bin/palomad /usr/local/bin/palomad -f
```

### Install Cosmovisor and create a service

```bash
# Download and install Cosmovisor
go install cosmossdk.io/tools/cosmovisor/cmd/cosmovisor@v1.4.0

# Create service
sudo tee /etc/systemd/system/palomad.service > /dev/null << EOF
[Unit]
Description=paloma node service
After=network-online.target

[Service]
User=$USER
ExecStart=$(which cosmovisor) run start
Restart=on-failure
RestartSec=10
LimitNOFILE=65535
Environment="DAEMON_HOME=$HOME/.paloma"
Environment="DAEMON_NAME=palomad"
Environment="UNSAFE_SKIP_BACKUP=true"
Environment="PIGEON_HEALTHCHECK_PORT=5757"

[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable palomad
```

### Initialize the node

```bash
# Set node configuration
palomad config chain-id messenger
palomad config keyring-backend file
palomad config node tcp://localhost:11057

# Initialize the node
palomad init $MONIKER --chain-id messenger

# Download genesis and addrbook
curl -Ls https://snapshots.kjnodes.com/paloma/genesis.json > $HOME/.paloma/config/genesis.json
curl -Ls https://snapshots.kjnodes.com/paloma/addrbook.json > $HOME/.paloma/config/addrbook.json

# Add seeds
sed -i -e "s|^seeds *=.*|seeds = \"400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@paloma.rpc.kjnodes.com:11059\"|" $HOME/.paloma/config/config.toml

# Set minimum gas price
sed -i -e "s|^minimum-gas-prices *=.*|minimum-gas-prices = \"0ugrain\"|" $HOME/.paloma/config/app.toml

# Set pruning
sed -i \
  -e 's|^pruning *=.*|pruning = "custom"|' \
  -e 's|^pruning-keep-recent *=.*|pruning-keep-recent = "100"|' \
  -e 's|^pruning-keep-every *=.*|pruning-keep-every = "0"|' \
  -e 's|^pruning-interval *=.*|pruning-interval = "19"|' \
  $HOME/.paloma/config/app.toml

# Set custom ports
sed -i -e "s%^proxy_app = \"tcp://127.0.0.1:26658\"%proxy_app = \"tcp://127.0.0.1:11058\"%; s%^laddr = \"tcp://127.0.0.1:26657\"%laddr = \"tcp://127.0.0.1:11057\"%; s%^pprof_laddr = \"localhost:6060\"%pprof_laddr = \"localhost:11060\"%; s%^laddr = \"tcp://0.0.0.0:26656\"%laddr = \"tcp://0.0.0.0:11056\"%; s%^prometheus_listen_addr = \":26660\"%prometheus_listen_addr = \":11066\"%" $HOME/.paloma/config/config.toml
sed -i -e "s%^address = \"tcp://0.0.0.0:1317\"%address = \"tcp://0.0.0.0:11017\"%; s%^address = \":8080\"%address = \":11080\"%; s%^address = \"0.0.0.0:9090\"%address = \"0.0.0.0:11090\"%; s%^address = \"0.0.0.0:9091\"%address = \"0.0.0.0:11091\"%; s%:8545%:11045%; s%:8546%:11046%; s%:6065%:11065%" $HOME/.paloma/config/app.toml
```

### Download latest chain snapshot

```bash
curl -L https://snapshots.kjnodes.com/paloma/snapshot_latest.tar.lz4 | tar -Ilz4 -xf - -C $HOME/.paloma
[[ -f $HOME/.paloma/data/upgrade-info.json ]] && cp $HOME/.paloma/data/upgrade-info.json $HOME/.paloma/cosmovisor/genesis/upgrade-info.json
```

### Start service and check the logs

```bash
sudo systemctl start palomad && sudo journalctl -u palomad -f --no-hostname -o cat
```
