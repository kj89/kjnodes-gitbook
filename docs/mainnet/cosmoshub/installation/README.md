---
description: Setting up your validator node has never been so easy. Get your validator running in minutes by following step by step instructions.
---

# Installation

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/cosmoshub.png" alt=""><figcaption></figcaption></figure>

**Chain ID**: cosmoshub-4 | **Latest Version Tag**: v10.0.0 | **Custom Port**: 134

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
rm -rf gaia
git clone https://github.com/cosmos/gaia.git
cd gaia
git checkout v10.0.0

# Build binaries
make build

# Prepare binaries for Cosmovisor
mkdir -p $HOME/.gaia/cosmovisor/genesis/bin
mv build/gaiad $HOME/.gaia/cosmovisor/genesis/bin/
rm -rf build

# Create application symlinks
sudo ln -s $HOME/.gaia/cosmovisor/genesis $HOME/.gaia/cosmovisor/current -f
sudo ln -s $HOME/.gaia/cosmovisor/current/bin/gaiad /usr/local/bin/gaiad -f
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
gaiad config node tcp://localhost:13457

# Initialize the node
gaiad init $MONIKER --chain-id cosmoshub-4

# Download genesis and addrbook
curl -Ls https://snapshots.kjnodes.com/cosmoshub/genesis.json > $HOME/.gaia/config/genesis.json
curl -Ls https://snapshots.kjnodes.com/cosmoshub/addrbook.json > $HOME/.gaia/config/addrbook.json

# Add seeds
sed -i -e "s|^seeds *=.*|seeds = \"400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@cosmoshub.rpc.kjnodes.com:13459\"|" $HOME/.gaia/config/config.toml

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
sed -i -e "s%^proxy_app = \"tcp://127.0.0.1:26658\"%proxy_app = \"tcp://127.0.0.1:13458\"%; s%^laddr = \"tcp://127.0.0.1:26657\"%laddr = \"tcp://127.0.0.1:13457\"%; s%^pprof_laddr = \"localhost:6060\"%pprof_laddr = \"localhost:13460\"%; s%^laddr = \"tcp://0.0.0.0:26656\"%laddr = \"tcp://0.0.0.0:13456\"%; s%^prometheus_listen_addr = \":26660\"%prometheus_listen_addr = \":13466\"%" $HOME/.gaia/config/config.toml
sed -i -e "s%^address = \"tcp://0.0.0.0:1317\"%address = \"tcp://0.0.0.0:13417\"%; s%^address = \":8080\"%address = \":13480\"%; s%^address = \"0.0.0.0:9090\"%address = \"0.0.0.0:13490\"%; s%^address = \"0.0.0.0:9091\"%address = \"0.0.0.0:13491\"%; s%:8545%:13445%; s%:8546%:13446%; s%:6065%:13465%" $HOME/.gaia/config/app.toml
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
