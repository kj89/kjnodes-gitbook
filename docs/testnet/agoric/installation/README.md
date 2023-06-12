---
description: Setting up your validator node has never been so easy. Get your validator running in minutes by following step by step instructions.
---

# Installation

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/agoric.png" alt=""><figcaption></figcaption></figure>

**Chain ID**: agoric-emerynet-8 | **Latest Version Tag**: mainnet1B-rc3 | **Custom Port**: 127

### Setup validator name

{% hint style='info' %}
Replace **YOUR_MONIKER_GOES_HERE** with your validator name
{% endhint %}

```bash
MONIKER="YOUR_MONIKER_GOES_HERE"
```

### Install dependencies

#### Add package repository for Node.js

```bash
curl -Ls https://deb.nodesource.com/setup_16.x | sudo bash
```

#### Add package repository for Yarn

```bash
curl -Ls https://dl.yarnpkg.com/debian/pubkey.gpg | gpg --dearmor | sudo tee /usr/share/keyrings/yarnkey.gpg >/dev/null
echo "deb [signed-by=/usr/share/keyrings/yarnkey.gpg] https://dl.yarnpkg.com/debian stable main" | sudo tee /etc/apt/sources.list.d/yarn.list
```

#### Update system and install build tools

```bash
sudo apt -q update
sudo apt -qy install curl git jq lz4 build-essential nodejs=16.* yarn
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
rm -rf mainnet1B-rc3
git clone https://github.com/Agoric/agoric-sdk.git mainnet1B-rc3
cd mainnet1B-rc3
git checkout mainnet1B-rc3

# Install and build Agoric Javascript packages
yarn install && yarn build

# Install and build Agoric Cosmos SDK support
(cd packages/cosmic-swingset && make)

# Prepare binaries for Cosmovisor
mkdir -p $HOME/.agoric/cosmovisor/genesis/bin
ln -s $HOME/mainnet1B-rc3/bin/agd $HOME/.agoric/cosmovisor/upgrades/agorictest-upgrade-10/bin/agd

# Create application symlinks
sudo ln -s $HOME/.agoric/cosmovisor/genesis $HOME/.agoric/cosmovisor/current -f

# Link binaries
sudo rm /usr/local/bin/agd
sudo tee /usr/local/bin/agd > /dev/null << EOF
#!/bin/bash
exec \$HOME/.agoric/cosmovisor/current/bin/agd "\$@"
EOF
sudo chmod 777 /usr/local/bin/agd
```

### Install Cosmovisor and create a service

```bash
# Download and install Cosmovisor
go install cosmossdk.io/tools/cosmovisor/cmd/cosmovisor@v1.4.0

# Create service
sudo tee /etc/systemd/system/agd.service > /dev/null << EOF
[Unit]
Description=agoric-testnet node service
After=network-online.target

[Service]
User=$USER
ExecStart=$(which cosmovisor) run start
Restart=on-failure
RestartSec=10
LimitNOFILE=65535
Environment="DAEMON_HOME=$HOME/.agoric"
Environment="DAEMON_NAME=agd"
Environment="UNSAFE_SKIP_BACKUP=true"
Environment="PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:$HOME/.agoric/cosmovisor/current/bin"

[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable agd
```

### Initialize the node

```bash
# Set node configuration
agd config chain-id agoric-emerynet-8
agd config keyring-backend test
agd config node tcp://localhost:12757

# Initialize the node
agd init $MONIKER --chain-id agoric-emerynet-8

# Download genesis and addrbook
curl -Ls https://snapshots.kjnodes.com/agoric-testnet/genesis.json > $HOME/.agoric/config/genesis.json
curl -Ls https://snapshots.kjnodes.com/agoric-testnet/addrbook.json > $HOME/.agoric/config/addrbook.json

# Add seeds
sed -i -e "s|^seeds *=.*|seeds = \"3f472746f46493309650e5a033076689996c8881@agoric-testnet.rpc.kjnodes.com:12759\"|" $HOME/.agoric/config/config.toml

# Set minimum gas price
sed -i -e "s|^minimum-gas-prices *=.*|minimum-gas-prices = \"0.025ubld\"|" $HOME/.agoric/config/app.toml

# Set pruning
sed -i \
  -e 's|^pruning *=.*|pruning = "custom"|' \
  -e 's|^pruning-keep-recent *=.*|pruning-keep-recent = "100"|' \
  -e 's|^pruning-keep-every *=.*|pruning-keep-every = "0"|' \
  -e 's|^pruning-interval *=.*|pruning-interval = "19"|' \
  $HOME/.agoric/config/app.toml

# Set custom ports
sed -i -e "s%^proxy_app = \"tcp://127.0.0.1:26658\"%proxy_app = \"tcp://127.0.0.1:12758\"%; s%^laddr = \"tcp://127.0.0.1:26657\"%laddr = \"tcp://127.0.0.1:12757\"%; s%^pprof_laddr = \"localhost:6060\"%pprof_laddr = \"localhost:12760\"%; s%^laddr = \"tcp://0.0.0.0:26656\"%laddr = \"tcp://0.0.0.0:12756\"%; s%^prometheus_listen_addr = \":26660\"%prometheus_listen_addr = \":12766\"%" $HOME/.agoric/config/config.toml
sed -i -e "s%^address = \"tcp://0.0.0.0:1317\"%address = \"tcp://0.0.0.0:12717\"%; s%^address = \":8080\"%address = \":12780\"%; s%^address = \"0.0.0.0:9090\"%address = \"0.0.0.0:12790\"%; s%^address = \"0.0.0.0:9091\"%address = \"0.0.0.0:12791\"%; s%:8545%:12745%; s%:8546%:12746%; s%:6065%:12765%" $HOME/.agoric/config/app.toml
```

### Download latest chain snapshot

```bash
curl -L https://snapshots.kjnodes.com/agoric-testnet/snapshot_latest.tar.lz4 | tar -Ilz4 -xf - -C $HOME/.agoric
[[ -f $HOME/.agoric/data/upgrade-info.json ]] && cp $HOME/.agoric/data/upgrade-info.json $HOME/.agoric/cosmovisor/genesis/upgrade-info.json
```

### Start service and check the logs

```bash
sudo systemctl start agd && sudo journalctl -u agd -f --no-hostname -o cat
```
