---
description: Setting up your validator node has never been so easy. Get your validator running in minutes by following step by step instructions.
---

# Installation

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/teritori.png" width="150" alt=""><figcaption></figcaption></figure>

**Chain ID**: teritori-1 | **Latest Version Tag**: v1.3.0 | **Custom Port**: 19

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
rm -rf teritori-chain
git clone https://github.com/TERITORI/teritori-chain.git
cd teritori-chain

# Compile genesis version v1.1.2
git checkout v1.1.2
make build
mkdir -p $HOME/.teritorid/cosmovisor/genesis/bin
mv build/teritorid $HOME/.teritorid/cosmovisor/genesis/bin/
rm -rf build

# Compile latest version v1.3.0
git checkout v1.3.0
make build
mkdir -p $HOME/.teritorid/cosmovisor/upgrades/v1.3.0/bin
mv build/teritorid $HOME/.teritorid/cosmovisor/upgrades/v1.3.0/bin/
rm build/teritorid -rf
```

### Install Cosmovisor and create a service

```bash
curl -Ls https://github.com/cosmos/cosmos-sdk/releases/download/cosmovisor%2Fv1.3.0/cosmovisor-v1.3.0-linux-amd64.tar.gz | tar xz
chmod 755 cosmovisor
sudo mv cosmovisor /usr/bin/cosmovisor

sudo tee /etc/systemd/system/teritorid.service > /dev/null << EOF
[Unit]
Description=teritori node service
After=network-online.target
[Service]
User=$USER
ExecStart=/usr/bin/cosmovisor run start
Restart=on-failure
RestartSec=10
LimitNOFILE=65535
Environment="DAEMON_HOME=$HOME/.teritorid"
Environment="DAEMON_NAME=teritorid"
Environment="UNSAFE_SKIP_BACKUP=true"
[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable teritorid
```

### Initialize the node

```bash
ln -s $HOME/.teritorid/cosmovisor/upgrades/v1.3.0 $HOME/.teritorid/cosmovisor/current
sudo ln -s $HOME/.teritorid/cosmovisor/current/bin/teritorid /usr/local/bin/teritorid
teritorid config chain-id teritori-1
teritorid config keyring-backend file
teritorid config node tcp://localhost:19657
teritorid init $MONIKER --chain-id teritori-1
curl -Ls https://snapshots.kjnodes.com/teritori/genesis.json > $HOME/.teritorid/config/genesis.json
curl -Ls https://snapshots.kjnodes.com/teritori/addrbook.json > $HOME/.teritorid/config/addrbook.json
sed -i -e "s|^seeds *=.*|seeds = \"400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@teritori.rpc.kjnodes.com:19659\"|" $HOME/.teritorid/config/config.toml
sed -i -e "s|^minimum-gas-prices *=.*|minimum-gas-prices = \"0utori\"|" $HOME/.teritorid/config/app.toml
sed -i -e "s|^pruning *=.*|pruning = \"custom\"|" $HOME/.teritorid/config/app.toml
sed -i -e "s|^pruning-keep-recent *=.*|pruning-keep-recent = \"100\"|" $HOME/.teritorid/config/app.toml
sed -i -e "s|^pruning-keep-every *=.*|pruning-keep-every = \"0\"|" $HOME/.teritorid/config/app.toml
sed -i -e "s|^pruning-interval *=.*|pruning-interval = \"19\"|" $HOME/.teritorid/config/app.toml

sed -i.bak -e "s%^proxy_app = \"tcp://127.0.0.1:26658\"%proxy_app = \"tcp://127.0.0.1:19658\"%; s%^laddr = \"tcp://127.0.0.1:26657\"%laddr = \"tcp://127.0.0.1:19657\"%; s%^pprof_laddr = \"localhost:6060\"%pprof_laddr = \"localhost:19060\"%; s%^laddr = \"tcp://0.0.0.0:26656\"%laddr = \"tcp://0.0.0.0:19656\"%; s%^prometheus_listen_addr = \":26660\"%prometheus_listen_addr = \":19660\"%" $HOME/.teritorid/config/config.toml
sed -i.bak -e "s%^address = \"tcp://0.0.0.0:1317\"%address = \"tcp://0.0.0.0:19317\"%; s%^address = \":8080\"%address = \":19080\"%; s%^address = \"0.0.0.0:9090\"%address = \"0.0.0.0:19090\"%; s%^address = \"0.0.0.0:9091\"%address = \"0.0.0.0:19091\"%; s%^address = \"0.0.0.0:8545\"%address = \"0.0.0.0:19545\"%; s%^ws-address = \"0.0.0.0:8546\"%ws-address = \"0.0.0.0:19546\"%" $HOME/.teritorid/config/app.toml
```

### Download latest chain snapshot

```bash
curl -L https://snapshots.kjnodes.com/teritori/snapshot_latest.tar.lz4 | lz4 -dc - | tar -xf - -C $HOME/.teritorid
```

### Start service and check the logs

```bash
sudo systemctl start teritorid && journalctl -u teritorid -f --no-hostname -o cat
```
