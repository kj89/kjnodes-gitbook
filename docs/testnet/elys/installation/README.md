---
description: Setting up your validator node has never been so easy. Get your validator running in minutes by following step by step instructions.
---

# Installation

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/elys.png" alt=""><figcaption></figcaption></figure>

**Chain ID**: elystestnet-1 | **Latest Version Tag**: v0.7.0 | **Custom Port**: 153

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
rm -rf elys
git clone https://github.com/elys-network/elys.git
cd elys
git checkout v0.7.0

# Build binaries
make build

# Prepare binaries for Cosmovisor
mkdir -p $HOME/.elys/cosmovisor/genesis/bin
mv build/elysd $HOME/.elys/cosmovisor/genesis/bin/
rm -rf build

# Create application symlinks
sudo ln -s $HOME/.elys/cosmovisor/genesis $HOME/.elys/cosmovisor/current -f
sudo ln -s $HOME/.elys/cosmovisor/current/bin/elysd /usr/local/bin/elysd -f
```

### Install Cosmovisor and create a service

```bash
# Download and install Cosmovisor
go install cosmossdk.io/tools/cosmovisor/cmd/cosmovisor@v1.4.0

# Create service
sudo tee /etc/systemd/system/elysd.service > /dev/null << EOF
[Unit]
Description=elys-testnet node service
After=network-online.target

[Service]
User=$USER
ExecStart=$(which cosmovisor) run start
Restart=on-failure
RestartSec=10
LimitNOFILE=65535
Environment="DAEMON_HOME=$HOME/.elys"
Environment="DAEMON_NAME=elysd"
Environment="UNSAFE_SKIP_BACKUP=true"
Environment="PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:$HOME/.elys/cosmovisor/current/bin"

[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable elysd
```

### Initialize the node

```bash
# Set node configuration
elysd config chain-id elystestnet-1
elysd config keyring-backend test
elysd config node tcp://localhost:15357

# Initialize the node
elysd init $MONIKER --chain-id elystestnet-1

# Download genesis and addrbook
curl -Ls https://snapshots.kjnodes.com/elys-testnet/genesis.json > $HOME/.elys/config/genesis.json
curl -Ls https://snapshots.kjnodes.com/elys-testnet/addrbook.json > $HOME/.elys/config/addrbook.json

# Add seeds
sed -i -e "s|^seeds *=.*|seeds = \"3f472746f46493309650e5a033076689996c8881@elys-testnet.rpc.kjnodes.com:15359\"|" $HOME/.elys/config/config.toml

# Set minimum gas price
sed -i -e "s|^minimum-gas-prices *=.*|minimum-gas-prices = \"0uelys\"|" $HOME/.elys/config/app.toml

# Set pruning
sed -i \
  -e 's|^pruning *=.*|pruning = "nothing"|' \
  -e 's|^pruning-keep-recent *=.*|pruning-keep-recent = "100"|' \
  -e 's|^pruning-keep-every *=.*|pruning-keep-every = "0"|' \
  -e 's|^pruning-interval *=.*|pruning-interval = "19"|' \
  $HOME/.elys/config/app.toml

# Set custom ports
sed -i -e "s%^proxy_app = \"tcp://127.0.0.1:26658\"%proxy_app = \"tcp://127.0.0.1:15358\"%; s%^laddr = \"tcp://127.0.0.1:26657\"%laddr = \"tcp://127.0.0.1:15357\"%; s%^pprof_laddr = \"localhost:6060\"%pprof_laddr = \"localhost:15360\"%; s%^laddr = \"tcp://0.0.0.0:26656\"%laddr = \"tcp://0.0.0.0:15356\"%; s%^prometheus_listen_addr = \":26660\"%prometheus_listen_addr = \":15366\"%" $HOME/.elys/config/config.toml
sed -i -e "s%^address = \"tcp://0.0.0.0:1317\"%address = \"tcp://0.0.0.0:15317\"%; s%^address = \":8080\"%address = \":15380\"%; s%^address = \"0.0.0.0:9090\"%address = \"0.0.0.0:15390\"%; s%^address = \"0.0.0.0:9091\"%address = \"0.0.0.0:15391\"%; s%:8545%:15345%; s%:8546%:15346%; s%:6065%:15365%" $HOME/.elys/config/app.toml
```

### Download latest chain snapshot

```bash
curl -L https://snapshots.kjnodes.com/elys-testnet/snapshot_latest.tar.lz4 | tar -Ilz4 -xf - -C $HOME/.elys
[[ -f $HOME/.elys/data/upgrade-info.json ]] && cp $HOME/.elys/data/upgrade-info.json $HOME/.elys/cosmovisor/genesis/upgrade-info.json
```

### Start service and check the logs

```bash
sudo systemctl start elysd && sudo journalctl -u elysd -f --no-hostname -o cat
```
