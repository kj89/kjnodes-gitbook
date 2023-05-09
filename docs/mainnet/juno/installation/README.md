---
description: Setting up your validator node has never been so easy. Get your validator running in minutes by following step by step instructions.
---

# Installation

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/juno.png" alt=""><figcaption></figcaption></figure>

**Chain ID**: juno-1 | **Latest Version Tag**: v14.0.0 | **Custom Port**: 157

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
curl -Ls https://go.dev/dl/go1.19.9.linux-amd64.tar.gz | sudo tar -xzf - -C /usr/local
eval $(echo 'export PATH=$PATH:/usr/local/go/bin' | sudo tee /etc/profile.d/golang.sh)
eval $(echo 'export PATH=$PATH:$HOME/go/bin' | tee -a $HOME/.profile)
```

### Download and build binaries

```bash
# Clone project repository
cd $HOME
rm -rf juno
git clone https://github.com/CosmosContracts/juno.git
cd juno
git checkout v14.0.0

# Build binaries
make build

# Prepare binaries for Cosmovisor
mkdir -p $HOME/.juno/cosmovisor/genesis/bin
mv bin/junod $HOME/.juno/cosmovisor/genesis/bin/
rm -rf build

# Create application symlinks
sudo ln -s $HOME/.juno/cosmovisor/genesis $HOME/.juno/cosmovisor/current -f
sudo ln -s $HOME/.juno/cosmovisor/current/bin/junod /usr/local/bin/junod -f
```

### Install Cosmovisor and create a service

```bash
# Download and install Cosmovisor
go install cosmossdk.io/tools/cosmovisor/cmd/cosmovisor@v1.4.0

# Create service
sudo tee /etc/systemd/system/junod.service > /dev/null << EOF
[Unit]
Description=juno node service
After=network-online.target

[Service]
User=$USER
ExecStart=$(which cosmovisor) run start
Restart=on-failure
RestartSec=10
LimitNOFILE=65535
Environment="DAEMON_HOME=$HOME/.juno"
Environment="DAEMON_NAME=junod"
Environment="UNSAFE_SKIP_BACKUP=true"
Environment="PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:$HOME/.juno/cosmovisor/current/bin"

[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable junod
```

### Initialize the node

```bash
# Set node configuration
junod config chain-id juno-1
junod config keyring-backend file
junod config node tcp://localhost:15757

# Initialize the node
junod init $MONIKER --chain-id juno-1

# Download genesis and addrbook
curl -Ls https://snapshots.kjnodes.com/juno/genesis.json > $HOME/.juno/config/genesis.json
curl -Ls https://snapshots.kjnodes.com/juno/addrbook.json > $HOME/.juno/config/addrbook.json

# Add seeds
sed -i -e "s|^seeds *=.*|seeds = \"400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@juno.rpc.kjnodes.com:15759\"|" $HOME/.juno/config/config.toml

# Set minimum gas price
sed -i -e "s|^minimum-gas-prices *=.*|minimum-gas-prices = \"0ujuno\"|" $HOME/.juno/config/app.toml

# Set pruning
sed -i \
  -e 's|^pruning *=.*|pruning = "custom"|' \
  -e 's|^pruning-keep-recent *=.*|pruning-keep-recent = "100"|' \
  -e 's|^pruning-keep-every *=.*|pruning-keep-every = "0"|' \
  -e 's|^pruning-interval *=.*|pruning-interval = "19"|' \
  $HOME/.juno/config/app.toml

# Set custom ports
sed -i -e "s%^proxy_app = \"tcp://127.0.0.1:26658\"%proxy_app = \"tcp://127.0.0.1:15758\"%; s%^laddr = \"tcp://127.0.0.1:26657\"%laddr = \"tcp://127.0.0.1:15757\"%; s%^pprof_laddr = \"localhost:6060\"%pprof_laddr = \"localhost:15760\"%; s%^laddr = \"tcp://0.0.0.0:26656\"%laddr = \"tcp://0.0.0.0:15756\"%; s%^prometheus_listen_addr = \":26660\"%prometheus_listen_addr = \":15766\"%" $HOME/.juno/config/config.toml
sed -i -e "s%^address = \"tcp://0.0.0.0:1317\"%address = \"tcp://0.0.0.0:15717\"%; s%^address = \":8080\"%address = \":15780\"%; s%^address = \"0.0.0.0:9090\"%address = \"0.0.0.0:15790\"%; s%^address = \"0.0.0.0:9091\"%address = \"0.0.0.0:15791\"%; s%:8545%:15745%; s%:8546%:15746%; s%:6065%:15765%" $HOME/.juno/config/app.toml
```

### Download latest chain snapshot

```bash
curl -L https://snapshots.kjnodes.com/juno/snapshot_latest.tar.lz4 | tar -Ilz4 -xf - -C $HOME/.juno
[[ -f $HOME/.juno/data/upgrade-info.json ]] && cp $HOME/.juno/data/upgrade-info.json $HOME/.juno/cosmovisor/genesis/upgrade-info.json
```

### Start service and check the logs

```bash
sudo systemctl start junod && sudo journalctl -u junod -f --no-hostname -o cat
```
