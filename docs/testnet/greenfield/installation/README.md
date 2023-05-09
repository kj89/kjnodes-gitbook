---
description: Setting up your validator node has never been so easy. Get your validator running in minutes by following step by step instructions.
---

# Installation

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/greenfield.png" alt=""><figcaption></figcaption></figure>

**Chain ID**: greenfield_5600-1 | **Latest Version Tag**: v0.1.1 | **Custom Port**: 154

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
rm -rf greenfield
git clone https://github.com/bnb-chain/greenfield.git
cd greenfield
git checkout v0.1.1

# Build binaries
make build

# Prepare binaries for Cosmovisor
mkdir -p $HOME/.gnfd/cosmovisor/genesis/bin
mv build/bin/gnfd $HOME/.gnfd/cosmovisor/genesis/bin/
rm -rf build

# Create application symlinks
sudo ln -s $HOME/.gnfd/cosmovisor/genesis $HOME/.gnfd/cosmovisor/current -f
sudo ln -s $HOME/.gnfd/cosmovisor/current/bin/gnfd /usr/local/bin/gnfd -f
```

### Install Cosmovisor and create a service

```bash
# Download and install Cosmovisor
go install cosmossdk.io/tools/cosmovisor/cmd/cosmovisor@v1.4.0

# Create service
sudo tee /etc/systemd/system/gnfd.service > /dev/null << EOF
[Unit]
Description=greenfield-testnet node service
After=network-online.target

[Service]
User=$USER
ExecStart=$(which cosmovisor) run start
Restart=on-failure
RestartSec=10
LimitNOFILE=65535
Environment="DAEMON_HOME=$HOME/.gnfd"
Environment="DAEMON_NAME=gnfd"
Environment="UNSAFE_SKIP_BACKUP=true"
Environment="PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:$HOME/.gnfd/cosmovisor/current/bin"

[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable gnfd
```

### Initialize the node

```bash
# Set node configuration
gnfd config chain-id greenfield_5600-1
gnfd config keyring-backend test
gnfd config node tcp://localhost:15457

# Initialize the node
gnfd init $MONIKER --chain-id greenfield_5600-1

# Download genesis and addrbook
curl -Ls https://snapshots.kjnodes.com/greenfield-testnet/genesis.json > $HOME/.gnfd/config/genesis.json
curl -Ls https://snapshots.kjnodes.com/greenfield-testnet/addrbook.json > $HOME/.gnfd/config/addrbook.json

# Add seeds
sed -i -e "s|^seeds *=.*|seeds = \"3f472746f46493309650e5a033076689996c8881@greenfield-testnet.rpc.kjnodes.com:15459\"|" $HOME/.gnfd/config/config.toml

# Set minimum gas price
sed -i -e "s|^minimum-gas-prices *=.*|minimum-gas-prices = \"5000000000BNB\"|" $HOME/.gnfd/config/app.toml

# Set pruning
sed -i \
  -e 's|^pruning *=.*|pruning = "custom"|' \
  -e 's|^pruning-keep-recent *=.*|pruning-keep-recent = "100"|' \
  -e 's|^pruning-keep-every *=.*|pruning-keep-every = "0"|' \
  -e 's|^pruning-interval *=.*|pruning-interval = "19"|' \
  -e 's|^src-chain-id *=.*|src-chain-id = "5600"|' \
  -e 's|^dest-chain-id *=.*|dest-chain-id = "5601"|' \
  -e 's|^denom-to-suggest *=.*|denom-to-suggest = "BNB"|' \
  $HOME/.gnfd/config/app.toml

# Set custom ports
sed -i -e "s%^proxy_app = \"tcp://127.0.0.1:26658\"%proxy_app = \"tcp://127.0.0.1:15458\"%; s%^laddr = \"tcp://127.0.0.1:26657\"%laddr = \"tcp://127.0.0.1:15457\"%; s%^pprof_laddr = \"localhost:6060\"%pprof_laddr = \"localhost:15460\"%; s%^laddr = \"tcp://0.0.0.0:26656\"%laddr = \"tcp://0.0.0.0:15456\"%; s%^prometheus_listen_addr = \":26660\"%prometheus_listen_addr = \":15466\"%" $HOME/.gnfd/config/config.toml
sed -i -e "s%^address = \"tcp://0.0.0.0:1317\"%address = \"tcp://0.0.0.0:15417\"%; s%^address = \":8080\"%address = \":15480\"%; s%^address = \"0.0.0.0:9090\"%address = \"0.0.0.0:15490\"%; s%^address = \"0.0.0.0:9091\"%address = \"0.0.0.0:15491\"%; s%:8545%:15445%; s%:8546%:15446%; s%:6065%:15465%" $HOME/.gnfd/config/app.toml
```

### Download latest chain snapshot

```bash
curl -L https://snapshots.kjnodes.com/greenfield-testnet/snapshot_latest.tar.lz4 | tar -Ilz4 -xf - -C $HOME/.gnfd
[[ -f $HOME/.gnfd/data/upgrade-info.json ]] && cp $HOME/.gnfd/data/upgrade-info.json $HOME/.gnfd/cosmovisor/genesis/upgrade-info.json
```

### Start service and check the logs

```bash
sudo systemctl start gnfd && sudo journalctl -u gnfd -f --no-hostname -o cat
```
