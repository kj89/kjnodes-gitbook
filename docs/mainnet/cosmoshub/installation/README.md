---
description: Setting up your validator node has never been so easy. Get your validator running in minutes by following step by step instructions.
---

# Installation

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/cosmoshub.png" width="150" alt=""><figcaption></figcaption></figure>

**Chain ID**: cosmoshub-4 | **Latest Version Tag**: v9.0.0 | **Custom Port**: 34

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
curl -Ls https://go.dev/dl/go1.18.10.linux-amd64.tar.gz | sudo tar -xzf - -C /usr/local
eval $(echo 'export PATH=$PATH:/usr/local/go/bin' | sudo tee /etc/profile.d/golang.sh)
eval $(echo 'export PATH=$PATH:$HOME/go/bin' | tee -a $HOME/.profile)
```

### Download and build binaries

```bash
# Clone project repository
cd $HOME
rm -rf gaia
git clone https://github.com/cosmos/gaia.git
cd gaia
git checkout v9.0.0

# Build binaries
make build

# Prepare binaries for Cosmovisor
mkdir -p $HOME/.gaia/cosmovisor/genesis/bin
mv build/gaiad $HOME/.gaia/cosmovisor/genesis/bin/
rm -rf build

# Create application symlinks
ln -s $HOME/.gaia/cosmovisor/genesis $HOME/.gaia/cosmovisor/current
sudo ln -s $HOME/.gaia/cosmovisor/current/bin/gaiad /usr/local/bin/gaiad
```

### Install Cosmovisor and create a service

```bash
# Download and install Cosmovisor
go install cosmossdk.io/tools/cosmovisor/cmd/cosmovisor@v1.4.0

# Create service
sudo tee /etc/systemd/system/gaiad.service > /dev/null << EOF
[Unit]
Description=cosmoshub node service
After=network-online.target

[Service]
User=$USER
ExecStart=$(which cosmovisor) run start
Restart=on-failure
RestartSec=10
LimitNOFILE=65535
Environment="DAEMON_HOME=$HOME/.gaia"
Environment="DAEMON_NAME=gaiad"
Environment="UNSAFE_SKIP_BACKUP=true"
Environment="PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:$HOME/.gaia/cosmovisor/current/bin"

[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable gaiad
```

### Initialize the node

```bash
# Set node configuration
gaiad config chain-id cosmoshub-4
gaiad config keyring-backend file
gaiad config node tcp://localhost:34657

# Initialize the node
gaiad init $MONIKER --chain-id cosmoshub-4

# Download genesis and addrbook
curl -Ls https://snapshots.kjnodes.com/cosmoshub/genesis.json > $HOME/.gaia/config/genesis.json
curl -Ls https://snapshots.kjnodes.com/cosmoshub/addrbook.json > $HOME/.gaia/config/addrbook.json

# Add seeds
sed -i -e "s|^seeds *=.*|seeds = \"400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@cosmoshub.rpc.kjnodes.com:34659\"|" $HOME/.gaia/config/config.toml

# Set minimum gas price
sed -i -e "s|^minimum-gas-prices *=.*|minimum-gas-prices = \"0uatom\"|" $HOME/.gaia/config/app.toml

# Set pruning
sed -i \
  -e 's|^pruning *=.*|pruning = "custom"|' \
  -e 's|^pruning-keep-recent *=.*|pruning-keep-recent = "100"|' \
  -e 's|^pruning-keep-every *=.*|pruning-keep-every = "0"|' \
  -e 's|^pruning-interval *=.*|pruning-interval = "19"|' \
  $HOME/.gaia/config/app.toml

# Set custom ports
sed -i -e "s%^proxy_app = \"tcp://127.0.0.1:26658\"%proxy_app = \"tcp://127.0.0.1:34658\"%; s%^laddr = \"tcp://127.0.0.1:26657\"%laddr = \"tcp://127.0.0.1:34657\"%; s%^pprof_laddr = \"localhost:6060\"%pprof_laddr = \"localhost:34060\"%; s%^laddr = \"tcp://0.0.0.0:26656\"%laddr = \"tcp://0.0.0.0:34656\"%; s%^prometheus_listen_addr = \":26660\"%prometheus_listen_addr = \":34660\"%" $HOME/.gaia/config/config.toml
sed -i -e "s%^address = \"tcp://0.0.0.0:1317\"%address = \"tcp://0.0.0.0:34317\"%; s%^address = \":8080\"%address = \":34080\"%; s%^address = \"0.0.0.0:9090\"%address = \"0.0.0.0:34090\"%; s%^address = \"0.0.0.0:9091\"%address = \"0.0.0.0:34091\"%; s%^address = \"0.0.0.0:8545\"%address = \"0.0.0.0:34545\"%; s%^ws-address = \"0.0.0.0:8546\"%ws-address = \"0.0.0.0:34546\"%" $HOME/.gaia/config/app.toml
```

### Download latest chain snapshot

```bash
curl -L https://snapshots.kjnodes.com/cosmoshub/snapshot_latest.tar.lz4 | tar -Ilz4 -xf - -C $HOME/.gaia
[[ -f $HOME/.gaia/data/upgrade-info.json ]] && cp $HOME/.gaia/data/upgrade-info.json $HOME/.gaia/cosmovisor/genesis/upgrade-info.json
```

### Start service and check the logs

```bash
sudo systemctl start gaiad && sudo journalctl -u gaiad -f --no-hostname -o cat
```
