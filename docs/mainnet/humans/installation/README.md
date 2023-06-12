---
description: Setting up your validator node has never been so easy. Get your validator running in minutes by following step by step instructions.
---

# Installation

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/humans.png" alt=""><figcaption></figcaption></figure>

**Chain ID**: humans_1089-1 | **Latest Version Tag**: v1.0.0 | **Custom Port**: 122

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
rm -rf humans
git clone https://github.com/humansdotai/humans.git
cd humans
git checkout v1.0.0

# Build binaries
make build

# Prepare binaries for Cosmovisor
mkdir -p $HOME/.humansd/cosmovisor/genesis/bin
mv build/humansd $HOME/.humansd/cosmovisor/genesis/bin/
rm -rf build

# Create application symlinks
sudo ln -s $HOME/.humansd/cosmovisor/genesis $HOME/.humansd/cosmovisor/current -f
sudo ln -s $HOME/.humansd/cosmovisor/current/bin/humansd /usr/local/bin/humansd -f
```

### Install Cosmovisor and create a service

```bash
# Download and install Cosmovisor
go install cosmossdk.io/tools/cosmovisor/cmd/cosmovisor@v1.4.0

# Create service
sudo tee /etc/systemd/system/humansd.service > /dev/null << EOF
[Unit]
Description=humans node service
After=network-online.target

[Service]
User=$USER
ExecStart=$(which cosmovisor) run start --metrics --pruning=nothing --evm.tracer=json --minimum-gas-prices=1800000000aheart json-rpc.api eth,net,web3,miner --api.enable
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
humansd config chain-id humans_1089-1
humansd config keyring-backend file
humansd config node tcp://localhost:12257

# Initialize the node
humansd init $MONIKER --chain-id humans_1089-1

# Download genesis and addrbook
curl -Ls https://snapshots.kjnodes.com/humans/genesis.json > $HOME/.humansd/config/genesis.json
curl -Ls https://snapshots.kjnodes.com/humans/addrbook.json > $HOME/.humansd/config/addrbook.json

# Add seeds
sed -i -e "s|^seeds *=.*|seeds = \"400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@humans.rpc.kjnodes.com:12259\"|" $HOME/.humansd/config/config.toml

# Set minimum gas price
sed -i -e "s|^minimum-gas-prices *=.*|minimum-gas-prices = \"0aheart\"|" $HOME/.humansd/config/app.toml

# Set pruning
sed -i \
  -e 's|^pruning *=.*|pruning = "nothing"|' \
  $HOME/.humansd/config/app.toml

# Set custom ports
sed -i -e "s%^proxy_app = \"tcp://127.0.0.1:26658\"%proxy_app = \"tcp://0.0.0.0:12258\"%; s%^laddr = \"tcp://127.0.0.1:26657\"%laddr = \"tcp://0.0.0.0:12257\"%; s%^pprof_laddr = \"localhost:6060\"%pprof_laddr = \"localhost:12266\"%; s%^laddr = \"tcp://0.0.0.0:26656\"%laddr = \"tcp://0.0.0.0:12256\"%; s%^prometheus_listen_addr = \":26660\"%prometheus_listen_addr = \":12260\"%" $HOME/.humansd/config/config.toml
sed -i -e "s%^address = \"tcp://0.0.0.0:1317\"%address = \"tcp://0.0.0.0:12217\"%; s%^address = \":8080\"%address = \":12280\"%; s%^address = \"0.0.0.0:9090\"%address = \"0.0.0.0:12290\"%; s%^address = \"0.0.0.0:9091\"%address = \"0.0.0.0:12291\"%; s%^address = \"127.0.0.1:8545\"%address = \"0.0.0.0:12245\"%; s%^ws-address = \"127.0.0.1:8546\"%ws-address = \"0.0.0.0:12246\"%; s%^metrics-address = \"127.0.0.1:6065\"%metrics-address = \"0.0.0.0:12265\"%" $HOME/.humansd/config/app.toml
```

# Configuration changes for optimization and metrics
```
# config.toml
sed -i \
  -e 's|^create_empty_blocks *=.*|create_empty_blocks = false|' \
  -e 's|^prometheus *=.*|prometheus = true|' \
  -e 's|^create_empty_blocks_interval *=.*|create_empty_blocks_interval = "30s"|' \
  -e 's|^timeout_propose *=.*|timeout_propose = "30s"|' \
  -e 's|^timeout_propose_delta *=.*|timeout_propose_delta = "5s"|' \
  -e 's|^timeout_prevote *=.*|timeout_prevote = "10s"|' \
  -e 's|^timeout_prevote_delta *=.*|timeout_prevote_delta = "5s"|' \
  -e 's|^cors_allowed_origins *=.*|cors_allowed_origins = ["*.humans.ai","*.humans.zone"]|' \
  -e 's|^timeout_prevote_delta *=.*|timeout_prevote_delta = "5s"|' \
  $HOME/.humansd/config/config.toml

# app.toml
sed -i \
  -e 's|^prometheus-retention-time *=.*|prometheus-retention-time = 1000000000000|' \
  -e 's|^enabled *=.*|enabled = true|' \
  -e '/^\[api\]$/,/^\[/ s/enable = false/enable = true/' \
  -e 's|^swagger *=.*|swagger = true|' \
  -e 's|^max-open-connections *=.*|max-open-connections = 100|' \
  -e 's|^rpc-read-timeout *=.*|rpc-read-timeout = 5|' \
  -e 's|^rpc-write-timeout *=.*|rpc-write-timeout = 3|' \
  -e 's|^rpc-max-body-bytes *=.*|rpc-max-body-bytes = 1000000|' \
  -e 's|^enabled-unsafe-cors *=.*|enabled-unsafe-cors = false|' \
  $HOME/.humansd/config/app.toml
```

### Download latest chain snapshot

```bash
curl -L https://snapshots.kjnodes.com/humans/snapshot_latest.tar.lz4 | tar -Ilz4 -xf - -C $HOME/.humansd
[[ -f $HOME/.humansd/data/upgrade-info.json ]] && cp $HOME/.humansd/data/upgrade-info.json $HOME/.humansd/cosmovisor/genesis/upgrade-info.json
```

### Start service and check the logs

```bash
sudo systemctl start humansd && sudo journalctl -u humansd -f --no-hostname -o cat
```
