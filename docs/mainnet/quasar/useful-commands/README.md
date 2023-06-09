---
description: Useful set of commands for node operators. From key management to chain governance.
---

# Useful commands

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/quasar.png" alt=""><figcaption></figcaption></figure>

## 🔑 Key management

#### Add new key

```bash
quasarnoded keys add wallet
```

#### Recover existing key

```bash
quasarnoded keys add wallet --recover
```

#### List all keys

```bash
quasarnoded keys list
```

#### Delete key

```bash
quasarnoded keys delete wallet
```

#### Export key to the file

```bash
quasarnoded keys export wallet
```

#### Import key from the file

```bash
quasarnoded keys import wallet wallet.backup
```

#### Query wallet balance

```bash
quasarnoded q bank balances $(quasarnoded keys show wallet -a)
```

## 👷 Validator management

{% hint style="info" %}
Please make sure you have adjusted **moniker**, **identity**, **details** and **website** to match your values.
{% endhint %}

#### Create new validator

```bash
quasarnoded tx staking create-validator \
--amount 1000000uqsr \
--pubkey $(quasarnoded tendermint show-validator) \
--moniker "YOUR_MONIKER_NAME" \
--identity "YOUR_KEYBASE_ID" \
--details "YOUR_DETAILS" \
--website "YOUR_WEBSITE_URL" \
--chain-id quasar-1 \
--commission-rate 0.05 \
--commission-max-rate 0.20 \
--commission-max-change-rate 0.01 \
--min-self-delegation 1 \
--from wallet \
--gas-adjustment 1.4 \
--gas auto \
--gas-prices 0.01ibc/0471F1C4E7AFD3F07702BEF6DC365268D64570F7C1FDC98EA6098DD6DE59817B \
-y
```

#### Edit existing validator

```bash
quasarnoded tx staking edit-validator \
--new-moniker "YOUR_MONIKER_NAME" \
--identity "YOUR_KEYBASE_ID" \
--details "YOUR_DETAILS" \
--website "YOUR_WEBSITE_URL" \
--chain-id quasar-1 \
--commission-rate 0.05 \
--from wallet \
--gas-adjustment 1.4 \
--gas auto \
--gas-prices 0.01ibc/0471F1C4E7AFD3F07702BEF6DC365268D64570F7C1FDC98EA6098DD6DE59817B \
-y
```

#### Unjail validator

```bash
quasarnoded tx slashing unjail --from wallet --chain-id quasar-1 --gas-adjustment 1.4 --gas auto --gas-prices 0.01ibc/0471F1C4E7AFD3F07702BEF6DC365268D64570F7C1FDC98EA6098DD6DE59817B -y
```

#### Jail reason

```bash
quasarnoded query slashing signing-info $(quasarnoded tendermint show-validator)
```

#### List all active validators

```bash
quasarnoded q staking validators -oj --limit=3000 | jq '.validators[] | select(.status=="BOND_STATUS_BONDED")' | jq -r '(.tokens|tonumber/pow(10; 6)|floor|tostring) + " \t " + .description.moniker' | sort -gr | nl
```

#### List all inactive validators

```bash
quasarnoded q staking validators -oj --limit=3000 | jq '.validators[] | select(.status=="BOND_STATUS_UNBONDED")' | jq -r '(.tokens|tonumber/pow(10; 6)|floor|tostring) + " \t " + .description.moniker' | sort -gr | nl
```

#### View validator details

```bash
quasarnoded q staking validator $(quasarnoded keys show wallet --bech val -a)
```

## 💲 Token management

#### Withdraw rewards from all validators

```bash
quasarnoded tx distribution withdraw-all-rewards --from wallet --chain-id quasar-1 --gas-adjustment 1.4 --gas auto --gas-prices 0.01ibc/0471F1C4E7AFD3F07702BEF6DC365268D64570F7C1FDC98EA6098DD6DE59817B -y
```

#### Withdraw commission and rewards from your validator

```bash
quasarnoded tx distribution withdraw-rewards $(quasarnoded keys show wallet --bech val -a) --commission --from wallet --chain-id quasar-1 --gas-adjustment 1.4 --gas auto --gas-prices 0.01ibc/0471F1C4E7AFD3F07702BEF6DC365268D64570F7C1FDC98EA6098DD6DE59817B -y
```

#### Delegate tokens to yourself

