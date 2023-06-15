---
description: Setting up your validator node has never been so easy. Get your validator running in minutes by following step by step instructions.
---

# Installation

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/umee.png" alt=""><figcaption></figcaption></figure>

**Chain ID**: umee-1 | **Latest Version Tag**: v5.0.1 | **Custom Port**: 162

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
rm -rf umee
git clone https://github.com/umee-network/umee.git
cd umee
git checkout v5.0.1

# Build binaries
make build

# Prepare binaries for Cosmovisor
mkdir -p $HOME/.umee/cosmovisor/genesis/bin
mv build/umeed $HOME/.umee/cosmovisor/genesis/bin/
rm -rf build

# Create application symlinks
sudo ln -s $HOME/.umee/cosmovisor/genesis $HOME/.umee/cosmovisor/current -f
sudo ln -s $HOME/.umee/cosmovisor/current/bin/umeed /usr/local/bin/umeed -f
```

### Install Cosmovisor and create a service

```bash
# Download and install Cosmovisor
go install cosmossdk.io/tools/cosmovisor/cmd/cosmovisor@v1.4.0

# Create service
sudo tee /etc/systemd/system/umeed.service > /dev/null << EOF
[Unit]
Description=umee node service
After=network-online.target

[Service]
User=$USER
ExecStart=$(which cosmovisor) run start
Restart=on-failure
RestartSec=10
LimitNOFILE=65535
Environment="DAEMON_HOME=$HOME/.umee"
Environment="DAEMON_NAME=umeed"
Environment="UNSAFE_SKIP_BACKUP=true"
Environment="PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:$HOME/.umee/cosmovisor/current/bin"

[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable umeed
```

### Initialize the node

```bash
# Set node configuration
umeed config chain-id umee-1
umeed config keyring-backend file
umeed config node tcp://localhost:16257

# Initialize the node
umeed init $MONIKER --chain-id umee-1

# Download genesis and addrbook
curl -Ls https://snapshots.kjnodes.com/umee/genesis.json > $HOME/.umee/config/genesis.json
curl -Ls https://snapshots.kjnodes.com/umee/addrbook.json > $HOME/.umee/config/addrbook.json

# Add seeds
sed -i -e "s|^seeds *=.*|seeds = \"400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@umee.rpc.kjnodes.com:16259\"|" $HOME/.umee/config/config.toml

# Set minimum gas price
sed -i -e "s|^minimum-gas-prices *=.*|minimum-gas-prices = \"0.1uumee\"|" $HOME/.umee/config/app.toml

# Set pruning
sed -i \
  -e 's|^pruning *=.*|pruning = "custom"|' \
  -e 's|^pruning-keep-recent *=.*|pruning-keep-recent = "100"|' \
  -e 's|^pruning-keep-every *=.*|pruning-keep-every = "0"|' \
  -e 's|^pruning-interval *=.*|pruning-interval = "19"|' \
  $HOME/.umee/config/app.toml

# Set custom ports
sed -i -e "s%^proxy_app = \"tcp://127.0.0.1:26658\"%proxy_app = \"tcp://127.0.0.1:16258\"%; s%^laddr = \"tcp://127.0.0.1:26657\"%laddr = \"tcp://127.0.0.1:16257\"%; s%^pprof_laddr = \"localhost:6060\"%pprof_laddr = \"localhost:16260\"%; s%^laddr = \"tcp://0.0.0.0:26656\"%laddr = \"tcp://0.0.0.0:16256\"%; s%^prometheus_listen_addr = \":26660\"%prometheus_listen_addr = \":16266\"%" $HOME/.umee/config/config.toml
sed -i -e "s%^address = \"tcp://0.0.0.0:1317\"%address = \"tcp://0.0.0.0:16217\"%; s%^address = \":8080\"%address = \":16280\"%; s%^address = \"0.0.0.0:9090\"%address = \"0.0.0.0:16290\"%; s%^address = \"0.0.0.0:9091\"%address = \"0.0.0.0:16291\"%; s%:8545%:16245%; s%:8546%:16246%; s%:6065%:16265%" $HOME/.umee/config/app.toml
```

### Download latest chain snapshot

```bash
curl -L https://snapshots.kjnodes.com/umee/snapshot_latest.tar.lz4 | tar -Ilz4 -xf - -C $HOME/.umee
[[ -f $HOME/.umee/data/upgrade-info.json ]] && cp $HOME/.umee/data/upgrade-info.json $HOME/.umee/cosmovisor/genesis/upgrade-info.json
```

### Start service and check the logs

```bash
sudo systemctl start umeed && sudo journalctl -u umeed -f --no-hostname -o cat
```
