---
description: Setting up your validator node has never been so easy. Get your validator running in minutes by following step by step instructions.
---

# Installation

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/okp4.png" alt=""><figcaption></figcaption></figure>

**Chain ID**: okp4-nemeton-1 | **Latest Version Tag**: v4.1.0 | **Custom Port**: 136

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
rm -rf okp4d
git clone https://github.com/okp4/okp4d.git
cd okp4d
git checkout v4.1.0

# Build binaries
make build

# Prepare binaries for Cosmovisor
mkdir -p $HOME/.okp4d/cosmovisor/genesis/bin
mv target/dist/okp4d $HOME/.okp4d/cosmovisor/genesis/bin/
rm -rf build

# Create application symlinks
sudo ln -s $HOME/.okp4d/cosmovisor/genesis $HOME/.okp4d/cosmovisor/current -f
sudo ln -s $HOME/.okp4d/cosmovisor/current/bin/okp4d /usr/local/bin/okp4d -f
```

### Install Cosmovisor and create a service

```bash
# Download and install Cosmovisor
go install cosmossdk.io/tools/cosmovisor/cmd/cosmovisor@v1.4.0

# Create service
sudo tee /etc/systemd/system/okp4d.service > /dev/null << EOF
[Unit]
Description=okp4-testnet node service
After=network-online.target

[Service]
User=$USER
ExecStart=$(which cosmovisor) run start
Restart=on-failure
RestartSec=10
LimitNOFILE=65535
Environment="DAEMON_HOME=$HOME/.okp4d"
Environment="DAEMON_NAME=okp4d"
Environment="UNSAFE_SKIP_BACKUP=true"
Environment="PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:$HOME/.okp4d/cosmovisor/current/bin"

[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable okp4d
```

### Initialize the node

```bash
# Set node configuration
okp4d config chain-id okp4-nemeton-1
okp4d config keyring-backend test
okp4d config node tcp://localhost:13657

# Initialize the node
okp4d init $MONIKER --chain-id okp4-nemeton-1

# Download genesis and addrbook
curl -Ls https://snapshots.kjnodes.com/okp4-testnet/genesis.json > $HOME/.okp4d/config/genesis.json
curl -Ls https://snapshots.kjnodes.com/okp4-testnet/addrbook.json > $HOME/.okp4d/config/addrbook.json

# Add seeds
sed -i -e "s|^seeds *=.*|seeds = \"3f472746f46493309650e5a033076689996c8881@okp4-testnet.rpc.kjnodes.com:13659\"|" $HOME/.okp4d/config/config.toml

# Set minimum gas price
sed -i -e "s|^minimum-gas-prices *=.*|minimum-gas-prices = \"0uknow\"|" $HOME/.okp4d/config/app.toml

# Set pruning
sed -i \
  -e 's|^pruning *=.*|pruning = "custom"|' \
  -e 's|^pruning-keep-recent *=.*|pruning-keep-recent = "100"|' \
  -e 's|^pruning-keep-every *=.*|pruning-keep-every = "0"|' \
  -e 's|^pruning-interval *=.*|pruning-interval = "19"|' \
  $HOME/.okp4d/config/app.toml

# Set custom ports
sed -i -e "s%^proxy_app = \"tcp://127.0.0.1:26658\"%proxy_app = \"tcp://127.0.0.1:13658\"%; s%^laddr = \"tcp://127.0.0.1:26657\"%laddr = \"tcp://127.0.0.1:13657\"%; s%^pprof_laddr = \"localhost:6060\"%pprof_laddr = \"localhost:13660\"%; s%^laddr = \"tcp://0.0.0.0:26656\"%laddr = \"tcp://0.0.0.0:13656\"%; s%^prometheus_listen_addr = \":26660\"%prometheus_listen_addr = \":13666\"%" $HOME/.okp4d/config/config.toml
sed -i -e "s%^address = \"tcp://0.0.0.0:1317\"%address = \"tcp://0.0.0.0:13617\"%; s%^address = \":8080\"%address = \":13680\"%; s%^address = \"0.0.0.0:9090\"%address = \"0.0.0.0:13690\"%; s%^address = \"0.0.0.0:9091\"%address = \"0.0.0.0:13691\"%; s%:8545%:13645%; s%:8546%:13646%; s%:6065%:13665%" $HOME/.okp4d/config/app.toml
```

### Download latest chain snapshot

```bash
curl -L https://snapshots.kjnodes.com/okp4-testnet/snapshot_latest.tar.lz4 | tar -Ilz4 -xf - -C $HOME/.okp4d
[[ -f $HOME/.okp4d/data/upgrade-info.json ]] && cp $HOME/.okp4d/data/upgrade-info.json $HOME/.okp4d/cosmovisor/genesis/upgrade-info.json
```

### Start service and check the logs

```bash
sudo systemctl start okp4d && sudo journalctl -u okp4d -f --no-hostname -o cat
```
