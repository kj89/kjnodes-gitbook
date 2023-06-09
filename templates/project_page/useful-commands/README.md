---
description: Useful set of commands for node operators. From key management to chain governance.
---

# Useful commands

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/${PROJECT_NAME}.png" alt=""><figcaption></figcaption></figure>

## 🔑 Key management

#### Add new key

```bash
${CHAIN_APP} keys add wallet
```

#### Recover existing key

```bash
${CHAIN_APP} keys add wallet --recover
```

#### List all keys

```bash
${CHAIN_APP} keys list
```

#### Delete key

```bash
${CHAIN_APP} keys delete wallet
```

#### Export key to the file

```bash
${CHAIN_APP} keys export wallet
```

#### Import key from the file

```bash
${CHAIN_APP} keys import wallet wallet.backup
```

#### Query wallet balance

```bash
${CHAIN_APP} q bank balances $(${CHAIN_APP} keys show wallet -a)
```

## 👷 Validator management

{% hint style="info" %}
Please make sure you have adjusted **moniker**, **identity**, **details** and **website** to match your values.
{% endhint %}

#### Create new validator

```bash
${CHAIN_APP} tx staking create-validator \
--amount 1000000${CHAIN_DENOM} \
--pubkey $(${CHAIN_APP} tendermint show-validator) \
--moniker "YOUR_MONIKER_NAME" \
--identity "YOUR_KEYBASE_ID" \
--details "YOUR_DETAILS" \
--website "YOUR_WEBSITE_URL" \
--chain-id ${CHAIN_ID} \
--commission-rate 0.05 \
--commission-max-rate 0.20 \
--commission-max-change-rate 0.01 \
--min-self-delegation 1 \
--from wallet \
--gas-adjustment 1.4 \
--gas auto \
--gas-prices ${TX_MIN_GAS_PRICE} \
-y
```

#### Edit existing validator

```bash
${CHAIN_APP} tx staking edit-validator \
--new-moniker "YOUR_MONIKER_NAME" \
--identity "YOUR_KEYBASE_ID" \
--details "YOUR_DETAILS" \
--website "YOUR_WEBSITE_URL" \
--chain-id ${CHAIN_ID} \
--commission-rate 0.05 \
--from wallet \
--gas-adjustment 1.4 \
--gas auto \
--gas-prices ${TX_MIN_GAS_PRICE} \
-y
```

#### Unjail validator

```bash
${CHAIN_APP} tx slashing unjail --from wallet --chain-id ${CHAIN_ID} --gas-adjustment 1.4 --gas auto --gas-prices ${TX_MIN_GAS_PRICE} -y
```

#### Jail reason

```bash
${CHAIN_APP} query slashing signing-info $(${CHAIN_APP} tendermint show-validator)
```

#### List all active validators

```bash
${CHAIN_APP} q staking validators -oj --limit=3000 | jq '.validators[] | select(.status=="BOND_STATUS_BONDED")' | jq -r '(.tokens|tonumber/pow(10; 6)|floor|tostring) + " \t " + .description.moniker' | sort -gr | nl
```

#### List all inactive validators

```bash
${CHAIN_APP} q staking validators -oj --limit=3000 | jq '.validators[] | select(.status=="BOND_STATUS_UNBONDED")' | jq -r '(.tokens|tonumber/pow(10; 6)|floor|tostring) + " \t " + .description.moniker' | sort -gr | nl
```

#### View validator details

```bash
${CHAIN_APP} q staking validator $(${CHAIN_APP} keys show wallet --bech val -a)
```

## 💲 Token management

#### Withdraw rewards from all validators

```bash
${CHAIN_APP} tx distribution withdraw-all-rewards --from wallet --chain-id ${CHAIN_ID} --gas-adjustment 1.4 --gas auto --gas-prices ${TX_MIN_GAS_PRICE} -y
```

#### Withdraw commission and rewards from your validator

```bash
${CHAIN_APP} tx distribution withdraw-rewards $(${CHAIN_APP} keys show wallet --bech val -a) --commission --from wallet --chain-id ${CHAIN_ID} --gas-adjustment 1.4 --gas auto --gas-prices ${TX_MIN_GAS_PRICE} -y
```

#### Delegate tokens to yourself

