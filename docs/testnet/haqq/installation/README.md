---
description: Setting up your validator node has never been so easy. Get your validator running in minutes by following step by step instructions.
---

# Installation

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/haqq.png" alt=""><figcaption></figcaption></figure>

**Chain ID**: haqq_54211-3 | **Latest Version Tag**: v1.3.1 | **Custom Port**: 135

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
curl -Ls https://go.dev/dl/go1.19.9.linux-amd64.tar.gz | sudo tar -xzf - -C /usr/local
eval $(echo 'export PATH=$PATH:/usr/local/go/bin' | sudo tee /etc/profile.d/golang.sh)
eval $(echo 'export PATH=$PATH:$HOME/go/bin' | tee -a $HOME/.profile)
```

### Download and build binaries

```bash
# Clone project repository
cd $HOME
rm -rf haqq
git clone https://github.com/haqq-network/haqq.git
cd haqq
git checkout v1.3.1

# Build binaries
make build

# Prepare binaries for Cosmovisor
mkdir -p $HOME/.haqqd/cosmovisor/genesis/bin
mv build/haqqd $HOME/.haqqd/cosmovisor/genesis/bin/
rm -rf build

# Create application symlinks
sudo ln -s $HOME/.haqqd/cosmovisor/genesis $HOME/.haqqd/cosmovisor/current -f
sudo ln -s $HOME/.haqqd/cosmovisor/current/bin/haqqd /usr/local/bin/haqqd -f
```

### Install Cosmovisor and create a service

```bash
# Download and install Cosmovisor
go install cosmossdk.io/tools/cosmovisor/cmd/cosmovisor@v1.4.0

# Create service
sudo tee /etc/systemd/system/haqqd.service > /dev/null << EOF
[Unit]
Description=haqq-testnet node service
After=network-online.target

[Service]
User=$USER
ExecStart=$(which cosmovisor) run start
Restart=on-failure
RestartSec=10
LimitNOFILE=65535
Environment="DAEMON_HOME=$HOME/.haqqd"
Environment="DAEMON_NAME=haqqd"
Environment="UNSAFE_SKIP_BACKUP=true"
Environment="PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:$HOME/.haqqd/cosmovisor/current/bin"

[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable haqqd
```

### Initialize the node

```bash
# Set node configuration
haqqd config chain-id haqq_54211-3
haqqd config keyring-backend test
haqqd config node tcp://localhost:13557

# Initialize the node
haqqd init $MONIKER --chain-id haqq_54211-3

# Download genesis and addrbook
curl -Ls https://snapshots.kjnodes.com/haqq-testnet/genesis.json > $HOME/.haqqd/config/genesis.json
curl -Ls https://snapshots.kjnodes.com/haqq-testnet/addrbook.json > $HOME/.haqqd/config/addrbook.json

# Add seeds
sed -i -e "s|^seeds *=.*|seeds = \"3f472746f46493309650e5a033076689996c8881@haqq-testnet.rpc.kjnodes.com:13559\"|" $HOME/.haqqd/config/config.toml

# Set minimum gas price
sed -i -e "s|^minimum-gas-prices *=.*|minimum-gas-prices = \"0aISLM\"|" $HOME/.haqqd/config/app.toml

# Set pruning
sed -i \
  -e 's|^pruning *=.*|pruning = "custom"|' \
  -e 's|^pruning-keep-recent *=.*|pruning-keep-recent = "100"|' \
  -e 's|^pruning-keep-every *=.*|pruning-keep-every = "0"|' \
  -e 's|^pruning-interval *=.*|pruning-interval = "19"|' \
  $HOME/.haqqd/config/app.toml

# Set custom ports
sed -i -e "s%^proxy_app = \"tcp://127.0.0.1:26658\"%proxy_app = \"tcp://127.0.0.1:13558\"%; s%^laddr = \"tcp://127.0.0.1:26657\"%laddr = \"tcp://127.0.0.1:13557\"%; s%^pprof_laddr = \"localhost:6060\"%pprof_laddr = \"localhost:13560\"%; s%^laddr = \"tcp://0.0.0.0:26656\"%laddr = \"tcp://0.0.0.0:13556\"%; s%^prometheus_listen_addr = \":26660\"%prometheus_listen_addr = \":13566\"%" $HOME/.haqqd/config/config.toml
sed -i -e "s%^address = \"tcp://0.0.0.0:1317\"%address = \"tcp://0.0.0.0:13517\"%; s%^address = \":8080\"%address = \":13580\"%; s%^address = \"0.0.0.0:9090\"%address = \"0.0.0.0:13590\"%; s%^address = \"0.0.0.0:9091\"%address = \"0.0.0.0:13591\"%; s%:8545%:13545%; s%:8546%:13546%; s%:6065%:13565%" $HOME/.haqqd/config/app.toml
```

### Download latest chain snapshot

```bash
curl -L https://snapshots.kjnodes.com/haqq-testnet/snapshot_latest.tar.lz4 | tar -Ilz4 -xf - -C $HOME/.haqqd
[[ -f $HOME/.haqqd/data/upgrade-info.json ]] && cp $HOME/.haqqd/data/upgrade-info.json $HOME/.haqqd/cosmovisor/genesis/upgrade-info.json
```

### Start service and check the logs

```bash
sudo systemctl start haqqd && sudo journalctl -u haqqd -f --no-hostname -o cat
```
