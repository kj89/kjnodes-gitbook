---
description: Setting up your validator node has never been so easy. Get your validator running in minutes by following step by step instructions.
---

# Installation

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/sei.png" width="150" alt=""><figcaption></figcaption></figure>

**Chain ID**: atlantic-2 | **Latest Version Tag**: 2.0.40beta | **Custom Port**: 12

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
curl -Ls https://go.dev/dl/go1.19.7.linux-amd64.tar.gz | sudo tar -xzf - -C /usr/local
eval $(echo 'export PATH=$PATH:/usr/local/go/bin' | sudo tee /etc/profile.d/golang.sh)
eval $(echo 'export PATH=$PATH:$HOME/go/bin' | tee -a $HOME/.profile)
```

### Download and build binaries

```bash
# Clone project repository
cd $HOME
rm -rf sei-chain
git clone https://github.com/sei-protocol/sei-chain.git
cd sei-chain
git checkout 2.0.40beta

# Build binaries
make build

# Prepare binaries for Cosmovisor
mkdir -p $HOME/.sei/cosmovisor/genesis/bin
mv build/seid $HOME/.sei/cosmovisor/genesis/bin/
rm -rf build

# Create application symlinks
ln -s $HOME/.sei/cosmovisor/genesis $HOME/.sei/cosmovisor/current
sudo ln -s $HOME/.sei/cosmovisor/current/bin/seid /usr/local/bin/seid
```

### Install Cosmovisor and create a service

```bash
# Download and install Cosmovisor
go install cosmossdk.io/tools/cosmovisor/cmd/cosmovisor@v1.4.0

# Create service
sudo tee /etc/systemd/system/seid.service > /dev/null << EOF
[Unit]
Description=sei-testnet node service
After=network-online.target

[Service]
User=$USER
ExecStart=$(which cosmovisor) run start
Restart=on-failure
RestartSec=10
LimitNOFILE=65535
Environment="DAEMON_HOME=$HOME/.sei"
Environment="DAEMON_NAME=seid"
Environment="UNSAFE_SKIP_BACKUP=true"
Environment="PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:$HOME/.sei/cosmovisor/current/bin"

[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable seid
```

### Initialize the node

```bash
# Set node configuration
seid config chain-id atlantic-2
seid config keyring-backend test
seid config node tcp://localhost:12657

# Initialize the node
seid init $MONIKER --chain-id atlantic-2

# Download genesis and addrbook
curl -Ls https://snapshots.kjnodes.com/sei-testnet/genesis.json > $HOME/.sei/config/genesis.json
curl -Ls https://snapshots.kjnodes.com/sei-testnet/addrbook.json > $HOME/.sei/config/addrbook.json

# Add seeds
sed -i -e "s|^seeds *=.*|seeds = \"3f472746f46493309650e5a033076689996c8881@sei-testnet.rpc.kjnodes.com:12659\"|" $HOME/.sei/config/config.toml

# Set minimum gas price
sed -i -e "s|^minimum-gas-prices *=.*|minimum-gas-prices = \"0.0001usei\"|" $HOME/.sei/config/app.toml

# Set pruning
sed -i \
  -e 's|^pruning *=.*|pruning = "custom"|' \
  -e 's|^pruning-keep-recent *=.*|pruning-keep-recent = "100"|' \
  -e 's|^pruning-keep-every *=.*|pruning-keep-every = "0"|' \
  -e 's|^pruning-interval *=.*|pruning-interval = "19"|' \
  $HOME/.sei/config/app.toml

# Set custom ports
sed -i -e "s%^proxy_app = \"tcp://127.0.0.1:26658\"%proxy_app = \"tcp://127.0.0.1:12658\"%; s%^laddr = \"tcp://127.0.0.1:26657\"%laddr = \"tcp://127.0.0.1:12657\"%; s%^pprof_laddr = \"localhost:6060\"%pprof_laddr = \"localhost:12060\"%; s%^laddr = \"tcp://0.0.0.0:26656\"%laddr = \"tcp://0.0.0.0:12656\"%; s%^prometheus_listen_addr = \":26660\"%prometheus_listen_addr = \":12660\"%" $HOME/.sei/config/config.toml
sed -i -e "s%^address = \"tcp://0.0.0.0:1317\"%address = \"tcp://0.0.0.0:12317\"%; s%^address = \":8080\"%address = \":12080\"%; s%^address = \"0.0.0.0:9090\"%address = \"0.0.0.0:12090\"%; s%^address = \"0.0.0.0:9091\"%address = \"0.0.0.0:12091\"%; s%^address = \"0.0.0.0:8545\"%address = \"0.0.0.0:12545\"%; s%^ws-address = \"0.0.0.0:8546\"%ws-address = \"0.0.0.0:12546\"%" $HOME/.sei/config/app.toml
```

### Download latest chain snapshot

```bash
curl -L https://snapshots.kjnodes.com/sei-testnet/snapshot_latest.tar.lz4 | tar -Ilz4 -xf - -C $HOME/.sei
[[ -f $HOME/.sei/data/upgrade-info.json ]] && cp $HOME/.sei/data/upgrade-info.json $HOME/.sei/cosmovisor/genesis/upgrade-info.json
```

### Start service and check the logs

```bash
sudo systemctl start seid && sudo journalctl -u seid -f --no-hostname -o cat
```
