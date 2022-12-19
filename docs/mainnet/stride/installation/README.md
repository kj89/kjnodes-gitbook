---
description: Setting up your validator node has never been so easy. Get your validator running in minutes by following step by step instructions.
---

# Installation

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/stride.png" width="150" alt=""><figcaption></figcaption></figure>

**Chain ID**: stride-1 | **Latest Version Tag**: v4.0.2 | **Custom Port**: 16

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
rm -rf stride
git clone https://github.com/Stride-Labs/stride.git
cd stride

# Build binaries
git checkout v4.0.2
make build
mkdir -p $HOME/.stride/cosmovisor/genesis/bin
mv build/strided $HOME/.stride/cosmovisor/genesis/bin/
rm -rf build
```

### Install Cosmovisor and create a service

```bash
# Download and install Cosmovisor
go install github.com/cosmos/cosmos-sdk/cosmovisor/cmd/cosmovisor@1.4.0

# Create service
sudo tee /etc/systemd/system/strided.service > /dev/null << EOF
[Unit]
Description=stride node service
After=network-online.target
[Service]
User=$USER
ExecStart=/usr/bin/cosmovisor run start
Restart=on-failure
RestartSec=10
LimitNOFILE=65535
Environment="DAEMON_HOME=$HOME/.stride"
Environment="DAEMON_NAME=strided"
Environment="UNSAFE_SKIP_BACKUP=true"
[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable strided

# Create application symlinks
ln -s $HOME/.stride/cosmovisor/genesis $HOME/.stride/cosmovisor/current
sudo ln -s $HOME/.stride/cosmovisor/current/bin/strided /usr/local/bin/strided
```

### Initialize the node

```bash
# Set node configuration
strided config chain-id stride-1
strided config keyring-backend file
strided config node tcp://localhost:16657

# Initialize the node
strided init $MONIKER --chain-id stride-1

# Download genesis and addrbook
curl -Ls https://snapshots.kjnodes.com/stride/genesis.json > $HOME/.stride/config/genesis.json
curl -Ls https://snapshots.kjnodes.com/stride/addrbook.json > $HOME/.stride/config/addrbook.json

# Add seeds
sed -i -e "s|^seeds *=.*|seeds = \"400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@stride.rpc.kjnodes.com:16659\"|" $HOME/.stride/config/config.toml

# Set minimum gas price
sed -i -e "s|^minimum-gas-prices *=.*|minimum-gas-prices = \"0ustrd\"|" $HOME/.stride/config/app.toml

# Set pruning
sed -i -e "s|^pruning *=.*|pruning = \"custom\"|" $HOME/.stride/config/app.toml
sed -i -e "s|^pruning-keep-recent *=.*|pruning-keep-recent = \"100\"|" $HOME/.stride/config/app.toml
sed -i -e "s|^pruning-keep-every *=.*|pruning-keep-every = \"0\"|" $HOME/.stride/config/app.toml
sed -i -e "s|^pruning-interval *=.*|pruning-interval = \"19\"|" $HOME/.stride/config/app.toml

# Set custom ports
sed -i.bak -e "s%^proxy_app = \"tcp://127.0.0.1:26658\"%proxy_app = \"tcp://127.0.0.1:16658\"%; s%^laddr = \"tcp://127.0.0.1:26657\"%laddr = \"tcp://127.0.0.1:16657\"%; s%^pprof_laddr = \"localhost:6060\"%pprof_laddr = \"localhost:16060\"%; s%^laddr = \"tcp://0.0.0.0:26656\"%laddr = \"tcp://0.0.0.0:16656\"%; s%^prometheus_listen_addr = \":26660\"%prometheus_listen_addr = \":16660\"%" $HOME/.stride/config/config.toml
sed -i.bak -e "s%^address = \"tcp://0.0.0.0:1317\"%address = \"tcp://0.0.0.0:16317\"%; s%^address = \":8080\"%address = \":16080\"%; s%^address = \"0.0.0.0:9090\"%address = \"0.0.0.0:16090\"%; s%^address = \"0.0.0.0:9091\"%address = \"0.0.0.0:16091\"%; s%^address = \"0.0.0.0:8545\"%address = \"0.0.0.0:16545\"%; s%^ws-address = \"0.0.0.0:8546\"%ws-address = \"0.0.0.0:16546\"%" $HOME/.stride/config/app.toml
```

### Download latest chain snapshot

```bash
curl -L https://snapshots.kjnodes.com/stride/snapshot_latest.tar.lz4 | lz4 -dc - | tar -xf - -C $HOME/.stride
```

### Start service and check the logs

```bash
sudo systemctl start strided && journalctl -u strided -f --no-hostname -o cat
```
