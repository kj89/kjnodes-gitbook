---
description: Useful set of commands for node operators. From key management to chain governance.
---

# Useful commands

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/paloma.png" alt=""><figcaption></figcaption></figure>

## 🔑 Key management

#### Add new key

```bash
palomad keys add wallet
```

#### Recover existing key

```bash
palomad keys add wallet --recover
```

#### List all keys

```bash
palomad keys list
```

#### Delete key

```bash
palomad keys delete wallet
```

#### Export key to the file

```bash
palomad keys export wallet
```

#### Import key from the file

```bash
palomad keys import wallet wallet.backup
```

#### Query wallet balance

```bash
palomad q bank balances $(palomad keys show wallet -a)
```

## 👷 Validator management

{% hint style="info" %}
Please make sure you have adjusted **moniker**, **identity**, **details** and **website** to match your values.
{% endhint %}

#### Create new validator

```bash
palomad tx staking create-validator \
--amount 1000000ugrain \
--pubkey $(palomad tendermint show-validator) \
--moniker "YOUR_MONIKER_NAME" \
--identity "YOUR_KEYBASE_ID" \
--details "YOUR_DETAILS" \
--website "YOUR_WEBSITE_URL" \
--chain-id messenger \
--commission-rate 0.05 \
--commission-max-rate 0.20 \
--commission-max-change-rate 0.01 \
--min-self-delegation 1 \
--from wallet \
--gas-adjustment 1.4 \
--gas auto \
--gas-prices 0ugrain \
-y
```

#### Edit existing validator

```bash
palomad tx staking edit-validator \
--new-moniker "YOUR_MONIKER_NAME" \
--identity "YOUR_KEYBASE_ID" \
--details "YOUR_DETAILS" \
--website "YOUR_WEBSITE_URL" \
--chain-id messenger \
--commission-rate 0.05 \
--from wallet \
--gas-adjustment 1.4 \
--gas auto \
--gas-prices 0ugrain \
-y
```

#### Unjail validator

```bash
palomad tx slashing unjail --from wallet --chain-id messenger --gas-adjustment 1.4 --gas auto --gas-prices 0ugrain -y
```

#### Jail reason

```bash
palomad query slashing signing-info $(palomad tendermint show-validator)
```

#### List all active validators

```bash
palomad q staking validators -oj --limit=3000 | jq '.validators[] | select(.status=="BOND_STATUS_BONDED")' | jq -r '(.tokens|tonumber/pow(10; 6)|floor|tostring) + " \t " + .description.moniker' | sort -gr | nl
```

#### List all inactive validators

```bash
palomad q staking validators -oj --limit=3000 | jq '.validators[] | select(.status=="BOND_STATUS_UNBONDED")' | jq -r '(.tokens|tonumber/pow(10; 6)|floor|tostring) + " \t " + .description.moniker' | sort -gr | nl
```

#### View validator details

```bash
palomad q staking validator $(palomad keys show wallet --bech val -a)
```

## 💲 Token management

#### Withdraw rewards from all validators

```bash
palomad tx distribution withdraw-all-rewards --from wallet --chain-id messenger --gas-adjustment 1.4 --gas auto --gas-prices 0ugrain -y
```

#### Withdraw commission and rewards from your validator

```bash
palomad tx distribution withdraw-rewards $(palomad keys show wallet --bech val -a) --commission --from wallet --chain-id messenger --gas-adjustment 1.4 --gas auto --gas-prices 0ugrain -y
```

#### Delegate tokens to yourself

```bash
palomad tx staking delegate $(palomad keys show wallet --bech val -a) 1000000ugrain --from wallet --chain-id messenger --gas-adjustment 1.4 --gas auto --gas-prices 0ugrain -y
```

#### Delegate tokens to validator

```bash
palomad tx staking delegate <TO_VALOPER_ADDRESS> 1000000ugrain --from wallet --chain-id messenger --gas-adjustment 1.4 --gas auto --gas-prices 0ugrain -y
```

#### Redelegate tokens to another validator

```bash
palomad tx staking redelegate $(palomad keys show wallet --bech val -a) <TO_VALOPER_ADDRESS> 1000000ugrain --from wallet --chain-id messenger --gas-adjustment 1.4 --gas auto --gas-prices 0ugrain -y
```

#### Unbond tokens from your validator

```bash
palomad tx staking unbond $(palomad keys show wallet --bech val -a) 1000000ugrain --from wallet --chain-id messenger --gas-adjustment 1.4 --gas auto --gas-prices 0ugrain -y
```

#### Send tokens to the wallet

```bash
palomad tx bank send wallet <TO_WALLET_ADDRESS> 1000000ugrain --from wallet --chain-id messenger --gas-adjustment 1.4 --gas auto --gas-prices 0ugrain -y
```

## 🗳 Governance

#### List all proposals

```bash
palomad query gov proposals
```

#### View proposal by id

```bash
palomad query gov proposal 1
```

#### Vote 'Yes'

```bash
palomad tx gov vote 1 yes --from wallet --chain-id messenger --gas-adjustment 1.4 --gas auto --gas-prices 0ugrain -y
```

#### Vote 'No'

```bash
palomad tx gov vote 1 no --from wallet --chain-id messenger --gas-adjustment 1.4 --gas auto --gas-prices 0ugrain -y
```

