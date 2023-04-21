---
description: Setting up your validator node has never been so easy. Get your validator running in minutes by following step by step instructions.
---

# Installation

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/agoricdev.png" width="150" alt=""><figcaption></figcaption></figure>

**Chain ID**: agoricdev-17 | **Latest Version Tag**: pismoC | **Custom Port**: 14

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
curl -Ls https://go.dev/dl/go1.19.8.linux-amd64.tar.gz | sudo tar -xzf - -C /usr/local
eval $(echo 'export PATH=$PATH:/usr/local/go/bin' | sudo tee /etc/profile.d/golang.sh)
eval $(echo 'export PATH=$PATH:$HOME/go/bin' | tee -a $HOME/.profile)
```

### Download and build binaries

```bash
# Clone project repository
cd $HOME
rm -rf agoric-sdk
git clone https://github.com/Agoric/agoric-sdk.git
cd agoric-sdk
git checkout pismoC

# Build binaries
make build

# Prepare binaries for Cosmovisor
mkdir -p $HOME/.agoric/cosmovisor/genesis/bin
mv golang/cosmos/build/agd $HOME/.agoric/cosmovisor/genesis/bin/
rm -rf build

# Create application symlinks
ln -s $HOME/.agoric/cosmovisor/genesis $HOME/.agoric/cosmovisor/current
sudo ln -s $HOME/.agoric/cosmovisor/current/bin/agd /usr/local/bin/agd
```

### Install Cosmovisor and create a service

```bash
# Download and install Cosmovisor
go install cosmossdk.io/tools/cosmovisor/cmd/cosmovisor@v1.4.0

# Create service
sudo tee /etc/systemd/system/agd.service > /dev/null << EOF
[Unit]
Description=agoricdev-testnet node service
After=network-online.target

[Service]
User=$USER
ExecStart=$(which cosmovisor) run start
Restart=on-failure
RestartSec=10
LimitNOFILE=65535
Environment="DAEMON_HOME=$HOME/.agoric"
Environment="DAEMON_NAME=agd"
Environment="UNSAFE_SKIP_BACKUP=true"
Environment="PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:$HOME/.agoric/cosmovisor/current/bin"

[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable agd
```

### Initialize the node

```bash
# Set node configuration
agd config chain-id agoricdev-17
agd config keyring-backend test
agd config node tcp://localhost:14657

# Initialize the node
agd init $MONIKER --chain-id agoricdev-17

# Download genesis and addrbook
curl -Ls https://snapshots.kjnodes.com/agoricdev-testnet/genesis.json > $HOME/.agoric/config/genesis.json
curl -Ls https://snapshots.kjnodes.com/agoricdev-testnet/addrbook.json > $HOME/.agoric/config/addrbook.json

# Add seeds
sed -i -e "s|^seeds *=.*|seeds = \"3f472746f46493309650e5a033076689996c8881@agoricdev-testnet.rpc.kjnodes.com:14659\"|" $HOME/.agoric/config/config.toml

# Set minimum gas price
sed -i -e "s|^minimum-gas-prices *=.*|minimum-gas-prices = \"0.025ubld\"|" $HOME/.agoric/config/app.toml

# Set pruning
sed -i \
  -e 's|^pruning *=.*|pruning = "custom"|' \
  -e 's|^pruning-keep-recent *=.*|pruning-keep-recent = "100"|' \
  -e 's|^pruning-keep-every *=.*|pruning-keep-every = "0"|' \
  -e 's|^pruning-interval *=.*|pruning-interval = "19"|' \
  $HOME/.agoric/config/app.toml

# Set custom ports
sed -i -e "s%^proxy_app = \"tcp://127.0.0.1:26658\"%proxy_app = \"tcp://127.0.0.1:14658\"%; s%^laddr = \"tcp://127.0.0.1:26657\"%laddr = \"tcp://127.0.0.1:14657\"%; s%^pprof_laddr = \"localhost:6060\"%pprof_laddr = \"localhost:14060\"%; s%^laddr = \"tcp://0.0.0.0:26656\"%laddr = \"tcp://0.0.0.0:14656\"%; s%^prometheus_listen_addr = \":26660\"%prometheus_listen_addr = \":14660\"%" $HOME/.agoric/config/config.toml
sed -i -e "s%^address = \"tcp://0.0.0.0:1317\"%address = \"tcp://0.0.0.0:14317\"%; s%^address = \":8080\"%address = \":14080\"%; s%^address = \"0.0.0.0:9090\"%address = \"0.0.0.0:14090\"%; s%^address = \"0.0.0.0:9091\"%address = \"0.0.0.0:14091\"%; s%:8545%:14545%; s%:8546%:14546%; s%:6065%:14065%" $HOME/.agoric/config/app.toml
```

### Download latest chain snapshot

```bash
curl -L https://snapshots.kjnodes.com/agoricdev-testnet/snapshot_latest.tar.lz4 | tar -Ilz4 -xf - -C $HOME/.agoric
[[ -f $HOME/.agoric/data/upgrade-info.json ]] && cp $HOME/.agoric/data/upgrade-info.json $HOME/.agoric/cosmovisor/genesis/upgrade-info.json
```

### Start service and check the logs

```bash
sudo systemctl start agd && sudo journalctl -u agd -f --no-hostname -o cat
```
