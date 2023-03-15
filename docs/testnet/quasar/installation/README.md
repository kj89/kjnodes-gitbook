---
description: Setting up your validator node has never been so easy. Get your validator running in minutes by following step by step instructions.
---

# Installation

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/quasar.png" width="150" alt=""><figcaption></figcaption></figure>

**Chain ID**: qsr-questnet-04 | **Latest Version Tag**: v0.0.2-alpha-11 | **Custom Port**: 48

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
curl -Ls https://go.dev/dl/go1.19.5.linux-amd64.tar.gz | sudo tar -xzf - -C /usr/local
eval $(echo 'export PATH=$PATH:/usr/local/go/bin' | sudo tee /etc/profile.d/golang.sh)
eval $(echo 'export PATH=$PATH:$HOME/go/bin' | tee -a $HOME/.profile)
```

### Download and build binaries

```bash
# Download project binaries
mkdir -p $HOME/.quasarnode/cosmovisor/genesis/bin
wget -O $HOME/.quasarnode/cosmovisor/genesis/bin/quasard https://github.com/quasar-finance/binary-release/raw/main/v0.0.2-alpha-11/quasarnoded-linux-amd64
chmod +x $HOME/.quasarnode/cosmovisor/genesis/bin/*

# Create application symlinks
ln -s $HOME/.quasarnode/cosmovisor/genesis $HOME/.quasarnode/cosmovisor/current
sudo ln -s $HOME/.quasarnode/cosmovisor/current/bin/quasard /usr/local/bin/quasard
```

### Install Cosmovisor and create a service

```bash
# Download and install Cosmovisor
go install cosmossdk.io/tools/cosmovisor/cmd/cosmovisor@v1.4.0

# Create service
sudo tee /etc/systemd/system/quasard.service > /dev/null << EOF
[Unit]
Description=quasar-testnet node service
After=network-online.target

[Service]
User=$USER
ExecStart=$(which cosmovisor) run start
Restart=on-failure
RestartSec=10
LimitNOFILE=65535
Environment="DAEMON_HOME=$HOME/.quasarnode"
Environment="DAEMON_NAME=quasard"
Environment="UNSAFE_SKIP_BACKUP=true"

[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable quasard
```

### Initialize the node

```bash
# Set node configuration
quasard config chain-id qsr-questnet-04
quasard config keyring-backend test
quasard config node tcp://localhost:48657

# Initialize the node
quasard init $MONIKER --chain-id qsr-questnet-04

# Download genesis and addrbook
curl -Ls https://snapshots.kjnodes.com/quasar-testnet/genesis.json > $HOME/.quasarnode/config/genesis.json
curl -Ls https://snapshots.kjnodes.com/quasar-testnet/addrbook.json > $HOME/.quasarnode/config/addrbook.json

# Add seeds
sed -i -e "s|^seeds *=.*|seeds = \"3f472746f46493309650e5a033076689996c8881@quasar-testnet.rpc.kjnodes.com:48659\"|" $HOME/.quasarnode/config/config.toml

# Set minimum gas price
sed -i -e "s|^minimum-gas-prices *=.*|minimum-gas-prices = \"0uqsr\"|" $HOME/.quasarnode/config/app.toml

# Set pruning
sed -i \
  -e 's|^pruning *=.*|pruning = "custom"|' \
  -e 's|^pruning-keep-recent *=.*|pruning-keep-recent = "100"|' \
  -e 's|^pruning-keep-every *=.*|pruning-keep-every = "0"|' \
  -e 's|^pruning-interval *=.*|pruning-interval = "19"|' \
  $HOME/.quasarnode/config/app.toml

# Set custom ports
sed -i -e "s%^proxy_app = \"tcp://127.0.0.1:26658\"%proxy_app = \"tcp://127.0.0.1:48658\"%; s%^laddr = \"tcp://127.0.0.1:26657\"%laddr = \"tcp://127.0.0.1:48657\"%; s%^pprof_laddr = \"localhost:6060\"%pprof_laddr = \"localhost:48060\"%; s%^laddr = \"tcp://0.0.0.0:26656\"%laddr = \"tcp://0.0.0.0:48656\"%; s%^prometheus_listen_addr = \":26660\"%prometheus_listen_addr = \":48660\"%" $HOME/.quasarnode/config/config.toml
sed -i -e "s%^address = \"tcp://0.0.0.0:1317\"%address = \"tcp://0.0.0.0:48317\"%; s%^address = \":8080\"%address = \":48080\"%; s%^address = \"0.0.0.0:9090\"%address = \"0.0.0.0:48090\"%; s%^address = \"0.0.0.0:9091\"%address = \"0.0.0.0:48091\"%; s%^address = \"0.0.0.0:8545\"%address = \"0.0.0.0:48545\"%; s%^ws-address = \"0.0.0.0:8546\"%ws-address = \"0.0.0.0:48546\"%" $HOME/.quasarnode/config/app.toml
```

### Download latest chain snapshot

```bash
curl -L https://snapshots.kjnodes.com/quasar-testnet/snapshot_latest.tar.lz4 | tar -Ilz4 -xf - -C $HOME/.quasarnode
[[ -f $HOME/.quasarnode/data/upgrade-info.json ]] && cp $HOME/.quasarnode/data/upgrade-info.json $HOME/.quasarnode/cosmovisor/genesis/upgrade-info.json
```

### Start service and check the logs

```bash
sudo systemctl start quasard && sudo journalctl -u quasard -f --no-hostname -o cat
```
