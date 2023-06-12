---
description: Setting up your validator node has never been so easy. Get your validator running in minutes by following step by step instructions.
---

# Installation

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/althea.png" alt=""><figcaption></figcaption></figure>

**Chain ID**: althea_7357-1 | **Latest Version Tag**: v0.3.2 | **Custom Port**: 152

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
rm -rf althea-chain
git clone https://github.com/althea-net/althea-chain.git
cd althea-chain
git checkout v0.3.2

# Build binaries
make build

# Prepare binaries for Cosmovisor
mkdir -p $HOME/.althea/cosmovisor/genesis/bin
mv build/althea $HOME/.althea/cosmovisor/genesis/bin/
rm -rf build

# Create application symlinks
sudo ln -s $HOME/.althea/cosmovisor/genesis $HOME/.althea/cosmovisor/current -f
sudo ln -s $HOME/.althea/cosmovisor/current/bin/althea /usr/local/bin/althea -f
```

### Install Cosmovisor and create a service

```bash
# Download and install Cosmovisor
go install cosmossdk.io/tools/cosmovisor/cmd/cosmovisor@v1.4.0

# Create service
sudo tee /etc/systemd/system/althea.service > /dev/null << EOF
[Unit]
Description=althea-testnet node service
After=network-online.target

[Service]
User=$USER
ExecStart=$(which cosmovisor) run start
Restart=on-failure
RestartSec=10
LimitNOFILE=65535
Environment="DAEMON_HOME=$HOME/.althea"
Environment="DAEMON_NAME=althea"
Environment="UNSAFE_SKIP_BACKUP=true"
Environment="PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:$HOME/.althea/cosmovisor/current/bin"

[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable althea
```

### Initialize the node

```bash
# Set node configuration
althea config chain-id althea_7357-1
althea config keyring-backend test
althea config node tcp://localhost:15257

# Initialize the node
althea init $MONIKER --chain-id althea_7357-1

# Download genesis and addrbook
curl -Ls https://snapshots.kjnodes.com/althea-testnet/genesis.json > $HOME/.althea/config/genesis.json
curl -Ls https://snapshots.kjnodes.com/althea-testnet/addrbook.json > $HOME/.althea/config/addrbook.json

# Add seeds
sed -i -e "s|^seeds *=.*|seeds = \"3f472746f46493309650e5a033076689996c8881@althea-testnet.rpc.kjnodes.com:15259\"|" $HOME/.althea/config/config.toml

# Set minimum gas price
sed -i -e "s|^minimum-gas-prices *=.*|minimum-gas-prices = \"0ualthea\"|" $HOME/.althea/config/app.toml

# Set pruning
sed -i \
  -e 's|^pruning *=.*|pruning = "custom"|' \
  -e 's|^pruning-keep-recent *=.*|pruning-keep-recent = "100"|' \
  -e 's|^pruning-keep-every *=.*|pruning-keep-every = "0"|' \
  -e 's|^pruning-interval *=.*|pruning-interval = "19"|' \
  $HOME/.althea/config/app.toml

# Set custom ports
sed -i -e "s%^proxy_app = \"tcp://127.0.0.1:26658\"%proxy_app = \"tcp://127.0.0.1:15258\"%; s%^laddr = \"tcp://127.0.0.1:26657\"%laddr = \"tcp://127.0.0.1:15257\"%; s%^pprof_laddr = \"localhost:6060\"%pprof_laddr = \"localhost:15260\"%; s%^laddr = \"tcp://0.0.0.0:26656\"%laddr = \"tcp://0.0.0.0:15256\"%; s%^prometheus_listen_addr = \":26660\"%prometheus_listen_addr = \":15266\"%" $HOME/.althea/config/config.toml
sed -i -e "s%^address = \"tcp://0.0.0.0:1317\"%address = \"tcp://0.0.0.0:15217\"%; s%^address = \":8080\"%address = \":15280\"%; s%^address = \"0.0.0.0:9090\"%address = \"0.0.0.0:15290\"%; s%^address = \"0.0.0.0:9091\"%address = \"0.0.0.0:15291\"%; s%:8545%:15245%; s%:8546%:15246%; s%:6065%:15265%" $HOME/.althea/config/app.toml
```

### Download latest chain snapshot

```bash
curl -L https://snapshots.kjnodes.com/althea-testnet/snapshot_latest.tar.lz4 | tar -Ilz4 -xf - -C $HOME/.althea
[[ -f $HOME/.althea/data/upgrade-info.json ]] && cp $HOME/.althea/data/upgrade-info.json $HOME/.althea/cosmovisor/genesis/upgrade-info.json
```

### Start service and check the logs

```bash
sudo systemctl start althea && sudo journalctl -u althea -f --no-hostname -o cat
```