```bash
quasarnoded tx staking delegate $(quasarnoded keys show wallet --bech val -a) 1000000uqsr --from wallet --chain-id quasar-1 --gas-adjustment 1.4 --gas auto --gas-prices 0.01ibc/0471F1C4E7AFD3F07702BEF6DC365268D64570F7C1FDC98EA6098DD6DE59817B -y
```

#### Delegate tokens to validator

```bash
quasarnoded tx staking delegate <TO_VALOPER_ADDRESS> 1000000uqsr --from wallet --chain-id quasar-1 --gas-adjustment 1.4 --gas auto --gas-prices 0.01ibc/0471F1C4E7AFD3F07702BEF6DC365268D64570F7C1FDC98EA6098DD6DE59817B -y
```

#### Redelegate tokens to another validator

```bash
quasarnoded tx staking redelegate $(quasarnoded keys show wallet --bech val -a) <TO_VALOPER_ADDRESS> 1000000uqsr --from wallet --chain-id quasar-1 --gas-adjustment 1.4 --gas auto --gas-prices 0.01ibc/0471F1C4E7AFD3F07702BEF6DC365268D64570F7C1FDC98EA6098DD6DE59817B -y
```

#### Unbond tokens from your validator

```bash
quasarnoded tx staking unbond $(quasarnoded keys show wallet --bech val -a) 1000000uqsr --from wallet --chain-id quasar-1 --gas-adjustment 1.4 --gas auto --gas-prices 0.01ibc/0471F1C4E7AFD3F07702BEF6DC365268D64570F7C1FDC98EA6098DD6DE59817B -y
```

#### Send tokens to the wallet

```bash
quasarnoded tx bank send wallet <TO_WALLET_ADDRESS> 1000000uqsr --from wallet --chain-id quasar-1 --gas-adjustment 1.4 --gas auto --gas-prices 0.01ibc/0471F1C4E7AFD3F07702BEF6DC365268D64570F7C1FDC98EA6098DD6DE59817B -y
```

## 🗳 Governance

#### List all proposals

```bash
quasarnoded query gov proposals
```

#### View proposal by id

```bash
quasarnoded query gov proposal 1
```

#### Vote 'Yes'

```bash
quasarnoded tx gov vote 1 yes --from wallet --chain-id quasar-1 --gas-adjustment 1.4 --gas auto --gas-prices 0.01ibc/0471F1C4E7AFD3F07702BEF6DC365268D64570F7C1FDC98EA6098DD6DE59817B -y
```

#### Vote 'No'

```bash
quasarnoded tx gov vote 1 no --from wallet --chain-id quasar-1 --gas-adjustment 1.4 --gas auto --gas-prices 0.01ibc/0471F1C4E7AFD3F07702BEF6DC365268D64570F7C1FDC98EA6098DD6DE59817B -y
```

#### Vote 'Abstain'

```bash
quasarnoded tx gov vote 1 abstain --from wallet --chain-id quasar-1 --gas-adjustment 1.4 --gas auto --gas-prices 0.01ibc/0471F1C4E7AFD3F07702BEF6DC365268D64570F7C1FDC98EA6098DD6DE59817B -y
```

#### Vote 'NoWithVeto'

```bash
quasarnoded tx gov vote 1 NoWithVeto --from wallet --chain-id quasar-1 --gas-adjustment 1.4 --gas auto --gas-prices 0.01ibc/0471F1C4E7AFD3F07702BEF6DC365268D64570F7C1FDC98EA6098DD6DE59817B -y
```

## ⚡️ Utility

#### Update ports

```bash
CUSTOM_PORT=110
sed -i -e "s%^proxy_app = \"tcp://127.0.0.1:26658\"%proxy_app = \"tcp://127.0.0.1:${CUSTOM_PORT}58\"%; s%^laddr = \"tcp://127.0.0.1:26657\"%laddr = \"tcp://127.0.0.1:${CUSTOM_PORT}57\"%; s%^pprof_laddr = \"localhost:6060\"%pprof_laddr = \"localhost:${CUSTOM_PORT}60\"%; s%^laddr = \"tcp://0.0.0.0:26656\"%laddr = \"tcp://0.0.0.0:${CUSTOM_PORT}56\"%; s%^prometheus_listen_addr = \":26660\"%prometheus_listen_addr = \":${CUSTOM_PORT}66\"%" $HOME/.quasarnode/config/config.toml
sed -i -e "s%^address = \"tcp://0.0.0.0:1317\"%address = \"tcp://0.0.0.0:${CUSTOM_PORT}17\"%; s%^address = \":8080\"%address = \":${CUSTOM_PORT}80\"%; s%^address = \"0.0.0.0:9090\"%address = \"0.0.0.0:${CUSTOM_PORT}90\"%; s%^address = \"0.0.0.0:9091\"%address = \"0.0.0.0:${CUSTOM_PORT}91\"%" $HOME/.quasarnode/config/app.toml
```

