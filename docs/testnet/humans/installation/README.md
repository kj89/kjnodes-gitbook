---
description: Setting up your validator node has never been so easy. Get your validator running in minutes by following step by step instructions.
---

# Installation

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/humans.png" width="150" alt=""><figcaption></figcaption></figure>

**Chain ID**: humans_3000-1 | **Latest Version Tag**: v0.1.0 | **Custom Port**: 22

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
curl -Ls https://go.dev/dl/go1.20.3.linux-amd64.tar.gz | sudo tar -xzf - -C /usr/local
eval $(echo 'export PATH=$PATH:/usr/local/go/bin' | sudo tee /etc/profile.d/golang.sh)
eval $(echo 'export PATH=$PATH:$HOME/go/bin' | tee -a $HOME/.profile)
```

### Download and build binaries

```bash
# Clone project repository
cd $HOME
rm -rf humans
git clone https://github.com/humansdotai/humans.git
cd humans
git checkout v0.1.0

# Build binaries
make build

# Prepare binaries for Cosmovisor
mkdir -p $HOME/.humansd/cosmovisor/genesis/bin
mv build/humansd $HOME/.humansd/cosmovisor/genesis/bin/
rm -rf build

# Create application symlinks
ln -s $HOME/.humansd/cosmovisor/genesis $HOME/.humansd/cosmovisor/current
sudo ln -s $HOME/.humansd/cosmovisor/current/bin/humansd /usr/local/bin/humansd
```

### Install Cosmovisor and create a service

```bash
# Download and install Cosmovisor
go install cosmossdk.io/tools/cosmovisor/cmd/cosmovisor@v1.4.0

# Create service
sudo tee /etc/systemd/system/humansd.service > /dev/null << EOF
[Unit]
Description=humans-testnet node service
After=network-online.target

[Service]
User=$USER
ExecStart=$(which cosmovisor) run start
Restart=on-failure
RestartSec=10
LimitNOFILE=65535
Environment="DAEMON_HOME=$HOME/.humansd"
Environment="DAEMON_NAME=humansd"
Environment="UNSAFE_SKIP_BACKUP=true"
Environment="PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:$HOME/.humansd/cosmovisor/current/bin"

[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable humansd
```

### Initialize the node

```bash
# Set node configuration
humansd config chain-id humans_3000-1
humansd config keyring-backend test
humansd config node tcp://localhost:22657

# Initialize the node
humansd init $MONIKER --chain-id humans_3000-1

# Download genesis and addrbook
curl -Ls https://snapshots.kjnodes.com/humans-testnet/genesis.json > $HOME/.humansd/config/genesis.json
curl -Ls https://snapshots.kjnodes.com/humans-testnet/addrbook.json > $HOME/.humansd/config/addrbook.json

# Add seeds
sed -i -e "s|^seeds *=.*|seeds = \"3f472746f46493309650e5a033076689996c8881@humans-testnet.rpc.kjnodes.com:22659\"|" $HOME/.humansd/config/config.toml

# Set minimum gas price
sed -i -e "s|^minimum-gas-prices *=.*|minimum-gas-prices = \"0aheart\"|" $HOME/.humansd/config/app.toml

# Set pruning
sed -i \
  -e 's|^pruning *=.*|pruning = "custom"|' \
  -e 's|^pruning-keep-recent *=.*|pruning-keep-recent = "100"|' \
  -e 's|^pruning-keep-every *=.*|pruning-keep-every = "0"|' \
  -e 's|^pruning-interval *=.*|pruning-interval = "19"|' \
  $HOME/.humansd/config/app.toml

# Set custom ports
sed -i -e "s%^proxy_app = \"tcp://127.0.0.1:26658\"%proxy_app = \"tcp://127.0.0.1:22658\"%; s%^laddr = \"tcp://127.0.0.1:26657\"%laddr = \"tcp://127.0.0.1:22657\"%; s%^pprof_laddr = \"localhost:6060\"%pprof_laddr = \"localhost:22060\"%; s%^laddr = \"tcp://0.0.0.0:26656\"%laddr = \"tcp://0.0.0.0:22656\"%; s%^prometheus_listen_addr = \":26660\"%prometheus_listen_addr = \":22660\"%" $HOME/.humansd/config/config.toml
sed -i -e "s%^address = \"tcp://0.0.0.0:1317\"%address = \"tcp://0.0.0.0:22317\"%; s%^address = \":8080\"%address = \":22080\"%; s%^address = \"0.0.0.0:9090\"%address = \"0.0.0.0:22090\"%; s%^address = \"0.0.0.0:9091\"%address = \"0.0.0.0:22091\"%; s%:8545%:22545%; s%:8546%:22546%; s%:6065%:22065%" $HOME/.humansd/config/app.toml
```

### Download latest chain snapshot

```bash
curl -L https://snapshots.kjnodes.com/humans-testnet/snapshot_latest.tar.lz4 | tar -Ilz4 -xf - -C $HOME/.humansd
[[ -f $HOME/.humansd/data/upgrade-info.json ]] && cp $HOME/.humansd/data/upgrade-info.json $HOME/.humansd/cosmovisor/genesis/upgrade-info.json
```

### Start service and check the logs

```bash
sudo systemctl start humansd && sudo journalctl -u humansd -f --no-hostname -o cat
```
