---
description: Setting up your validator node has never been so easy. Get your validator running in minutes by following step by step instructions.
---

# Installation

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/teritori.png" width="150" alt=""><figcaption></figcaption></figure>

**Chain ID**: teritori-testnet-v3 | **Latest Version Tag**: v1.3.0 | **Custom Port**: 19

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
rm -rf teritori-chain
git clone https://github.com/TERITORI/teritori-chain.git
cd teritori-chain

# Build binaries
git checkout v1.3.0
make build
mkdir -p $HOME/.teritorid/cosmovisor/genesis/bin
mv build/teritorid $HOME/.teritorid/cosmovisor/genesis/bin/
rm -rf build
```

### Install Cosmovisor and create a service

```bash
# Download and install Cosmovisor
go install github.com/cosmos/cosmos-sdk/cosmovisor/cmd/cosmovisor@1.4.0

# Create service
sudo tee /etc/systemd/system/teritorid.service > /dev/null << EOF
[Unit]
Description=teritori-testnet node service
After=network-online.target
[Service]
User=$USER
ExecStart=/usr/bin/cosmovisor run start
Restart=on-failure
RestartSec=10
LimitNOFILE=65535
Environment="DAEMON_HOME=$HOME/.teritorid"
Environment="DAEMON_NAME=teritorid"
Environment="UNSAFE_SKIP_BACKUP=true"
[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable teritorid

# Create application symlinks
ln -s $HOME/.teritorid/cosmovisor/genesis $HOME/.teritorid/cosmovisor/current
sudo ln -s $HOME/.teritorid/cosmovisor/current/bin/teritorid /usr/local/bin/teritorid
```

### Initialize the node

```bash
# Set node configuration
teritorid config chain-id teritori-testnet-v3
teritorid config keyring-backend test
teritorid config node tcp://localhost:19657

# Initialize the node
teritorid init $MONIKER --chain-id teritori-testnet-v3

# Download genesis and addrbook
curl -Ls https://snapshots.kjnodes.com/teritori-testnet/genesis.json > $HOME/.teritorid/config/genesis.json
curl -Ls https://snapshots.kjnodes.com/teritori-testnet/addrbook.json > $HOME/.teritorid/config/addrbook.json

# Add seeds
sed -i -e "s|^seeds *=.*|seeds = \"3f472746f46493309650e5a033076689996c8881@teritori-testnet.rpc.kjnodes.com:19659\"|" $HOME/.teritorid/config/config.toml

# Set minimum gas price
sed -i -e "s|^minimum-gas-prices *=.*|minimum-gas-prices = \"0utori\"|" $HOME/.teritorid/config/app.toml

# Set pruning
sed -i -e "s|^pruning *=.*|pruning = \"custom\"|" $HOME/.teritorid/config/app.toml
sed -i -e "s|^pruning-keep-recent *=.*|pruning-keep-recent = \"100\"|" $HOME/.teritorid/config/app.toml
sed -i -e "s|^pruning-keep-every *=.*|pruning-keep-every = \"0\"|" $HOME/.teritorid/config/app.toml
sed -i -e "s|^pruning-interval *=.*|pruning-interval = \"19\"|" $HOME/.teritorid/config/app.toml

# Set custom ports
sed -i.bak -e "s%^proxy_app = \"tcp://127.0.0.1:26658\"%proxy_app = \"tcp://127.0.0.1:19658\"%; s%^laddr = \"tcp://127.0.0.1:26657\"%laddr = \"tcp://127.0.0.1:19657\"%; s%^pprof_laddr = \"localhost:6060\"%pprof_laddr = \"localhost:19060\"%; s%^laddr = \"tcp://0.0.0.0:26656\"%laddr = \"tcp://0.0.0.0:19656\"%; s%^prometheus_listen_addr = \":26660\"%prometheus_listen_addr = \":19660\"%" $HOME/.teritorid/config/config.toml
sed -i.bak -e "s%^address = \"tcp://0.0.0.0:1317\"%address = \"tcp://0.0.0.0:19317\"%; s%^address = \":8080\"%address = \":19080\"%; s%^address = \"0.0.0.0:9090\"%address = \"0.0.0.0:19090\"%; s%^address = \"0.0.0.0:9091\"%address = \"0.0.0.0:19091\"%; s%^address = \"0.0.0.0:8545\"%address = \"0.0.0.0:19545\"%; s%^ws-address = \"0.0.0.0:8546\"%ws-address = \"0.0.0.0:19546\"%" $HOME/.teritorid/config/app.toml
```

### Download latest chain snapshot

```bash
curl -L https://snapshots.kjnodes.com/teritori-testnet/snapshot_latest.tar.lz4 | lz4 -dc - | tar -xf - -C $HOME/.teritorid
```

### Start service and check the logs

```bash
sudo systemctl start teritorid && journalctl -u teritorid -f --no-hostname -o cat
```