#### Update Indexer

**Disable indexer**

```bash
sed -i -e 's|^indexer *=.*|indexer = "null"|' $HOME/.quasarnode/config/config.toml
```

**Enable indexer**

```bash
sed -i -e 's|^indexer *=.*|indexer = "kv"|' $HOME/.quasarnode/config/config.toml
```

#### Update pruning

```bash
sed -i \
  -e 's|^pruning *=.*|pruning = "custom"|' \
  -e 's|^pruning-keep-recent *=.*|pruning-keep-recent = "100"|' \
  -e 's|^pruning-keep-every *=.*|pruning-keep-every = "0"|' \
  -e 's|^pruning-interval *=.*|pruning-interval = "19"|' \
  $HOME/.quasarnode/config/app.toml
```

## 🚨 Maintenance

#### Get validator info

```bash
quasarnoded status 2>&1 | jq .ValidatorInfo
```

#### Get sync info

```bash
quasarnoded status 2>&1 | jq .SyncInfo
```

#### Get node peer

```bash
echo $(quasarnoded tendermint show-node-id)'@'$(curl -s ifconfig.me)':'$(cat $HOME/.quasarnode/config/config.toml | sed -n '/Address to listen for incoming connection/{n;p;}' | sed 's/.*://; s/".*//')
```

#### Check if validator key is correct

```bash
[[ $(quasarnoded q staking validator $(quasarnoded keys show wallet --bech val -a) -oj | jq -r .consensus_pubkey.key) = $(quasarnoded status | jq -r .ValidatorInfo.PubKey.value) ]] && echo -e "\n\e[1m\e[32mTrue\e[0m\n" || echo -e "\n\e[1m\e[31mFalse\e[0m\n"
```

#### Get live peers

```bash
curl -sS http://localhost:14857/net_info | jq -r '.result.peers[] | "\(.node_info.id)@\(.remote_ip):\(.node_info.listen_addr)"' | awk -F ':' '{print $1":"$(NF)}'
```

#### Set minimum gas price

```bash
sed -i -e "s/^minimum-gas-prices *=.*/minimum-gas-prices = \"0.01ibc/0471F1C4E7AFD3F07702BEF6DC365268D64570F7C1FDC98EA6098DD6DE59817B,0.01ibc/FA0006F056DB6719B8C16C551FC392B62F5729978FC0B125AC9A432DBB2AA1A5,0.01ibc/FA7775734CC73176B7425910DE001A1D2AD9B6D9E93129A5D0750EAD13E4E63A\"/" $HOME/.quasarnode/config/app.toml
```

#### Enable prometheus

```bash
sed -i -e "s/prometheus = false/prometheus = true/" $HOME/.quasarnode/config/config.toml
```

#### Reset chain data

```bash
quasarnoded tendermint unsafe-reset-all --keep-addr-book --home $HOME/.quasarnode --keep-addr-book
```

#### Remove node

{% hint style='danger' %}
Please, before proceeding with the next step! All chain data will be lost! Make sure you have backed up your **priv_validator_key.json**!
{% endhint %}

```bash
cd $HOME
sudo systemctl stop quasarnoded
sudo systemctl disable quasarnoded
sudo rm /etc/systemd/system/quasarnoded.service
sudo systemctl daemon-reload
rm -f $(which quasarnoded)
rm -rf $HOME/.quasarnode
rm -rf $HOME/quasar-preview
```

## ⚙️ Service Management

#### Reload service configuration

```bash
sudo systemctl daemon-reload
```

#### Enable service

```bash
sudo systemctl enable quasarnoded
```

#### Disable service

```bash
sudo systemctl disable quasarnoded
```

#### Start service

```bash
sudo systemctl start quasarnoded
```

#### Stop service

```bash
sudo systemctl stop quasarnoded
```

#### Restart service

```bash
sudo systemctl restart quasarnoded
```

#### Check service status

```bash
sudo systemctl status quasarnoded
```

#### Check service logs

```bash
sudo journalctl -u quasarnoded -f --no-hostname -o cat
```
