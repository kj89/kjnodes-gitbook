---
description: Setting up your validator node has never been so easy. Get your validator running in minutes by following step by step instructions.
---

# Installation

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/migaloo.png" alt=""><figcaption></figcaption></figure>

**Chain ID**: migaloo-1 | **Latest Version Tag**: v2.0.5 | **Custom Port**: 149

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
rm -rf migaloo-chain
git clone https://github.com/White-Whale-Defi-Platform/migaloo-chain.git
cd migaloo-chain
git checkout v2.0.5

# Build binaries
make build

# Prepare binaries for Cosmovisor
mkdir -p $HOME/.migalood/cosmovisor/genesis/bin
mv bin/migalood $HOME/.migalood/cosmovisor/genesis/bin/
rm -rf build

# Create application symlinks
sudo ln -s $HOME/.migalood/cosmovisor/genesis $HOME/.migalood/cosmovisor/current -f
sudo ln -s $HOME/.migalood/cosmovisor/current/bin/migalood /usr/local/bin/migalood -f
```

### Install Cosmovisor and create a service

```bash
# Download and install Cosmovisor
go install cosmossdk.io/tools/cosmovisor/cmd/cosmovisor@v1.4.0

# Create service
sudo tee /etc/systemd/system/migalood.service > /dev/null << EOF
[Unit]
Description=migaloo node service
After=network-online.target

[Service]
User=$USER
ExecStart=$(which cosmovisor) run start
Restart=on-failure
RestartSec=10
LimitNOFILE=65535
Environment="DAEMON_HOME=$HOME/.migalood"
Environment="DAEMON_NAME=migalood"
Environment="UNSAFE_SKIP_BACKUP=true"
Environment="PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:$HOME/.migalood/cosmovisor/current/bin"

[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable migalood
```

### Initialize the node

```bash
# Set node configuration
migalood config chain-id migaloo-1
migalood config keyring-backend file
migalood config node tcp://localhost:14957

# Initialize the node
migalood init $MONIKER --chain-id migaloo-1

# Download genesis and addrbook
curl -Ls https://snapshots.kjnodes.com/migaloo/genesis.json > $HOME/.migalood/config/genesis.json
curl -Ls https://snapshots.kjnodes.com/migaloo/addrbook.json > $HOME/.migalood/config/addrbook.json

# Add seeds
sed -i -e "s|^seeds *=.*|seeds = \"400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@migaloo.rpc.kjnodes.com:14959\"|" $HOME/.migalood/config/config.toml

# Set minimum gas price
sed -i -e "s|^minimum-gas-prices *=.*|minimum-gas-prices = \"0.25uwhale\"|" $HOME/.migalood/config/app.toml

# Set pruning
sed -i \
  -e 's|^pruning *=.*|pruning = "custom"|' \
  -e 's|^pruning-keep-recent *=.*|pruning-keep-recent = "100"|' \
  -e 's|^pruning-keep-every *=.*|pruning-keep-every = "0"|' \
  -e 's|^pruning-interval *=.*|pruning-interval = "19"|' \
  $HOME/.migalood/config/app.toml

# Set custom ports
sed -i -e "s%^proxy_app = \"tcp://127.0.0.1:26658\"%proxy_app = \"tcp://127.0.0.1:14958\"%; s%^laddr = \"tcp://127.0.0.1:26657\"%laddr = \"tcp://127.0.0.1:14957\"%; s%^pprof_laddr = \"localhost:6060\"%pprof_laddr = \"localhost:14960\"%; s%^laddr = \"tcp://0.0.0.0:26656\"%laddr = \"tcp://0.0.0.0:14956\"%; s%^prometheus_listen_addr = \":26660\"%prometheus_listen_addr = \":14966\"%" $HOME/.migalood/config/config.toml
sed -i -e "s%^address = \"tcp://0.0.0.0:1317\"%address = \"tcp://0.0.0.0:14917\"%; s%^address = \":8080\"%address = \":14980\"%; s%^address = \"0.0.0.0:9090\"%address = \"0.0.0.0:14990\"%; s%^address = \"0.0.0.0:9091\"%address = \"0.0.0.0:14991\"%; s%:8545%:14945%; s%:8546%:14946%; s%:6065%:14965%" $HOME/.migalood/config/app.toml
```

### Download latest chain snapshot

```bash
curl -L https://snapshots.kjnodes.com/migaloo/snapshot_latest.tar.lz4 | tar -Ilz4 -xf - -C $HOME/.migalood
[[ -f $HOME/.migalood/data/upgrade-info.json ]] && cp $HOME/.migalood/data/upgrade-info.json $HOME/.migalood/cosmovisor/genesis/upgrade-info.json
```

### Start service and check the logs

```bash
sudo systemctl start migalood && sudo journalctl -u migalood -f --no-hostname -o cat
```
