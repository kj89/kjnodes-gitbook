---
description: Setting up your validator node has never been so easy. Get your validator running in minutes by following step by step instructions.
---

# Installation

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/${PROJECT_NAME}.png" alt=""><figcaption></figcaption></figure>

**Chain ID**: ${CHAIN_ID} | **Latest Version Tag**: ${LATEST_VERSION_TAG} | **Custom Port**: ${CHAIN_PORT}

### Setup validator name

{% hint style='info' %}
Replace **YOUR_MONIKER_GOES_HERE** with your validator name
{% endhint %}

```bash
MONIKER="YOUR_MONIKER_GOES_HERE"
```

### Install dependencies

#### Update system and install build tools

```bash
sudo apt -q update
sudo apt -qy install curl git jq lz4 build-essential
sudo apt -qy upgrade
```

#### Install Go

```bash
sudo rm -rf /usr/local/go
curl -Ls https://go.dev/dl/go${GO_VERSION}.linux-amd64.tar.gz | sudo tar -xzf - -C /usr/local
eval $(echo 'export PATH=$PATH:/usr/local/go/bin' | sudo tee /etc/profile.d/golang.sh)
eval $(echo 'export PATH=$PATH:$HOME/go/bin' | tee -a $HOME/.profile)
```

### Download and build binaries

```bash
# Clone project repository
cd $HOME
rm -rf ${GIT_DIR}
git clone ${GIT_URL}
cd ${GIT_DIR}
git checkout ${LATEST_VERSION_TAG}

# Build binaries
make build

# Prepare binaries for Cosmovisor
mkdir -p $HOME/${CHAIN_DIR}/cosmovisor/genesis/bin
mv ${CHAIN_BINARY_SRC} $HOME/${CHAIN_DIR}/cosmovisor/genesis/bin/
rm -rf build

# Create application symlinks
sudo ln -s $HOME/${CHAIN_DIR}/cosmovisor/genesis $HOME/${CHAIN_DIR}/cosmovisor/current -f
sudo ln -s $HOME/${CHAIN_DIR}/cosmovisor/current/bin/${CHAIN_APP} /usr/local/bin/${CHAIN_APP} -f
```

### Install Cosmovisor and create a service

```bash
# Download and install Cosmovisor
go install cosmossdk.io/tools/cosmovisor/cmd/cosmovisor@v${COSMOVISOR_VERSION}

# Create service
sudo tee /etc/systemd/system/${CHAIN_APP}.service > /dev/null << EOF
[Unit]
Description=${CHAIN_NAME} node service
After=network-online.target

[Service]
User=$USER
ExecStart=$(which cosmovisor) run start
Restart=on-failure
RestartSec=10
LimitNOFILE=65535
Environment="DAEMON_HOME=$HOME/${CHAIN_DIR}"
Environment="DAEMON_NAME=${CHAIN_APP}"
Environment="UNSAFE_SKIP_BACKUP=true"
Environment="PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:$HOME/${CHAIN_DIR}/cosmovisor/current/bin"

[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable ${CHAIN_APP}
```

### Initialize the node

