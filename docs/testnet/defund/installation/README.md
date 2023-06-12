---
description: Setting up your validator node has never been so easy. Get your validator running in minutes by following step by step instructions.
---

# Installation

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/defund.png" alt=""><figcaption></figcaption></figure>

**Chain ID**: orbit-alpha-1 | **Latest Version Tag**: v0.2.6 | **Custom Port**: 140

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
rm -rf defund
git clone https://github.com/defund-labs/defund.git
cd defund
git checkout v0.2.6

# Build binaries
make build

# Prepare binaries for Cosmovisor
mkdir -p $HOME/.defund/cosmovisor/genesis/bin
mv build/defundd $HOME/.defund/cosmovisor/genesis/bin/
rm -rf build

# Create application symlinks
sudo ln -s $HOME/.defund/cosmovisor/genesis $HOME/.defund/cosmovisor/current -f
sudo ln -s $HOME/.defund/cosmovisor/current/bin/defundd /usr/local/bin/defundd -f
```

### Install Cosmovisor and create a service

```bash
# Download and install Cosmovisor
go install cosmossdk.io/tools/cosmovisor/cmd/cosmovisor@v1.4.0

# Create service
sudo tee /etc/systemd/system/defundd.service > /dev/null << EOF
[Unit]
Description=defund-testnet node service
After=network-online.target

[Service]
User=$USER
ExecStart=$(which cosmovisor) run start
Restart=on-failure
RestartSec=10
LimitNOFILE=65535
Environment="DAEMON_HOME=$HOME/.defund"
Environment="DAEMON_NAME=defundd"
Environment="UNSAFE_SKIP_BACKUP=true"
Environment="PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:$HOME/.defund/cosmovisor/current/bin"

[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable defundd
```

### Initialize the node

```bash
# Set node configuration
defundd config chain-id orbit-alpha-1
defundd config keyring-backend test
defundd config node tcp://localhost:14057

# Initialize the node
defundd init $MONIKER --chain-id orbit-alpha-1

# Download genesis and addrbook
curl -Ls https://snapshots.kjnodes.com/defund-testnet/genesis.json > $HOME/.defund/config/genesis.json
curl -Ls https://snapshots.kjnodes.com/defund-testnet/addrbook.json > $HOME/.defund/config/addrbook.json

# Add seeds
sed -i -e "s|^seeds *=.*|seeds = \"3f472746f46493309650e5a033076689996c8881@defund-testnet.rpc.kjnodes.com:14059\"|" $HOME/.defund/config/config.toml

# Set minimum gas price
sed -i -e "s|^minimum-gas-prices *=.*|minimum-gas-prices = \"0ufetf\"|" $HOME/.defund/config/app.toml

# Set pruning
sed -i \
  -e 's|^pruning *=.*|pruning = "custom"|' \
  -e 's|^pruning-keep-recent *=.*|pruning-keep-recent = "100"|' \
  -e 's|^pruning-keep-every *=.*|pruning-keep-every = "0"|' \
  -e 's|^pruning-interval *=.*|pruning-interval = "19"|' \
  $HOME/.defund/config/app.toml

# Set custom ports
sed -i -e "s%^proxy_app = \"tcp://127.0.0.1:26658\"%proxy_app = \"tcp://127.0.0.1:14058\"%; s%^laddr = \"tcp://127.0.0.1:26657\"%laddr = \"tcp://127.0.0.1:14057\"%; s%^pprof_laddr = \"localhost:6060\"%pprof_laddr = \"localhost:14060\"%; s%^laddr = \"tcp://0.0.0.0:26656\"%laddr = \"tcp://0.0.0.0:14056\"%; s%^prometheus_listen_addr = \":26660\"%prometheus_listen_addr = \":14066\"%" $HOME/.defund/config/config.toml
sed -i -e "s%^address = \"tcp://0.0.0.0:1317\"%address = \"tcp://0.0.0.0:14017\"%; s%^address = \":8080\"%address = \":14080\"%; s%^address = \"0.0.0.0:9090\"%address = \"0.0.0.0:14090\"%; s%^address = \"0.0.0.0:9091\"%address = \"0.0.0.0:14091\"%; s%:8545%:14045%; s%:8546%:14046%; s%:6065%:14065%" $HOME/.defund/config/app.toml
```

### Download latest chain snapshot

```bash
curl -L https://snapshots.kjnodes.com/defund-testnet/snapshot_latest.tar.lz4 | tar -Ilz4 -xf - -C $HOME/.defund
[[ -f $HOME/.defund/data/upgrade-info.json ]] && cp $HOME/.defund/data/upgrade-info.json $HOME/.defund/cosmovisor/genesis/upgrade-info.json
```

### Start service and check the logs

```bash
sudo systemctl start defundd && sudo journalctl -u defundd -f --no-hostname -o cat
```
