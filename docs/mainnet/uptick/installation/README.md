---
description: Setting up your validator node has never been so easy. Get your validator running in minutes by following step by step instructions.
---

# Installation

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/uptick.png" alt=""><figcaption></figcaption></figure>

**Chain ID**: uptick_117-1 | **Latest Version Tag**: v0.2.8 | **Custom Port**: 115

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
rm -rf uptick
git clone https://github.com/UptickNetwork/uptick.git
cd uptick
git checkout v0.2.8

# Build binaries
make build

# Prepare binaries for Cosmovisor
mkdir -p $HOME/.uptickd/cosmovisor/genesis/bin
mv build/uptickd $HOME/.uptickd/cosmovisor/genesis/bin/
rm -rf build

# Create application symlinks
sudo ln -s $HOME/.uptickd/cosmovisor/genesis $HOME/.uptickd/cosmovisor/current -f
sudo ln -s $HOME/.uptickd/cosmovisor/current/bin/uptickd /usr/local/bin/uptickd -f
```

### Install Cosmovisor and create a service

```bash
# Download and install Cosmovisor
go install cosmossdk.io/tools/cosmovisor/cmd/cosmovisor@v1.4.0

# Create service
sudo tee /etc/systemd/system/uptickd.service > /dev/null << EOF
[Unit]
Description=uptick node service
After=network-online.target

[Service]
User=$USER
ExecStart=$(which cosmovisor) run start
Restart=on-failure
RestartSec=10
LimitNOFILE=65535
Environment="DAEMON_HOME=$HOME/.uptickd"
Environment="DAEMON_NAME=uptickd"
Environment="UNSAFE_SKIP_BACKUP=true"
Environment="PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:$HOME/.uptickd/cosmovisor/current/bin"

[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable uptickd
```

### Initialize the node

```bash
# Set node configuration
uptickd config chain-id uptick_117-1
uptickd config keyring-backend file
uptickd config node tcp://localhost:11557

# Initialize the node
uptickd init $MONIKER --chain-id uptick_117-1

# Download genesis and addrbook
curl -Ls https://snapshots.kjnodes.com/uptick/genesis.json > $HOME/.uptickd/config/genesis.json
curl -Ls https://snapshots.kjnodes.com/uptick/addrbook.json > $HOME/.uptickd/config/addrbook.json

# Add seeds
sed -i -e "s|^seeds *=.*|seeds = \"400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@uptick.rpc.kjnodes.com:11559\"|" $HOME/.uptickd/config/config.toml

# Set minimum gas price
sed -i -e "s|^minimum-gas-prices *=.*|minimum-gas-prices = \"0auptick\"|" $HOME/.uptickd/config/app.toml

# Set pruning
sed -i \
  -e 's|^pruning *=.*|pruning = "custom"|' \
  -e 's|^pruning-keep-recent *=.*|pruning-keep-recent = "100"|' \
  -e 's|^pruning-keep-every *=.*|pruning-keep-every = "0"|' \
  -e 's|^pruning-interval *=.*|pruning-interval = "19"|' \
  $HOME/.uptickd/config/app.toml

# Set custom ports
sed -i -e "s%^proxy_app = \"tcp://127.0.0.1:26658\"%proxy_app = \"tcp://127.0.0.1:11558\"%; s%^laddr = \"tcp://127.0.0.1:26657\"%laddr = \"tcp://127.0.0.1:11557\"%; s%^pprof_laddr = \"localhost:6060\"%pprof_laddr = \"localhost:11560\"%; s%^laddr = \"tcp://0.0.0.0:26656\"%laddr = \"tcp://0.0.0.0:11556\"%; s%^prometheus_listen_addr = \":26660\"%prometheus_listen_addr = \":11566\"%" $HOME/.uptickd/config/config.toml
sed -i -e "s%^address = \"tcp://0.0.0.0:1317\"%address = \"tcp://0.0.0.0:11517\"%; s%^address = \":8080\"%address = \":11580\"%; s%^address = \"0.0.0.0:9090\"%address = \"0.0.0.0:11590\"%; s%^address = \"0.0.0.0:9091\"%address = \"0.0.0.0:11591\"%; s%:8545%:11545%; s%:8546%:11546%; s%:6065%:11565%" $HOME/.uptickd/config/app.toml
```

### Download latest chain snapshot

```bash
curl -L https://snapshots.kjnodes.com/uptick/snapshot_latest.tar.lz4 | tar -Ilz4 -xf - -C $HOME/.uptickd
[[ -f $HOME/.uptickd/data/upgrade-info.json ]] && cp $HOME/.uptickd/data/upgrade-info.json $HOME/.uptickd/cosmovisor/genesis/upgrade-info.json
```

### Start service and check the logs

```bash
sudo systemctl start uptickd && sudo journalctl -u uptickd -f --no-hostname -o cat
```
