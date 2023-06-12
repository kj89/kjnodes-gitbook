---
description: Setting up your validator node has never been so easy. Get your validator running in minutes by following step by step instructions.
---

# Installation

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/aura.png" alt=""><figcaption></figcaption></figure>

**Chain ID**: euphoria-2 | **Latest Version Tag**: euphoria_v0.5.1 | **Custom Port**: 117

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
rm -rf aura
git clone https://github.com/aura-nw/aura.git
cd aura
git checkout euphoria_v0.5.1

# Build binaries
make build

# Prepare binaries for Cosmovisor
mkdir -p $HOME/.aura/cosmovisor/genesis/bin
mv build/aurad $HOME/.aura/cosmovisor/genesis/bin/
rm -rf build

# Create application symlinks
sudo ln -s $HOME/.aura/cosmovisor/genesis $HOME/.aura/cosmovisor/current -f
sudo ln -s $HOME/.aura/cosmovisor/current/bin/aurad /usr/local/bin/aurad -f
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
ExecStart=$(which cosmovisor) run start
Restart=on-failure
RestartSec=10
LimitNOFILE=65535
Environment="DAEMON_HOME=$HOME/.aura"
Environment="DAEMON_NAME=aurad"
Environment="UNSAFE_SKIP_BACKUP=true"
Environment="PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:$HOME/.aura/cosmovisor/current/bin"

[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable aurad
```

### Initialize the node

```bash
# Set node configuration
aurad config chain-id euphoria-2
aurad config keyring-backend test
aurad config node tcp://localhost:11757

# Initialize the node
aurad init $MONIKER --chain-id euphoria-2

# Download genesis and addrbook
curl -Ls https://snapshots.kjnodes.com/aura-testnet/genesis.json > $HOME/.aura/config/genesis.json
curl -Ls https://snapshots.kjnodes.com/aura-testnet/addrbook.json > $HOME/.aura/config/addrbook.json

# Add seeds
sed -i -e "s|^seeds *=.*|seeds = \"3f472746f46493309650e5a033076689996c8881@aura-testnet.rpc.kjnodes.com:11759\"|" $HOME/.aura/config/config.toml

# Set minimum gas price
sed -i -e "s|^minimum-gas-prices *=.*|minimum-gas-prices = \"0ueaura\"|" $HOME/.aura/config/app.toml

# Set pruning
sed -i \
  -e 's|^pruning *=.*|pruning = "custom"|' \
  -e 's|^pruning-keep-recent *=.*|pruning-keep-recent = "100"|' \
  -e 's|^pruning-keep-every *=.*|pruning-keep-every = "0"|' \
  -e 's|^pruning-interval *=.*|pruning-interval = "19"|' \
  $HOME/.aura/config/app.toml

# Set custom ports
sed -i -e "s%^proxy_app = \"tcp://127.0.0.1:26658\"%proxy_app = \"tcp://127.0.0.1:11758\"%; s%^laddr = \"tcp://127.0.0.1:26657\"%laddr = \"tcp://127.0.0.1:11757\"%; s%^pprof_laddr = \"localhost:6060\"%pprof_laddr = \"localhost:11760\"%; s%^laddr = \"tcp://0.0.0.0:26656\"%laddr = \"tcp://0.0.0.0:11756\"%; s%^prometheus_listen_addr = \":26660\"%prometheus_listen_addr = \":11766\"%" $HOME/.aura/config/config.toml
sed -i -e "s%^address = \"tcp://0.0.0.0:1317\"%address = \"tcp://0.0.0.0:11717\"%; s%^address = \":8080\"%address = \":11780\"%; s%^address = \"0.0.0.0:9090\"%address = \"0.0.0.0:11790\"%; s%^address = \"0.0.0.0:9091\"%address = \"0.0.0.0:11791\"%; s%:8545%:11745%; s%:8546%:11746%; s%:6065%:11765%" $HOME/.aura/config/app.toml
```

### Download latest chain snapshot

```bash
curl -L https://snapshots.kjnodes.com/aura-testnet/snapshot_latest.tar.lz4 | tar -Ilz4 -xf - -C $HOME/.aura
[[ -f $HOME/.aura/data/upgrade-info.json ]] && cp $HOME/.aura/data/upgrade-info.json $HOME/.aura/cosmovisor/genesis/upgrade-info.json
```

### Start service and check the logs

```bash
sudo systemctl start aurad && sudo journalctl -u aurad -f --no-hostname -o cat
```
