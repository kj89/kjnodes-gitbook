---
description: Setting up your validator node has never been so easy. Get your validator running in minutes by following step by step instructions.
---

# Installation

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/ollo.png" alt=""><figcaption></figcaption></figure>

**Chain ID**: ollo-testnet-1 | **Latest Version Tag**: v0.0.1 | **Custom Port**: 132

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
rm -rf ollo
git clone https://github.com/OLLO-Station/ollo.git
cd ollo
git checkout v0.0.1

# Build binaries
make build

# Prepare binaries for Cosmovisor
mkdir -p $HOME/.ollo/cosmovisor/genesis/bin
mv bin/ollod $HOME/.ollo/cosmovisor/genesis/bin/
rm -rf build

# Create application symlinks
sudo ln -s $HOME/.ollo/cosmovisor/genesis $HOME/.ollo/cosmovisor/current -f
sudo ln -s $HOME/.ollo/cosmovisor/current/bin/ollod /usr/local/bin/ollod -f
```

### Install Cosmovisor and create a service

```bash
# Download and install Cosmovisor
go install cosmossdk.io/tools/cosmovisor/cmd/cosmovisor@v1.4.0

# Create service
sudo tee /etc/systemd/system/ollod.service > /dev/null << EOF
[Unit]
Description=ollo-testnet node service
After=network-online.target

[Service]
User=$USER
ExecStart=$(which cosmovisor) run start
Restart=on-failure
RestartSec=10
LimitNOFILE=65535
Environment="DAEMON_HOME=$HOME/.ollo"
Environment="DAEMON_NAME=ollod"
Environment="UNSAFE_SKIP_BACKUP=true"
Environment="PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:$HOME/.ollo/cosmovisor/current/bin"

[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable ollod
```

### Initialize the node

```bash
# Set node configuration
ollod config chain-id ollo-testnet-1
ollod config keyring-backend test
ollod config node tcp://localhost:13257

# Initialize the node
ollod init $MONIKER --chain-id ollo-testnet-1

# Download genesis and addrbook
curl -Ls https://snapshots.kjnodes.com/ollo-testnet/genesis.json > $HOME/.ollo/config/genesis.json
curl -Ls https://snapshots.kjnodes.com/ollo-testnet/addrbook.json > $HOME/.ollo/config/addrbook.json

# Add seeds
sed -i -e "s|^seeds *=.*|seeds = \"3f472746f46493309650e5a033076689996c8881@ollo-testnet.rpc.kjnodes.com:13259\"|" $HOME/.ollo/config/config.toml

# Set minimum gas price
sed -i -e "s|^minimum-gas-prices *=.*|minimum-gas-prices = \"0utollo\"|" $HOME/.ollo/config/app.toml

# Set pruning
sed -i \
  -e 's|^pruning *=.*|pruning = "custom"|' \
  -e 's|^pruning-keep-recent *=.*|pruning-keep-recent = "100"|' \
  -e 's|^pruning-keep-every *=.*|pruning-keep-every = "0"|' \
  -e 's|^pruning-interval *=.*|pruning-interval = "19"|' \
  $HOME/.ollo/config/app.toml

# Set custom ports
sed -i -e "s%^proxy_app = \"tcp://127.0.0.1:26658\"%proxy_app = \"tcp://127.0.0.1:13258\"%; s%^laddr = \"tcp://127.0.0.1:26657\"%laddr = \"tcp://127.0.0.1:13257\"%; s%^pprof_laddr = \"localhost:6060\"%pprof_laddr = \"localhost:13260\"%; s%^laddr = \"tcp://0.0.0.0:26656\"%laddr = \"tcp://0.0.0.0:13256\"%; s%^prometheus_listen_addr = \":26660\"%prometheus_listen_addr = \":13266\"%" $HOME/.ollo/config/config.toml
sed -i -e "s%^address = \"tcp://0.0.0.0:1317\"%address = \"tcp://0.0.0.0:13217\"%; s%^address = \":8080\"%address = \":13280\"%; s%^address = \"0.0.0.0:9090\"%address = \"0.0.0.0:13290\"%; s%^address = \"0.0.0.0:9091\"%address = \"0.0.0.0:13291\"%; s%:8545%:13245%; s%:8546%:13246%; s%:6065%:13265%" $HOME/.ollo/config/app.toml
```

### Download latest chain snapshot

```bash
curl -L https://snapshots.kjnodes.com/ollo-testnet/snapshot_latest.tar.lz4 | tar -Ilz4 -xf - -C $HOME/.ollo
[[ -f $HOME/.ollo/data/upgrade-info.json ]] && cp $HOME/.ollo/data/upgrade-info.json $HOME/.ollo/cosmovisor/genesis/upgrade-info.json
```

### Start service and check the logs

```bash
sudo systemctl start ollod && sudo journalctl -u ollod -f --no-hostname -o cat
```
