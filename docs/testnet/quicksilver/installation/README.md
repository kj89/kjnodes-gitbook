---
description: Setting up your validator node has never been so easy. Get your validator running in minutes by following step by step instructions.
---

# Installation

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/quicksilver.png" alt=""><figcaption></figcaption></figure>

**Chain ID**: rhye-1 | **Latest Version Tag**: v1.4.2-rc7 | **Custom Port**: 111

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
rm -rf quicksilver
git clone https://github.com/ingenuity-build/quicksilver.git
cd quicksilver
git checkout v1.4.2-rc7

# Build binaries
make build

# Prepare binaries for Cosmovisor
mkdir -p $HOME/.quicksilverd/cosmovisor/genesis/bin
mv build/quicksilverd $HOME/.quicksilverd/cosmovisor/genesis/bin/
rm -rf build

# Create application symlinks
sudo ln -s $HOME/.quicksilverd/cosmovisor/genesis $HOME/.quicksilverd/cosmovisor/current -f
sudo ln -s $HOME/.quicksilverd/cosmovisor/current/bin/quicksilverd /usr/local/bin/quicksilverd -f
```

### Install Cosmovisor and create a service

```bash
# Download and install Cosmovisor
go install cosmossdk.io/tools/cosmovisor/cmd/cosmovisor@v1.4.0

# Create service
sudo tee /etc/systemd/system/quicksilverd.service > /dev/null << EOF
[Unit]
Description=quicksilver-testnet node service
After=network-online.target

[Service]
User=$USER
ExecStart=$(which cosmovisor) run start
Restart=on-failure
RestartSec=10
LimitNOFILE=65535
Environment="DAEMON_HOME=$HOME/.quicksilverd"
Environment="DAEMON_NAME=quicksilverd"
Environment="UNSAFE_SKIP_BACKUP=true"
Environment="PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:$HOME/.quicksilverd/cosmovisor/current/bin"

[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable quicksilverd
```

### Initialize the node

```bash
# Set node configuration
quicksilverd config chain-id rhye-1
quicksilverd config keyring-backend test
quicksilverd config node tcp://localhost:11157

# Initialize the node
quicksilverd init $MONIKER --chain-id rhye-1

# Download genesis and addrbook
curl -Ls https://snapshots.kjnodes.com/quicksilver-testnet/genesis.json > $HOME/.quicksilverd/config/genesis.json
curl -Ls https://snapshots.kjnodes.com/quicksilver-testnet/addrbook.json > $HOME/.quicksilverd/config/addrbook.json

# Add seeds
sed -i -e "s|^seeds *=.*|seeds = \"3f472746f46493309650e5a033076689996c8881@quicksilver-testnet.rpc.kjnodes.com:11159\"|" $HOME/.quicksilverd/config/config.toml

# Set minimum gas price
sed -i -e "s|^minimum-gas-prices *=.*|minimum-gas-prices = \"0.0001uqck\"|" $HOME/.quicksilverd/config/app.toml

# Set pruning
sed -i \
  -e 's|^pruning *=.*|pruning = "custom"|' \
  -e 's|^pruning-keep-recent *=.*|pruning-keep-recent = "100"|' \
  -e 's|^pruning-keep-every *=.*|pruning-keep-every = "0"|' \
  -e 's|^pruning-interval *=.*|pruning-interval = "19"|' \
  $HOME/.quicksilverd/config/app.toml

# Set custom ports
sed -i -e "s%^proxy_app = \"tcp://127.0.0.1:26658\"%proxy_app = \"tcp://127.0.0.1:11158\"%; s%^laddr = \"tcp://127.0.0.1:26657\"%laddr = \"tcp://127.0.0.1:11157\"%; s%^pprof_laddr = \"localhost:6060\"%pprof_laddr = \"localhost:11160\"%; s%^laddr = \"tcp://0.0.0.0:26656\"%laddr = \"tcp://0.0.0.0:11156\"%; s%^prometheus_listen_addr = \":26660\"%prometheus_listen_addr = \":11166\"%" $HOME/.quicksilverd/config/config.toml
sed -i -e "s%^address = \"tcp://0.0.0.0:1317\"%address = \"tcp://0.0.0.0:11117\"%; s%^address = \":8080\"%address = \":11180\"%; s%^address = \"0.0.0.0:9090\"%address = \"0.0.0.0:11190\"%; s%^address = \"0.0.0.0:9091\"%address = \"0.0.0.0:11191\"%; s%:8545%:11145%; s%:8546%:11146%; s%:6065%:11165%" $HOME/.quicksilverd/config/app.toml
```

### Download latest chain snapshot

```bash
curl -L https://snapshots.kjnodes.com/quicksilver-testnet/snapshot_latest.tar.lz4 | tar -Ilz4 -xf - -C $HOME/.quicksilverd
[[ -f $HOME/.quicksilverd/data/upgrade-info.json ]] && cp $HOME/.quicksilverd/data/upgrade-info.json $HOME/.quicksilverd/cosmovisor/genesis/upgrade-info.json
```

### Start service and check the logs

```bash
sudo systemctl start quicksilverd && sudo journalctl -u quicksilverd -f --no-hostname -o cat
```
