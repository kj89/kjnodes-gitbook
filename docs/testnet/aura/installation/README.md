---
description: Setting up your validator node has never been so easy. Get your validator running in minutes by following step by step instructions.
---

# Installation

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/aura.png" width="150" alt=""><figcaption></figcaption></figure>

**Chain ID**: euphoria-2 | **Latest Version Tag**: euphoria_v0.4.2 | **Custom Port**: 17

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
sudo curl -Ls https://golang.org/dl/go1.19.4.linux-amd64.tar.gz | sudo tar -C /usr/local -xz
tee -a $HOME/.profile > /dev/null << EOF
export PATH=$PATH:/usr/local/go/bin:$HOME/go/bin
EOF
source $HOME/.profile
```

### Download and build binaries

```bash
# Clone project repository
cd $HOME
rm -rf aura
git clone https://github.com/aura-nw/aura.git
cd aura

# Build binaries
git checkout euphoria_v0.4.2
make build
mkdir -p $HOME/.aura/cosmovisor/genesis/bin
mv build/aurad $HOME/.aura/cosmovisor/genesis/bin/
rm -rf build
```

### Install Cosmovisor and create a service

```bash
# Download and install Cosmovisor
go install cosmossdk.io/tools/cosmovisor/cmd/cosmovisor@v1.4.0

# Create service
sudo tee /etc/systemd/system/aurad.service > /dev/null << EOF
[Unit]
Description=aura-testnet node service
After=network-online.target
[Service]
User=$USER
ExecStart=/usr/bin/cosmovisor run start
Restart=on-failure
RestartSec=10
LimitNOFILE=65535
Environment="DAEMON_HOME=$HOME/.aura"
Environment="DAEMON_NAME=aurad"
Environment="UNSAFE_SKIP_BACKUP=true"
[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable aurad

# Create application symlinks
ln -s $HOME/.aura/cosmovisor/genesis $HOME/.aura/cosmovisor/current
sudo ln -s $HOME/.aura/cosmovisor/current/bin/aurad /usr/local/bin/aurad
```

### Initialize the node

```bash
# Set node configuration
aurad config chain-id euphoria-2
aurad config keyring-backend test
aurad config node tcp://localhost:17657

# Initialize the node
aurad init $MONIKER --chain-id euphoria-2

# Download genesis and addrbook
curl -Ls https://snapshots.kjnodes.com/aura-testnet/genesis.json > $HOME/.aura/config/genesis.json
curl -Ls https://snapshots.kjnodes.com/aura-testnet/addrbook.json > $HOME/.aura/config/addrbook.json

# Add seeds
sed -i -e "s|^seeds *=.*|seeds = \"3f472746f46493309650e5a033076689996c8881@aura-testnet.rpc.kjnodes.com:17659\"|" $HOME/.aura/config/config.toml

# Set minimum gas price
sed -i -e "s|^minimum-gas-prices *=.*|minimum-gas-prices = \"0ueaura\"|" $HOME/.aura/config/app.toml

# Set pruning
sed -i -e "s|^pruning *=.*|pruning = \"custom\"|" $HOME/.aura/config/app.toml
sed -i -e "s|^pruning-keep-recent *=.*|pruning-keep-recent = \"100\"|" $HOME/.aura/config/app.toml
sed -i -e "s|^pruning-keep-every *=.*|pruning-keep-every = \"0\"|" $HOME/.aura/config/app.toml
sed -i -e "s|^pruning-interval *=.*|pruning-interval = \"19\"|" $HOME/.aura/config/app.toml

# Set custom ports
sed -i.bak -e "s%^proxy_app = \"tcp://127.0.0.1:26658\"%proxy_app = \"tcp://127.0.0.1:17658\"%; s%^laddr = \"tcp://127.0.0.1:26657\"%laddr = \"tcp://127.0.0.1:17657\"%; s%^pprof_laddr = \"localhost:6060\"%pprof_laddr = \"localhost:17060\"%; s%^laddr = \"tcp://0.0.0.0:26656\"%laddr = \"tcp://0.0.0.0:17656\"%; s%^prometheus_listen_addr = \":26660\"%prometheus_listen_addr = \":17660\"%" $HOME/.aura/config/config.toml
sed -i.bak -e "s%^address = \"tcp://0.0.0.0:1317\"%address = \"tcp://0.0.0.0:17317\"%; s%^address = \":8080\"%address = \":17080\"%; s%^address = \"0.0.0.0:9090\"%address = \"0.0.0.0:17090\"%; s%^address = \"0.0.0.0:9091\"%address = \"0.0.0.0:17091\"%; s%^address = \"0.0.0.0:8545\"%address = \"0.0.0.0:17545\"%; s%^ws-address = \"0.0.0.0:8546\"%ws-address = \"0.0.0.0:17546\"%" $HOME/.aura/config/app.toml
```

### Download latest chain snapshot

```bash
curl -L https://snapshots.kjnodes.com/aura-testnet/snapshot_latest.tar.lz4 | lz4 -dc - | tar -xf - -C $HOME/.aura
```

### Start service and check the logs

```bash
sudo systemctl start aurad && journalctl -u aurad -f --no-hostname -o cat
```