```bash
${CHAIN_APP} tx staking delegate $(${CHAIN_APP} keys show wallet --bech val -a) 1000000${CHAIN_DENOM} --from wallet --chain-id ${CHAIN_ID} --gas-adjustment 1.4 --gas auto --gas-prices ${TX_MIN_GAS_PRICE} -y
```

#### Delegate tokens to validator

```bash
${CHAIN_APP} tx staking delegate <TO_VALOPER_ADDRESS> 1000000${CHAIN_DENOM} --from wallet --chain-id ${CHAIN_ID} --gas-adjustment 1.4 --gas auto --gas-prices ${TX_MIN_GAS_PRICE} -y
```

#### Redelegate tokens to another validator

```bash
${CHAIN_APP} tx staking redelegate $(${CHAIN_APP} keys show wallet --bech val -a) <TO_VALOPER_ADDRESS> 1000000${CHAIN_DENOM} --from wallet --chain-id ${CHAIN_ID} --gas-adjustment 1.4 --gas auto --gas-prices ${TX_MIN_GAS_PRICE} -y
```

#### Unbond tokens from your validator

```bash
${CHAIN_APP} tx staking unbond $(${CHAIN_APP} keys show wallet --bech val -a) 1000000${CHAIN_DENOM} --from wallet --chain-id ${CHAIN_ID} --gas-adjustment 1.4 --gas auto --gas-prices ${TX_MIN_GAS_PRICE} -y
```

#### Send tokens to the wallet

```bash
${CHAIN_APP} tx bank send wallet <TO_WALLET_ADDRESS> 1000000${CHAIN_DENOM} --from wallet --chain-id ${CHAIN_ID} --gas-adjustment 1.4 --gas auto --gas-prices ${TX_MIN_GAS_PRICE} -y
```

## 🗳 Governance

#### List all proposals

```bash
${CHAIN_APP} query gov proposals
```

#### View proposal by id

```bash
${CHAIN_APP} query gov proposal 1
```

#### Vote 'Yes'

```bash
${CHAIN_APP} tx gov vote 1 yes --from wallet --chain-id ${CHAIN_ID} --gas-adjustment 1.4 --gas auto --gas-prices ${TX_MIN_GAS_PRICE} -y
```

#### Vote 'No'

```bash
${CHAIN_APP} tx gov vote 1 no --from wallet --chain-id ${CHAIN_ID} --gas-adjustment 1.4 --gas auto --gas-prices ${TX_MIN_GAS_PRICE} -y
```

#### Vote 'Abstain'

```bash
${CHAIN_APP} tx gov vote 1 abstain --from wallet --chain-id ${CHAIN_ID} --gas-adjustment 1.4 --gas auto --gas-prices ${TX_MIN_GAS_PRICE} -y
```

#### Vote 'NoWithVeto'

```bash
${CHAIN_APP} tx gov vote 1 NoWithVeto --from wallet --chain-id ${CHAIN_ID} --gas-adjustment 1.4 --gas auto --gas-prices ${TX_MIN_GAS_PRICE} -y
```

## ⚡️ Utility

#### Update ports

```bash
CUSTOM_PORT=110
sed -i -e "s%^proxy_app = \"tcp://127.0.0.1:26658\"%proxy_app = \"tcp://127.0.0.1:${CUSTOM_PORT}58\"%; s%^laddr = \"tcp://127.0.0.1:26657\"%laddr = \"tcp://127.0.0.1:${CUSTOM_PORT}57\"%; s%^pprof_laddr = \"localhost:6060\"%pprof_laddr = \"localhost:${CUSTOM_PORT}60\"%; s%^laddr = \"tcp://0.0.0.0:26656\"%laddr = \"tcp://0.0.0.0:${CUSTOM_PORT}56\"%; s%^prometheus_listen_addr = \":26660\"%prometheus_listen_addr = \":${CUSTOM_PORT}66\"%" $HOME/${CHAIN_DIR}/config/config.toml
sed -i -e "s%^address = \"tcp://0.0.0.0:1317\"%address = \"tcp://0.0.0.0:${CUSTOM_PORT}17\"%; s%^address = \":8080\"%address = \":${CUSTOM_PORT}80\"%; s%^address = \"0.0.0.0:9090\"%address = \"0.0.0.0:${CUSTOM_PORT}90\"%; s%^address = \"0.0.0.0:9091\"%address = \"0.0.0.0:${CUSTOM_PORT}91\"%" $HOME/${CHAIN_DIR}/config/app.toml
```

