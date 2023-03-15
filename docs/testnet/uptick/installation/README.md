---
description: Setting up your validator node has never been so easy. Get your validator running in minutes by following step by step instructions.
---

# Installation

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/uptick.png" width="150" alt=""><figcaption></figcaption></figure>

**Chain ID**: uptick_7000-2 | **Latest Version Tag**: v0.2.6 | **Custom Port**: 15

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
curl -Ls https://go.dev/dl/go1.19.7.linux-amd64.tar.gz | sudo tar -xzf - -C /usr/local
eval $(echo 'export PATH=$PATH:/usr/local/go/bin' | sudo tee /etc/profile.d/golang.sh)
eval $(echo 'export PATH=$PATH:$HOME/go/bin' | tee -a $HOME/.profile)
```

### Download and build binaries

```bash
# Clone project repository
cd $HOME
rm -rf uptick
git clone https://github.com/UptickNetwork/uptick.git
cd uptick
git checkout v0.2.6

# Build binaries
make build

# Prepare binaries for Cosmovisor
mkdir -p $HOME/.uptickd/cosmovisor/genesis/bin
mv build/uptickd $HOME/.uptickd/cosmovisor/genesis/bin/
rm -rf build

# Create application symlinks
ln -s $HOME/.uptickd/cosmovisor/genesis $HOME/.uptickd/cosmovisor/current
sudo ln -s $HOME/.uptickd/cosmovisor/current/bin/uptickd /usr/local/bin/uptickd
```

### Install Cosmovisor and create a service

```bash
# Download and install Cosmovisor
go install cosmossdk.io/tools/cosmovisor/cmd/cosmovisor@v1.4.0

# Create service
sudo tee /etc/systemd/system/uptickd.service > /dev/null << EOF
[Unit]
Description=uptick-testnet node service
After=network-online.target

[Service]
User=$USER
ExecStart=$(which cosmovisor) run start
Restart=on-failure
RestartSec=10
LimitNOFILE=65535
Environment="DAEMON_HOME=$HOME/.uptickd"
Environment="DAEMON_NAME=uptickd"
Environment="UNSAFE_SKIP_BACKUP=true"
Environment="PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:$HOME/.uptickd/cosmovisor/current/bin"

[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable uptickd
```

### Initialize the node

```bash
# Set node configuration
uptickd config chain-id uptick_7000-2
uptickd config keyring-backend test
uptickd config node tcp://localhost:15657

# Initialize the node
uptickd init $MONIKER --chain-id uptick_7000-2

# Download genesis and addrbook
curl -Ls https://snapshots.kjnodes.com/uptick-testnet/genesis.json > $HOME/.uptickd/config/genesis.json
curl -Ls https://snapshots.kjnodes.com/uptick-testnet/addrbook.json > $HOME/.uptickd/config/addrbook.json

# Add seeds
sed -i -e "s|^seeds *=.*|seeds = \"3f472746f46493309650e5a033076689996c8881@uptick-testnet.rpc.kjnodes.com:15659\"|" $HOME/.uptickd/config/config.toml

# Set minimum gas price
sed -i -e "s|^minimum-gas-prices *=.*|minimum-gas-prices = \"0auptick\"|" $HOME/.uptickd/config/app.toml

# Set pruning
sed -i \
  -e 's|^pruning *=.*|pruning = "custom"|' \
  -e 's|^pruning-keep-recent *=.*|pruning-keep-recent = "100"|' \
  -e 's|^pruning-keep-every *=.*|pruning-keep-every = "0"|' \
  -e 's|^pruning-interval *=.*|pruning-interval = "19"|' \
  $HOME/.uptickd/config/app.toml

# Set custom ports
sed -i -e "s%^proxy_app = \"tcp://127.0.0.1:26658\"%proxy_app = \"tcp://127.0.0.1:15658\"%; s%^laddr = \"tcp://127.0.0.1:26657\"%laddr = \"tcp://127.0.0.1:15657\"%; s%^pprof_laddr = \"localhost:6060\"%pprof_laddr = \"localhost:15060\"%; s%^laddr = \"tcp://0.0.0.0:26656\"%laddr = \"tcp://0.0.0.0:15656\"%; s%^prometheus_listen_addr = \":26660\"%prometheus_listen_addr = \":15660\"%" $HOME/.uptickd/config/config.toml
sed -i -e "s%^address = \"tcp://0.0.0.0:1317\"%address = \"tcp://0.0.0.0:15317\"%; s%^address = \":8080\"%address = \":15080\"%; s%^address = \"0.0.0.0:9090\"%address = \"0.0.0.0:15090\"%; s%^address = \"0.0.0.0:9091\"%address = \"0.0.0.0:15091\"%; s%^address = \"0.0.0.0:8545\"%address = \"0.0.0.0:15545\"%; s%^ws-address = \"0.0.0.0:8546\"%ws-address = \"0.0.0.0:15546\"%" $HOME/.uptickd/config/app.toml
```

### Download latest chain snapshot

```bash
curl -L https://snapshots.kjnodes.com/uptick-testnet/snapshot_latest.tar.lz4 | tar -Ilz4 -xf - -C $HOME/.uptickd
[[ -f $HOME/.uptickd/data/upgrade-info.json ]] && cp $HOME/.uptickd/data/upgrade-info.json $HOME/.uptickd/cosmovisor/genesis/upgrade-info.json
```

### Start service and check the logs

```bash
sudo systemctl start uptickd && sudo journalctl -u uptickd -f --no-hostname -o cat
```
