---
description: Setting up your validator node has never been so easy. Get your validator running in minutes by following step by step instructions.
---

# Installation

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/hypersign.png" width="150" alt=""><figcaption></figcaption></figure>

**Chain ID**: jagrat | **Latest Version Tag**: v0.1.5 | **Custom Port**: 31

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
rm -rf hid-node
git clone https://github.com/hypersign-protocol/hid-node.git
cd hid-node

# Build binaries
git checkout v0.1.5
make build
mkdir -p $HOME/.hid-node/cosmovisor/genesis/bin
mv build/hid-noded $HOME/.hid-node/cosmovisor/genesis/bin/
rm -rf build
```

### Install Cosmovisor and create a service

```bash
# Download and install Cosmovisor
go install cosmossdk.io/tools/cosmovisor/cmd/cosmovisor@v1.4.0

# Create service
sudo tee /etc/systemd/system/hid-noded.service > /dev/null << EOF
[Unit]
Description=hypersign-testnet node service
After=network-online.target
[Service]
User=$USER
ExecStart=$(which cosmovisor) run start
Restart=on-failure
RestartSec=10
LimitNOFILE=65535
Environment="DAEMON_HOME=$HOME/.hid-node"
Environment="DAEMON_NAME=hid-noded"
Environment="UNSAFE_SKIP_BACKUP=true"
[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable hid-noded

# Create application symlinks
ln -s $HOME/.hid-node/cosmovisor/genesis $HOME/.hid-node/cosmovisor/current
sudo ln -s $HOME/.hid-node/cosmovisor/current/bin/hid-noded /usr/local/bin/hid-noded
```

### Initialize the node

```bash
# Set node configuration
hid-noded config chain-id jagrat
hid-noded config keyring-backend test
hid-noded config node tcp://localhost:31657

# Initialize the node
hid-noded init $MONIKER --chain-id jagrat

# Download genesis and addrbook
curl -Ls https://snapshots.kjnodes.com/hypersign-testnet/genesis.json > $HOME/.hid-node/config/genesis.json
curl -Ls https://snapshots.kjnodes.com/hypersign-testnet/addrbook.json > $HOME/.hid-node/config/addrbook.json

# Add seeds
sed -i -e "s|^seeds *=.*|seeds = \"3f472746f46493309650e5a033076689996c8881@hypersign-testnet.rpc.kjnodes.com:31659\"|" $HOME/.hid-node/config/config.toml

# Set minimum gas price
sed -i -e "s|^minimum-gas-prices *=.*|minimum-gas-prices = \"0uhid\"|" $HOME/.hid-node/config/app.toml

# Set pruning
sed -i -e "s|^pruning *=.*|pruning = \"custom\"|" $HOME/.hid-node/config/app.toml
sed -i -e "s|^pruning-keep-recent *=.*|pruning-keep-recent = \"100\"|" $HOME/.hid-node/config/app.toml
sed -i -e "s|^pruning-keep-every *=.*|pruning-keep-every = \"0\"|" $HOME/.hid-node/config/app.toml
sed -i -e "s|^pruning-interval *=.*|pruning-interval = \"19\"|" $HOME/.hid-node/config/app.toml

# Set custom ports
sed -i.bak -e "s%^proxy_app = \"tcp://127.0.0.1:26658\"%proxy_app = \"tcp://127.0.0.1:31658\"%; s%^laddr = \"tcp://127.0.0.1:26657\"%laddr = \"tcp://127.0.0.1:31657\"%; s%^pprof_laddr = \"localhost:6060\"%pprof_laddr = \"localhost:31060\"%; s%^laddr = \"tcp://0.0.0.0:26656\"%laddr = \"tcp://0.0.0.0:31656\"%; s%^prometheus_listen_addr = \":26660\"%prometheus_listen_addr = \":31660\"%" $HOME/.hid-node/config/config.toml
sed -i.bak -e "s%^address = \"tcp://0.0.0.0:1317\"%address = \"tcp://0.0.0.0:31317\"%; s%^address = \":8080\"%address = \":31080\"%; s%^address = \"0.0.0.0:9090\"%address = \"0.0.0.0:31090\"%; s%^address = \"0.0.0.0:9091\"%address = \"0.0.0.0:31091\"%; s%^address = \"0.0.0.0:8545\"%address = \"0.0.0.0:31545\"%; s%^ws-address = \"0.0.0.0:8546\"%ws-address = \"0.0.0.0:31546\"%" $HOME/.hid-node/config/app.toml
```

### Download latest chain snapshot

```bash
curl -L https://snapshots.kjnodes.com/hypersign-testnet/snapshot_latest.tar.lz4 | lz4 -dc - | tar -xf - -C $HOME/.hid-node
```

### Start service and check the logs

```bash
sudo systemctl start hid-noded && journalctl -u hid-noded -f --no-hostname -o cat
```