#### Update Indexer

**Disable indexer**

```bash
sed -i -e 's|^indexer *=.*|indexer = "null"|' $HOME/${CHAIN_DIR}/config/config.toml
```

**Enable indexer**

```bash
sed -i -e 's|^indexer *=.*|indexer = "kv"|' $HOME/${CHAIN_DIR}/config/config.toml
```

#### Update pruning

```bash
sed -i \
  -e 's|^pruning *=.*|pruning = "custom"|' \
  -e 's|^pruning-keep-recent *=.*|pruning-keep-recent = "100"|' \
  -e 's|^pruning-keep-every *=.*|pruning-keep-every = "0"|' \
  -e 's|^pruning-interval *=.*|pruning-interval = "19"|' \
  $HOME/${CHAIN_DIR}/config/app.toml
```

## 🚨 Maintenance

#### Get validator info

```bash
${CHAIN_APP} status 2>&1 | jq .ValidatorInfo
```

#### Get sync info

```bash
${CHAIN_APP} status 2>&1 | jq .SyncInfo
```

#### Get node peer

```bash
echo $(${CHAIN_APP} tendermint show-node-id)'@'$(curl -s ifconfig.me)':'$(cat $HOME/${CHAIN_DIR}/config/config.toml | sed -n '/Address to listen for incoming connection/{n;p;}' | sed 's/.*://; s/".*//')
```

#### Check if validator key is correct

```bash
[[ $(${CHAIN_APP} q staking validator $(${CHAIN_APP} keys show wallet --bech val -a) -oj | jq -r .consensus_pubkey.key) = $(${CHAIN_APP} status | jq -r .ValidatorInfo.PubKey.value) ]] && echo -e "\n\e[1m\e[32mTrue\e[0m\n" || echo -e "\n\e[1m\e[31mFalse\e[0m\n"
```

#### Get live peers

```bash
curl -sS http://localhost:${CHAIN_PORT}57/net_info | jq -r '.result.peers[] | "\(.node_info.id)@\(.remote_ip):\(.node_info.listen_addr)"' | awk -F ':' '{print $1":"$(NF)}'
```

#### Set minimum gas price

```bash
sed -i -e "s/^minimum-gas-prices *=.*/minimum-gas-prices = \"${MIN_GAS_PRICE}\"/" $HOME/${CHAIN_DIR}/config/app.toml
```

#### Enable prometheus

```bash
sed -i -e "s/prometheus = false/prometheus = true/" $HOME/${CHAIN_DIR}/config/config.toml
```

#### Reset chain data

```bash
${CHAIN_APP} tendermint unsafe-reset-all --keep-addr-book --home $HOME/${CHAIN_DIR} --keep-addr-book
```

#### Remove node

{% hint style='danger' %}
Please, before proceeding with the next step! All chain data will be lost! Make sure you have backed up your **priv_validator_key.json**!
{% endhint %}

```bash
cd $HOME
sudo systemctl stop ${CHAIN_APP}
sudo systemctl disable ${CHAIN_APP}
sudo rm /etc/systemd/system/${CHAIN_APP}.service
sudo systemctl daemon-reload
rm -f $(which ${CHAIN_APP})
rm -rf $HOME/${CHAIN_DIR}
rm -rf $HOME/${GIT_DIR}
```

## ⚙️ Service Management

#### Reload service configuration

```bash
sudo systemctl daemon-reload
```

#### Enable service

```bash
sudo systemctl enable ${CHAIN_APP}
```

#### Disable service

```bash
sudo systemctl disable ${CHAIN_APP}
```

#### Start service

```bash
sudo systemctl start ${CHAIN_APP}
```

#### Stop service

```bash
sudo systemctl stop ${CHAIN_APP}
```

#### Restart service

```bash
sudo systemctl restart ${CHAIN_APP}
```

#### Check service status

```bash
sudo systemctl status ${CHAIN_APP}
```

#### Check service logs

```bash
sudo journalctl -u ${CHAIN_APP} -f --no-hostname -o cat
```
