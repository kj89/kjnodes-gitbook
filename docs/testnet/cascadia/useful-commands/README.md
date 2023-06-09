---
description: Useful set of commands for node operators. From key management to chain governance.
---

# Useful commands

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/cascadia.png" alt=""><figcaption></figcaption></figure>

## 🔑 Key management

#### Add new key

```bash
cascadiad keys add wallet
```

#### Recover existing key

```bash
cascadiad keys add wallet --recover
```

#### List all keys

```bash
cascadiad keys list
```

#### Delete key

```bash
cascadiad keys delete wallet
```

#### Export key to the file

```bash
cascadiad keys export wallet
```

#### Import key from the file

```bash
cascadiad keys import wallet wallet.backup
```

#### Query wallet balance

```bash
cascadiad q bank balances $(cascadiad keys show wallet -a)
```

## 👷 Validator management

{% hint style="info" %}
Please make sure you have adjusted **moniker**, **identity**, **details** and **website** to match your values.
{% endhint %}

#### Create new validator

```bash
cascadiad tx staking create-validator \
--amount 1000000aCC \
--pubkey $(cascadiad tendermint show-validator) \
--moniker "YOUR_MONIKER_NAME" \
--identity "YOUR_KEYBASE_ID" \
--details "YOUR_DETAILS" \
--website "YOUR_WEBSITE_URL" \
--chain-id cascadia_6102-1 \
--commission-rate 0.05 \
--commission-max-rate 0.20 \
--commission-max-change-rate 0.01 \
--min-self-delegation 1 \
--from wallet \
--gas-adjustment 1.4 \
--gas auto \
--gas-prices 7aCC \
-y
```

#### Edit existing validator

```bash
cascadiad tx staking edit-validator \
--new-moniker "YOUR_MONIKER_NAME" \
--identity "YOUR_KEYBASE_ID" \
--details "YOUR_DETAILS" \
--website "YOUR_WEBSITE_URL" \
--chain-id cascadia_6102-1 \
--commission-rate 0.05 \
--from wallet \
--gas-adjustment 1.4 \
--gas auto \
--gas-prices 7aCC \
-y
```

#### Unjail validator

```bash
cascadiad tx slashing unjail --from wallet --chain-id cascadia_6102-1 --gas-adjustment 1.4 --gas auto --gas-prices 7aCC -y
```

#### Jail reason

```bash
cascadiad query slashing signing-info $(cascadiad tendermint show-validator)
```

#### List all active validators

```bash
cascadiad q staking validators -oj --limit=3000 | jq '.validators[] | select(.status=="BOND_STATUS_BONDED")' | jq -r '(.tokens|tonumber/pow(10; 6)|floor|tostring) + " \t " + .description.moniker' | sort -gr | nl
```

#### List all inactive validators

```bash
cascadiad q staking validators -oj --limit=3000 | jq '.validators[] | select(.status=="BOND_STATUS_UNBONDED")' | jq -r '(.tokens|tonumber/pow(10; 6)|floor|tostring) + " \t " + .description.moniker' | sort -gr | nl
```

#### View validator details

```bash
cascadiad q staking validator $(cascadiad keys show wallet --bech val -a)
```

## 💲 Token management

#### Withdraw rewards from all validators

```bash
cascadiad tx distribution withdraw-all-rewards --from wallet --chain-id cascadia_6102-1 --gas-adjustment 1.4 --gas auto --gas-prices 7aCC -y
```

#### Withdraw commission and rewards from your validator

```bash
cascadiad tx distribution withdraw-rewards $(cascadiad keys show wallet --bech val -a) --commission --from wallet --chain-id cascadia_6102-1 --gas-adjustment 1.4 --gas auto --gas-prices 7aCC -y
```

#### Delegate tokens to yourself

```bash
cascadiad tx staking delegate $(cascadiad keys show wallet --bech val -a) 1000000aCC --from wallet --chain-id cascadia_6102-1 --gas-adjustment 1.4 --gas auto --gas-prices 7aCC -y
```

#### Delegate tokens to validator

```bash
cascadiad tx staking delegate <TO_VALOPER_ADDRESS> 1000000aCC --from wallet --chain-id cascadia_6102-1 --gas-adjustment 1.4 --gas auto --gas-prices 7aCC -y
```

#### Redelegate tokens to another validator

```bash
cascadiad tx staking redelegate $(cascadiad keys show wallet --bech val -a) <TO_VALOPER_ADDRESS> 1000000aCC --from wallet --chain-id cascadia_6102-1 --gas-adjustment 1.4 --gas auto --gas-prices 7aCC -y
```

#### Unbond tokens from your validator

```bash
cascadiad tx staking unbond $(cascadiad keys show wallet --bech val -a) 1000000aCC --from wallet --chain-id cascadia_6102-1 --gas-adjustment 1.4 --gas auto --gas-prices 7aCC -y
```

#### Send tokens to the wallet

```bash
cascadiad tx bank send wallet <TO_WALLET_ADDRESS> 1000000aCC --from wallet --chain-id cascadia_6102-1 --gas-adjustment 1.4 --gas auto --gas-prices 7aCC -y
```

## 🗳 Governance

#### List all proposals

```bash
cascadiad query gov proposals
```

#### View proposal by id

```bash
cascadiad query gov proposal 1
```

#### Vote 'Yes'

```bash
cascadiad tx gov vote 1 yes --from wallet --chain-id cascadia_6102-1 --gas-adjustment 1.4 --gas auto --gas-prices 7aCC -y
```

#### Vote 'No'

