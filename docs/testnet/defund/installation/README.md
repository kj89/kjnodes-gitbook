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
rm -rf defund
git clone https://github.com/defund-labs/defund.git
cd defund

# Compile genesis version v0.1.0
git checkout v0.1.0
make build
mkdir -p $HOME/.defund/cosmovisor/genesis/bin
mv build/defundd $HOME/.defund/cosmovisor/genesis/bin/
rm build -rf


```

### Install Cosmovisor and create a service

```bash
curl -Ls https://github.com/cosmos/cosmos-sdk/releases/download/cosmovisor%2Fv1.3.0/cosmovisor-v1.3.0-linux-amd64.tar.gz | tar xz
chmod 755 cosmovisor
sudo mv cosmovisor /usr/bin/cosmovisor

sudo tee /etc/systemd/system/defundd.service > /dev/null << EOF
[Unit]
Description=defund-testnet node service
After=network-online.target
[Service]
User=$USER
ExecStart=/usr/bin/cosmovisor run start
Restart=on-failure
RestartSec=10
LimitNOFILE=65535
Environment="DAEMON_HOME=$HOME/.defund"
Environment="DAEMON_NAME=defundd"
Environment="UNSAFE_SKIP_BACKUP=true"
[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable defundd
```

### Initialize the node

```bash
ln -s $HOME/.defund/cosmovisor/genesis $HOME/.defund/cosmovisor/current
sudo ln -s $HOME/.defund/cosmovisor/current/bin/defundd /usr/local/bin/defundd
defundd config chain-id defund-private-2
defundd config node tcp://localhost:40657
defundd init $MONIKER --chain-id defund-private-2
curl -Ls https://snapshots.kjnodes.com/defund-testnet/genesis.json > $HOME/.defund/config/genesis.json
curl -Ls https://snapshots.kjnodes.com/defund-testnet/addrbook.json > $HOME/.defund/config/addrbook.json
sed -i -e "s|^seeds *=.*|seeds = \"400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@defund-testnet.rpc.kjnodes.com:40659\"|" $HOME/.defund/config/config.toml
tee $HOME/.defund/data/priv_validator_state.json > /dev/null << EOF
{
  "height": "0",
  "round": 0,
  "step": 0
}
EOF
sed -i -e "s|^minimum-gas-prices *=.*|minimum-gas-prices = \"0ufetf\"|" $HOME/.defund/config/app.toml
sed -i -e "s|^pruning *=.*|pruning = \"custom\"|" $HOME/.defund/config/app.toml
sed -i -e "s|^pruning-keep-recent *=.*|pruning-keep-recent = \"5\"|" $HOME/.defund/config/app.toml
sed -i -e "s|^pruning-keep-every *=.*|pruning-keep-every = \"0\"|" $HOME/.defund/config/app.toml
sed -i -e "s|^pruning-interval *=.*|pruning-interval = \"1000\"|" $HOME/.defund/config/app.toml

sed -i.bak -e "s%^proxy_app = \"tcp://127.0.0.1:26658\"%proxy_app = \"tcp://127.0.0.1:40658\"%; s%^laddr = \"tcp://127.0.0.1:26657\"%laddr = \"tcp://127.0.0.1:40657\"%; s%^pprof_laddr = \"localhost:6060\"%pprof_laddr = \"localhost:40060\"%; s%^laddr = \"tcp://0.0.0.0:26656\"%laddr = \"tcp://0.0.0.0:40656\"%; s%^prometheus_listen_addr = \":26660\"%prometheus_listen_addr = \":40660\"%" $HOME/.defund/config/config.toml
sed -i.bak -e "s%^address = \"tcp://0.0.0.0:1317\"%address = \"tcp://0.0.0.0:40317\"%; s%^address = \":8080\"%address = \":40080\"%; s%^address = \"0.0.0.0:9090\"%address = \"0.0.0.0:40090\"%; s%^address = \"0.0.0.0:9091\"%address = \"0.0.0.0:40091\"%; s%^address = \"0.0.0.0:8545\"%address = \"0.0.0.0:40545\"%; s%^ws-address = \"0.0.0.0:8546\"%ws-address = \"0.0.0.0:40546\"%" $HOME/.defund/config/app.toml
```

### Download latest chain snapshot

```bash
curl -L https://snapshots.kjnodes.com/defund-testnet/snapshot_latest.tar.lz4 | lz4 -dc - | tar -xf - -C $HOME/.defund
```

### Start service and check the logs

```bash
sudo systemctl start defundd && journalctl -u defundd -f --no-hostname -o cat
```
