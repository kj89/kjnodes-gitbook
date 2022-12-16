---
description: Setting up your validator node has never been so easy. Get your validator running in minutes by following step by step instructions.
---

# Installation

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/bitcanna.png" width="150" alt=""><figcaption></figcaption></figure>

**Chain ID**: bitcanna-1 | **Latest Version Tag**: v1.5.3 | **Custom Port**: 42

### Setup validator name

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
sudo curl -Ls https://go.dev/dl/go1.19.linux-amd64.tar.gz | sudo tar -C /usr/local -xz
tee -a $HOME/.profile > /dev/null << EOF
export PATH=$PATH:/usr/local/go/bin
EOF
source $HOME/.profile
```

### Download and build binaries

```bash
# Clone project repository
cd $HOME
rm -rf bcna
git clone https://github.com/BitCannaGlobal/bcna.git
cd bcna

# Build binaries
git checkout v1.5.3
make build
mkdir -p $HOME/.bcna/cosmovisor/genesis/bin
mv build/bcnad $HOME/.bcna/cosmovisor/genesis/bin/
rm -rf build
```

### Install Cosmovisor and create a service

```bash
# Download and install Cosmovisor
curl -Ls https://github.com/cosmos/cosmos-sdk/releases/download/cosmovisor%2Fv1.3.0/cosmovisor-v1.3.0-linux-amd64.tar.gz | tar xz
chmod 755 cosmovisor
sudo mv cosmovisor /usr/bin/cosmovisor

# Create service
sudo tee /etc/systemd/system/bcnad.service > /dev/null << EOF
[Unit]
Description=bitcanna node service
After=network-online.target
[Service]
User=$USER
ExecStart=/usr/bin/cosmovisor run start
Restart=on-failure
RestartSec=10
LimitNOFILE=65535
Environment="DAEMON_HOME=$HOME/.bcna"
Environment="DAEMON_NAME=bcnad"
Environment="UNSAFE_SKIP_BACKUP=true"
[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable bcnad

# Create application symlinks
ln -s $HOME/.bcna/cosmovisor/genesis $HOME/.bcna/cosmovisor/current
sudo ln -s $HOME/.bcna/cosmovisor/current/bin/bcnad /usr/local/bin/bcnad
```

### Initialize the node

```bash
# Set node configuration
bcnad config chain-id bitcanna-1
bcnad config keyring-backend file
bcnad config node tcp://localhost:42657

# Initialize the node
bcnad init $MONIKER --chain-id bitcanna-1

# Download genesis and addrbook
curl -Ls https://snapshots.kjnodes.com/bitcanna/genesis.json > $HOME/.bcna/config/genesis.json
curl -Ls https://snapshots.kjnodes.com/bitcanna/addrbook.json > $HOME/.bcna/config/addrbook.json

# Add seeds
sed -i -e "s|^seeds *=.*|seeds = \"400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@bitcanna.rpc.kjnodes.com:42659\"|" $HOME/.bcna/config/config.toml

# Set minimum gas price
sed -i -e "s|^minimum-gas-prices *=.*|minimum-gas-prices = \"0ubcna\"|" $HOME/.bcna/config/app.toml

# Set pruning
sed -i -e "s|^pruning *=.*|pruning = \"custom\"|" $HOME/.bcna/config/app.toml
sed -i -e "s|^pruning-keep-recent *=.*|pruning-keep-recent = \"100\"|" $HOME/.bcna/config/app.toml
sed -i -e "s|^pruning-keep-every *=.*|pruning-keep-every = \"0\"|" $HOME/.bcna/config/app.toml
sed -i -e "s|^pruning-interval *=.*|pruning-interval = \"19\"|" $HOME/.bcna/config/app.toml

# Set custom ports
sed -i.bak -e "s%^proxy_app = \"tcp://127.0.0.1:26658\"%proxy_app = \"tcp://127.0.0.1:42658\"%; s%^laddr = \"tcp://127.0.0.1:26657\"%laddr = \"tcp://127.0.0.1:42657\"%; s%^pprof_laddr = \"localhost:6060\"%pprof_laddr = \"localhost:42060\"%; s%^laddr = \"tcp://0.0.0.0:26656\"%laddr = \"tcp://0.0.0.0:42656\"%; s%^prometheus_listen_addr = \":26660\"%prometheus_listen_addr = \":42660\"%" $HOME/.bcna/config/config.toml
sed -i.bak -e "s%^address = \"tcp://0.0.0.0:1317\"%address = \"tcp://0.0.0.0:42317\"%; s%^address = \":8080\"%address = \":42080\"%; s%^address = \"0.0.0.0:9090\"%address = \"0.0.0.0:42090\"%; s%^address = \"0.0.0.0:9091\"%address = \"0.0.0.0:42091\"%; s%^address = \"0.0.0.0:8545\"%address = \"0.0.0.0:42545\"%; s%^ws-address = \"0.0.0.0:8546\"%ws-address = \"0.0.0.0:42546\"%" $HOME/.bcna/config/app.toml
```

### Download latest chain snapshot

```bash
curl -L https://snapshots.kjnodes.com/bitcanna/snapshot_latest.tar.lz4 | lz4 -dc - | tar -xf - -C $HOME/.bcna
```

### Start service and check the logs

```bash
sudo systemctl start bcnad && journalctl -u bcnad -f --no-hostname -o cat
```
