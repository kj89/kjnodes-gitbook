---
description: Setting up your validator node has never been so easy. Get your validator running in minutes by following step by step instructions.
---

# Installation

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/cosmoshub.png" width="150" alt=""><figcaption></figcaption></figure>

**Chain ID**: cosmoshub-4 | **Latest Version Tag**: v7.1.0 | **Custom Port**: 34

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
rm -rf gaia
git clone https://github.com/cosmos/gaia.git
cd gaia

# Compile genesis version v2.0.0
git checkout v2.0.0
make build
mkdir -p $HOME/.gaia/cosmovisor/genesis/bin
mv build/gaiad $HOME/.gaia/cosmovisor/genesis/bin/
rm -rf build

# Compile latest version v7.1.0
git checkout v7.1.0
make build
mkdir -p $HOME/.gaia/cosmovisor/upgrades/v7-Theta/bin
mv build/gaiad $HOME/.gaia/cosmovisor/upgrades/v7-Theta/bin/
rm build/gaiad -rf
```

### Install Cosmovisor and create a service

```bash
curl -Ls https://github.com/cosmos/cosmos-sdk/releases/download/cosmovisor%2Fv1.3.0/cosmovisor-v1.3.0-linux-amd64.tar.gz | tar xz
chmod 755 cosmovisor
sudo mv cosmovisor /usr/bin/cosmovisor

sudo tee /etc/systemd/system/gaiad.service > /dev/null << EOF
[Unit]
Description=cosmoshub node service
After=network-online.target
[Service]
User=$USER
ExecStart=/usr/bin/cosmovisor run start
Restart=on-failure
RestartSec=10
LimitNOFILE=65535
Environment="DAEMON_HOME=$HOME/.gaia"
Environment="DAEMON_NAME=gaiad"
Environment="UNSAFE_SKIP_BACKUP=true"
[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable gaiad
```

### Initialize the node

```bash
ln -s $HOME/.gaia/cosmovisor/upgrades/v7-Theta $HOME/.gaia/cosmovisor/current
sudo ln -s $HOME/.gaia/cosmovisor/current/bin/gaiad /usr/local/bin/gaiad
gaiad config chain-id cosmoshub-4
gaiad config keyring-backend file
gaiad config node tcp://localhost:34657
gaiad init $MONIKER --chain-id cosmoshub-4
curl -Ls https://snapshots.kjnodes.com/cosmoshub/genesis.json > $HOME/.gaia/config/genesis.json
curl -Ls https://snapshots.kjnodes.com/cosmoshub/addrbook.json > $HOME/.gaia/config/addrbook.json
sed -i -e "s|^seeds *=.*|seeds = \"400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@cosmoshub.rpc.kjnodes.com:34659\"|" $HOME/.gaia/config/config.toml
sed -i -e "s|^minimum-gas-prices *=.*|minimum-gas-prices = \"0uatom\"|" $HOME/.gaia/config/app.toml
sed -i -e "s|^pruning *=.*|pruning = \"custom\"|" $HOME/.gaia/config/app.toml
sed -i -e "s|^pruning-keep-recent *=.*|pruning-keep-recent = \"100\"|" $HOME/.gaia/config/app.toml
sed -i -e "s|^pruning-keep-every *=.*|pruning-keep-every = \"0\"|" $HOME/.gaia/config/app.toml
sed -i -e "s|^pruning-interval *=.*|pruning-interval = \"19\"|" $HOME/.gaia/config/app.toml

sed -i.bak -e "s%^proxy_app = \"tcp://127.0.0.1:26658\"%proxy_app = \"tcp://127.0.0.1:34658\"%; s%^laddr = \"tcp://127.0.0.1:26657\"%laddr = \"tcp://127.0.0.1:34657\"%; s%^pprof_laddr = \"localhost:6060\"%pprof_laddr = \"localhost:34060\"%; s%^laddr = \"tcp://0.0.0.0:26656\"%laddr = \"tcp://0.0.0.0:34656\"%; s%^prometheus_listen_addr = \":26660\"%prometheus_listen_addr = \":34660\"%" $HOME/.gaia/config/config.toml
sed -i.bak -e "s%^address = \"tcp://0.0.0.0:1317\"%address = \"tcp://0.0.0.0:34317\"%; s%^address = \":8080\"%address = \":34080\"%; s%^address = \"0.0.0.0:9090\"%address = \"0.0.0.0:34090\"%; s%^address = \"0.0.0.0:9091\"%address = \"0.0.0.0:34091\"%; s%^address = \"0.0.0.0:8545\"%address = \"0.0.0.0:34545\"%; s%^ws-address = \"0.0.0.0:8546\"%ws-address = \"0.0.0.0:34546\"%" $HOME/.gaia/config/app.toml
```

### Download latest chain snapshot

```bash
curl -L https://snapshots.kjnodes.com/cosmoshub/snapshot_latest.tar.lz4 | lz4 -dc - | tar -xf - -C $HOME/.gaia
```

### Start service and check the logs

```bash
sudo systemctl start gaiad && journalctl -u gaiad -f --no-hostname -o cat
```
