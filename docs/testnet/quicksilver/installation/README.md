---
description: Setting up your validator node has never been so easy. Get your validator running in minutes by following step by step instructions.
---

# Installation

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/quicksilver.png" width="150" alt=""><figcaption></figcaption></figure>

**Chain ID**: innuendo-3 | **Latest Binary Version**: v0.10.3 | **Custom Port**: 11

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
sudo wget -O /usr/bin/quicksilverd https://github.com/ingenuity-build/testnets/releases/download/v0.10.0/quicksilverd-v0.10.1-amd64
chmod +x /usr/bin/quicksilverd
```

### Create a service

```bash
sudo tee /etc/systemd/system/quicksilverd.service > /dev/null << EOF
[Unit]
Description=quicksilver-testnet node service
After=network-online.target

[Service]
User=$USER
ExecStart=$(which quicksilverd) start --home $HOME/.quicksilverd
Restart=on-failure
RestartSec=3
LimitNOFILE=65535

[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable quicksilverd
```

### Initialize the node

```bash
quicksilverd config chain-id innuendo-3
quicksilverd config keyring-backend test
quicksilverd config node tcp://localhost:11657
quicksilverd init $MONIKER --chain-id innuendo-3
curl -Ls https://snapshots.kjnodes.com/quicksilver-testnet/genesis.json > $HOME/.quicksilverd/config/genesis.json
curl -Ls https://snapshots.kjnodes.com/quicksilver-testnet/addrbook.json > $HOME/.quicksilverd/config/addrbook.json
sed -i -e "s|^seeds *=.*|seeds = \"3f472746f46493309650e5a033076689996c8881@quicksilver-testnet.rpc.kjnodes.com:11659\"|" $HOME/.quicksilverd/config/config.toml
sed -i -e "s|^minimum-gas-prices *=.*|minimum-gas-prices = \"0uqck\"|" $HOME/.quicksilverd/config/app.toml
sed -i -e "s|^pruning *=.*|pruning = \"custom\"|" $HOME/.quicksilverd/config/app.toml
sed -i -e "s|^pruning-keep-recent *=.*|pruning-keep-recent = \"100\"|" $HOME/.quicksilverd/config/app.toml
sed -i -e "s|^pruning-keep-every *=.*|pruning-keep-every = \"0\"|" $HOME/.quicksilverd/config/app.toml
sed -i -e "s|^pruning-interval *=.*|pruning-interval = \"19\"|" $HOME/.quicksilverd/config/app.toml

sed -i.bak -e "s%^proxy_app = \"tcp://127.0.0.1:26658\"%proxy_app = \"tcp://127.0.0.1:11658\"%; s%^laddr = \"tcp://127.0.0.1:26657\"%laddr = \"tcp://127.0.0.1:11657\"%; s%^pprof_laddr = \"localhost:6060\"%pprof_laddr = \"localhost:11060\"%; s%^laddr = \"tcp://0.0.0.0:26656\"%laddr = \"tcp://0.0.0.0:11656\"%; s%^prometheus_listen_addr = \":26660\"%prometheus_listen_addr = \":11660\"%" $HOME/.quicksilverd/config/config.toml
sed -i.bak -e "s%^address = \"tcp://0.0.0.0:1317\"%address = \"tcp://0.0.0.0:11317\"%; s%^address = \":8080\"%address = \":11080\"%; s%^address = \"0.0.0.0:9090\"%address = \"0.0.0.0:11090\"%; s%^address = \"0.0.0.0:9091\"%address = \"0.0.0.0:11091\"%; s%^address = \"0.0.0.0:8545\"%address = \"0.0.0.0:11545\"%; s%^ws-address = \"0.0.0.0:8546\"%ws-address = \"0.0.0.0:11546\"%" $HOME/.quicksilverd/config/app.toml
```

### Download latest chain snapshot

```bash
curl -L https://snapshots.kjnodes.com/quicksilver-testnet/snapshot_latest.tar.lz4 | lz4 -dc - | tar -xf - -C $HOME/.quicksilverd
```

### Start service and check the logs

```bash
sudo systemctl start quicksilverd && journalctl -u quicksilverd -f --no-hostname -o cat
```
