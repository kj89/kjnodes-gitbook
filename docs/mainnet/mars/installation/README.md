---
description: Setting up your validator node has never been so easy. Get your validator running in minutes by following step by step instructions.
---

# Installation

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/mars.png" alt=""><figcaption></figcaption></figure>

**Chain ID**: mars-1 | **Latest Version Tag**: v1.0.2 | **Custom Port**: 145

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
curl -Ls https://go.dev/dl/go1.19.9.linux-amd64.tar.gz | sudo tar -xzf - -C /usr/local
eval $(echo 'export PATH=$PATH:/usr/local/go/bin' | sudo tee /etc/profile.d/golang.sh)
eval $(echo 'export PATH=$PATH:$HOME/go/bin' | tee -a $HOME/.profile)
```

### Download and build binaries

```bash
# Clone project repository
cd $HOME
rm -rf hub
git clone https://github.com/mars-protocol/hub.git
cd hub
git checkout v1.0.2

# Build binaries
make build

# Prepare binaries for Cosmovisor
mkdir -p $HOME/.mars/cosmovisor/genesis/bin
mv build/marsd $HOME/.mars/cosmovisor/genesis/bin/
rm -rf build

# Create application symlinks
sudo ln -s $HOME/.mars/cosmovisor/genesis $HOME/.mars/cosmovisor/current -f
sudo ln -s $HOME/.mars/cosmovisor/current/bin/marsd /usr/local/bin/marsd -f
```

### Install Cosmovisor and create a service

```bash
# Download and install Cosmovisor
go install cosmossdk.io/tools/cosmovisor/cmd/cosmovisor@v1.4.0

# Create service
sudo tee /etc/systemd/system/marsd.service > /dev/null << EOF
[Unit]
Description=mars node service
After=network-online.target

[Service]
User=$USER
ExecStart=$(which cosmovisor) run start
Restart=on-failure
RestartSec=10
LimitNOFILE=65535
Environment="DAEMON_HOME=$HOME/.mars"
Environment="DAEMON_NAME=marsd"
Environment="UNSAFE_SKIP_BACKUP=true"
Environment="PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:$HOME/.mars/cosmovisor/current/bin"

[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable marsd
```

### Initialize the node

```bash
# Set node configuration
marsd config chain-id mars-1
marsd config keyring-backend file
marsd config node tcp://localhost:14557

# Initialize the node
marsd init $MONIKER --chain-id mars-1

# Download genesis and addrbook
curl -Ls https://snapshots.kjnodes.com/mars/genesis.json > $HOME/.mars/config/genesis.json
curl -Ls https://snapshots.kjnodes.com/mars/addrbook.json > $HOME/.mars/config/addrbook.json

# Add seeds
sed -i -e "s|^seeds *=.*|seeds = \"400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@mars.rpc.kjnodes.com:14559\"|" $HOME/.mars/config/config.toml

# Set minimum gas price
sed -i -e "s|^minimum-gas-prices *=.*|minimum-gas-prices = \"0umars\"|" $HOME/.mars/config/app.toml

# Set pruning
sed -i \
  -e 's|^pruning *=.*|pruning = "custom"|' \
  -e 's|^pruning-keep-recent *=.*|pruning-keep-recent = "100"|' \
  -e 's|^pruning-keep-every *=.*|pruning-keep-every = "0"|' \
  -e 's|^pruning-interval *=.*|pruning-interval = "19"|' \
  $HOME/.mars/config/app.toml

# Set custom ports
sed -i -e "s%^proxy_app = \"tcp://127.0.0.1:26658\"%proxy_app = \"tcp://127.0.0.1:14558\"%; s%^laddr = \"tcp://127.0.0.1:26657\"%laddr = \"tcp://127.0.0.1:14557\"%; s%^pprof_laddr = \"localhost:6060\"%pprof_laddr = \"localhost:14560\"%; s%^laddr = \"tcp://0.0.0.0:26656\"%laddr = \"tcp://0.0.0.0:14556\"%; s%^prometheus_listen_addr = \":26660\"%prometheus_listen_addr = \":14566\"%" $HOME/.mars/config/config.toml
sed -i -e "s%^address = \"tcp://0.0.0.0:1317\"%address = \"tcp://0.0.0.0:14517\"%; s%^address = \":8080\"%address = \":14580\"%; s%^address = \"0.0.0.0:9090\"%address = \"0.0.0.0:14590\"%; s%^address = \"0.0.0.0:9091\"%address = \"0.0.0.0:14591\"%; s%:8545%:14545%; s%:8546%:14546%; s%:6065%:14565%" $HOME/.mars/config/app.toml
```

### Download latest chain snapshot

```bash
curl -L https://snapshots.kjnodes.com/mars/snapshot_latest.tar.lz4 | tar -Ilz4 -xf - -C $HOME/.mars
[[ -f $HOME/.mars/data/upgrade-info.json ]] && cp $HOME/.mars/data/upgrade-info.json $HOME/.mars/cosmovisor/genesis/upgrade-info.json
```

### Start service and check the logs

```bash
sudo systemctl start marsd && sudo journalctl -u marsd -f --no-hostname -o cat
```
