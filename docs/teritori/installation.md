---
description: >-
  This page contain instructions that will help you to setup a node. For the
  installation we use Ubuntu 20.04
---

# Installation

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

# Compile version v1.3.0
git checkout v1.3.0
make build
mkdir -p $HOME/.teritorid/cosmovisor/genesis/bin
mv build/teritorid $HOME/.teritorid/cosmovisor/genesis/bin/
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
teritorid init $MONIKER --chain-id teritori-1
curl -Ls https://snapshots.kjnodes.com/teritori/genesis.json > $HOME/.teritorid/config/genesis.json
sed -i -e "s|^seeds *=.*|seeds = \"d07f430ddf0725804b3755c31660f88518547345@teritori.rpc.kjnodes.com:16659\"|" $HOME/.teritorid/config/config.toml
tee $HOME/.teritorid/data/priv_validator_state.json > /dev/null << EOF
{
  "height": "0",
  "round": 0,
  "step": 0
}
EOF
sed -i -e "s|^minimum-gas-prices *=.*|minimum-gas-prices = \"0utori\"|" $HOME/.teritorid/config/app.toml
sed -i -e "s|^pruning *=.*|pruning = \"custom\"|" $HOME/.teritorid/config/app.toml
sed -i -e "s|^pruning-keep-recent *=.*|pruning-keep-recent = \"5\"|" $HOME/.teritorid/config/app.toml
sed -i -e "s|^pruning-keep-every *=.*|pruning-keep-every = \"0\"|" $HOME/.teritorid/config/app.toml
sed -i -e "s|^pruning-interval *=.*|pruning-interval = \"1000\"|" $HOME/.teritorid/config/app.toml
```

### Download latest chain snapshot

```bash
curl -L https://snapshots.kjnodes.com/teritori/snapshot_latest.tar.lz4 | lz4 -dc - | tar -xf - -C $HOME/.teritorid
```

### Start service and check the logs

```bash
sudo systemctl start teritorid && journalctl -u teritorid -f --no-hostname -o cat
```
