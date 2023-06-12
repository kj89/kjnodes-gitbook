---
description: Setting up your validator node has never been so easy. Get your validator running in minutes by following step by step instructions.
---

# Installation

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/quasar.png" alt=""><figcaption></figcaption></figure>

**Chain ID**: quasar-1 | **Latest Version Tag**: v0.1.1 | **Custom Port**: 148

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
rm -rf quasar-preview
git clone https://github.com/quasar-finance/quasar-preview.git
cd quasar-preview
git checkout v0.1.1

# Build binaries
make build

# Prepare binaries for Cosmovisor
mkdir -p $HOME/.quasarnode/cosmovisor/genesis/bin
mv build/quasarnoded $HOME/.quasarnode/cosmovisor/genesis/bin/
rm -rf build

# Create application symlinks
sudo ln -s $HOME/.quasarnode/cosmovisor/genesis $HOME/.quasarnode/cosmovisor/current -f
sudo ln -s $HOME/.quasarnode/cosmovisor/current/bin/quasarnoded /usr/local/bin/quasarnoded -f
```

### Install Cosmovisor and create a service

```bash
# Download and install Cosmovisor
go install cosmossdk.io/tools/cosmovisor/cmd/cosmovisor@v1.4.0

# Create service
sudo tee /etc/systemd/system/quasarnoded.service > /dev/null << EOF
[Unit]
Description=quasar node service
After=network-online.target

[Service]
User=$USER
ExecStart=$(which cosmovisor) run start
Restart=on-failure
RestartSec=10
LimitNOFILE=65535
Environment="DAEMON_HOME=$HOME/.quasarnode"
Environment="DAEMON_NAME=quasarnoded"
Environment="UNSAFE_SKIP_BACKUP=true"
Environment="PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:$HOME/.quasarnode/cosmovisor/current/bin"

[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable quasarnoded
```

### Initialize the node

```bash
# Set node configuration
quasarnoded config chain-id quasar-1
quasarnoded config keyring-backend file
quasarnoded config node tcp://localhost:14857

# Initialize the node
quasarnoded init $MONIKER --chain-id quasar-1

# Download genesis and addrbook
curl -Ls https://snapshots.kjnodes.com/quasar/genesis.json > $HOME/.quasarnode/config/genesis.json
curl -Ls https://snapshots.kjnodes.com/quasar/addrbook.json > $HOME/.quasarnode/config/addrbook.json

# Add seeds
sed -i -e "s|^seeds *=.*|seeds = \"400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@quasar.rpc.kjnodes.com:14859\"|" $HOME/.quasarnode/config/config.toml

# Set minimum gas price
sed -i -e "s|^minimum-gas-prices *=.*|minimum-gas-prices = \"0.01ibc/0471F1C4E7AFD3F07702BEF6DC365268D64570F7C1FDC98EA6098DD6DE59817B,0.01ibc/FA0006F056DB6719B8C16C551FC392B62F5729978FC0B125AC9A432DBB2AA1A5,0.01ibc/FA7775734CC73176B7425910DE001A1D2AD9B6D9E93129A5D0750EAD13E4E63A\"|" $HOME/.quasarnode/config/app.toml

# Set pruning
sed -i \
  -e 's|^pruning *=.*|pruning = "custom"|' \
  -e 's|^pruning-keep-recent *=.*|pruning-keep-recent = "100"|' \
  -e 's|^pruning-keep-every *=.*|pruning-keep-every = "0"|' \
  -e 's|^pruning-interval *=.*|pruning-interval = "19"|' \
  $HOME/.quasarnode/config/app.toml

# Set custom ports
sed -i -e "s%^proxy_app = \"tcp://127.0.0.1:26658\"%proxy_app = \"tcp://127.0.0.1:14858\"%; s%^laddr = \"tcp://127.0.0.1:26657\"%laddr = \"tcp://127.0.0.1:14857\"%; s%^pprof_laddr = \"localhost:6060\"%pprof_laddr = \"localhost:14860\"%; s%^laddr = \"tcp://0.0.0.0:26656\"%laddr = \"tcp://0.0.0.0:14856\"%; s%^prometheus_listen_addr = \":26660\"%prometheus_listen_addr = \":14866\"%" $HOME/.quasarnode/config/config.toml
sed -i -e "s%^address = \"tcp://0.0.0.0:1317\"%address = \"tcp://0.0.0.0:14817\"%; s%^address = \":8080\"%address = \":14880\"%; s%^address = \"0.0.0.0:9090\"%address = \"0.0.0.0:14890\"%; s%^address = \"0.0.0.0:9091\"%address = \"0.0.0.0:14891\"%; s%:8545%:14845%; s%:8546%:14846%; s%:6065%:14865%" $HOME/.quasarnode/config/app.toml
```

### Download latest chain snapshot

```bash
curl -L https://snapshots.kjnodes.com/quasar/snapshot_latest.tar.lz4 | tar -Ilz4 -xf - -C $HOME/.quasarnode
[[ -f $HOME/.quasarnode/data/upgrade-info.json ]] && cp $HOME/.quasarnode/data/upgrade-info.json $HOME/.quasarnode/cosmovisor/genesis/upgrade-info.json
```

### Start service and check the logs

```bash
sudo systemctl start quasarnoded && sudo journalctl -u quasarnoded -f --no-hostname -o cat
```
