---
description: Setting up your validator node has never been so easy. Get your validator running in minutes by following step by step instructions.
---

# Installation

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/nois.png" alt=""><figcaption></figcaption></figure>

**Chain ID**: nois-1 | **Latest Version Tag**: v1.0.3 | **Custom Port**: 151

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
rm -rf noisd
git clone https://github.com/noislabs/noisd.git
cd noisd
git checkout v1.0.3

# Build binaries
make build

# Prepare binaries for Cosmovisor
mkdir -p $HOME/.noisd/cosmovisor/genesis/bin
mv build/noisd $HOME/.noisd/cosmovisor/genesis/bin/
rm -rf build

# Create application symlinks
sudo ln -s $HOME/.noisd/cosmovisor/genesis $HOME/.noisd/cosmovisor/current -f
sudo ln -s $HOME/.noisd/cosmovisor/current/bin/noisd /usr/local/bin/noisd -f
```

### Install Cosmovisor and create a service

```bash
# Download and install Cosmovisor
go install cosmossdk.io/tools/cosmovisor/cmd/cosmovisor@v1.4.0

# Create service
sudo tee /etc/systemd/system/noisd.service > /dev/null << EOF
[Unit]
Description=nois node service
After=network-online.target

[Service]
User=$USER
ExecStart=$(which cosmovisor) run start
Restart=on-failure
RestartSec=10
LimitNOFILE=65535
Environment="DAEMON_HOME=$HOME/.noisd"
Environment="DAEMON_NAME=noisd"
Environment="UNSAFE_SKIP_BACKUP=true"
Environment="PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:$HOME/.noisd/cosmovisor/current/bin"

[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable noisd
```

### Initialize the node

```bash
# Set node configuration
noisd config chain-id nois-1
noisd config keyring-backend file
noisd config node tcp://localhost:15157

# Initialize the node
noisd init $MONIKER --chain-id nois-1

# Download genesis and addrbook
curl -Ls https://snapshots.kjnodes.com/nois/genesis.json > $HOME/.noisd/config/genesis.json
curl -Ls https://snapshots.kjnodes.com/nois/addrbook.json > $HOME/.noisd/config/addrbook.json

# Add seeds
sed -i -e "s|^seeds *=.*|seeds = \"400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@nois.rpc.kjnodes.com:15159\"|" $HOME/.noisd/config/config.toml

# Set minimum gas price
sed -i -e "s|^minimum-gas-prices *=.*|minimum-gas-prices = \"0.05unois\"|" $HOME/.noisd/config/app.toml

# Set pruning
sed -i \
  -e 's|^pruning *=.*|pruning = "custom"|' \
  -e 's|^pruning-keep-recent *=.*|pruning-keep-recent = "100"|' \
  -e 's|^pruning-keep-every *=.*|pruning-keep-every = "0"|' \
  -e 's|^pruning-interval *=.*|pruning-interval = "19"|' \
  $HOME/.noisd/config/app.toml

# Set custom ports
sed -i -e "s%^proxy_app = \"tcp://127.0.0.1:26658\"%proxy_app = \"tcp://127.0.0.1:15158\"%; s%^laddr = \"tcp://127.0.0.1:26657\"%laddr = \"tcp://127.0.0.1:15157\"%; s%^pprof_laddr = \"localhost:6060\"%pprof_laddr = \"localhost:15160\"%; s%^laddr = \"tcp://0.0.0.0:26656\"%laddr = \"tcp://0.0.0.0:15156\"%; s%^prometheus_listen_addr = \":26660\"%prometheus_listen_addr = \":15166\"%" $HOME/.noisd/config/config.toml
sed -i -e "s%^address = \"tcp://0.0.0.0:1317\"%address = \"tcp://0.0.0.0:15117\"%; s%^address = \":8080\"%address = \":15180\"%; s%^address = \"0.0.0.0:9090\"%address = \"0.0.0.0:15190\"%; s%^address = \"0.0.0.0:9091\"%address = \"0.0.0.0:15191\"%; s%:8545%:15145%; s%:8546%:15146%; s%:6065%:15165%" $HOME/.noisd/config/app.toml
```

### Download latest chain snapshot

```bash
curl -L https://snapshots.kjnodes.com/nois/snapshot_latest.tar.lz4 | tar -Ilz4 -xf - -C $HOME/.noisd
[[ -f $HOME/.noisd/data/upgrade-info.json ]] && cp $HOME/.noisd/data/upgrade-info.json $HOME/.noisd/cosmovisor/genesis/upgrade-info.json
```

### Start service and check the logs

```bash
sudo systemctl start noisd && sudo journalctl -u noisd -f --no-hostname -o cat
```
