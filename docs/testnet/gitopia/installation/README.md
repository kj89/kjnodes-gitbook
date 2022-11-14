---
description: Setting up your validator node has never been so easy. Get your validator running in minutes by following step by step instructions.
---

# Installation

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/gitopia.png" width="150" alt=""><figcaption></figcaption></figure>

**Chain ID**: gitopia-janus-testnet-2 | **Latest Version Tag**: v1.2.0 | **Custom Port**: 41

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
rm -rf gitopia
git clone gitopia://gitopia/gitopia
cd gitopia

# Compile genesis version v1.2.0
git checkout v1.2.0
make build
mkdir -p $HOME/.gitopia/cosmovisor/genesis/bin
mv build/gitopiad $HOME/.gitopia/cosmovisor/genesis/bin/
rm -rf build

```

### Install Cosmovisor and create a service

```bash
curl -Ls https://github.com/cosmos/cosmos-sdk/releases/download/cosmovisor%2Fv1.3.0/cosmovisor-v1.3.0-linux-amd64.tar.gz | tar xz
chmod 755 cosmovisor
sudo mv cosmovisor /usr/bin/cosmovisor

sudo tee /etc/systemd/system/gitopiad.service > /dev/null << EOF
[Unit]
Description=gitopia-testnet node service
After=network-online.target
[Service]
User=$USER
ExecStart=/usr/bin/cosmovisor run start
Restart=on-failure
RestartSec=10
LimitNOFILE=65535
Environment="DAEMON_HOME=$HOME/.gitopia"
Environment="DAEMON_NAME=gitopiad"
Environment="UNSAFE_SKIP_BACKUP=true"
[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable gitopiad
```

### Initialize the node

```bash
ln -s $HOME/.gitopia/cosmovisor/genesis $HOME/.gitopia/cosmovisor/current
sudo ln -s $HOME/.gitopia/cosmovisor/current/bin/gitopiad /usr/local/bin/gitopiad
gitopiad config chain-id gitopia-janus-testnet-2
gitopiad config keyring-backend test
gitopiad config node tcp://localhost:41657
gitopiad init $MONIKER --chain-id gitopia-janus-testnet-2
curl -Ls https://snapshots.kjnodes.com/gitopia-testnet/genesis.json > $HOME/.gitopia/config/genesis.json
curl -Ls https://snapshots.kjnodes.com/gitopia-testnet/addrbook.json > $HOME/.gitopia/config/addrbook.json
sed -i -e "s|^seeds *=.*|seeds = \"3f472746f46493309650e5a033076689996c8881@gitopia-testnet.rpc.kjnodes.com:41659\"|" $HOME/.gitopia/config/config.toml
sed -i -e "s|^minimum-gas-prices *=.*|minimum-gas-prices = \"0.001utlore\"|" $HOME/.gitopia/config/app.toml
sed -i -e "s|^pruning *=.*|pruning = \"custom\"|" $HOME/.gitopia/config/app.toml
sed -i -e "s|^pruning-keep-recent *=.*|pruning-keep-recent = \"100\"|" $HOME/.gitopia/config/app.toml
sed -i -e "s|^pruning-keep-every *=.*|pruning-keep-every = \"0\"|" $HOME/.gitopia/config/app.toml
sed -i -e "s|^pruning-interval *=.*|pruning-interval = \"19\"|" $HOME/.gitopia/config/app.toml

sed -i.bak -e "s%^proxy_app = \"tcp://127.0.0.1:26658\"%proxy_app = \"tcp://127.0.0.1:41658\"%; s%^laddr = \"tcp://127.0.0.1:26657\"%laddr = \"tcp://127.0.0.1:41657\"%; s%^pprof_laddr = \"localhost:6060\"%pprof_laddr = \"localhost:41060\"%; s%^laddr = \"tcp://0.0.0.0:26656\"%laddr = \"tcp://0.0.0.0:41656\"%; s%^prometheus_listen_addr = \":26660\"%prometheus_listen_addr = \":41660\"%" $HOME/.gitopia/config/config.toml
sed -i.bak -e "s%^address = \"tcp://0.0.0.0:1317\"%address = \"tcp://0.0.0.0:41317\"%; s%^address = \":8080\"%address = \":41080\"%; s%^address = \"0.0.0.0:9090\"%address = \"0.0.0.0:41090\"%; s%^address = \"0.0.0.0:9091\"%address = \"0.0.0.0:41091\"%; s%^address = \"0.0.0.0:8545\"%address = \"0.0.0.0:41545\"%; s%^ws-address = \"0.0.0.0:8546\"%ws-address = \"0.0.0.0:41546\"%" $HOME/.gitopia/config/app.toml
```

### Download latest chain snapshot

```bash
curl -L https://snapshots.kjnodes.com/gitopia-testnet/snapshot_latest.tar.lz4 | lz4 -dc - | tar -xf - -C $HOME/.gitopia
```

### Start service and check the logs

```bash
sudo systemctl start gitopiad && journalctl -u gitopiad -f --no-hostname -o cat
```
