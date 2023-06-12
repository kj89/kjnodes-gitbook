---
description: Setting up your validator node has never been so easy. Get your validator running in minutes by following step by step instructions.
---

# Installation

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/teritori.png" alt=""><figcaption></figcaption></figure>

**Chain ID**: teritori-1 | **Latest Version Tag**: v1.4.0 | **Custom Port**: 119

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
rm -rf teritori-chain
git clone https://github.com/TERITORI/teritori-chain.git
cd teritori-chain
git checkout v1.4.0

# Build binaries
make build

# Prepare binaries for Cosmovisor
mkdir -p $HOME/.teritorid/cosmovisor/genesis/bin
mv build/teritorid $HOME/.teritorid/cosmovisor/genesis/bin/
rm -rf build

# Create application symlinks
sudo ln -s $HOME/.teritorid/cosmovisor/genesis $HOME/.teritorid/cosmovisor/current -f
sudo ln -s $HOME/.teritorid/cosmovisor/current/bin/teritorid /usr/local/bin/teritorid -f
```

### Install Cosmovisor and create a service

```bash
# Download and install Cosmovisor
go install cosmossdk.io/tools/cosmovisor/cmd/cosmovisor@v1.4.0

# Create service
sudo tee /etc/systemd/system/teritorid.service > /dev/null << EOF
[Unit]
Description=teritori node service
After=network-online.target

[Service]
User=$USER
ExecStart=$(which cosmovisor) run start
Restart=on-failure
RestartSec=10
LimitNOFILE=65535
Environment="DAEMON_HOME=$HOME/.teritorid"
Environment="DAEMON_NAME=teritorid"
Environment="UNSAFE_SKIP_BACKUP=true"
Environment="PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:$HOME/.teritorid/cosmovisor/current/bin"

[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable teritorid
```

### Initialize the node

```bash
# Set node configuration
teritorid config chain-id teritori-1
teritorid config keyring-backend file
teritorid config node tcp://localhost:11957

# Initialize the node
teritorid init $MONIKER --chain-id teritori-1

# Download genesis and addrbook
curl -Ls https://snapshots.kjnodes.com/teritori/genesis.json > $HOME/.teritorid/config/genesis.json
curl -Ls https://snapshots.kjnodes.com/teritori/addrbook.json > $HOME/.teritorid/config/addrbook.json

# Add seeds
sed -i -e "s|^seeds *=.*|seeds = \"400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@teritori.rpc.kjnodes.com:11959\"|" $HOME/.teritorid/config/config.toml

# Set minimum gas price
sed -i -e "s|^minimum-gas-prices *=.*|minimum-gas-prices = \"0utori\"|" $HOME/.teritorid/config/app.toml

# Set pruning
sed -i \
  -e 's|^pruning *=.*|pruning = "custom"|' \
  -e 's|^pruning-keep-recent *=.*|pruning-keep-recent = "100"|' \
  -e 's|^pruning-keep-every *=.*|pruning-keep-every = "0"|' \
  -e 's|^pruning-interval *=.*|pruning-interval = "19"|' \
  $HOME/.teritorid/config/app.toml

# Set custom ports
sed -i -e "s%^proxy_app = \"tcp://127.0.0.1:26658\"%proxy_app = \"tcp://127.0.0.1:11958\"%; s%^laddr = \"tcp://127.0.0.1:26657\"%laddr = \"tcp://127.0.0.1:11957\"%; s%^pprof_laddr = \"localhost:6060\"%pprof_laddr = \"localhost:11960\"%; s%^laddr = \"tcp://0.0.0.0:26656\"%laddr = \"tcp://0.0.0.0:11956\"%; s%^prometheus_listen_addr = \":26660\"%prometheus_listen_addr = \":11966\"%" $HOME/.teritorid/config/config.toml
sed -i -e "s%^address = \"tcp://0.0.0.0:1317\"%address = \"tcp://0.0.0.0:11917\"%; s%^address = \":8080\"%address = \":11980\"%; s%^address = \"0.0.0.0:9090\"%address = \"0.0.0.0:11990\"%; s%^address = \"0.0.0.0:9091\"%address = \"0.0.0.0:11991\"%; s%:8545%:11945%; s%:8546%:11946%; s%:6065%:11965%" $HOME/.teritorid/config/app.toml
```

### Download latest chain snapshot

```bash
curl -L https://snapshots.kjnodes.com/teritori/snapshot_latest.tar.lz4 | tar -Ilz4 -xf - -C $HOME/.teritorid
[[ -f $HOME/.teritorid/data/upgrade-info.json ]] && cp $HOME/.teritorid/data/upgrade-info.json $HOME/.teritorid/cosmovisor/genesis/upgrade-info.json
```

### Start service and check the logs

```bash
sudo systemctl start teritorid && sudo journalctl -u teritorid -f --no-hostname -o cat
```
