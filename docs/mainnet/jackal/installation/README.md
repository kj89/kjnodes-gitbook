---
description: Setting up your validator node has never been so easy. Get your validator running in minutes by following step by step instructions.
---

# Installation

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/jackal.png" width="150" alt=""><figcaption></figcaption></figure>

**Chain ID**: jackal-1 | **Latest Version Tag**: v1.1.2-hotfix | **Custom Port**: 37

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
curl -Ls https://go.dev/dl/go1.19.7.linux-amd64.tar.gz | sudo tar -xzf - -C /usr/local
eval $(echo 'export PATH=$PATH:/usr/local/go/bin' | sudo tee /etc/profile.d/golang.sh)
eval $(echo 'export PATH=$PATH:$HOME/go/bin' | tee -a $HOME/.profile)
```

### Download and build binaries

```bash
# Clone project repository
cd $HOME
rm -rf canine-chain
git clone https://github.com/JackalLabs/canine-chain.git
cd canine-chain
git checkout v1.1.2-hotfix

# Build binaries
make build

# Prepare binaries for Cosmovisor
mkdir -p $HOME/.canine/cosmovisor/genesis/bin
mv build/canined $HOME/.canine/cosmovisor/genesis/bin/
rm -rf build

# Create application symlinks
ln -s $HOME/.canine/cosmovisor/genesis $HOME/.canine/cosmovisor/current
sudo ln -s $HOME/.canine/cosmovisor/current/bin/canined /usr/local/bin/canined
```

### Install Cosmovisor and create a service

```bash
# Download and install Cosmovisor
go install cosmossdk.io/tools/cosmovisor/cmd/cosmovisor@v1.4.0

# Create service
sudo tee /etc/systemd/system/canined.service > /dev/null << EOF
[Unit]
Description=jackal node service
After=network-online.target

[Service]
User=$USER
ExecStart=$(which cosmovisor) run start
Restart=on-failure
RestartSec=10
LimitNOFILE=65535
Environment="DAEMON_HOME=$HOME/.canine"
Environment="DAEMON_NAME=canined"
Environment="UNSAFE_SKIP_BACKUP=true"
Environment="PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:$HOME/.canine/cosmovisor/current/bin"

[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable canined
```

### Initialize the node

```bash
# Set node configuration
canined config chain-id jackal-1
canined config keyring-backend file
canined config node tcp://localhost:37657

# Initialize the node
canined init $MONIKER --chain-id jackal-1

# Download genesis and addrbook
curl -Ls https://snapshots.kjnodes.com/jackal/genesis.json > $HOME/.canine/config/genesis.json
curl -Ls https://snapshots.kjnodes.com/jackal/addrbook.json > $HOME/.canine/config/addrbook.json

# Add seeds
sed -i -e "s|^seeds *=.*|seeds = \"400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@jackal.rpc.kjnodes.com:37659\"|" $HOME/.canine/config/config.toml

# Set minimum gas price
sed -i -e "s|^minimum-gas-prices *=.*|minimum-gas-prices = \"0.002ujkl\"|" $HOME/.canine/config/app.toml

# Set pruning
sed -i \
  -e 's|^pruning *=.*|pruning = "custom"|' \
  -e 's|^pruning-keep-recent *=.*|pruning-keep-recent = "100"|' \
  -e 's|^pruning-keep-every *=.*|pruning-keep-every = "0"|' \
  -e 's|^pruning-interval *=.*|pruning-interval = "19"|' \
  $HOME/.canine/config/app.toml

# Set custom ports
sed -i -e "s%^proxy_app = \"tcp://127.0.0.1:26658\"%proxy_app = \"tcp://127.0.0.1:37658\"%; s%^laddr = \"tcp://127.0.0.1:26657\"%laddr = \"tcp://127.0.0.1:37657\"%; s%^pprof_laddr = \"localhost:6060\"%pprof_laddr = \"localhost:37060\"%; s%^laddr = \"tcp://0.0.0.0:26656\"%laddr = \"tcp://0.0.0.0:37656\"%; s%^prometheus_listen_addr = \":26660\"%prometheus_listen_addr = \":37660\"%" $HOME/.canine/config/config.toml
sed -i -e "s%^address = \"tcp://0.0.0.0:1317\"%address = \"tcp://0.0.0.0:37317\"%; s%^address = \":8080\"%address = \":37080\"%; s%^address = \"0.0.0.0:9090\"%address = \"0.0.0.0:37090\"%; s%^address = \"0.0.0.0:9091\"%address = \"0.0.0.0:37091\"%; s%^address = \"0.0.0.0:8545\"%address = \"0.0.0.0:37545\"%; s%^ws-address = \"0.0.0.0:8546\"%ws-address = \"0.0.0.0:37546\"%" $HOME/.canine/config/app.toml
```

### Download latest chain snapshot

```bash
curl -L https://snapshots.kjnodes.com/jackal/snapshot_latest.tar.lz4 | tar -Ilz4 -xf - -C $HOME/.canine
[[ -f $HOME/.canine/data/upgrade-info.json ]] && cp $HOME/.canine/data/upgrade-info.json $HOME/.canine/cosmovisor/genesis/upgrade-info.json
```

### Start service and check the logs

```bash
sudo systemctl start canined && sudo journalctl -u canined -f --no-hostname -o cat
```
