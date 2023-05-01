---
description: Useful set of commands for node operators. From key management to chain governance.
---

# Useful commands

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/mars.png" alt=""><figcaption></figcaption></figure>

## 🔑 Key management

#### Add new key

```bash
marsd keys add wallet
```

#### Recover existing key

```bash
marsd keys add wallet --recover
```

#### List all keys

```bash
marsd keys list
```

#### Delete key

```bash
marsd keys delete wallet
```

#### Export key to the file

```bash
marsd keys export wallet
```

#### Import key from the file

```bash
marsd keys import wallet wallet.backup
```

#### Query wallet balance

```bash
marsd q bank balances $(marsd keys show wallet -a)
```

## 👷 Validator management

{% hint style="info" %}
Please make sure you have adjusted **moniker**, **identity**, **details** and **website** to match your values.
{% endhint %}

#### Create new validator

```bash
marsd tx staking create-validator \
--amount 1000000umars \
--pubkey $(marsd tendermint show-validator) \
--moniker "YOUR_MONIKER_NAME" \
--identity "YOUR_KEYBASE_ID" \
--details "YOUR_DETAILS" \
--website "YOUR_WEBSITE_URL" \
--chain-id mars-1 \
--commission-rate 0.05 \
--commission-max-rate 0.20 \
--commission-max-change-rate 0.01 \
--min-self-delegation 1 \
--from wallet \
--gas-adjustment 1.4 \
--gas auto \
--gas-prices 0umars \
-y
```

#### Edit existing validator

```bash
marsd tx staking edit-validator \
--new-moniker "YOUR_MONIKER_NAME" \
--identity "YOUR_KEYBASE_ID" \
--details "YOUR_DETAILS" \
--website "YOUR_WEBSITE_URL" \
--chain-id mars-1 \
--commission-rate 0.05 \
--from wallet \
--gas-adjustment 1.4 \
--gas auto \
--gas-prices 0umars \
-y
```

#### Unjail validator

```bash
marsd tx slashing unjail --from wallet --chain-id mars-1 --gas-adjustment 1.4 --gas auto --gas-prices 0umars -y
```

#### Jail reason

```bash
marsd query slashing signing-info $(marsd tendermint show-validator)
```

#### List all active validators

```bash
marsd q staking validators -oj --limit=3000 | jq '.validators[] | select(.status=="BOND_STATUS_BONDED")' | jq -r '(.tokens|tonumber/pow(10; 6)|floor|tostring) + " \t " + .description.moniker' | sort -gr | nl
```

#### List all inactive validators

```bash
marsd q staking validators -oj --limit=3000 | jq '.validators[] | select(.status=="BOND_STATUS_UNBONDED")' | jq -r '(.tokens|tonumber/pow(10; 6)|floor|tostring) + " \t " + .description.moniker' | sort -gr | nl
```

#### View validator details

```bash
marsd q staking validator $(marsd keys show wallet --bech val -a)
```

## 💲 Token management

#### Withdraw rewards from all validators

```bash
marsd tx distribution withdraw-all-rewards --from wallet --chain-id mars-1 --gas-adjustment 1.4 --gas auto --gas-prices 0umars -y
```

#### Withdraw commission and rewards from your validator

```bash
marsd tx distribution withdraw-rewards $(marsd keys show wallet --bech val -a) --commission --from wallet --chain-id mars-1 --gas-adjustment 1.4 --gas auto --gas-prices 0umars -y
```

#### Delegate tokens to yourself

```bash
marsd tx staking delegate $(marsd keys show wallet --bech val -a) 1000000umars --from wallet --chain-id mars-1 --gas-adjustment 1.4 --gas auto --gas-prices 0umars -y
```

#### Delegate tokens to validator

```bash
marsd tx staking delegate <TO_VALOPER_ADDRESS> 1000000umars --from wallet --chain-id mars-1 --gas-adjustment 1.4 --gas auto --gas-prices 0umars -y
```

#### Redelegate tokens to another validator

```bash
marsd tx staking redelegate $(marsd keys show wallet --bech val -a) <TO_VALOPER_ADDRESS> 1000000umars --from wallet --chain-id mars-1 --gas-adjustment 1.4 --gas auto --gas-prices 0umars -y
```

#### Unbond tokens from your validator

```bash
marsd tx staking unbond $(marsd keys show wallet --bech val -a) 1000000umars --from wallet --chain-id mars-1 --gas-adjustment 1.4 --gas auto --gas-prices 0umars -y
```

#### Send tokens to the wallet

```bash
marsd tx bank send wallet <TO_WALLET_ADDRESS> 1000000umars --from wallet --chain-id mars-1 --gas-adjustment 1.4 --gas auto --gas-prices 0umars -y
```

## 🗳 Governance

#### List all proposals

```bash
marsd query gov proposals
```

#### View proposal by id

```bash
marsd query gov proposal 1
```

#### Vote 'Yes'

```bash
marsd tx gov vote 1 yes --from wallet --chain-id mars-1 --gas-adjustment 1.4 --gas auto --gas-prices 0umars -y
```

#### Vote 'No'

```bash
marsd tx gov vote 1 no --from wallet --chain-id mars-1 --gas-adjustment 1.4 --gas auto --gas-prices 0umars -y
```

