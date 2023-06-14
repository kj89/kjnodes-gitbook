---
description: Setting up your validator node has never been so easy. Get your validator running in minutes by following step by step instructions.
---

# Installation

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/noria.png" alt=""><figcaption></figcaption></figure>

**Chain ID**: oasis-3 | **Latest Version Tag**: v1.3.0 | **Custom Port**: 161

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
rm -rf noria
git clone https://github.com/noria-net/noria.git
cd noria
git checkout v1.3.0

# Build binaries
make build

# Prepare binaries for Cosmovisor
mkdir -p $HOME/.noria/cosmovisor/genesis/bin
mv build/noriad $HOME/.noria/cosmovisor/genesis/bin/
rm -rf build

# Create application symlinks
sudo ln -s $HOME/.noria/cosmovisor/genesis $HOME/.noria/cosmovisor/current -f
sudo ln -s $HOME/.noria/cosmovisor/current/bin/noriad /usr/local/bin/noriad -f
```

### Install Cosmovisor and create a service

```bash
# Download and install Cosmovisor
go install cosmossdk.io/tools/cosmovisor/cmd/cosmovisor@v1.4.0

# Create service
sudo tee /etc/systemd/system/noriad.service > /dev/null << EOF
[Unit]
Description=noria-testnet node service
After=network-online.target

[Service]
User=$USER
ExecStart=$(which cosmovisor) run start
Restart=on-failure
RestartSec=10
LimitNOFILE=65535
Environment="DAEMON_HOME=$HOME/.noria"
Environment="DAEMON_NAME=noriad"
Environment="UNSAFE_SKIP_BACKUP=true"
Environment="PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:$HOME/.noria/cosmovisor/current/bin"

[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable noriad
```

### Initialize the node

```bash
# Set node configuration
noriad config chain-id oasis-3
noriad config keyring-backend test
noriad config node tcp://localhost:16157

# Initialize the node
noriad init $MONIKER --chain-id oasis-3

# Download genesis and addrbook
curl -Ls https://snapshots.kjnodes.com/noria-testnet/genesis.json > $HOME/.noria/config/genesis.json
curl -Ls https://snapshots.kjnodes.com/noria-testnet/addrbook.json > $HOME/.noria/config/addrbook.json

# Add seeds
sed -i -e "s|^seeds *=.*|seeds = \"3f472746f46493309650e5a033076689996c8881@noria-testnet.rpc.kjnodes.com:16159\"|" $HOME/.noria/config/config.toml

# Set minimum gas price
sed -i -e "s|^minimum-gas-prices *=.*|minimum-gas-prices = \"0.0025ucrd\"|" $HOME/.noria/config/app.toml

# Set pruning
sed -i \
  -e 's|^pruning *=.*|pruning = "custom"|' \
  -e 's|^pruning-keep-recent *=.*|pruning-keep-recent = "100"|' \
  -e 's|^pruning-keep-every *=.*|pruning-keep-every = "0"|' \
  -e 's|^pruning-interval *=.*|pruning-interval = "19"|' \
  $HOME/.noria/config/app.toml

# Set custom ports
sed -i -e "s%^proxy_app = \"tcp://127.0.0.1:26658\"%proxy_app = \"tcp://127.0.0.1:16158\"%; s%^laddr = \"tcp://127.0.0.1:26657\"%laddr = \"tcp://127.0.0.1:16157\"%; s%^pprof_laddr = \"localhost:6060\"%pprof_laddr = \"localhost:16160\"%; s%^laddr = \"tcp://0.0.0.0:26656\"%laddr = \"tcp://0.0.0.0:16156\"%; s%^prometheus_listen_addr = \":26660\"%prometheus_listen_addr = \":16166\"%" $HOME/.noria/config/config.toml
sed -i -e "s%^address = \"tcp://localhost:1317\"%address = \"tcp://0.0.0.0:16117\"%; s%^address = \":8080\"%address = \":16180\"%; s%^address = \"localhost:9090\"%address = \"0.0.0.0:16190\"%; s%^address = \"localhost:9091\"%address = \"0.0.0.0:16191\"%; s%:8545%:16145%; s%:8546%:16146%; s%:6065%:16165%" $HOME/.noria/config/app.toml
```

### Download latest chain snapshot

```bash
curl -L https://snapshots.kjnodes.com/noria-testnet/snapshot_latest.tar.lz4 | tar -Ilz4 -xf - -C $HOME/.noria
[[ -f $HOME/.noria/data/upgrade-info.json ]] && cp $HOME/.noria/data/upgrade-info.json $HOME/.noria/cosmovisor/genesis/upgrade-info.json
```

### Start service and check the logs

```bash
sudo systemctl start noriad && sudo journalctl -u noriad -f --no-hostname -o cat
```
