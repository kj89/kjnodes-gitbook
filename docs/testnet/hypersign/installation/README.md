---
description: Setting up your validator node has never been so easy. Get your validator running in minutes by following step by step instructions.
---

# Installation

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/hypersign.png" alt=""><figcaption></figcaption></figure>

**Chain ID**: jagrat | **Latest Version Tag**: v0.1.7 | **Custom Port**: 131

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
rm -rf hid-node
git clone https://github.com/hypersign-protocol/hid-node.git
cd hid-node
git checkout v0.1.7

# Build binaries
make build

# Prepare binaries for Cosmovisor
mkdir -p $HOME/.hid-node/cosmovisor/genesis/bin
mv build/hid-noded $HOME/.hid-node/cosmovisor/genesis/bin/
rm -rf build

# Create application symlinks
sudo ln -s $HOME/.hid-node/cosmovisor/genesis $HOME/.hid-node/cosmovisor/current -f
sudo ln -s $HOME/.hid-node/cosmovisor/current/bin/hid-noded /usr/local/bin/hid-noded -f
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
Environment="PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:$HOME/.hid-node/cosmovisor/current/bin"

[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable hid-noded
```

### Initialize the node

```bash
# Initialize the node
hid-noded init $MONIKER --chain-id jagrat

# Download genesis and addrbook
curl -Ls https://snapshots.kjnodes.com/hypersign-testnet/genesis.json > $HOME/.hid-node/config/genesis.json
curl -Ls https://snapshots.kjnodes.com/hypersign-testnet/addrbook.json > $HOME/.hid-node/config/addrbook.json

# Add seeds
sed -i -e "s|^seeds *=.*|seeds = \"3f472746f46493309650e5a033076689996c8881@hypersign-testnet.rpc.kjnodes.com:13159\"|" $HOME/.hid-node/config/config.toml

# Set minimum gas price
sed -i -e "s|^minimum-gas-prices *=.*|minimum-gas-prices = \"0uhid\"|" $HOME/.hid-node/config/app.toml

# Set pruning
sed -i \
  -e 's|^pruning *=.*|pruning = "custom"|' \
  -e 's|^pruning-keep-recent *=.*|pruning-keep-recent = "100"|' \
  -e 's|^pruning-keep-every *=.*|pruning-keep-every = "0"|' \
  -e 's|^pruning-interval *=.*|pruning-interval = "19"|' \
  $HOME/.hid-node/config/app.toml

# Set custom ports
sed -i -e "s%^proxy_app = \"tcp://127.0.0.1:26658\"%proxy_app = \"tcp://127.0.0.1:13158\"%; s%^laddr = \"tcp://127.0.0.1:26657\"%laddr = \"tcp://127.0.0.1:13157\"%; s%^pprof_laddr = \"localhost:6060\"%pprof_laddr = \"localhost:13160\"%; s%^laddr = \"tcp://0.0.0.0:26656\"%laddr = \"tcp://0.0.0.0:13156\"%; s%^prometheus_listen_addr = \":26660\"%prometheus_listen_addr = \":13166\"%" $HOME/.hid-node/config/config.toml
sed -i -e "s%^address = \"tcp://0.0.0.0:1317\"%address = \"tcp://0.0.0.0:13117\"%; s%^address = \":8080\"%address = \":13180\"%; s%^address = \"0.0.0.0:9090\"%address = \"0.0.0.0:13190\"%; s%^address = \"0.0.0.0:9091\"%address = \"0.0.0.0:13191\"%; s%:8545%:13145%; s%:8546%:13146%; s%:6065%:13165%" $HOME/.hid-node/config/app.toml
```

### Download latest chain snapshot

```bash
curl -L https://snapshots.kjnodes.com/hypersign-testnet/snapshot_latest.tar.lz4 | tar -Ilz4 -xf - -C $HOME/.hid-node
[[ -f $HOME/.hid-node/data/upgrade-info.json ]] && cp $HOME/.hid-node/data/upgrade-info.json $HOME/.hid-node/cosmovisor/genesis/upgrade-info.json
```

### Start service and check the logs

```bash
sudo systemctl start hid-noded && sudo journalctl -u hid-noded -f --no-hostname -o cat
```
