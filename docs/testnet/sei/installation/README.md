# Installation

**Chain ID**: atlantic-1 | **Latest Version Tag**: 1.2.2beta-postfix

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
rm -rf sei-chain
git clone https://github.com/sei-protocol/sei-chain.git
cd sei-chain

# Compile genesis version 1.0.6beta-val-count-fix
git checkout 1.0.6beta-val-count-fix
make build
mkdir -p $HOME/.sei/cosmovisor/genesis/bin
mv build/seid $HOME/.sei/cosmovisor/genesis/bin/

# Compile latest version 1.2.2beta-postfix
git checkout 1.2.2beta-postfix
make build
mkdir -p $HOME/.sei/cosmovisor/upgrades/1.2.2beta-postfix/bin
mv build/seid $HOME/$.sei/cosmovisor/upgrades/$1.2.2beta-postfix/bin/
rm build/seid -rf
```

### Install Cosmovisor and create a service

```bash
curl -Ls https://github.com/cosmos/cosmos-sdk/releases/download/cosmovisor%2Fv1.3.0/cosmovisor-v1.3.0-linux-amd64.tar.gz | tar xz
chmod 755 cosmovisor
sudo mv cosmovisor /usr/bin/cosmovisor

sudo tee /etc/systemd/system/seid.service > /dev/null << EOF
[Unit]
Description=sei-testnet node service
After=network-online.target
[Service]
User=$USER
ExecStart=/usr/bin/cosmovisor run start
Restart=on-failure
RestartSec=10
LimitNOFILE=65535
Environment="DAEMON_HOME=$HOME/.sei"
Environment="DAEMON_NAME=seid"
Environment="UNSAFE_SKIP_BACKUP=true"
[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable seid
```

### Initialize the node

```bash
ln -s $HOME/.sei/cosmovisor/upgrades/1.2.2beta-postfix $HOME/.sei/cosmovisor/current
sudo ln -s $HOME/.sei/cosmovisor/current/bin/seid /usr/local/bin/seid
seid config chain-id atlantic-1
seid config keyring-backend test
seid config node tcp://localhost:12657
seid init $MONIKER --chain-id atlantic-1
curl -Ls https://snapshots.kjnodes.com/sei-testnet/genesis.json > $HOME/.sei/config/genesis.json
curl -Ls https://snapshots.kjnodes.com/sei-testnet/addrbook.json > $HOME/.sei/config/addrbook.json
sed -i -e "s|^seeds *=.*|seeds = \"3f472746f46493309650e5a033076689996c8881@sei-testnet.rpc.kjnodes.com:12659\"|" $HOME/.sei/config/config.toml
tee $HOME/.sei/data/priv_validator_state.json > /dev/null << EOF
{
  "height": "0",
  "round": 0,
  "step": 0
}
EOF
sed -i -e "s|^minimum-gas-prices *=.*|minimum-gas-prices = \"0usei\"|" $HOME/.sei/config/app.toml
sed -i -e "s|^pruning *=.*|pruning = \"custom\"|" $HOME/.sei/config/app.toml
sed -i -e "s|^pruning-keep-recent *=.*|pruning-keep-recent = \"100\"|" $HOME/.sei/config/app.toml
sed -i -e "s|^pruning-keep-every *=.*|pruning-keep-every = \"0\"|" $HOME/.sei/config/app.toml
sed -i -e "s|^pruning-interval *=.*|pruning-interval = \"19\"|" $HOME/.sei/config/app.toml

sed -i.bak -e "s%^proxy_app = \"tcp://127.0.0.1:26658\"%proxy_app = \"tcp://127.0.0.1:12658\"%; s%^laddr = \"tcp://127.0.0.1:26657\"%laddr = \"tcp://127.0.0.1:12657\"%; s%^pprof_laddr = \"localhost:6060\"%pprof_laddr = \"localhost:12060\"%; s%^laddr = \"tcp://0.0.0.0:26656\"%laddr = \"tcp://0.0.0.0:12656\"%; s%^prometheus_listen_addr = \":26660\"%prometheus_listen_addr = \":12660\"%" $HOME/.sei/config/config.toml
sed -i.bak -e "s%^address = \"tcp://0.0.0.0:1317\"%address = \"tcp://0.0.0.0:12317\"%; s%^address = \":8080\"%address = \":12080\"%; s%^address = \"0.0.0.0:9090\"%address = \"0.0.0.0:12090\"%; s%^address = \"0.0.0.0:9091\"%address = \"0.0.0.0:12091\"%; s%^address = \"0.0.0.0:8545\"%address = \"0.0.0.0:12545\"%; s%^ws-address = \"0.0.0.0:8546\"%ws-address = \"0.0.0.0:12546\"%" $HOME/.sei/config/app.toml
```

### Download latest chain snapshot

```bash
curl -L https://snapshots.kjnodes.com/sei-testnet/snapshot_latest.tar.lz4 | lz4 -dc - | tar -xf - -C $HOME/.sei
```

### Start service and check the logs

```bash
sudo systemctl start seid && journalctl -u seid -f --no-hostname -o cat
```