```bash
# Set node configuration
${CHAIN_APP} config chain-id ${CHAIN_ID}
${CHAIN_APP} config keyring-backend ${KEYRING_BACKEND}
${CHAIN_APP} config node tcp://localhost:${CHAIN_PORT}57

# Initialize the node
${CHAIN_APP} init $MONIKER --chain-id ${CHAIN_ID}

# Download genesis and addrbook
curl -Ls https://snapshots.kjnodes.com/${CHAIN_NAME}/genesis.json > $HOME/${CHAIN_DIR}/config/genesis.json
curl -Ls https://snapshots.kjnodes.com/${CHAIN_NAME}/addrbook.json > $HOME/${CHAIN_DIR}/config/addrbook.json

# Add seeds
sed -i -e "s|^seeds *=.*|seeds = \"${CHAIN_TENDERSEED_PEER}@${CHAIN_NAME}.rpc.kjnodes.com:${CHAIN_PORT}59\"|" $HOME/${CHAIN_DIR}/config/config.toml

# Set minimum gas price
sed -i -e "s|^minimum-gas-prices *=.*|minimum-gas-prices = \"${MIN_GAS_PRICE}\"|" $HOME/${CHAIN_DIR}/config/app.toml

# Set pruning
sed -i \
  -e 's|^pruning *=.*|pruning = "custom"|' \
  -e 's|^pruning-keep-recent *=.*|pruning-keep-recent = "100"|' \
  -e 's|^pruning-keep-every *=.*|pruning-keep-every = "0"|' \
  -e 's|^pruning-interval *=.*|pruning-interval = "19"|' \
  $HOME/${CHAIN_DIR}/config/app.toml

# Set custom ports
sed -i -e "s%^proxy_app = \"tcp://127.0.0.1:26658\"%proxy_app = \"tcp://127.0.0.1:${CHAIN_PORT}58\"%; s%^laddr = \"tcp://127.0.0.1:26657\"%laddr = \"tcp://127.0.0.1:${CHAIN_PORT}57\"%; s%^pprof_laddr = \"localhost:6060\"%pprof_laddr = \"localhost:${CHAIN_PORT}60\"%; s%^laddr = \"tcp://0.0.0.0:26656\"%laddr = \"tcp://0.0.0.0:${CHAIN_PORT}56\"%; s%^prometheus_listen_addr = \":26660\"%prometheus_listen_addr = \":${CHAIN_PORT}66\"%" $HOME/${CHAIN_DIR}/config/config.toml
sed -i -e "s%^address = \"tcp://0.0.0.0:1317\"%address = \"tcp://0.0.0.0:${CHAIN_PORT}17\"%; s%^address = \":8080\"%address = \":${CHAIN_PORT}80\"%; s%^address = \"0.0.0.0:9090\"%address = \"0.0.0.0:${CHAIN_PORT}90\"%; s%^address = \"0.0.0.0:9091\"%address = \"0.0.0.0:${CHAIN_PORT}91\"%; s%:8545%:${CHAIN_PORT}45%; s%:8546%:${CHAIN_PORT}46%; s%:6065%:${CHAIN_PORT}65%" $HOME/${CHAIN_DIR}/config/app.toml
```

### Download latest chain snapshot

```bash
curl -L https://snapshots.kjnodes.com/${CHAIN_NAME}/snapshot_latest.tar.lz4 | tar -Ilz4 -xf - -C $HOME/${CHAIN_DIR}
[[ -f $HOME/${CHAIN_DIR}/data/upgrade-info.json ]] && cp $HOME/${CHAIN_DIR}/data/upgrade-info.json $HOME/${CHAIN_DIR}/cosmovisor/genesis/upgrade-info.json
```

### Start service and check the logs

```bash
sudo systemctl start ${CHAIN_APP} && sudo journalctl -u ${CHAIN_APP} -f --no-hostname -o cat
```

# Set up a pricefeeder
{% hint style="warning" %}
To run pricefeeder you validator should be in active set. Otherwise price feeder will not vote on periods.
{% endhint %}

1. Install the pricefeeder binary
```bash
curl -s https://get.nibiru.fi/pricefeeder! | bash
```

2. Create new wallet for pricefeeder and save `24 word mnemonic phrase`
```bash
nibid keys add pricefeeder-wallet
```

