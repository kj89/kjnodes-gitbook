---
description: Setting up your validator node has never been so easy. Get your validator running in minutes by following step by step instructions.
---

# Installation

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/source.png" alt=""><figcaption></figcaption></figure>

**Chain ID**: sourcechain-testnet | **Latest Version Tag**: e06b810e842e57ec8f5432c9cdd57883a69b3cee | **Custom Port**: 128

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
rm -rf source
git clone https://github.com/Source-Protocol-Cosmos/source.git
cd source
git checkout e06b810e842e57ec8f5432c9cdd57883a69b3cee

# Build binaries
make build

# Prepare binaries for Cosmovisor
mkdir -p $HOME/.source/cosmovisor/genesis/bin
mv bin/sourced $HOME/.source/cosmovisor/genesis/bin/
rm -rf build

# Create application symlinks
sudo ln -s $HOME/.source/cosmovisor/genesis $HOME/.source/cosmovisor/current -f
sudo ln -s $HOME/.source/cosmovisor/current/bin/sourced /usr/local/bin/sourced -f
```

### Install Cosmovisor and create a service

```bash
# Download and install Cosmovisor
go install cosmossdk.io/tools/cosmovisor/cmd/cosmovisor@v1.4.0

# Create service
sudo tee /etc/systemd/system/sourced.service > /dev/null << EOF
[Unit]
Description=source-testnet node service
After=network-online.target

[Service]
User=$USER
ExecStart=$(which cosmovisor) run start
Restart=on-failure
RestartSec=10
LimitNOFILE=65535
Environment="DAEMON_HOME=$HOME/.source"
Environment="DAEMON_NAME=sourced"
Environment="UNSAFE_SKIP_BACKUP=true"
Environment="PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:$HOME/.source/cosmovisor/current/bin"

[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable sourced
```

### Initialize the node

```bash
# Set node configuration
sourced config chain-id sourcechain-testnet
sourced config keyring-backend test
sourced config node tcp://localhost:12857

# Initialize the node
sourced init $MONIKER --chain-id sourcechain-testnet

# Download genesis and addrbook
curl -Ls https://snapshots.kjnodes.com/source-testnet/genesis.json > $HOME/.source/config/genesis.json
curl -Ls https://snapshots.kjnodes.com/source-testnet/addrbook.json > $HOME/.source/config/addrbook.json

# Add seeds
sed -i -e "s|^seeds *=.*|seeds = \"3f472746f46493309650e5a033076689996c8881@source-testnet.rpc.kjnodes.com:12859\"|" $HOME/.source/config/config.toml

# Set minimum gas price
sed -i -e "s|^minimum-gas-prices *=.*|minimum-gas-prices = \"0usource\"|" $HOME/.source/config/app.toml

# Set pruning
sed -i \
  -e 's|^pruning *=.*|pruning = "custom"|' \
  -e 's|^pruning-keep-recent *=.*|pruning-keep-recent = "100"|' \
  -e 's|^pruning-keep-every *=.*|pruning-keep-every = "0"|' \
  -e 's|^pruning-interval *=.*|pruning-interval = "19"|' \
  $HOME/.source/config/app.toml

# Set custom ports
sed -i -e "s%^proxy_app = \"tcp://127.0.0.1:26658\"%proxy_app = \"tcp://127.0.0.1:12858\"%; s%^laddr = \"tcp://127.0.0.1:26657\"%laddr = \"tcp://127.0.0.1:12857\"%; s%^pprof_laddr = \"localhost:6060\"%pprof_laddr = \"localhost:12860\"%; s%^laddr = \"tcp://0.0.0.0:26656\"%laddr = \"tcp://0.0.0.0:12856\"%; s%^prometheus_listen_addr = \":26660\"%prometheus_listen_addr = \":12866\"%" $HOME/.source/config/config.toml
sed -i -e "s%^address = \"tcp://0.0.0.0:1317\"%address = \"tcp://0.0.0.0:12817\"%; s%^address = \":8080\"%address = \":12880\"%; s%^address = \"0.0.0.0:9090\"%address = \"0.0.0.0:12890\"%; s%^address = \"0.0.0.0:9091\"%address = \"0.0.0.0:12891\"%; s%:8545%:12845%; s%:8546%:12846%; s%:6065%:12865%" $HOME/.source/config/app.toml
```

### Download latest chain snapshot

```bash
curl -L https://snapshots.kjnodes.com/source-testnet/snapshot_latest.tar.lz4 | tar -Ilz4 -xf - -C $HOME/.source
[[ -f $HOME/.source/data/upgrade-info.json ]] && cp $HOME/.source/data/upgrade-info.json $HOME/.source/cosmovisor/genesis/upgrade-info.json
```

### Start service and check the logs

```bash
sudo systemctl start sourced && sudo journalctl -u sourced -f --no-hostname -o cat
```
