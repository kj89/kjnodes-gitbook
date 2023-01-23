---
description: Setting up your validator node has never been so easy. Get your validator running in minutes by following step by step instructions.
---

# Installation

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/kujira.png" width="150" alt=""><figcaption></figcaption></figure>

**Chain ID**: kaiyo-1 | **Latest Version Tag**: v0.7.1 | **Custom Port**: 13

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
# Clone project repository
cd $HOME
rm -rf core
git clone https://github.com/Team-Kujira/core.git
cd core
git checkout v0.7.1

# Build binaries
make build

# Prepare binaries for Cosmovisor
mkdir -p $HOME/.kujira/cosmovisor/genesis/bin
mv build/kujirad $HOME/.kujira/cosmovisor/genesis/bin/
rm -rf build

# Create application symlinks
ln -s $HOME/.kujira/cosmovisor/genesis $HOME/.kujira/cosmovisor/current
sudo ln -s $HOME/.kujira/cosmovisor/current/bin/kujirad /usr/local/bin/kujirad
```

### Install Cosmovisor and create a service

```bash
# Download and install Cosmovisor
go install cosmossdk.io/tools/cosmovisor/cmd/cosmovisor@v1.4.0

# Create service
sudo tee /etc/systemd/system/kujirad.service > /dev/null << EOF
[Unit]
Description=kujira node service
After=network-online.target

[Service]
User=$USER
ExecStart=$(which cosmovisor) run start
Restart=on-failure
RestartSec=10
LimitNOFILE=65535
Environment="DAEMON_HOME=$HOME/.kujira"
Environment="DAEMON_NAME=kujirad"
Environment="UNSAFE_SKIP_BACKUP=true"

[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable kujirad
```

### Initialize the node

```bash
# Set node configuration
kujirad config chain-id kaiyo-1
kujirad config keyring-backend file
kujirad config node tcp://localhost:13657

# Initialize the node
kujirad init $MONIKER --chain-id kaiyo-1

# Download genesis and addrbook
curl -Ls https://snapshots.kjnodes.com/kujira/genesis.json > $HOME/.kujira/config/genesis.json
curl -Ls https://snapshots.kjnodes.com/kujira/addrbook.json > $HOME/.kujira/config/addrbook.json

# Add seeds
sed -i -e "s|^seeds *=.*|seeds = \"400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@kujira.rpc.kjnodes.com:13659\"|" $HOME/.kujira/config/config.toml

# Set minimum gas price
sed -i -e "s|^minimum-gas-prices *=.*|minimum-gas-prices = \"0.00119ukuji\"|" $HOME/.kujira/config/app.toml

# Set pruning
sed -i \
  -e 's|^pruning *=.*|pruning = "custom"|' \
  -e 's|^pruning-keep-recent *=.*|pruning-keep-recent = "100"|' \
  -e 's|^pruning-keep-every *=.*|pruning-keep-every = "0"|' \
  -e 's|^pruning-interval *=.*|pruning-interval = "19"|' \
  $HOME/.kujira/config/app.toml

# Set custom ports
sed -i -e "s%^proxy_app = \"tcp://127.0.0.1:26658\"%proxy_app = \"tcp://127.0.0.1:13658\"%; s%^laddr = \"tcp://127.0.0.1:26657\"%laddr = \"tcp://127.0.0.1:13657\"%; s%^pprof_laddr = \"localhost:6060\"%pprof_laddr = \"localhost:13060\"%; s%^laddr = \"tcp://0.0.0.0:26656\"%laddr = \"tcp://0.0.0.0:13656\"%; s%^prometheus_listen_addr = \":26660\"%prometheus_listen_addr = \":13660\"%" $HOME/.kujira/config/config.toml
sed -i -e "s%^address = \"tcp://0.0.0.0:1317\"%address = \"tcp://0.0.0.0:13317\"%; s%^address = \":8080\"%address = \":13080\"%; s%^address = \"0.0.0.0:9090\"%address = \"0.0.0.0:13090\"%; s%^address = \"0.0.0.0:9091\"%address = \"0.0.0.0:13091\"%; s%^address = \"0.0.0.0:8545\"%address = \"0.0.0.0:13545\"%; s%^ws-address = \"0.0.0.0:8546\"%ws-address = \"0.0.0.0:13546\"%" $HOME/.kujira/config/app.toml
```

### Download latest chain snapshot

```bash
curl -L https://snapshots.kjnodes.com/kujira/snapshot_latest.tar.lz4 | tar -Ilz4 -xf - -C $HOME/.kujira
[[ -f $HOME/.kujira/data/upgrade-info.json ]] && cp $HOME/.kujira/data/upgrade-info.json $HOME/.kujira/cosmovisor/genesis/upgrade-info.json
```

### Start service and check the logs

```bash
sudo systemctl start kujirad && sudo journalctl -u kujirad -f --no-hostname -o cat
```