3. Top up the pricefeeder-wallet going to [Nibiru Discord](https://discord.gg/nibiru) #faucet channel.
{% hint style="info" %}
In order to make pricefeeder work, it needs some testnet tokens to pay for transaction fees
{% endhint %}

4. Export pricefeeder mnemonic into environment variable
```bash
export FEEDER_MNEMONIC="my pricefeeder 24 word mnemonic phrase goes here ..."
```

5. Setup the systemd service
```bash
export CHAIN_ID="nibiru-itn-1"
export GRPC_ENDPOINT="localhost:39090"
export WEBSOCKET_ENDPOINT="ws://localhost:39657/websocket"
export EXCHANGE_SYMBOLS_MAP='{ "bitfinex": { "ubtc:uusd": "tBTCUSD", "ueth:uusd": "tETHUSD", "uusdt:uusd": "tUSTUSD" }, "binance": { "ubtc:uusd": "BTCUSD", "ueth:uusd": "ETHUSD", "uusdt:uusd": "USDTUSD", "uusdc:uusd": "USDCUSD", "uatom:uusd": "ATOMUSD", "ubnb:uusd": "BNBUSD", "uavax:uusd": "AVAXUSD", "usol:uusd": "SOLUSD", "uada:uusd": "ADAUSD", "ubtc:unusd": "BTCUSD", "ueth:unusd": "ETHUSD", "uusdt:unusd": "USDTUSD", "uusdc:unusd": "USDCUSD", "uatom:unusd": "ATOMUSD", "ubnb:unusd": "BNBUSD", "uavax:unusd": "AVAXUSD", "usol:unusd": "SOLUSD", "uada:unusd": "ADAUSD" } }'
export VALIDATOR_ADDRESS=$(nibid keys show wallet --bech val -a)

sudo tee /etc/systemd/system/pricefeeder.service<<EOF
[Unit]
Description=Nibiru Pricefeeder
Requires=network-online.target
After=network-online.target

[Service]
Type=exec
User=$USER
Group=$USER
ExecStart=/usr/local/bin/pricefeeder
Restart=on-failure
ExecReload=/bin/kill -HUP $MAINPID
KillSignal=SIGTERM
PermissionsStartOnly=true
LimitNOFILE=65535
Environment=CHAIN_ID='$CHAIN_ID'
Environment=GRPC_ENDPOINT='$GRPC_ENDPOINT'
Environment=WEBSOCKET_ENDPOINT='$WEBSOCKET_ENDPOINT'
Environment=EXCHANGE_SYMBOLS_MAP='$EXCHANGE_SYMBOLS_MAP'
Environment=FEEDER_MNEMONIC='$FEEDER_MNEMONIC'
Environment=VALIDATOR_ADDRESS='$VALIDATOR_ADDRESS'

[Install]
WantedBy=multi-user.target
EOF
```

6. Delegate pricefeeder responsibility

{% hint style="info" %}
As a validator, if you'd like another account to post prices on your behalf (i.e. you don't want your validator mnemonic sending txs), you can delegate pricefeeder responsibilities to another nibi address.
{% endhint %}

```bash
nibid tx oracle set-feeder $(nibid keys show pricefeeder-wallet -a) --from wallet
```

7. Register and start the systemd service
```bash
sudo systemctl daemon-reload && \
sudo systemctl enable pricefeeder && \
sudo systemctl start pricefeeder
```

8. View pricefeeder logs
```bash
journalctl -fu pricefeeder
```

