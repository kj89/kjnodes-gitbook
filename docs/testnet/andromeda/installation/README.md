---
description: Setting up your validator node has never been so easy. Get your validator running in minutes by following step by step instructions.
---

# Installation

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/andromeda.png" alt=""><figcaption></figcaption></figure>

**Chain ID**: galileo-3 | **Latest Version Tag**: galileo-3-v1.1.0-beta1 | **Custom Port**: 147

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
rm -rf andromedad
git clone https://github.com/andromedaprotocol/andromedad.git
cd andromedad
git checkout galileo-3-v1.1.0-beta1

# Build binaries
make build

# Prepare binaries for Cosmovisor
mkdir -p $HOME/.andromedad/cosmovisor/genesis/bin
mv build/andromedad $HOME/.andromedad/cosmovisor/genesis/bin/
rm -rf build

# Create application symlinks
sudo ln -s $HOME/.andromedad/cosmovisor/genesis $HOME/.andromedad/cosmovisor/current -f
sudo ln -s $HOME/.andromedad/cosmovisor/current/bin/andromedad /usr/local/bin/andromedad -f
```

### Install Cosmovisor and create a service

```bash
# Download and install Cosmovisor
go install cosmossdk.io/tools/cosmovisor/cmd/cosmovisor@v1.4.0

# Create service
sudo tee /etc/systemd/system/andromedad.service > /dev/null << EOF
[Unit]
Description=andromeda-testnet node service
After=network-online.target

[Service]
User=$USER
ExecStart=$(which cosmovisor) run start
Restart=on-failure
RestartSec=10
LimitNOFILE=65535
Environment="DAEMON_HOME=$HOME/.andromedad"
Environment="DAEMON_NAME=andromedad"
Environment="UNSAFE_SKIP_BACKUP=true"
Environment="PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:$HOME/.andromedad/cosmovisor/current/bin"

[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable andromedad
```

### Initialize the node

```bash
# Set node configuration
andromedad config chain-id galileo-3
andromedad config keyring-backend test
andromedad config node tcp://localhost:14757

# Initialize the node
andromedad init $MONIKER --chain-id galileo-3

# Download genesis and addrbook
curl -Ls https://snapshots.kjnodes.com/andromeda-testnet/genesis.json > $HOME/.andromedad/config/genesis.json
curl -Ls https://snapshots.kjnodes.com/andromeda-testnet/addrbook.json > $HOME/.andromedad/config/addrbook.json

# Add seeds
sed -i -e "s|^seeds *=.*|seeds = \"3f472746f46493309650e5a033076689996c8881@andromeda-testnet.rpc.kjnodes.com:14759\"|" $HOME/.andromedad/config/config.toml

# Set minimum gas price
sed -i -e "s|^minimum-gas-prices *=.*|minimum-gas-prices = \"0.0001uandr\"|" $HOME/.andromedad/config/app.toml

# Set pruning
sed -i \
  -e 's|^pruning *=.*|pruning = "custom"|' \
  -e 's|^pruning-keep-recent *=.*|pruning-keep-recent = "100"|' \
  -e 's|^pruning-keep-every *=.*|pruning-keep-every = "0"|' \
  -e 's|^pruning-interval *=.*|pruning-interval = "19"|' \
  $HOME/.andromedad/config/app.toml

# Set custom ports
sed -i -e "s%^proxy_app = \"tcp://127.0.0.1:26658\"%proxy_app = \"tcp://127.0.0.1:14758\"%; s%^laddr = \"tcp://127.0.0.1:26657\"%laddr = \"tcp://127.0.0.1:14757\"%; s%^pprof_laddr = \"localhost:6060\"%pprof_laddr = \"localhost:14760\"%; s%^laddr = \"tcp://0.0.0.0:26656\"%laddr = \"tcp://0.0.0.0:14756\"%; s%^prometheus_listen_addr = \":26660\"%prometheus_listen_addr = \":14766\"%" $HOME/.andromedad/config/config.toml
sed -i -e "s%^address = \"tcp://0.0.0.0:1317\"%address = \"tcp://0.0.0.0:14717\"%; s%^address = \":8080\"%address = \":14780\"%; s%^address = \"0.0.0.0:9090\"%address = \"0.0.0.0:14790\"%; s%^address = \"0.0.0.0:9091\"%address = \"0.0.0.0:14791\"%; s%:8545%:14745%; s%:8546%:14746%; s%:6065%:14765%" $HOME/.andromedad/config/app.toml
```

### Download latest chain snapshot

```bash
curl -L https://snapshots.kjnodes.com/andromeda-testnet/snapshot_latest.tar.lz4 | tar -Ilz4 -xf - -C $HOME/.andromedad
[[ -f $HOME/.andromedad/data/upgrade-info.json ]] && cp $HOME/.andromedad/data/upgrade-info.json $HOME/.andromedad/cosmovisor/genesis/upgrade-info.json
```

### Start service and check the logs

```bash
sudo systemctl start andromedad && sudo journalctl -u andromedad -f --no-hostname -o cat
```
