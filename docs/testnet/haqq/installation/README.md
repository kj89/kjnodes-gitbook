---
description: Setting up your validator node has never been so easy. Get your validator running in minutes by following step by step instructions.
---

# Installation

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/haqq.png" width="150" alt=""><figcaption></figcaption></figure>

**Chain ID**: haqq_54211-3 | **Latest Version Tag**: v1.2.1 | **Custom Port**: 35

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
rm -rf haqq
git clone https://github.com/haqq-network/haqq.git
cd haqq

git checkout v1.2.1
make build
mkdir -p $HOME/.haqqd/cosmovisor/genesis/bin
mv build/haqqd $HOME/.haqqd/cosmovisor/genesis/bin/
rm -rf build
```

### Install Cosmovisor and create a service

```bash
curl -Ls https://github.com/cosmos/cosmos-sdk/releases/download/cosmovisor%2Fv1.3.0/cosmovisor-v1.3.0-linux-amd64.tar.gz | tar xz
chmod 755 cosmovisor
sudo mv cosmovisor /usr/bin/cosmovisor

sudo tee /etc/systemd/system/haqqd.service > /dev/null << EOF
[Unit]
Description=haqq-testnet node service
After=network-online.target
[Service]
User=$USER
ExecStart=/usr/bin/cosmovisor run start
Restart=on-failure
RestartSec=10
LimitNOFILE=65535
Environment="DAEMON_HOME=$HOME/.haqqd"
Environment="DAEMON_NAME=haqqd"
Environment="UNSAFE_SKIP_BACKUP=true"
[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable haqqd
```

### Initialize the node

```bash
ln -s $HOME/.haqqd/cosmovisor/genesis $HOME/.haqqd/cosmovisor/current
sudo ln -s $HOME/.haqqd/cosmovisor/current/bin/haqqd /usr/local/bin/haqqd
haqqd config chain-id haqq_54211-3
haqqd config keyring-backend test
haqqd config node tcp://localhost:35657
haqqd init $MONIKER --chain-id haqq_54211-3
curl -Ls https://snapshots.kjnodes.com/haqq-testnet/genesis.json > $HOME/.haqqd/config/genesis.json
curl -Ls https://snapshots.kjnodes.com/haqq-testnet/addrbook.json > $HOME/.haqqd/config/addrbook.json
sed -i -e "s|^seeds *=.*|seeds = \"3f472746f46493309650e5a033076689996c8881@haqq-testnet.rpc.kjnodes.com:35659\"|" $HOME/.haqqd/config/config.toml
sed -i -e "s|^minimum-gas-prices *=.*|minimum-gas-prices = \"0aISLM\"|" $HOME/.haqqd/config/app.toml
sed -i -e "s|^pruning *=.*|pruning = \"custom\"|" $HOME/.haqqd/config/app.toml
sed -i -e "s|^pruning-keep-recent *=.*|pruning-keep-recent = \"100\"|" $HOME/.haqqd/config/app.toml
sed -i -e "s|^pruning-keep-every *=.*|pruning-keep-every = \"0\"|" $HOME/.haqqd/config/app.toml
sed -i -e "s|^pruning-interval *=.*|pruning-interval = \"19\"|" $HOME/.haqqd/config/app.toml

sed -i.bak -e "s%^proxy_app = \"tcp://127.0.0.1:26658\"%proxy_app = \"tcp://127.0.0.1:35658\"%; s%^laddr = \"tcp://127.0.0.1:26657\"%laddr = \"tcp://127.0.0.1:35657\"%; s%^pprof_laddr = \"localhost:6060\"%pprof_laddr = \"localhost:35060\"%; s%^laddr = \"tcp://0.0.0.0:26656\"%laddr = \"tcp://0.0.0.0:35656\"%; s%^prometheus_listen_addr = \":26660\"%prometheus_listen_addr = \":35660\"%" $HOME/.haqqd/config/config.toml
sed -i.bak -e "s%^address = \"tcp://0.0.0.0:1317\"%address = \"tcp://0.0.0.0:35317\"%; s%^address = \":8080\"%address = \":35080\"%; s%^address = \"0.0.0.0:9090\"%address = \"0.0.0.0:35090\"%; s%^address = \"0.0.0.0:9091\"%address = \"0.0.0.0:35091\"%; s%^address = \"0.0.0.0:8545\"%address = \"0.0.0.0:35545\"%; s%^ws-address = \"0.0.0.0:8546\"%ws-address = \"0.0.0.0:35546\"%" $HOME/.haqqd/config/app.toml
```

### Download latest chain snapshot

```bash
curl -L https://snapshots.kjnodes.com/haqq-testnet/snapshot_latest.tar.lz4 | lz4 -dc - | tar -xf - -C $HOME/.haqqd
```

### Start service and check the logs

```bash
sudo systemctl start haqqd && journalctl -u haqqd -f --no-hostname -o cat
```
