---
description: Setting up your validator node was never been so easy. Get your validator running in minutes by following step by step instructions.
---

# Installation

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/jackal.png" width="150" alt=""><figcaption></figcaption></figure>

**Chain ID**: jackal-1 | **Latest Version Tag**: v1.1.2-hotfix | **Custom Port**: 37

### Setup validator name

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
sudo curl -Ls https://go.dev/dl/go1.19.linux-amd64.tar.gz | sudo tar -C /usr/local -xz
tee -a $HOME/.profile > /dev/null << EOF
export PATH=$PATH:/usr/local/go/bin
EOF
source $HOME/.profile
```

### Download and build binaries

```bash
cd $HOME
rm -rf canine-chain
git clone https://github.com/JackalLabs/canine-chain.git
cd canine-chain

# Compile genesis version v1.1.1
git checkout v1.1.1
make build
mkdir -p $HOME/.canine/cosmovisor/genesis/bin
mv build/canined $HOME/.canine/cosmovisor/genesis/bin/
rm -rf build

# Compile latest version v1.1.2-hotfix
git checkout v1.1.2-hotfix
make build
mkdir -p $HOME/.canine/cosmovisor/upgrades/v1.1.2-hotfix/bin
mv build/canined $HOME/.canine/cosmovisor/upgrades/v1.1.2-hotfix/bin/
rm build/canined -rf
```

### Install Cosmovisor and create a service

```bash
curl -Ls https://github.com/cosmos/cosmos-sdk/releases/download/cosmovisor%2Fv1.3.0/cosmovisor-v1.3.0-linux-amd64.tar.gz | tar xz
chmod 755 cosmovisor
sudo mv cosmovisor /usr/bin/cosmovisor

sudo tee /etc/systemd/system/canined.service > /dev/null << EOF
[Unit]
Description=jackal node service
After=network-online.target
[Service]
User=$USER
ExecStart=/usr/bin/cosmovisor run start
Restart=on-failure
RestartSec=10
LimitNOFILE=65535
Environment="DAEMON_HOME=$HOME/.canine"
Environment="DAEMON_NAME=canined"
Environment="UNSAFE_SKIP_BACKUP=true"
[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable canined
```

### Initialize the node

```bash
ln -s $HOME/.canine/cosmovisor/upgrades/v1.1.2-hotfix $HOME/.canine/cosmovisor/current
sudo ln -s $HOME/.canine/cosmovisor/current/bin/canined /usr/local/bin/canined
canined config chain-id jackal-1
canined config keyring-backend file
canined config node tcp://localhost:37657
canined init $MONIKER --chain-id jackal-1
curl -Ls https://snapshots.kjnodes.com/jackal/genesis.json > $HOME/.canine/config/genesis.json
curl -Ls https://snapshots.kjnodes.com/jackal/addrbook.json > $HOME/.canine/config/addrbook.json
sed -i -e "s|^seeds *=.*|seeds = \"400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@jackal.rpc.kjnodes.com:37659\"|" $HOME/.canine/config/config.toml
tee $HOME/.canine/data/priv_validator_state.json > /dev/null << EOF
{
  "height": "0",
  "round": 0,
  "step": 0
}
EOF
sed -i -e "s|^minimum-gas-prices *=.*|minimum-gas-prices = \"0.002ujkl\"|" $HOME/.canine/config/app.toml
sed -i -e "s|^pruning *=.*|pruning = \"custom\"|" $HOME/.canine/config/app.toml
sed -i -e "s|^pruning-keep-recent *=.*|pruning-keep-recent = \"100\"|" $HOME/.canine/config/app.toml
sed -i -e "s|^pruning-keep-every *=.*|pruning-keep-every = \"0\"|" $HOME/.canine/config/app.toml
sed -i -e "s|^pruning-interval *=.*|pruning-interval = \"19\"|" $HOME/.canine/config/app.toml

sed -i.bak -e "s%^proxy_app = \"tcp://127.0.0.1:26658\"%proxy_app = \"tcp://127.0.0.1:37658\"%; s%^laddr = \"tcp://127.0.0.1:26657\"%laddr = \"tcp://127.0.0.1:37657\"%; s%^pprof_laddr = \"localhost:6060\"%pprof_laddr = \"localhost:37060\"%; s%^laddr = \"tcp://0.0.0.0:26656\"%laddr = \"tcp://0.0.0.0:37656\"%; s%^prometheus_listen_addr = \":26660\"%prometheus_listen_addr = \":37660\"%" $HOME/.canine/config/config.toml
sed -i.bak -e "s%^address = \"tcp://0.0.0.0:1317\"%address = \"tcp://0.0.0.0:37317\"%; s%^address = \":8080\"%address = \":37080\"%; s%^address = \"0.0.0.0:9090\"%address = \"0.0.0.0:37090\"%; s%^address = \"0.0.0.0:9091\"%address = \"0.0.0.0:37091\"%; s%^address = \"0.0.0.0:8545\"%address = \"0.0.0.0:37545\"%; s%^ws-address = \"0.0.0.0:8546\"%ws-address = \"0.0.0.0:37546\"%" $HOME/.canine/config/app.toml
```

### Download latest chain snapshot

```bash
curl -L https://snapshots.kjnodes.com/jackal/snapshot_latest.tar.lz4 | lz4 -dc - | tar -xf - -C $HOME/.canine
```

### Start service and check the logs

```bash
sudo systemctl start canined && journalctl -u canined -f --no-hostname -o cat
```
