---
description: Setting up your validator node has never been so easy. Get your validator running in minutes by following step by step instructions.
---

# Installation

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/archway.png" alt=""><figcaption></figcaption></figure>

**Chain ID**: constantine-3 | **Latest Version Tag**: v1.0.0-rc.1 | **Custom Port**: 156

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
rm -rf archway
git clone https://github.com/archway-network/archway.git
cd archway
git checkout v1.0.0-rc.1

# Build binaries
make build

# Prepare binaries for Cosmovisor
mkdir -p $HOME/.archway/cosmovisor/genesis/bin
mv build/archwayd $HOME/.archway/cosmovisor/genesis/bin/
rm -rf build

# Create application symlinks
sudo ln -s $HOME/.archway/cosmovisor/genesis $HOME/.archway/cosmovisor/current -f
sudo ln -s $HOME/.archway/cosmovisor/current/bin/archwayd /usr/local/bin/archwayd -f
```

### Install Cosmovisor and create a service

```bash
# Download and install Cosmovisor
go install cosmossdk.io/tools/cosmovisor/cmd/cosmovisor@v1.4.0

# Create service
sudo tee /etc/systemd/system/archwayd.service > /dev/null << EOF
[Unit]
Description=archway-testnet node service
After=network-online.target

[Service]
User=$USER
ExecStart=$(which cosmovisor) run start
Restart=on-failure
RestartSec=10
LimitNOFILE=65535
Environment="DAEMON_HOME=$HOME/.archway"
Environment="DAEMON_NAME=archwayd"
Environment="UNSAFE_SKIP_BACKUP=true"
Environment="PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:$HOME/.archway/cosmovisor/current/bin"

[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable archwayd
```

### Initialize the node

```bash
# Set node configuration
archwayd config chain-id constantine-3
archwayd config keyring-backend test
archwayd config node tcp://localhost:15657

# Initialize the node
archwayd init $MONIKER --chain-id constantine-3

# Download genesis and addrbook
curl -Ls https://snapshots.kjnodes.com/archway-testnet/genesis.json > $HOME/.archway/config/genesis.json
curl -Ls https://snapshots.kjnodes.com/archway-testnet/addrbook.json > $HOME/.archway/config/addrbook.json

# Add seeds
sed -i -e "s|^seeds *=.*|seeds = \"3f472746f46493309650e5a033076689996c8881@archway-testnet.rpc.kjnodes.com:15659\"|" $HOME/.archway/config/config.toml

# Set minimum gas price
sed -i -e "s|^minimum-gas-prices *=.*|minimum-gas-prices = \"0aconst\"|" $HOME/.archway/config/app.toml

# Set pruning
sed -i \
  -e 's|^pruning *=.*|pruning = "custom"|' \
  -e 's|^pruning-keep-recent *=.*|pruning-keep-recent = "100"|' \
  -e 's|^pruning-keep-every *=.*|pruning-keep-every = "0"|' \
  -e 's|^pruning-interval *=.*|pruning-interval = "19"|' \
  $HOME/.archway/config/app.toml

# Set custom ports
sed -i -e "s%^proxy_app = \"tcp://127.0.0.1:26658\"%proxy_app = \"tcp://127.0.0.1:15658\"%; s%^laddr = \"tcp://127.0.0.1:26657\"%laddr = \"tcp://127.0.0.1:15657\"%; s%^pprof_laddr = \"localhost:6060\"%pprof_laddr = \"localhost:15660\"%; s%^laddr = \"tcp://0.0.0.0:26656\"%laddr = \"tcp://0.0.0.0:15656\"%; s%^prometheus_listen_addr = \":26660\"%prometheus_listen_addr = \":15666\"%" $HOME/.archway/config/config.toml
sed -i -e "s%^address = \"tcp://0.0.0.0:1317\"%address = \"tcp://0.0.0.0:15617\"%; s%^address = \":8080\"%address = \":15680\"%; s%^address = \"0.0.0.0:9090\"%address = \"0.0.0.0:15690\"%; s%^address = \"0.0.0.0:9091\"%address = \"0.0.0.0:15691\"%; s%:8545%:15645%; s%:8546%:15646%; s%:6065%:15665%" $HOME/.archway/config/app.toml
```

### Download latest chain snapshot

```bash
curl -L https://snapshots.kjnodes.com/archway-testnet/snapshot_latest.tar.lz4 | tar -Ilz4 -xf - -C $HOME/.archway
[[ -f $HOME/.archway/data/upgrade-info.json ]] && cp $HOME/.archway/data/upgrade-info.json $HOME/.archway/cosmovisor/genesis/upgrade-info.json
```

### Start service and check the logs

```bash
sudo systemctl start archwayd && sudo journalctl -u archwayd -f --no-hostname -o cat
```
