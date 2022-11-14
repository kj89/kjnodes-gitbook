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
sudo apt install curl git jq lz4 build-essential nodejs=16.* yarn -y
```

#### Install GO

```bash
sudo rm -rf /usr/local/go
sudo curl -Ls https://go.dev/dl/go1.19.linux-amd64.tar.gz | sudo tar -C /usr/local -xz
tee -a $HOME/.profile > /dev/null << EOF
export PATH=$PATH:/usr/local/go/bin:$HOME/go/bin
EOF
source $HOME/.profile
```

#### Install Git Remote Helper
```
curl https://get.gitopia.com | bash
```

### Download and build binaries

```bash
cd $HOME && rm -rf gitopia
git clone -b v1.2.0 gitopia://gitopia/gitopia && cd gitopia
make install
```

### Create a service

```bash
sudo tee /etc/systemd/system/gitopiad.service > /dev/null << EOF
[Unit]
Description=gitopia-testnet node service
After=network-online.target

[Service]
User=$USER
ExecStart=$(which gitopiad) start --home $HOME/.gitopia
Restart=on-failure
RestartSec=3
LimitNOFILE=65535

[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable gitopiad
```

### Initialize the node

```bash
gitopiad config chain-id gitopia-janus-testnet-2
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