#### Vote 'Abstain'

```bash
palomad tx gov vote 1 abstain --from wallet --chain-id messenger --gas-adjustment 1.4 --gas auto --gas-prices 0ugrain -y
```

#### Vote 'NoWithVeto'

```bash
palomad tx gov vote 1 NoWithVeto --from wallet --chain-id messenger --gas-adjustment 1.4 --gas auto --gas-prices 0ugrain -y
```

## ⚡️ Utility

#### Update ports

```bash
CUSTOM_PORT=110
sed -i -e "s%^proxy_app = \"tcp://127.0.0.1:26658\"%proxy_app = \"tcp://127.0.0.1:${CUSTOM_PORT}58\"%; s%^laddr = \"tcp://127.0.0.1:26657\"%laddr = \"tcp://127.0.0.1:${CUSTOM_PORT}57\"%; s%^pprof_laddr = \"localhost:6060\"%pprof_laddr = \"localhost:${CUSTOM_PORT}60\"%; s%^laddr = \"tcp://0.0.0.0:26656\"%laddr = \"tcp://0.0.0.0:${CUSTOM_PORT}56\"%; s%^prometheus_listen_addr = \":26660\"%prometheus_listen_addr = \":${CUSTOM_PORT}66\"%" $HOME/.paloma/config/config.toml
sed -i -e "s%^address = \"tcp://0.0.0.0:1317\"%address = \"tcp://0.0.0.0:${CUSTOM_PORT}17\"%; s%^address = \":8080\"%address = \":${CUSTOM_PORT}80\"%; s%^address = \"0.0.0.0:9090\"%address = \"0.0.0.0:${CUSTOM_PORT}90\"%; s%^address = \"0.0.0.0:9091\"%address = \"0.0.0.0:${CUSTOM_PORT}91\"%" $HOME/.paloma/config/app.toml
```

#### Update Indexer

**Disable indexer**

```bash
sed -i -e 's|^indexer *=.*|indexer = "null"|' $HOME/.paloma/config/config.toml
```

**Enable indexer**

```bash
sed -i -e 's|^indexer *=.*|indexer = "kv"|' $HOME/.paloma/config/config.toml
```

#### Update pruning

```bash
sed -i \
  -e 's|^pruning *=.*|pruning = "custom"|' \
  -e 's|^pruning-keep-recent *=.*|pruning-keep-recent = "100"|' \
  -e 's|^pruning-keep-every *=.*|pruning-keep-every = "0"|' \
  -e 's|^pruning-interval *=.*|pruning-interval = "19"|' \
  $HOME/.paloma/config/app.toml
```

## 🚨 Maintenance

#### Get validator info

```bash
palomad status 2>&1 | jq .ValidatorInfo
```

#### Get sync info

```bash
palomad status 2>&1 | jq .SyncInfo
```

#### Get node peer

```bash
echo $(palomad tendermint show-node-id)'@'$(curl -s ifconfig.me)':'$(cat $HOME/.paloma/config/config.toml | sed -n '/Address to listen for incoming connection/{n;p;}' | sed 's/.*://; s/".*//')
```

#### Check if validator key is correct

```bash
[[ $(palomad q staking validator $(palomad keys show wallet --bech val -a) -oj | jq -r .consensus_pubkey.key) = $(palomad status | jq -r .ValidatorInfo.PubKey.value) ]] && echo -e "\n\e[1m\e[32mTrue\e[0m\n" || echo -e "\n\e[1m\e[31mFalse\e[0m\n"
```

#### Get live peers

```bash
curl -sS http://localhost:11057/net_info | jq -r '.result.peers[] | "\(.node_info.id)@\(.remote_ip):\(.node_info.listen_addr)"' | awk -F ':' '{print $1":"$(NF)}'
```

#### Set minimum gas price

```bash
sed -i -e "s/^minimum-gas-prices *=.*/minimum-gas-prices = \"0ugrain\"/" $HOME/.paloma/config/app.toml
```

#### Enable prometheus

```bash
sed -i -e "s/prometheus = false/prometheus = true/" $HOME/.paloma/config/config.toml
```

#### Reset chain data

```bash
palomad tendermint unsafe-reset-all --keep-addr-book --home $HOME/.paloma --keep-addr-book
```

#### Remove node

{% hint style='danger' %}
Please, before proceeding with the next step! All chain data will be lost! Make sure you have backed up your **priv_validator_key.json**!
{% endhint %}

```bash
cd $HOME
sudo systemctl stop palomad
sudo systemctl disable palomad
sudo rm /etc/systemd/system/palomad.service
sudo systemctl daemon-reload
rm -f $(which palomad)
rm -rf $HOME/.paloma
rm -rf $HOME/paloma
```

## ⚙️ Service Management

#### Reload service configuration

```bash
sudo systemctl daemon-reload
```

#### Enable service

```bash
sudo systemctl enable palomad
```

#### Disable service

```bash
sudo systemctl disable palomad
```

#### Start service

```bash
sudo systemctl start palomad
```

#### Stop service

```bash
sudo systemctl stop palomad
```

#### Restart service

```bash
sudo systemctl restart palomad
```

#### Check service status

```bash
sudo systemctl status palomad
```

#### Check service logs

```bash
sudo journalctl -u palomad -f --no-hostname -o cat
```
