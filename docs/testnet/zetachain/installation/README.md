---
description: Setting up your validator node has never been so easy. Get your validator running in minutes by following step by step instructions.
---

# Installation

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/zetachain.png" alt=""><figcaption></figcaption></figure>

**Chain ID**: athens_7001-13 | **Latest Version Tag**: latest | **Custom Port**: 160

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
# Download project binaries
mkdir -p $HOME/.zetacored/cosmovisor/genesis/bin
wget -O $HOME/.zetacored/cosmovisor/genesis/bin/zetacored https://zetachain-external-files.s3.amazonaws.com/binaries/athens3/latest/zetacored-ubuntu-22-amd64
chmod +x $HOME/.zetacored/cosmovisor/genesis/bin/zetacored

# Create application symlinks
sudo ln -s $HOME/.zetacored/cosmovisor/genesis $HOME/.zetacored/cosmovisor/current -f
sudo ln -s $HOME/.zetacored/cosmovisor/current/bin/zetacored /usr/local/bin/zetacored -f
```

### Install Cosmovisor and create a service

```bash
# Download and install Cosmovisor
go install cosmossdk.io/tools/cosmovisor/cmd/cosmovisor@v1.4.0

# Create service
sudo tee /etc/systemd/system/zetacored.service > /dev/null << EOF
[Unit]
Description=zetachain-testnet node service
After=network-online.target

[Service]
User=$USER
ExecStart=$(which cosmovisor) run start
Restart=on-failure
RestartSec=10
LimitNOFILE=65535
Environment="DAEMON_HOME=$HOME/.zetacored"
Environment="DAEMON_NAME=zetacored"
Environment="UNSAFE_SKIP_BACKUP=true"
Environment="PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:$HOME/.zetacored/cosmovisor/current/bin"

[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable zetacored
```

### Initialize the node

```bash
# Set node configuration
zetacored config chain-id athens_7001-13
zetacored config keyring-backend test
zetacored config node tcp://localhost:16057

# Initialize the node
zetacored init $MONIKER --chain-id athens_7001-13

# Download genesis and addrbook
curl -Ls https://snapshots.kjnodes.com/zetachain-testnet/genesis.json > $HOME/.zetacored/config/genesis.json
curl -Ls https://snapshots.kjnodes.com/zetachain-testnet/addrbook.json > $HOME/.zetacored/config/addrbook.json

# Add seeds
sed -i -e "s|^seeds *=.*|seeds = \"3f472746f46493309650e5a033076689996c8881@zetachain-testnet.rpc.kjnodes.com:16059\"|" $HOME/.zetacored/config/config.toml

# Set minimum gas price
sed -i -e "s|^minimum-gas-prices *=.*|minimum-gas-prices = \"0azeta\"|" $HOME/.zetacored/config/app.toml

# Set pruning
sed -i \
  -e 's|^pruning *=.*|pruning = "custom"|' \
  -e 's|^pruning-keep-recent *=.*|pruning-keep-recent = "100"|' \
  -e 's|^pruning-keep-every *=.*|pruning-keep-every = "0"|' \
  -e 's|^pruning-interval *=.*|pruning-interval = "19"|' \
  $HOME/.zetacored/config/app.toml

# Set custom ports
sed -i -e "s%^proxy_app = \"tcp://127.0.0.1:26658\"%proxy_app = \"tcp://127.0.0.1:16058\"%; s%^laddr = \"tcp://127.0.0.1:26657\"%laddr = \"tcp://127.0.0.1:16057\"%; s%^pprof_laddr = \"localhost:6060\"%pprof_laddr = \"localhost:16060\"%; s%^laddr = \"tcp://0.0.0.0:26656\"%laddr = \"tcp://0.0.0.0:16056\"%; s%^prometheus_listen_addr = \":26660\"%prometheus_listen_addr = \":16066\"%" $HOME/.zetacored/config/config.toml
sed -i -e "s%^address = \"tcp://0.0.0.0:1317\"%address = \"tcp://0.0.0.0:16017\"%; s%^address = \":8080\"%address = \":16080\"%; s%^address = \"0.0.0.0:9090\"%address = \"0.0.0.0:16090\"%; s%^address = \"0.0.0.0:9091\"%address = \"0.0.0.0:16091\"%; s%:8545%:16045%; s%:8546%:16046%; s%:6065%:16065%" $HOME/.zetacored/config/app.toml
```

### Download latest chain snapshot

```bash
curl -L https://snapshots.kjnodes.com/zetachain-testnet/snapshot_latest.tar.lz4 | tar -Ilz4 -xf - -C $HOME/.zetacored
[[ -f $HOME/.zetacored/data/upgrade-info.json ]] && cp $HOME/.zetacored/data/upgrade-info.json $HOME/.zetacored/cosmovisor/genesis/upgrade-info.json
```

### Start service and check the logs

```bash
sudo systemctl start zetacored && sudo journalctl -u zetacored -f --no-hostname -o cat
```