```bash
cascadiad tx gov vote 1 no --from wallet --chain-id cascadia_6102-1 --gas-adjustment 1.4 --gas auto --gas-prices 7aCC -y
```

#### Vote 'Abstain'

```bash
cascadiad tx gov vote 1 abstain --from wallet --chain-id cascadia_6102-1 --gas-adjustment 1.4 --gas auto --gas-prices 7aCC -y
```

#### Vote 'NoWithVeto'

```bash
cascadiad tx gov vote 1 NoWithVeto --from wallet --chain-id cascadia_6102-1 --gas-adjustment 1.4 --gas auto --gas-prices 7aCC -y
```

## ⚡️ Utility

#### Update ports

```bash
CUSTOM_PORT=110
sed -i -e "s%^proxy_app = \"tcp://127.0.0.1:26658\"%proxy_app = \"tcp://127.0.0.1:${CUSTOM_PORT}58\"%; s%^laddr = \"tcp://127.0.0.1:26657\"%laddr = \"tcp://127.0.0.1:${CUSTOM_PORT}57\"%; s%^pprof_laddr = \"localhost:6060\"%pprof_laddr = \"localhost:${CUSTOM_PORT}60\"%; s%^laddr = \"tcp://0.0.0.0:26656\"%laddr = \"tcp://0.0.0.0:${CUSTOM_PORT}56\"%; s%^prometheus_listen_addr = \":26660\"%prometheus_listen_addr = \":${CUSTOM_PORT}66\"%" $HOME/.cascadiad/config/config.toml
sed -i -e "s%^address = \"tcp://0.0.0.0:1317\"%address = \"tcp://0.0.0.0:${CUSTOM_PORT}17\"%; s%^address = \":8080\"%address = \":${CUSTOM_PORT}80\"%; s%^address = \"0.0.0.0:9090\"%address = \"0.0.0.0:${CUSTOM_PORT}90\"%; s%^address = \"0.0.0.0:9091\"%address = \"0.0.0.0:${CUSTOM_PORT}91\"%" $HOME/.cascadiad/config/app.toml
```

#### Update Indexer

**Disable indexer**

```bash
sed -i -e 's|^indexer *=.*|indexer = "null"|' $HOME/.cascadiad/config/config.toml
```

**Enable indexer**

```bash
sed -i -e 's|^indexer *=.*|indexer = "kv"|' $HOME/.cascadiad/config/config.toml
```

#### Update pruning

```bash
sed -i \
  -e 's|^pruning *=.*|pruning = "custom"|' \
  -e 's|^pruning-keep-recent *=.*|pruning-keep-recent = "100"|' \
  -e 's|^pruning-keep-every *=.*|pruning-keep-every = "0"|' \
  -e 's|^pruning-interval *=.*|pruning-interval = "19"|' \
  $HOME/.cascadiad/config/app.toml
```

## 🚨 Maintenance

#### Get validator info

```bash
cascadiad status 2>&1 | jq .ValidatorInfo
```

#### Get sync info

```bash
cascadiad status 2>&1 | jq .SyncInfo
```

#### Get node peer

```bash
echo $(cascadiad tendermint show-node-id)'@'$(curl -s ifconfig.me)':'$(cat $HOME/.cascadiad/config/config.toml | sed -n '/Address to listen for incoming connection/{n;p;}' | sed 's/.*://; s/".*//')
```

#### Check if validator key is correct

```bash
[[ $(cascadiad q staking validator $(cascadiad keys show wallet --bech val -a) -oj | jq -r .consensus_pubkey.key) = $(cascadiad status | jq -r .ValidatorInfo.PubKey.value) ]] && echo -e "\n\e[1m\e[32mTrue\e[0m\n" || echo -e "\n\e[1m\e[31mFalse\e[0m\n"
```

#### Get live peers

```bash
curl -sS http://localhost:15557/net_info | jq -r '.result.peers[] | "\(.node_info.id)@\(.remote_ip):\(.node_info.listen_addr)"' | awk -F ':' '{print $1":"$(NF)}'
```

#### Set minimum gas price

```bash
sed -i -e "s/^minimum-gas-prices *=.*/minimum-gas-prices = \"7aCC\"/" $HOME/.cascadiad/config/app.toml
```

#### Enable prometheus

```bash
sed -i -e "s/prometheus = false/prometheus = true/" $HOME/.cascadiad/config/config.toml
```

#### Reset chain data

```bash
cascadiad tendermint unsafe-reset-all --keep-addr-book --home $HOME/.cascadiad --keep-addr-book
```

#### Remove node

{% hint style='danger' %}
Please, before proceeding with the next step! All chain data will be lost! Make sure you have backed up your **priv_validator_key.json**!
{% endhint %}

```bash
cd $HOME
sudo systemctl stop cascadiad
sudo systemctl disable cascadiad
sudo rm /etc/systemd/system/cascadiad.service
sudo systemctl daemon-reload
rm -f $(which cascadiad)
rm -rf $HOME/.cascadiad
rm -rf $HOME/cascadia
```

## ⚙️ Service Management

#### Reload service configuration

```bash
sudo systemctl daemon-reload
```

#### Enable service

```bash
sudo systemctl enable cascadiad
```

#### Disable service

```bash
sudo systemctl disable cascadiad
```

#### Start service

```bash
sudo systemctl start cascadiad
```

#### Stop service

```bash
sudo systemctl stop cascadiad
```

#### Restart service

```bash
sudo systemctl restart cascadiad
```

#### Check service status

```bash
sudo systemctl status cascadiad
```

#### Check service logs

```bash
sudo journalctl -u cascadiad -f --no-hostname -o cat
```
