---
description: Setting up your validator node has never been so easy. Get your validator running in minutes by following step by step instructions.
---

# Installation

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/bitcanna.png" alt=""><figcaption></figcaption></figure>

**Chain ID**: bitcanna-1 | **Latest Version Tag**: v1.7.0 | **Custom Port**: 142

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
rm -rf bcna
git clone https://github.com/BitCannaGlobal/bcna.git
cd bcna
git checkout v1.7.0

# Build binaries
make build

# Prepare binaries for Cosmovisor
mkdir -p $HOME/.bcna/cosmovisor/genesis/bin
mv build/bcnad $HOME/.bcna/cosmovisor/genesis/bin/
rm -rf build

# Create application symlinks
sudo ln -s $HOME/.bcna/cosmovisor/genesis $HOME/.bcna/cosmovisor/current -f
sudo ln -s $HOME/.bcna/cosmovisor/current/bin/bcnad /usr/local/bin/bcnad -f
```

### Install Cosmovisor and create a service

```bash
# Download and install Cosmovisor
go install cosmossdk.io/tools/cosmovisor/cmd/cosmovisor@v1.4.0

# Create service
sudo tee /etc/systemd/system/bcnad.service > /dev/null << EOF
[Unit]
Description=bitcanna node service
After=network-online.target

[Service]
User=$USER
ExecStart=$(which cosmovisor) run start
Restart=on-failure
RestartSec=10
LimitNOFILE=65535
Environment="DAEMON_HOME=$HOME/.bcna"
Environment="DAEMON_NAME=bcnad"
Environment="UNSAFE_SKIP_BACKUP=true"
Environment="PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:$HOME/.bcna/cosmovisor/current/bin"

[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable bcnad
```

### Initialize the node

```bash
# Set node configuration
bcnad config chain-id bitcanna-1
bcnad config keyring-backend file
bcnad config node tcp://localhost:14257

# Initialize the node
bcnad init $MONIKER --chain-id bitcanna-1

# Download genesis and addrbook
curl -Ls https://snapshots.kjnodes.com/bitcanna/genesis.json > $HOME/.bcna/config/genesis.json
curl -Ls https://snapshots.kjnodes.com/bitcanna/addrbook.json > $HOME/.bcna/config/addrbook.json

# Add seeds
sed -i -e "s|^seeds *=.*|seeds = \"400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@bitcanna.rpc.kjnodes.com:14259\"|" $HOME/.bcna/config/config.toml

# Set minimum gas price
sed -i -e "s|^minimum-gas-prices *=.*|minimum-gas-prices = \"0ubcna\"|" $HOME/.bcna/config/app.toml

# Set pruning
sed -i \
  -e 's|^pruning *=.*|pruning = "custom"|' \
  -e 's|^pruning-keep-recent *=.*|pruning-keep-recent = "100"|' \
  -e 's|^pruning-keep-every *=.*|pruning-keep-every = "0"|' \
  -e 's|^pruning-interval *=.*|pruning-interval = "19"|' \
  $HOME/.bcna/config/app.toml

# Set custom ports
sed -i -e "s%^proxy_app = \"tcp://127.0.0.1:26658\"%proxy_app = \"tcp://127.0.0.1:14258\"%; s%^laddr = \"tcp://127.0.0.1:26657\"%laddr = \"tcp://127.0.0.1:14257\"%; s%^pprof_laddr = \"localhost:6060\"%pprof_laddr = \"localhost:14260\"%; s%^laddr = \"tcp://0.0.0.0:26656\"%laddr = \"tcp://0.0.0.0:14256\"%; s%^prometheus_listen_addr = \":26660\"%prometheus_listen_addr = \":14266\"%" $HOME/.bcna/config/config.toml
sed -i -e "s%^address = \"tcp://0.0.0.0:1317\"%address = \"tcp://0.0.0.0:14217\"%; s%^address = \":8080\"%address = \":14280\"%; s%^address = \"0.0.0.0:9090\"%address = \"0.0.0.0:14290\"%; s%^address = \"0.0.0.0:9091\"%address = \"0.0.0.0:14291\"%; s%:8545%:14245%; s%:8546%:14246%; s%:6065%:14265%" $HOME/.bcna/config/app.toml
```

### Download latest chain snapshot

```bash
curl -L https://snapshots.kjnodes.com/bitcanna/snapshot_latest.tar.lz4 | tar -Ilz4 -xf - -C $HOME/.bcna
[[ -f $HOME/.bcna/data/upgrade-info.json ]] && cp $HOME/.bcna/data/upgrade-info.json $HOME/.bcna/cosmovisor/genesis/upgrade-info.json
```

### Start service and check the logs

```bash
sudo systemctl start bcnad && sudo journalctl -u bcnad -f --no-hostname -o cat
```
