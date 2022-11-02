---
description: >-
  This page contain instructions that will help you to setup a node. For the
  installation we use Ubuntu 20.04
---

# Installation

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
rm -rf ${GIT_DIR}
git clone ${GIT_URL}
cd ${GIT_DIR}

# Compile version ${VERSION}
git checkout ${VERSION}
make build
mkdir -p $HOME/${CHAIN_DIR}/cosmovisor/genesis/bin
mv build/${CHAIN_APP} $HOME/${CHAIN_DIR}/cosmovisor/genesis/bin/
```

### Install Cosmovisor and create a service

```bash
curl -Ls https://github.com/cosmos/cosmos-sdk/releases/download/cosmovisor%2Fv1.3.0/cosmovisor-v1.3.0-linux-amd64.tar.gz | tar xz
chmod 755 cosmovisor
sudo mv cosmovisor /usr/bin/cosmovisor

sudo tee /etc/systemd/system/${CHAIN_APP}.service > /dev/null << EOF
[Unit]
Description=${CHAIN_NAME} node service
After=network-online.target
[Service]
User=$USER
ExecStart=/usr/bin/cosmovisor run start
Restart=on-failure
RestartSec=10
LimitNOFILE=65535
Environment="DAEMON_HOME=$HOME/${CHAIN_DIR}"
Environment="DAEMON_NAME=${CHAIN_APP}"
Environment="UNSAFE_SKIP_BACKUP=true"
[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable ${CHAIN_APP}
```

### Initialize the node

```bash
MONIKER="YOUR_MONIKER_GOES_HERE"

# ln -s $HOME/${CHAIN_DIR}/cosmovisor/genesis $HOME/${CHAIN_DIR}/cosmovisor/current
# ln -s $HOME/${CHAIN_DIR}/cosmovisor/upgrades/${VERSION} $HOME/${CHAIN_DIR}/cosmovisor/current
sudo ln -s $HOME/${CHAIN_DIR}/cosmovisor/current/bin/${CHAIN_APP} /usr/local/bin/${CHAIN_APP}
${CHAIN_APP} config chain-id ${CHAIN_ID}
${CHAIN_APP} init $MONIKER --chain-id ${CHAIN_ID}
curl -Ls https://snapshots.kjnodes.com/${CHAIN_NAME}/genesis.json > $HOME/${CHAIN_DIR}/config/genesis.json
sed -i -e "s|^seeds *=.*|seeds = \"d07f430ddf0725804b3755c31660f88518547345@${CHAIN_NAME}.rpc.kjnodes.com:16659\"|" $HOME/${CHAIN_DIR}/config/config.toml
tee $HOME/${CHAIN_DIR}/data/priv_validator_state.json > /dev/null << EOF
{
  "height": "0",
  "round": 0,
  "step": 0
}
EOF
sed -i -e "s|^minimum-gas-prices *=.*|minimum-gas-prices = \"${MIN_GAS_PRICE}\"|" $HOME/${CHAIN_DIR}/config/app.toml
sed -i -e "s|^pruning *=.*|pruning = \"custom\"|" $HOME/${CHAIN_DIR}/config/app.toml
sed -i -e "s|^pruning-keep-recent *=.*|pruning-keep-recent = \"5\"|" $HOME/${CHAIN_DIR}/config/app.toml
sed -i -e "s|^pruning-keep-every *=.*|pruning-keep-every = \"0\"|" $HOME/${CHAIN_DIR}/config/app.toml
sed -i -e "s|^pruning-interval *=.*|pruning-interval = \"1000\"|" $HOME/${CHAIN_DIR}/config/app.toml
```

### Download latest chain snapshot

```bash
curl -L https://snapshots.kjnodes.com/${CHAIN_NAME}/snapshot_latest.tar.lz4 | lz4 -dc - | tar -xf - -C $HOME/${CHAIN_DIR}
```

### Start service and check the logs

```bash
sudo systemctl start ${CHAIN_APP} && journalctl -u ${CHAIN_APP} -f --no-hostname -o cat
```