#### Vote 'Abstain'

```bash
marsd tx gov vote 1 abstain --from wallet --chain-id mars-1 --gas-adjustment 1.4 --gas auto --gas-prices 0umars -y
```

#### Vote 'NoWithVeto'

```bash
marsd tx gov vote 1 NoWithVeto --from wallet --chain-id mars-1 --gas-adjustment 1.4 --gas auto --gas-prices 0umars -y
```

## ⚡️ Utility

#### Update ports

```bash
CUSTOM_PORT=110
sed -i -e "s%^proxy_app = \"tcp://127.0.0.1:26658\"%proxy_app = \"tcp://127.0.0.1:${CUSTOM_PORT}58\"%; s%^laddr = \"tcp://127.0.0.1:26657\"%laddr = \"tcp://127.0.0.1:${CUSTOM_PORT}57\"%; s%^pprof_laddr = \"localhost:6060\"%pprof_laddr = \"localhost:${CUSTOM_PORT}60\"%; s%^laddr = \"tcp://0.0.0.0:26656\"%laddr = \"tcp://0.0.0.0:${CUSTOM_PORT}56\"%; s%^prometheus_listen_addr = \":26660\"%prometheus_listen_addr = \":${CUSTOM_PORT}66\"%" $HOME/.mars/config/config.toml
sed -i -e "s%^address = \"tcp://0.0.0.0:1317\"%address = \"tcp://0.0.0.0:${CUSTOM_PORT}17\"%; s%^address = \":8080\"%address = \":${CUSTOM_PORT}80\"%; s%^address = \"0.0.0.0:9090\"%address = \"0.0.0.0:${CUSTOM_PORT}90\"%; s%^address = \"0.0.0.0:9091\"%address = \"0.0.0.0:${CUSTOM_PORT}91\"%" $HOME/.mars/config/app.toml
```

#### Update Indexer

**Disable indexer**

```bash
sed -i -e 's|^indexer *=.*|indexer = "null"|' $HOME/.mars/config/config.toml
```

**Enable indexer**

```bash
sed -i -e 's|^indexer *=.*|indexer = "kv"|' $HOME/.mars/config/config.toml
```

#### Update pruning

```bash
sed -i \
  -e 's|^pruning *=.*|pruning = "custom"|' \
  -e 's|^pruning-keep-recent *=.*|pruning-keep-recent = "100"|' \
  -e 's|^pruning-keep-every *=.*|pruning-keep-every = "0"|' \
  -e 's|^pruning-interval *=.*|pruning-interval = "19"|' \
  $HOME/.mars/config/app.toml
```

## 🚨 Maintenance

#### Get validator info

```bash
marsd status 2>&1 | jq .ValidatorInfo
```

#### Get sync info

```bash
marsd status 2>&1 | jq .SyncInfo
```

#### Get node peer

```bash
echo $(marsd tendermint show-node-id)'@'$(curl -s ifconfig.me)':'$(cat $HOME/.mars/config/config.toml | sed -n '/Address to listen for incoming connection/{n;p;}' | sed 's/.*://; s/".*//')
```

#### Check if validator key is correct

```bash
[[ $(marsd q staking validator $(marsd keys show wallet --bech val -a) -oj | jq -r .consensus_pubkey.key) = $(marsd status | jq -r .ValidatorInfo.PubKey.value) ]] && echo -e "\n\e[1m\e[32mTrue\e[0m\n" || echo -e "\n\e[1m\e[31mFalse\e[0m\n"
```

#### Get live peers

```bash
curl -sS http://localhost:14557/net_info | jq -r '.result.peers[] | "\(.node_info.id)@\(.remote_ip):\(.node_info.listen_addr)"' | awk -F ':' '{print $1":"$(NF)}'
```

#### Set minimum gas price

```bash
sed -i -e "s/^minimum-gas-prices *=.*/minimum-gas-prices = \"0umars\"/" $HOME/.mars/config/app.toml
```

#### Enable prometheus

```bash
sed -i -e "s/prometheus = false/prometheus = true/" $HOME/.mars/config/config.toml
```

#### Reset chain data

```bash
marsd tendermint unsafe-reset-all --home $HOME/.mars --keep-addr-book
```

#### Remove node

{% hint style='danger' %}
Please, before proceeding with the next step! All chain data will be lost! Make sure you have backed up your **priv_validator_key.json**!
{% endhint %}

```bash
cd $HOME
sudo systemctl stop marsd
sudo systemctl disable marsd
sudo rm /etc/systemd/system/marsd.service
sudo systemctl daemon-reload
rm -f $(which marsd)
rm -rf $HOME/.mars
rm -rf $HOME/hub
```

## ⚙️ Service Management

#### Reload service configuration

```bash
sudo systemctl daemon-reload
```

#### Enable service

```bash
sudo systemctl enable marsd
```

#### Disable service

```bash
sudo systemctl disable marsd
```

#### Start service

```bash
sudo systemctl start marsd
```

#### Stop service

```bash
sudo systemctl stop marsd
```

#### Restart service

```bash
sudo systemctl restart marsd
```

#### Check service status

```bash
sudo systemctl status marsd
```

#### Check service logs

```bash
sudo journalctl -u marsd -f --no-hostname -o cat
```
