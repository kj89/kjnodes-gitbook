---
description: Setting up your validator node has never been so easy. Get your validator running in minutes by following step by step instructions.
---

# Installation

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/stride.png" alt=""><figcaption></figcaption></figure>

**Chain ID**: stride-1 | **Latest Version Tag**: v9.2.1 | **Custom Port**: 116

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
rm -rf stride
git clone https://github.com/Stride-Labs/stride.git
cd stride
git checkout v9.2.1

# Build binaries
make build

# Prepare binaries for Cosmovisor
mkdir -p $HOME/.stride/cosmovisor/genesis/bin
mv build/strided $HOME/.stride/cosmovisor/genesis/bin/
rm -rf build

# Create application symlinks
sudo ln -s $HOME/.stride/cosmovisor/genesis $HOME/.stride/cosmovisor/current -f
sudo ln -s $HOME/.stride/cosmovisor/current/bin/strided /usr/local/bin/strided -f
```

### Install Cosmovisor and create a service

```bash
# Download and install Cosmovisor
go install cosmossdk.io/tools/cosmovisor/cmd/cosmovisor@v1.4.0

# Create service
sudo tee /etc/systemd/system/strided.service > /dev/null << EOF
[Unit]
Description=stride node service
After=network-online.target

[Service]
User=$USER
ExecStart=$(which cosmovisor) run start
Restart=on-failure
RestartSec=10
LimitNOFILE=65535
Environment="DAEMON_HOME=$HOME/.stride"
Environment="DAEMON_NAME=strided"
Environment="UNSAFE_SKIP_BACKUP=true"
Environment="PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:$HOME/.stride/cosmovisor/current/bin"

[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable strided
```

### Initialize the node

```bash
# Set node configuration
strided config chain-id stride-1
strided config keyring-backend file
strided config node tcp://localhost:11657

# Initialize the node
strided init $MONIKER --chain-id stride-1

# Download genesis and addrbook
curl -Ls https://snapshots.kjnodes.com/stride/genesis.json > $HOME/.stride/config/genesis.json
curl -Ls https://snapshots.kjnodes.com/stride/addrbook.json > $HOME/.stride/config/addrbook.json

# Add seeds
sed -i -e "s|^seeds *=.*|seeds = \"400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@stride.rpc.kjnodes.com:11659\"|" $HOME/.stride/config/config.toml

# Set minimum gas price
sed -i -e "s|^minimum-gas-prices *=.*|minimum-gas-prices = \"0ustrd\"|" $HOME/.stride/config/app.toml

# Set pruning
sed -i \
  -e 's|^pruning *=.*|pruning = "custom"|' \
  -e 's|^pruning-keep-recent *=.*|pruning-keep-recent = "100"|' \
  -e 's|^pruning-keep-every *=.*|pruning-keep-every = "0"|' \
  -e 's|^pruning-interval *=.*|pruning-interval = "19"|' \
  $HOME/.stride/config/app.toml

# Set custom ports
sed -i -e "s%^proxy_app = \"tcp://127.0.0.1:26658\"%proxy_app = \"tcp://127.0.0.1:11658\"%; s%^laddr = \"tcp://127.0.0.1:26657\"%laddr = \"tcp://127.0.0.1:11657\"%; s%^pprof_laddr = \"localhost:6060\"%pprof_laddr = \"localhost:11660\"%; s%^laddr = \"tcp://0.0.0.0:26656\"%laddr = \"tcp://0.0.0.0:11656\"%; s%^prometheus_listen_addr = \":26660\"%prometheus_listen_addr = \":11666\"%" $HOME/.stride/config/config.toml
sed -i -e "s%^address = \"tcp://0.0.0.0:1317\"%address = \"tcp://0.0.0.0:11617\"%; s%^address = \":8080\"%address = \":11680\"%; s%^address = \"0.0.0.0:9090\"%address = \"0.0.0.0:11690\"%; s%^address = \"0.0.0.0:9091\"%address = \"0.0.0.0:11691\"%; s%:8545%:11645%; s%:8546%:11646%; s%:6065%:11665%" $HOME/.stride/config/app.toml
```

### Download latest chain snapshot

```bash
curl -L https://snapshots.kjnodes.com/stride/snapshot_latest.tar.lz4 | tar -Ilz4 -xf - -C $HOME/.stride
[[ -f $HOME/.stride/data/upgrade-info.json ]] && cp $HOME/.stride/data/upgrade-info.json $HOME/.stride/cosmovisor/genesis/upgrade-info.json
```

### Start service and check the logs

```bash
sudo systemctl start strided && sudo journalctl -u strided -f --no-hostname -o cat
```
