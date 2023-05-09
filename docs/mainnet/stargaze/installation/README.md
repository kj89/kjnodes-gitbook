---
description: Setting up your validator node has never been so easy. Get your validator running in minutes by following step by step instructions.
---

# Installation

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/stargaze.png" alt=""><figcaption></figcaption></figure>

**Chain ID**: stargaze-1 | **Latest Version Tag**: v9.0.0 | **Custom Port**: 158

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
curl -Ls https://go.dev/dl/go1.20.4.linux-amd64.tar.gz | sudo tar -xzf - -C /usr/local
eval $(echo 'export PATH=$PATH:/usr/local/go/bin' | sudo tee /etc/profile.d/golang.sh)
eval $(echo 'export PATH=$PATH:$HOME/go/bin' | tee -a $HOME/.profile)
```

### Download and build binaries

```bash
# Clone project repository
cd $HOME
rm -rf stargaze
git clone https://github.com/public-awesome/stargaze.git
cd stargaze
git checkout v9.0.0

# Build binaries
make build

# Prepare binaries for Cosmovisor
mkdir -p $HOME/.starsd/cosmovisor/genesis/bin
mv bin/starsd $HOME/.starsd/cosmovisor/genesis/bin/
rm -rf build

# Create application symlinks
sudo ln -s $HOME/.starsd/cosmovisor/genesis $HOME/.starsd/cosmovisor/current -f
sudo ln -s $HOME/.starsd/cosmovisor/current/bin/starsd /usr/local/bin/starsd -f
```

### Install Cosmovisor and create a service

```bash
# Download and install Cosmovisor
go install cosmossdk.io/tools/cosmovisor/cmd/cosmovisor@v1.4.0

# Create service
sudo tee /etc/systemd/system/starsd.service > /dev/null << EOF
[Unit]
Description=stargaze node service
After=network-online.target

[Service]
User=$USER
ExecStart=$(which cosmovisor) run start
Restart=on-failure
RestartSec=10
LimitNOFILE=65535
Environment="DAEMON_HOME=$HOME/.starsd"
Environment="DAEMON_NAME=starsd"
Environment="UNSAFE_SKIP_BACKUP=true"
Environment="PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:$HOME/.starsd/cosmovisor/current/bin"

[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable starsd
```

### Initialize the node

```bash
# Set node configuration
starsd config chain-id stargaze-1
starsd config keyring-backend file
starsd config node tcp://localhost:15857

# Initialize the node
starsd init $MONIKER --chain-id stargaze-1

# Download genesis and addrbook
curl -Ls https://snapshots.kjnodes.com/stargaze/genesis.json > $HOME/.starsd/config/genesis.json
curl -Ls https://snapshots.kjnodes.com/stargaze/addrbook.json > $HOME/.starsd/config/addrbook.json

# Add seeds
sed -i -e "s|^seeds *=.*|seeds = \"400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@stargaze.rpc.kjnodes.com:15859\"|" $HOME/.starsd/config/config.toml

# Set minimum gas price
sed -i -e "s|^minimum-gas-prices *=.*|minimum-gas-prices = \"0ustars\"|" $HOME/.starsd/config/app.toml

# Set pruning
sed -i \
  -e 's|^pruning *=.*|pruning = "custom"|' \
  -e 's|^pruning-keep-recent *=.*|pruning-keep-recent = "100"|' \
  -e 's|^pruning-keep-every *=.*|pruning-keep-every = "0"|' \
  -e 's|^pruning-interval *=.*|pruning-interval = "19"|' \
  $HOME/.starsd/config/app.toml

# Set custom ports
sed -i -e "s%^proxy_app = \"tcp://127.0.0.1:26658\"%proxy_app = \"tcp://127.0.0.1:15858\"%; s%^laddr = \"tcp://127.0.0.1:26657\"%laddr = \"tcp://127.0.0.1:15857\"%; s%^pprof_laddr = \"localhost:6060\"%pprof_laddr = \"localhost:15860\"%; s%^laddr = \"tcp://0.0.0.0:26656\"%laddr = \"tcp://0.0.0.0:15856\"%; s%^prometheus_listen_addr = \":26660\"%prometheus_listen_addr = \":15866\"%" $HOME/.starsd/config/config.toml
sed -i -e "s%^address = \"tcp://0.0.0.0:1317\"%address = \"tcp://0.0.0.0:15817\"%; s%^address = \":8080\"%address = \":15880\"%; s%^address = \"0.0.0.0:9090\"%address = \"0.0.0.0:15890\"%; s%^address = \"0.0.0.0:9091\"%address = \"0.0.0.0:15891\"%; s%:8545%:15845%; s%:8546%:15846%; s%:6065%:15865%" $HOME/.starsd/config/app.toml
```

### Download latest chain snapshot

```bash
curl -L https://snapshots.kjnodes.com/stargaze/snapshot_latest.tar.lz4 | tar -Ilz4 -xf - -C $HOME/.starsd
[[ -f $HOME/.starsd/data/upgrade-info.json ]] && cp $HOME/.starsd/data/upgrade-info.json $HOME/.starsd/cosmovisor/genesis/upgrade-info.json
```

### Start service and check the logs

```bash
sudo systemctl start starsd && sudo journalctl -u starsd -f --no-hostname -o cat
```
