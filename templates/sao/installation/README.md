---
description: Setting up your validator node has never been so easy. Get your validator running in minutes by following step by step instructions.
---

# Installation

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/sao.png" width="150" alt=""><figcaption></figcaption></figure>

**Chain ID**: sao-testnet0 | **Latest Version Tag**: v0.0.9 | **Custom Port**: 49

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
curl -Ls https://go.dev/dl/go1.19.6.linux-amd64.tar.gz | sudo tar -xzf - -C /usr/local
eval $(echo 'export PATH=$PATH:/usr/local/go/bin' | sudo tee /etc/profile.d/golang.sh)
eval $(echo 'export PATH=$PATH:$HOME/go/bin' | tee -a $HOME/.profile)
```

### Download and build binaries

```bash
# Clone project repository
cd $HOME
rm -rf sao-consensus
git clone https://github.com/SaoNetwork/sao-consensus.git
cd sao-consensus
git checkout testnet0

# Build binaries
make build

# Prepare binaries for Cosmovisor
mkdir -p $HOME/.sao/cosmovisor/genesis/bin
mv build/linux/saod $HOME/.sao/cosmovisor/genesis/bin/
rm -rf build

# Create application symlinks
ln -s $HOME/.sao/cosmovisor/genesis $HOME/.sao/cosmovisor/current
sudo ln -s $HOME/.sao/cosmovisor/current/bin/saod /usr/local/bin/saod
```

### Install Cosmovisor and create a service

```bash
# Download and install Cosmovisor
go install cosmossdk.io/tools/cosmovisor/cmd/cosmovisor@v1.4.0

# Create service
sudo tee /etc/systemd/system/saod.service > /dev/null << EOF
[Unit]
Description=sao-testnet node service
After=network-online.target

[Service]
User=$USER
ExecStart=$(which cosmovisor) run start
Restart=on-failure
RestartSec=10
LimitNOFILE=65535
Environment="DAEMON_HOME=$HOME/.sao"
Environment="DAEMON_NAME=saod"
Environment="UNSAFE_SKIP_BACKUP=true"
Environment="PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:$HOME/.sao/cosmovisor/current/bin"

[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable saod
```

### Initialize the node

```bash
# Set node configuration
saod config chain-id sao-testnet0
saod config keyring-backend test
saod config node tcp://localhost:49657

# Initialize the node
saod init $MONIKER --chain-id sao-testnet0

# Download genesis and addrbook
curl -Ls https://snapshots.kjnodes.com/sao-testnet/genesis.json > $HOME/.sao/config/genesis.json
curl -Ls https://snapshots.kjnodes.com/sao-testnet/addrbook.json > $HOME/.sao/config/addrbook.json

# Add seeds
sed -i -e "s|^seeds *=.*|seeds = \"3f472746f46493309650e5a033076689996c8881@sao-testnet.rpc.kjnodes.com:49659\"|" $HOME/.sao/config/config.toml

# Set minimum gas price
sed -i -e "s|^minimum-gas-prices *=.*|minimum-gas-prices = \"0.0001sao\"|" $HOME/.sao/config/app.toml

# Set pruning
sed -i \
  -e 's|^pruning *=.*|pruning = "custom"|' \
  -e 's|^pruning-keep-recent *=.*|pruning-keep-recent = "100"|' \
  -e 's|^pruning-keep-every *=.*|pruning-keep-every = "0"|' \
  -e 's|^pruning-interval *=.*|pruning-interval = "19"|' \
  $HOME/.sao/config/app.toml

# Set custom ports
sed -i -e "s%^proxy_app = \"tcp://127.0.0.1:26658\"%proxy_app = \"tcp://127.0.0.1:49658\"%; s%^laddr = \"tcp://127.0.0.1:26657\"%laddr = \"tcp://127.0.0.1:49657\"%; s%^pprof_laddr = \"localhost:6060\"%pprof_laddr = \"localhost:49060\"%; s%^laddr = \"tcp://0.0.0.0:26656\"%laddr = \"tcp://0.0.0.0:49656\"%; s%^prometheus_listen_addr = \":26660\"%prometheus_listen_addr = \":49660\"%" $HOME/.sao/config/config.toml
sed -i -e "s%^address = \"tcp://0.0.0.0:1317\"%address = \"tcp://0.0.0.0:49317\"%; s%^address = \":8080\"%address = \":49080\"%; s%^address = \"0.0.0.0:9090\"%address = \"0.0.0.0:49090\"%; s%^address = \"0.0.0.0:9091\"%address = \"0.0.0.0:49091\"%; s%^address = \"0.0.0.0:8545\"%address = \"0.0.0.0:49545\"%; s%^ws-address = \"0.0.0.0:8546\"%ws-address = \"0.0.0.0:49546\"%" $HOME/.sao/config/app.toml
```

### Download latest chain snapshot

```bash
curl -L https://snapshots.kjnodes.com/sao-testnet/snapshot_latest.tar.lz4 | tar -Ilz4 -xf - -C $HOME/.sao
[[ -f $HOME/.sao/data/upgrade-info.json ]] && cp $HOME/.sao/data/upgrade-info.json $HOME/.sao/cosmovisor/genesis/upgrade-info.json
```

### Start service and check the logs

```bash
sudo systemctl start saod && sudo journalctl -u saod -f --no-hostname -o cat
```
