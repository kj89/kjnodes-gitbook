# Installation

### Chain configuration

| key               | value                  |
| ----------------- | ---------------------- |
| chain-id          | **agoric-3**        |
| custom-port       | **27**      |
| chain-denom       | **ubld**     |
| genesis-version   | **agoric-3.1** |
| latest-version    | **pismoA**  |

### Setup validator name

```bash
MONIKER="YOUR_MONIKER_GOES_HERE"
```

### Install dependencies

#### Download the nodesource PPA for Node.js
```
curl https://deb.nodesource.com/setup_16.x | sudo bash
```

#### Install the Yarn package manager
```
curl -sL https://dl.yarnpkg.com/debian/pubkey.gpg | gpg --dearmor | sudo tee /usr/share/keyrings/yarnkey.gpg >/dev/null
echo "deb [signed-by=/usr/share/keyrings/yarnkey.gpg] https://dl.yarnpkg.com/debian stable main" | sudo tee /etc/apt/sources.list.d/yarn.list
```

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
export PATH=$PATH:/usr/local/go/bin
EOF
source $HOME/.profile
```

### Download and build binaries

```bash
# Clone git repository
cd $HOME
rm -rf agoric-sdk
git clone https://github.com/Agoric/agoric-sdk.git
cd agoric-sdk
git checkout pismoA

# Install and build Agoric Javascript packages
yarn install && yarn build

# Install and build Agoric Cosmos SDK support
(cd packages/cosmic-swingset && make)
```

### Initialize the node

```bash
agd config chain-id agoric-3
agd config node tcp://localhost:27657
agd init $MONIKER --chain-id agoric-3
curl -Ls https://snapshots.kjnodes.com/agoric/genesis.json > $HOME/.agoric/config/genesis.json
curl -Ls https://snapshots.kjnodes.com/agoric/addrbook.json > $HOME/.agoric/config/addrbook.json
sed -i -e "s|^seeds *=.*|seeds = \"400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@agoric.rpc.kjnodes.com:27659\"|" $HOME/.agoric/config/config.toml
tee $HOME/.agoric/data/priv_validator_state.json > /dev/null << EOF
{
  "height": "0",
  "round": 0,
  "step": 0
}
EOF
sed -i -e "s|^minimum-gas-prices *=.*|minimum-gas-prices = \"0.025ubld\"|" $HOME/.agoric/config/app.toml
sed -i -e "s|^pruning *=.*|pruning = \"custom\"|" $HOME/.agoric/config/app.toml
sed -i -e "s|^pruning-keep-recent *=.*|pruning-keep-recent = \"5\"|" $HOME/.agoric/config/app.toml
sed -i -e "s|^pruning-keep-every *=.*|pruning-keep-every = \"0\"|" $HOME/.agoric/config/app.toml
sed -i -e "s|^pruning-interval *=.*|pruning-interval = \"1000\"|" $HOME/.agoric/config/app.toml

sed -i.bak -e "s%^proxy_app = \"tcp://127.0.0.1:26658\"%proxy_app = \"tcp://127.0.0.1:27658\"%; s%^laddr = \"tcp://127.0.0.1:26657\"%laddr = \"tcp://127.0.0.1:27657\"%; s%^pprof_laddr = \"localhost:6060\"%pprof_laddr = \"localhost:27060\"%; s%^laddr = \"tcp://0.0.0.0:26656\"%laddr = \"tcp://0.0.0.0:27656\"%; s%^prometheus_listen_addr = \":26660\"%prometheus_listen_addr = \":27660\"%" $HOME/.agoric/config/config.toml
sed -i.bak -e "s%^address = \"tcp://0.0.0.0:1317\"%address = \"tcp://0.0.0.0:27317\"%; s%^address = \":8080\"%address = \":27080\"%; s%^address = \"0.0.0.0:9090\"%address = \"0.0.0.0:27090\"%; s%^address = \"0.0.0.0:9091\"%address = \"0.0.0.0:27091\"%; s%^address = \"0.0.0.0:8545\"%address = \"0.0.0.0:27545\"%; s%^ws-address = \"0.0.0.0:8546\"%ws-address = \"0.0.0.0:27546\"%" $HOME/.agoric/config/app.toml
```

### Download latest chain snapshot

```bash
curl -L https://snapshots.kjnodes.com/agoric/snapshot_latest.tar.lz4 | lz4 -dc - | tar -xf - -C $HOME/.agoric
```

### Start service and check the logs

```bash
sudo systemctl start agd && journalctl -u agd -f --no-hostname -o cat
```
