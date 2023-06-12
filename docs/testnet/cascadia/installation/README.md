---
description: Setting up your validator node has never been so easy. Get your validator running in minutes by following step by step instructions.
---

# Installation

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/cascadia.png" alt=""><figcaption></figcaption></figure>

**Chain ID**: cascadia_6102-1 | **Latest Version Tag**: v0.1.2 | **Custom Port**: 155

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
rm -rf cascadia
git clone https://github.com/CascadiaFoundation/cascadia.git
cd cascadia
git checkout v0.1.2

# Build binaries
make build

# Prepare binaries for Cosmovisor
mkdir -p $HOME/.cascadiad/cosmovisor/genesis/bin
mv build/cascadiad $HOME/.cascadiad/cosmovisor/genesis/bin/
rm -rf build

# Create application symlinks
sudo ln -s $HOME/.cascadiad/cosmovisor/genesis $HOME/.cascadiad/cosmovisor/current -f
sudo ln -s $HOME/.cascadiad/cosmovisor/current/bin/cascadiad /usr/local/bin/cascadiad -f
```

### Install Cosmovisor and create a service

```bash
# Download and install Cosmovisor
go install cosmossdk.io/tools/cosmovisor/cmd/cosmovisor@v1.4.0

# Create service
sudo tee /etc/systemd/system/cascadiad.service > /dev/null << EOF
[Unit]
Description=cascadia-testnet node service
After=network-online.target

[Service]
User=$USER
ExecStart=$(which cosmovisor) run start
Restart=on-failure
RestartSec=10
LimitNOFILE=65535
Environment="DAEMON_HOME=$HOME/.cascadiad"
Environment="DAEMON_NAME=cascadiad"
Environment="UNSAFE_SKIP_BACKUP=true"
Environment="PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:$HOME/.cascadiad/cosmovisor/current/bin"

[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable cascadiad
```

### Initialize the node

```bash
# Set node configuration
cascadiad config chain-id cascadia_6102-1
cascadiad config keyring-backend test
cascadiad config node tcp://localhost:15557

# Initialize the node
cascadiad init $MONIKER --chain-id cascadia_6102-1

# Download genesis and addrbook
curl -Ls https://snapshots.kjnodes.com/cascadia-testnet/genesis.json > $HOME/.cascadiad/config/genesis.json
curl -Ls https://snapshots.kjnodes.com/cascadia-testnet/addrbook.json > $HOME/.cascadiad/config/addrbook.json

# Add seeds
sed -i -e "s|^seeds *=.*|seeds = \"3f472746f46493309650e5a033076689996c8881@cascadia-testnet.rpc.kjnodes.com:15559\"|" $HOME/.cascadiad/config/config.toml

# Set minimum gas price
sed -i -e "s|^minimum-gas-prices *=.*|minimum-gas-prices = \"7aCC\"|" $HOME/.cascadiad/config/app.toml

# Set pruning
sed -i \
  -e 's|^pruning *=.*|pruning = "custom"|' \
  -e 's|^pruning-keep-recent *=.*|pruning-keep-recent = "100"|' \
  -e 's|^pruning-keep-every *=.*|pruning-keep-every = "0"|' \
  -e 's|^pruning-interval *=.*|pruning-interval = "19"|' \
  $HOME/.cascadiad/config/app.toml

# Set custom ports
sed -i -e "s%^proxy_app = \"tcp://127.0.0.1:26658\"%proxy_app = \"tcp://127.0.0.1:15558\"%; s%^laddr = \"tcp://127.0.0.1:26657\"%laddr = \"tcp://127.0.0.1:15557\"%; s%^pprof_laddr = \"localhost:6060\"%pprof_laddr = \"localhost:15560\"%; s%^laddr = \"tcp://0.0.0.0:26656\"%laddr = \"tcp://0.0.0.0:15556\"%; s%^prometheus_listen_addr = \":26660\"%prometheus_listen_addr = \":15566\"%" $HOME/.cascadiad/config/config.toml
sed -i -e "s%^address = \"tcp://0.0.0.0:1317\"%address = \"tcp://0.0.0.0:15517\"%; s%^address = \":8080\"%address = \":15580\"%; s%^address = \"0.0.0.0:9090\"%address = \"0.0.0.0:15590\"%; s%^address = \"0.0.0.0:9091\"%address = \"0.0.0.0:15591\"%; s%:8545%:15545%; s%:8546%:15546%; s%:6065%:15565%" $HOME/.cascadiad/config/app.toml
```

### Download latest chain snapshot

```bash
curl -L https://snapshots.kjnodes.com/cascadia-testnet/snapshot_latest.tar.lz4 | tar -Ilz4 -xf - -C $HOME/.cascadiad
[[ -f $HOME/.cascadiad/data/upgrade-info.json ]] && cp $HOME/.cascadiad/data/upgrade-info.json $HOME/.cascadiad/cosmovisor/genesis/upgrade-info.json
```

### Start service and check the logs

```bash
sudo systemctl start cascadiad && sudo journalctl -u cascadiad -f --no-hostname -o cat
```
