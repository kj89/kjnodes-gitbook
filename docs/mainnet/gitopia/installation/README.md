---
description: Setting up your validator node has never been so easy. Get your validator running in minutes by following step by step instructions.
---

# Installation

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/gitopia.png" alt=""><figcaption></figcaption></figure>

**Chain ID**: gitopia | **Latest Version Tag**: v2.1.1 | **Custom Port**: 141

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
rm -rf gitopia
git clone https://github.com/gitopia/gitopia.git
cd gitopia
git checkout v2.1.1

# Build binaries
make build

# Prepare binaries for Cosmovisor
mkdir -p $HOME/.gitopia/cosmovisor/genesis/bin
mv build/gitopiad $HOME/.gitopia/cosmovisor/genesis/bin/
rm -rf build

# Create application symlinks
sudo ln -s $HOME/.gitopia/cosmovisor/genesis $HOME/.gitopia/cosmovisor/current -f
sudo ln -s $HOME/.gitopia/cosmovisor/current/bin/gitopiad /usr/local/bin/gitopiad -f
```

### Install Cosmovisor and create a service

```bash
# Download and install Cosmovisor
go install cosmossdk.io/tools/cosmovisor/cmd/cosmovisor@v1.4.0

# Create service
sudo tee /etc/systemd/system/gitopiad.service > /dev/null << EOF
[Unit]
Description=gitopia node service
After=network-online.target

[Service]
User=$USER
ExecStart=$(which cosmovisor) run start
Restart=on-failure
RestartSec=10
LimitNOFILE=65535
Environment="DAEMON_HOME=$HOME/.gitopia"
Environment="DAEMON_NAME=gitopiad"
Environment="UNSAFE_SKIP_BACKUP=true"
Environment="PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:$HOME/.gitopia/cosmovisor/current/bin"

[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable gitopiad
```

### Initialize the node

```bash
# Set node configuration
gitopiad config chain-id gitopia
gitopiad config keyring-backend file
gitopiad config node tcp://localhost:14157

# Initialize the node
gitopiad init $MONIKER --chain-id gitopia

# Download genesis and addrbook
curl -Ls https://snapshots.kjnodes.com/gitopia/genesis.json > $HOME/.gitopia/config/genesis.json
curl -Ls https://snapshots.kjnodes.com/gitopia/addrbook.json > $HOME/.gitopia/config/addrbook.json

# Add seeds
sed -i -e "s|^seeds *=.*|seeds = \"400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@gitopia.rpc.kjnodes.com:14159\"|" $HOME/.gitopia/config/config.toml

# Set minimum gas price
sed -i -e "s|^minimum-gas-prices *=.*|minimum-gas-prices = \"0.001ulore\"|" $HOME/.gitopia/config/app.toml

# Set pruning
sed -i \
  -e 's|^pruning *=.*|pruning = "custom"|' \
  -e 's|^pruning-keep-recent *=.*|pruning-keep-recent = "100"|' \
  -e 's|^pruning-keep-every *=.*|pruning-keep-every = "0"|' \
  -e 's|^pruning-interval *=.*|pruning-interval = "19"|' \
  $HOME/.gitopia/config/app.toml

# Set custom ports
sed -i -e "s%^proxy_app = \"tcp://127.0.0.1:26658\"%proxy_app = \"tcp://127.0.0.1:14158\"%; s%^laddr = \"tcp://127.0.0.1:26657\"%laddr = \"tcp://127.0.0.1:14157\"%; s%^pprof_laddr = \"localhost:6060\"%pprof_laddr = \"localhost:14160\"%; s%^laddr = \"tcp://0.0.0.0:26656\"%laddr = \"tcp://0.0.0.0:14156\"%; s%^prometheus_listen_addr = \":26660\"%prometheus_listen_addr = \":14166\"%" $HOME/.gitopia/config/config.toml
sed -i -e "s%^address = \"tcp://0.0.0.0:1317\"%address = \"tcp://0.0.0.0:14117\"%; s%^address = \":8080\"%address = \":14180\"%; s%^address = \"0.0.0.0:9090\"%address = \"0.0.0.0:14190\"%; s%^address = \"0.0.0.0:9091\"%address = \"0.0.0.0:14191\"%; s%:8545%:14145%; s%:8546%:14146%; s%:6065%:14165%" $HOME/.gitopia/config/app.toml
```

### Download latest chain snapshot

```bash
curl -L https://snapshots.kjnodes.com/gitopia/snapshot_latest.tar.lz4 | tar -Ilz4 -xf - -C $HOME/.gitopia
[[ -f $HOME/.gitopia/data/upgrade-info.json ]] && cp $HOME/.gitopia/data/upgrade-info.json $HOME/.gitopia/cosmovisor/genesis/upgrade-info.json
```

### Start service and check the logs

```bash
sudo systemctl start gitopiad && sudo journalctl -u gitopiad -f --no-hostname -o cat
```
