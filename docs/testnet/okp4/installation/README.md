---
description: Setting up your validator node has never been so easy. Get your validator running in minutes by following step by step instructions.
---

# Installation

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/okp4.png" width="150" alt=""><figcaption></figcaption></figure>

**Chain ID**: okp4-nemeton-1 | **Latest Version Tag**: v3.0.0 | **Custom Port**: 36

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
sudo apt update
sudo apt install curl git jq lz4 build-essential -y
```

#### Install GO

```bash
sudo rm -rf /usr/local/go
sudo curl -Ls https://go.dev/dl/go1.19.linux-amd64.tar.gz | sudo tar -C /usr/local -xz
tee -a $HOME/.profile > /dev/null << EOF
export PATH=$PATH:/usr/local/go/bin
EOF
source $HOME/.profile
```

### Download and build binaries

```bash
# Clone project repository
cd $HOME
rm -rf okp4d
git clone https://github.com/okp4/okp4d.git
cd okp4d

# Build binaries
git checkout v3.0.0
make build
mkdir -p $HOME/.okp4d/cosmovisor/genesis/bin
mv target/dist/okp4d $HOME/.okp4d/cosmovisor/genesis/bin/
rm -rf build
```

### Install Cosmovisor and create a service

```bash
# Download and install Cosmovisor
curl -Ls https://github.com/cosmos/cosmos-sdk/releases/download/cosmovisor%2Fv1.3.0/cosmovisor-v1.3.0-linux-amd64.tar.gz | tar xz
chmod 755 cosmovisor
sudo mv cosmovisor /usr/bin/cosmovisor

# Create service
sudo tee /etc/systemd/system/okp4d.service > /dev/null << EOF
[Unit]
Description=okp4-testnet node service
After=network-online.target
[Service]
User=$USER
ExecStart=/usr/bin/cosmovisor run start
Restart=on-failure
RestartSec=10
LimitNOFILE=65535
Environment="DAEMON_HOME=$HOME/.okp4d"
Environment="DAEMON_NAME=okp4d"
Environment="UNSAFE_SKIP_BACKUP=true"
[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable okp4d

# Create application symlinks
ln -s $HOME/.okp4d/cosmovisor/genesis $HOME/.okp4d/cosmovisor/current
sudo ln -s $HOME/.okp4d/cosmovisor/current/bin/okp4d /usr/local/bin/okp4d
```

### Initialize the node

```bash
# Set node configuration
okp4d config chain-id okp4-nemeton-1
okp4d config keyring-backend test
okp4d config node tcp://localhost:36657

# Initialize the node
okp4d init $MONIKER --chain-id okp4-nemeton-1

# Download genesis and addrbook
curl -Ls https://snapshots.kjnodes.com/okp4-testnet/genesis.json > $HOME/.okp4d/config/genesis.json
curl -Ls https://snapshots.kjnodes.com/okp4-testnet/addrbook.json > $HOME/.okp4d/config/addrbook.json

# Add seeds
sed -i -e "s|^seeds *=.*|seeds = \"3f472746f46493309650e5a033076689996c8881@okp4-testnet.rpc.kjnodes.com:36659\"|" $HOME/.okp4d/config/config.toml

# Set minimum gas price
sed -i -e "s|^minimum-gas-prices *=.*|minimum-gas-prices = \"0uknow\"|" $HOME/.okp4d/config/app.toml

# Set pruning
sed -i -e "s|^pruning *=.*|pruning = \"custom\"|" $HOME/.okp4d/config/app.toml
sed -i -e "s|^pruning-keep-recent *=.*|pruning-keep-recent = \"100\"|" $HOME/.okp4d/config/app.toml
sed -i -e "s|^pruning-keep-every *=.*|pruning-keep-every = \"0\"|" $HOME/.okp4d/config/app.toml
sed -i -e "s|^pruning-interval *=.*|pruning-interval = \"19\"|" $HOME/.okp4d/config/app.toml

# Set custom ports
sed -i.bak -e "s%^proxy_app = \"tcp://127.0.0.1:26658\"%proxy_app = \"tcp://127.0.0.1:36658\"%; s%^laddr = \"tcp://127.0.0.1:26657\"%laddr = \"tcp://127.0.0.1:36657\"%; s%^pprof_laddr = \"localhost:6060\"%pprof_laddr = \"localhost:36060\"%; s%^laddr = \"tcp://0.0.0.0:26656\"%laddr = \"tcp://0.0.0.0:36656\"%; s%^prometheus_listen_addr = \":26660\"%prometheus_listen_addr = \":36660\"%" $HOME/.okp4d/config/config.toml
sed -i.bak -e "s%^address = \"tcp://0.0.0.0:1317\"%address = \"tcp://0.0.0.0:36317\"%; s%^address = \":8080\"%address = \":36080\"%; s%^address = \"0.0.0.0:9090\"%address = \"0.0.0.0:36090\"%; s%^address = \"0.0.0.0:9091\"%address = \"0.0.0.0:36091\"%; s%^address = \"0.0.0.0:8545\"%address = \"0.0.0.0:36545\"%; s%^ws-address = \"0.0.0.0:8546\"%ws-address = \"0.0.0.0:36546\"%" $HOME/.okp4d/config/app.toml
```

### Download latest chain snapshot

```bash
curl -L https://snapshots.kjnodes.com/okp4-testnet/snapshot_latest.tar.lz4 | lz4 -dc - | tar -xf - -C $HOME/.okp4d
```

### Start service and check the logs

```bash
sudo systemctl start okp4d && journalctl -u okp4d -f --no-hostname -o cat
```
