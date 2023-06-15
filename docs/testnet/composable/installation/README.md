---
description: Setting up your validator node has never been so easy. Get your validator running in minutes by following step by step instructions.
---

# Installation

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/composable.png" alt=""><figcaption></figcaption></figure>

**Chain ID**: banksy-testnet-3 | **Latest Version Tag**: v3.0.3-testnet | **Custom Port**: 159

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
curl -Ls https://go.dev/dl/go1.20.5.linux-amd64.tar.gz | sudo tar -xzf - -C /usr/local
eval $(echo 'export PATH=$PATH:/usr/local/go/bin' | sudo tee /etc/profile.d/golang.sh)
eval $(echo 'export PATH=$PATH:$HOME/go/bin' | tee -a $HOME/.profile)
```

### Download and build binaries

```bash
# Clone project repository
cd $HOME
rm -rf composable-testnet
git clone https://github.com/notional-labs/composable-testnet.git
cd composable-testnet
git checkout v3.0.3-testnet

# Build binaries
make build

# Prepare binaries for Cosmovisor
mkdir -p $HOME/.banksy/cosmovisor/genesis/bin
mv bin/centaurid $HOME/.banksy/cosmovisor/genesis/bin/
rm -rf build

# Create application symlinks
sudo ln -s $HOME/.banksy/cosmovisor/genesis $HOME/.banksy/cosmovisor/current -f
sudo ln -s $HOME/.banksy/cosmovisor/current/bin/centaurid /usr/local/bin/centaurid -f
```

### Install Cosmovisor and create a service

```bash
# Download and install Cosmovisor
go install cosmossdk.io/tools/cosmovisor/cmd/cosmovisor@v1.4.0

# Create service
sudo tee /etc/systemd/system/centaurid.service > /dev/null << EOF
[Unit]
Description=composable-testnet node service
After=network-online.target

[Service]
User=$USER
ExecStart=$(which cosmovisor) run start
Restart=on-failure
RestartSec=10
LimitNOFILE=65535
Environment="DAEMON_HOME=$HOME/.banksy"
Environment="DAEMON_NAME=centaurid"
Environment="UNSAFE_SKIP_BACKUP=true"
Environment="PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:$HOME/.banksy/cosmovisor/current/bin"

[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable centaurid
```

### Initialize the node

```bash
# Set node configuration
centaurid config chain-id banksy-testnet-3
centaurid config keyring-backend test
centaurid config node tcp://localhost:15957

# Initialize the node
centaurid init $MONIKER --chain-id banksy-testnet-3

# Download genesis and addrbook
curl -Ls https://snapshots.kjnodes.com/composable-testnet/genesis.json > $HOME/.banksy/config/genesis.json
curl -Ls https://snapshots.kjnodes.com/composable-testnet/addrbook.json > $HOME/.banksy/config/addrbook.json

# Add seeds
sed -i -e "s|^seeds *=.*|seeds = \"3f472746f46493309650e5a033076689996c8881@composable-testnet.rpc.kjnodes.com:15959\"|" $HOME/.banksy/config/config.toml

# Set minimum gas price
sed -i -e "s|^minimum-gas-prices *=.*|minimum-gas-prices = \"0ppica\"|" $HOME/.banksy/config/app.toml

# Set pruning
sed -i \
  -e 's|^pruning *=.*|pruning = "custom"|' \
  -e 's|^pruning-keep-recent *=.*|pruning-keep-recent = "100"|' \
  -e 's|^pruning-keep-every *=.*|pruning-keep-every = "0"|' \
  -e 's|^pruning-interval *=.*|pruning-interval = "19"|' \
  $HOME/.banksy/config/app.toml

# Set custom ports
sed -i -e "s%^proxy_app = \"tcp://127.0.0.1:26658\"%proxy_app = \"tcp://127.0.0.1:15958\"%; s%^laddr = \"tcp://127.0.0.1:26657\"%laddr = \"tcp://127.0.0.1:15957\"%; s%^pprof_laddr = \"localhost:6060\"%pprof_laddr = \"localhost:15960\"%; s%^laddr = \"tcp://0.0.0.0:26656\"%laddr = \"tcp://0.0.0.0:15956\"%; s%^prometheus_listen_addr = \":26660\"%prometheus_listen_addr = \":15966\"%" $HOME/.banksy/config/config.toml
sed -i -e "s%^address = \"tcp://0.0.0.0:1317\"%address = \"tcp://0.0.0.0:15917\"%; s%^address = \":8080\"%address = \":15980\"%; s%^address = \"0.0.0.0:9090\"%address = \"0.0.0.0:15990\"%; s%^address = \"0.0.0.0:9091\"%address = \"0.0.0.0:15991\"%; s%:8545%:15945%; s%:8546%:15946%; s%:6065%:15965%" $HOME/.banksy/config/app.toml
```

### Download latest chain snapshot

```bash
curl -L https://snapshots.kjnodes.com/composable-testnet/snapshot_latest.tar.lz4 | tar -Ilz4 -xf - -C $HOME/.banksy
[[ -f $HOME/.banksy/data/upgrade-info.json ]] && cp $HOME/.banksy/data/upgrade-info.json $HOME/.banksy/cosmovisor/genesis/upgrade-info.json
```

### Start service and check the logs

```bash
sudo systemctl start centaurid && sudo journalctl -u centaurid -f --no-hostname -o cat
```
