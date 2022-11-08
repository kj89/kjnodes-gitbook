# Installation

chain-id: **euphoria-1**\
custom-port: **17**\
chain-denom: **ueaura**\
genesis-version: **euphoria_4027003**\
latest-version: **euphoria_v0.3.3**

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
rm -rf aura
git clone https://github.com/aura-nw/aura.git
cd aura

# Compile genesis version euphoria_4027003
git checkout euphoria_4027003
make build
mkdir -p $HOME/.aura/cosmovisor/genesis/bin
mv build/aurad $HOME/.aura/cosmovisor/genesis/bin/

# Compile latest version euphoria_v0.3.3
git checkout euphoria_v0.3.3
make build
mkdir -p $HOME/.aura/cosmovisor/upgrades/euphoria_v0.3.3/bin
mv build/aurad $HOME/$.aura/cosmovisor/upgrades/$euphoria_v0.3.3/bin/
rm build/aurad -rf
```

### Install Cosmovisor and create a service

```bash
curl -Ls https://github.com/cosmos/cosmos-sdk/releases/download/cosmovisor%2Fv1.3.0/cosmovisor-v1.3.0-linux-amd64.tar.gz | tar xz
chmod 755 cosmovisor
sudo mv cosmovisor /usr/bin/cosmovisor

sudo tee /etc/systemd/system/aurad.service > /dev/null << EOF
[Unit]
Description=aura-testnet node service
After=network-online.target
[Service]
User=$USER
ExecStart=/usr/bin/cosmovisor run start
Restart=on-failure
RestartSec=10
LimitNOFILE=65535
Environment="DAEMON_HOME=$HOME/.aura"
Environment="DAEMON_NAME=aurad"
Environment="UNSAFE_SKIP_BACKUP=true"
[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable aurad
```

### Initialize the node

```bash
ln -s $HOME/.aura/cosmovisor/upgrades/euphoria_v0.3.3 $HOME/.aura/cosmovisor/current
sudo ln -s $HOME/.aura/cosmovisor/current/bin/aurad /usr/local/bin/aurad
aurad config chain-id euphoria-1
aurad config keyring-backend test
aurad config node tcp://localhost:17657
aurad init $MONIKER --chain-id euphoria-1
curl -Ls https://snapshots.kjnodes.com/aura-testnet/genesis.json > $HOME/.aura/config/genesis.json
curl -Ls https://snapshots.kjnodes.com/aura-testnet/addrbook.json > $HOME/.aura/config/addrbook.json
sed -i -e "s|^seeds *=.*|seeds = \"3f472746f46493309650e5a033076689996c8881@aura-testnet.rpc.kjnodes.com:17659\"|" $HOME/.aura/config/config.toml
tee $HOME/.aura/data/priv_validator_state.json > /dev/null << EOF
{
  "height": "0",
  "round": 0,
  "step": 0
}
EOF
sed -i -e "s|^minimum-gas-prices *=.*|minimum-gas-prices = \"0ueaura\"|" $HOME/.aura/config/app.toml
sed -i -e "s|^pruning *=.*|pruning = \"custom\"|" $HOME/.aura/config/app.toml
sed -i -e "s|^pruning-keep-recent *=.*|pruning-keep-recent = \"5\"|" $HOME/.aura/config/app.toml
sed -i -e "s|^pruning-keep-every *=.*|pruning-keep-every = \"0\"|" $HOME/.aura/config/app.toml
sed -i -e "s|^pruning-interval *=.*|pruning-interval = \"1000\"|" $HOME/.aura/config/app.toml

sed -i.bak -e "s%^proxy_app = \"tcp://127.0.0.1:26658\"%proxy_app = \"tcp://127.0.0.1:17658\"%; s%^laddr = \"tcp://127.0.0.1:26657\"%laddr = \"tcp://127.0.0.1:17657\"%; s%^pprof_laddr = \"localhost:6060\"%pprof_laddr = \"localhost:17060\"%; s%^laddr = \"tcp://0.0.0.0:26656\"%laddr = \"tcp://0.0.0.0:17656\"%; s%^prometheus_listen_addr = \":26660\"%prometheus_listen_addr = \":17660\"%" $HOME/.aura/config/config.toml
sed -i.bak -e "s%^address = \"tcp://0.0.0.0:1317\"%address = \"tcp://0.0.0.0:17317\"%; s%^address = \":8080\"%address = \":17080\"%; s%^address = \"0.0.0.0:9090\"%address = \"0.0.0.0:17090\"%; s%^address = \"0.0.0.0:9091\"%address = \"0.0.0.0:17091\"%; s%^address = \"0.0.0.0:8545\"%address = \"0.0.0.0:17545\"%; s%^ws-address = \"0.0.0.0:8546\"%ws-address = \"0.0.0.0:17546\"%" $HOME/.aura/config/app.toml
```

### Download latest chain snapshot

```bash
curl -L https://snapshots.kjnodes.com/aura-testnet/snapshot_latest.tar.lz4 | lz4 -dc - | tar -xf - -C $HOME/.aura
```

### Start service and check the logs

```bash
sudo systemctl start aurad && journalctl -u aurad -f --no-hostname -o cat
```