Successfull Log examples:
```
Feb 27 19:09:33 pricefeeder[3632198]: {"level":"info","voting-period-height":405780,"tx-hash":"8FC418510A2BBFEF6E2FF17108B5D1C909B14DC0AFB22129A73C7373E649329F","time":1677521373,"message":"successfully forwarded prices"}
Feb 27 19:09:48 pricefeeder[3632198]: {"level":"info","voting-period":{"Height":405790},"time":1677521388,"message":"new voting period"}
Feb 27 19:09:48 pricefeeder[3632198]: {"level":"info","voting-period-height":405790,"vote":{"salt":"337","exchange_rates":"(unibi:unusd,0.066667000000000000)|(ubtc:unusd,23296.630000000000000000)|(ueth:unusd,1628.900000000000000000)|(uatom:unusd,12.760000000000000000)|(ubnb:unusd,301.740800000000000000)|(uusdc:unusd,0.999900000000000000)|(uusdt:unusd,1.000100000000000000)|(unibi:uusd,0.066667000000000000)|(ubtc:uusd,23314.000000000000000000)|(ueth:uusd,1629.900000000000000000)|(uatom:uusd,12.760000000000000000)|(ubnb:uusd,301.740800000000000000)|(uusdc:uusd,0.999900000000000000)|(uusdt:uusd,1.000100000000000000)","feeder":"nibi1w9d0u9ln9tx9dnn5qku9977jn2rtrupxxx0lrn","validator":"nibivaloper195w5wxp8hgqgz7schdukq7u5kadc2tnrsc00a0"},"time":1677521388,"message":"prepared vote message"}
Feb 27 19:09:50 pricefeeder[3632198]: {"level":"info","voting-period-height":405790,"tx-hash":"ACB94C8421AE056468BDAAE68655D86CEB87FB6881A526A31A7A2E98234C8D13","time":1677521390,"message":"successfully forwarded prices"}
Feb 27 19:10:05 pricefeeder[3632198]: {"level":"info","voting-period":{"Height":405800},"time":1677521405,"message":"new voting period"}
Feb 27 19:10:05 pricefeeder[3632198]: {"level":"info","voting-period-height":405800,"vote":{"salt":"3334","exchange_rates":"(unibi:unusd,0.066667000000000000)|(ubtc:unusd,23296.680000000000000000)|(ueth:unusd,1628.780000000000000000)|(uatom:unusd,12.760000000000000000)|(ubnb:unusd,301.740800000000000000)|(uusdc:unusd,0.999900000000000000)|(uusdt:unusd,1.000100000000000000)|(unibi:uusd,0.066667000000000000)|(ubtc:uusd,23296.680000000000000000)|(ueth:uusd,1628.780000000000000000)|(uatom:uusd,12.760000000000000000)|(ubnb:uusd,301.740800000000000000)|(uusdc:uusd,0.999900000000000000)|(uusdt:uusd,1.000100000000000000)","feeder":"nibi1w9d0u9ln9tx9dnn5qku9977jn2rtrupxxx0lrn","validator":"nibivaloper195w5wxp8hgqgz7schdukq7u5kadc2tnrsc00a0"},"time":1677521405,"message":"prepared vote message"}
Feb 27 19:10:06 pricefeeder[3632198]: {"level":"info","voting-period-height":405800,"tx-hash":"1E85AD6307DD8D734AAB6565CC57FB09F0EA0F7CFE0B8EE8AB50FC8A08B4111A","time":1677521406,"message":"successfully forwarded prices"}
Feb 27 19:10:22 pricefeeder[3632198]: {"level":"info","voting-period":{"Height":405810},"time":1677521422,"message":"new voting period"}
Feb 27 19:10:22 pricefeeder[3632198]: {"level":"info","voting-period-height":405810,"vote":{"salt":"9672","exchange_rates":"(unibi:unusd,0.066667000000000000)|(ubtc:unusd,23310.000000000000000000)|(ueth:unusd,1630.010000000000000000)|(uatom:unusd,12.760000000000000000)|(ubnb:unusd,301.737500000000000000)|(uusdc:unusd,0.999900000000000000)|(uusdt:unusd,1.000000000000000000)|(unibi:uusd,0.066667000000000000)|(ubtc:uusd,23307.000000000000000000)|(ueth:uusd,1629.200000000000000000)|(uatom:uusd,12.760000000000000000)|(ubnb:uusd,301.737500000000000000)|(uusdc:uusd,0.999900000000000000)|(uusdt:uusd,1.000000000000000000)","feeder":"nibi1w9d0u9ln9tx9dnn5qku9977jn2rtrupxxx0lrn","validator":"nibivaloper195w5wxp8hgqgz7schdukq7u5kadc2tnrsc00a0"},"time":1677521422,"message":"prepared vote message"}
Feb 27 19:10:23 pricefeeder[3632198]: {"level":"info","voting-period-height":405810,"tx-hash":"24B3B16FB8B6B047885928FB6A254D7B0B44E17E0DC6AF37B1F077F78C7099A9","time":1677521423,"message":"successfully forwarded prices"}
```

Also you can check that your pricefeeder-wallet is doing transactions on chain at [Chain Explorer](https://explorer.kjnodes.com/nibiru-testnet)
<figure><img src="https://i.ibb.co/748MW95/pricefeeder-transactions.png" alt=""><figcaption><p>Price Feeder Transactions</p></figcaption></figure>
