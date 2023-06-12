---
description: Setting up your validator node has never been so easy. Get your validator running in minutes by following step by step instructions.
---

# Installation

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/nolus.png" alt=""><figcaption></figcaption></figure>

**Chain ID**: pirin-1 | **Latest Version Tag**: v0.4.0 | **Custom Port**: 143

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
rm -rf nolus-core
git clone https://github.com/Nolus-Protocol/nolus-core.git
cd nolus-core
git checkout v0.4.0

# Build binaries
make build

# Prepare binaries for Cosmovisor
mkdir -p $HOME/.nolus/cosmovisor/genesis/bin
mv target/release/nolusd $HOME/.nolus/cosmovisor/genesis/bin/
rm -rf build

# Create application symlinks
sudo ln -s $HOME/.nolus/cosmovisor/genesis $HOME/.nolus/cosmovisor/current -f
sudo ln -s $HOME/.nolus/cosmovisor/current/bin/nolusd /usr/local/bin/nolusd -f
```

### Install Cosmovisor and create a service

```bash
# Download and install Cosmovisor
go install cosmossdk.io/tools/cosmovisor/cmd/cosmovisor@v1.4.0

# Create service
sudo tee /etc/systemd/system/nolusd.service > /dev/null << EOF
[Unit]
Description=nolus node service
After=network-online.target

[Service]
User=$USER
ExecStart=$(which cosmovisor) run start
Restart=on-failure
RestartSec=10
LimitNOFILE=65535
Environment="DAEMON_HOME=$HOME/.nolus"
Environment="DAEMON_NAME=nolusd"
Environment="UNSAFE_SKIP_BACKUP=true"
Environment="PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:$HOME/.nolus/cosmovisor/current/bin"

[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable nolusd
```

### Initialize the node

```bash
# Set node configuration
nolusd config chain-id pirin-1
nolusd config keyring-backend file
nolusd config node tcp://localhost:14357

# Initialize the node
nolusd init $MONIKER --chain-id pirin-1

# Download genesis and addrbook
curl -Ls https://snapshots.kjnodes.com/nolus/genesis.json > $HOME/.nolus/config/genesis.json
curl -Ls https://snapshots.kjnodes.com/nolus/addrbook.json > $HOME/.nolus/config/addrbook.json

# Add seeds
sed -i -e "s|^seeds *=.*|seeds = \"400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@nolus.rpc.kjnodes.com:14359\"|" $HOME/.nolus/config/config.toml

# Set minimum gas price
sed -i -e "s|^minimum-gas-prices *=.*|minimum-gas-prices = \"0.0025unls\"|" $HOME/.nolus/config/app.toml

# Set pruning
sed -i \
  -e 's|^pruning *=.*|pruning = "nothing"|' \
  $HOME/.nolus/config/app.toml

# Set custom ports
sed -i -e "s%^proxy_app = \"tcp://127.0.0.1:26658\"%proxy_app = \"tcp://127.0.0.1:14358\"%; s%^laddr = \"tcp://127.0.0.1:26657\"%laddr = \"tcp://127.0.0.1:14357\"%; s%^pprof_laddr = \"localhost:6060\"%pprof_laddr = \"localhost:14360\"%; s%^laddr = \"tcp://0.0.0.0:26656\"%laddr = \"tcp://0.0.0.0:14356\"%; s%^prometheus_listen_addr = \":26660\"%prometheus_listen_addr = \":14366\"%" $HOME/.nolus/config/config.toml
sed -i -e "s%^address = \"tcp://0.0.0.0:1317\"%address = \"tcp://0.0.0.0:14317\"%; s%^address = \":8080\"%address = \":14380\"%; s%^address = \"0.0.0.0:9090\"%address = \"0.0.0.0:14390\"%; s%^address = \"0.0.0.0:9091\"%address = \"0.0.0.0:14391\"%; s%:8545%:14345%; s%:8546%:14346%; s%:6065%:14365%" $HOME/.nolus/config/app.toml
```

### Download latest chain snapshot

```bash
curl -L https://snapshots.kjnodes.com/nolus/snapshot_latest.tar.lz4 | tar -Ilz4 -xf - -C $HOME/.nolus
[[ -f $HOME/.nolus/data/upgrade-info.json ]] && cp $HOME/.nolus/data/upgrade-info.json $HOME/.nolus/cosmovisor/genesis/upgrade-info.json
```

### Start service and check the logs

```bash
sudo systemctl start nolusd && sudo journalctl -u nolusd -f --no-hostname -o cat
```
