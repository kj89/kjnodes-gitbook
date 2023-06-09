---
description: Useful set of commands for node operators. From key management to chain governance.
---

# Useful commands

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/bitcanna.png" alt=""><figcaption></figcaption></figure>

## 🔑 Key management

#### Add new key

```bash
bcnad keys add wallet
```

#### Recover existing key

```bash
bcnad keys add wallet --recover
```

#### List all keys

```bash
bcnad keys list
```

#### Delete key

```bash
bcnad keys delete wallet
```

#### Export key to the file

```bash
bcnad keys export wallet
```

#### Import key from the file

```bash
bcnad keys import wallet wallet.backup
```

#### Query wallet balance

```bash
bcnad q bank balances $(bcnad keys show wallet -a)
```

## 👷 Validator management

{% hint style="info" %}
Please make sure you have adjusted **moniker**, **identity**, **details** and **website** to match your values.
{% endhint %}

#### Create new validator

```bash
bcnad tx staking create-validator \
--amount 1000000ubcna \
--pubkey $(bcnad tendermint show-validator) \
--moniker "YOUR_MONIKER_NAME" \
--identity "YOUR_KEYBASE_ID" \
--details "YOUR_DETAILS" \
--website "YOUR_WEBSITE_URL" \
--chain-id bitcanna-dev-1 \
--commission-rate 0.05 \
--commission-max-rate 0.20 \
--commission-max-change-rate 0.01 \
--min-self-delegation 1 \
--from wallet \
--gas-adjustment 1.4 \
--gas auto \
--gas-prices 0ubcna \
-y
```

#### Edit existing validator

```bash
bcnad tx staking edit-validator \
--new-moniker "YOUR_MONIKER_NAME" \
--identity "YOUR_KEYBASE_ID" \
--details "YOUR_DETAILS" \
--website "YOUR_WEBSITE_URL" \
--chain-id bitcanna-dev-1 \
--commission-rate 0.05 \
--from wallet \
--gas-adjustment 1.4 \
--gas auto \
--gas-prices 0ubcna \
-y
```

#### Unjail validator

```bash
bcnad tx slashing unjail --from wallet --chain-id bitcanna-dev-1 --gas-adjustment 1.4 --gas auto --gas-prices 0ubcna -y
```

#### Jail reason

```bash
bcnad query slashing signing-info $(bcnad tendermint show-validator)
```

#### List all active validators

```bash
bcnad q staking validators -oj --limit=3000 | jq '.validators[] | select(.status=="BOND_STATUS_BONDED")' | jq -r '(.tokens|tonumber/pow(10; 6)|floor|tostring) + " \t " + .description.moniker' | sort -gr | nl
```

#### List all inactive validators

```bash
bcnad q staking validators -oj --limit=3000 | jq '.validators[] | select(.status=="BOND_STATUS_UNBONDED")' | jq -r '(.tokens|tonumber/pow(10; 6)|floor|tostring) + " \t " + .description.moniker' | sort -gr | nl
```

#### View validator details

```bash
bcnad q staking validator $(bcnad keys show wallet --bech val -a)
```

## 💲 Token management

#### Withdraw rewards from all validators

```bash
bcnad tx distribution withdraw-all-rewards --from wallet --chain-id bitcanna-dev-1 --gas-adjustment 1.4 --gas auto --gas-prices 0ubcna -y
```

#### Withdraw commission and rewards from your validator

```bash
bcnad tx distribution withdraw-rewards $(bcnad keys show wallet --bech val -a) --commission --from wallet --chain-id bitcanna-dev-1 --gas-adjustment 1.4 --gas auto --gas-prices 0ubcna -y
```

#### Delegate tokens to yourself

```bash
bcnad tx staking delegate $(bcnad keys show wallet --bech val -a) 1000000ubcna --from wallet --chain-id bitcanna-dev-1 --gas-adjustment 1.4 --gas auto --gas-prices 0ubcna -y
```

#### Delegate tokens to validator

```bash
bcnad tx staking delegate <TO_VALOPER_ADDRESS> 1000000ubcna --from wallet --chain-id bitcanna-dev-1 --gas-adjustment 1.4 --gas auto --gas-prices 0ubcna -y
```

#### Redelegate tokens to another validator

```bash
bcnad tx staking redelegate $(bcnad keys show wallet --bech val -a) <TO_VALOPER_ADDRESS> 1000000ubcna --from wallet --chain-id bitcanna-dev-1 --gas-adjustment 1.4 --gas auto --gas-prices 0ubcna -y
```

#### Unbond tokens from your validator

```bash
bcnad tx staking unbond $(bcnad keys show wallet --bech val -a) 1000000ubcna --from wallet --chain-id bitcanna-dev-1 --gas-adjustment 1.4 --gas auto --gas-prices 0ubcna -y
```

#### Send tokens to the wallet

```bash
bcnad tx bank send wallet <TO_WALLET_ADDRESS> 1000000ubcna --from wallet --chain-id bitcanna-dev-1 --gas-adjustment 1.4 --gas auto --gas-prices 0ubcna -y
```

## 🗳 Governance

#### List all proposals

```bash
bcnad query gov proposals
```

#### View proposal by id

```bash
bcnad query gov proposal 1
```

#### Vote 'Yes'

```bash
bcnad tx gov vote 1 yes --from wallet --chain-id bitcanna-dev-1 --gas-adjustment 1.4 --gas auto --gas-prices 0ubcna -y
```

#### Vote 'No'

```bash
bcnad tx gov vote 1 no --from wallet --chain-id bitcanna-dev-1 --gas-adjustment 1.4 --gas auto --gas-prices 0ubcna -y
```

#### Vote 'Abstain'

```bash
bcnad tx gov vote 1 abstain --from wallet --chain-id bitcanna-dev-1 --gas-adjustment 1.4 --gas auto --gas-prices 0ubcna -y
```

#### Vote 'NoWithVeto'

```bash
bcnad tx gov vote 1 NoWithVeto --from wallet --chain-id bitcanna-dev-1 --gas-adjustment 1.4 --gas auto --gas-prices 0ubcna -y
```

## ⚡️ Utility

#### Update ports

```bash
CUSTOM_PORT=110
sed -i -e "s%^proxy_app = \"tcp://127.0.0.1:26658\"%proxy_app = \"tcp://127.0.0.1:${CUSTOM_PORT}58\"%; s%^laddr = \"tcp://127.0.0.1:26657\"%laddr = \"tcp://127.0.0.1:${CUSTOM_PORT}57\"%; s%^pprof_laddr = \"localhost:6060\"%pprof_laddr = \"localhost:${CUSTOM_PORT}60\"%; s%^laddr = \"tcp://0.0.0.0:26656\"%laddr = \"tcp://0.0.0.0:${CUSTOM_PORT}56\"%; s%^prometheus_listen_addr = \":26660\"%prometheus_listen_addr = \":${CUSTOM_PORT}66\"%" $HOME/.bcna/config/config.toml
sed -i -e "s%^address = \"tcp://0.0.0.0:1317\"%address = \"tcp://0.0.0.0:${CUSTOM_PORT}17\"%; s%^address = \":8080\"%address = \":${CUSTOM_PORT}80\"%; s%^address = \"0.0.0.0:9090\"%address = \"0.0.0.0:${CUSTOM_PORT}90\"%; s%^address = \"0.0.0.0:9091\"%address = \"0.0.0.0:${CUSTOM_PORT}91\"%" $HOME/.bcna/config/app.toml
```

#### Update Indexer

**Disable indexer**

```bash
sed -i -e 's|^indexer *=.*|indexer = "null"|' $HOME/.bcna/config/config.toml
```

**Enable indexer**

```bash
sed -i -e 's|^indexer *=.*|indexer = "kv"|' $HOME/.bcna/config/config.toml
```

#### Update pruning

```bash
sed -i \
  -e 's|^pruning *=.*|pruning = "custom"|' \
  -e 's|^pruning-keep-recent *=.*|pruning-keep-recent = "100"|' \
  -e 's|^pruning-keep-every *=.*|pruning-keep-every = "0"|' \
  -e 's|^pruning-interval *=.*|pruning-interval = "19"|' \
  $HOME/.bcna/config/app.toml
```

## 🚨 Maintenance

#### Get validator info

```bash
bcnad status 2>&1 | jq .ValidatorInfo
```

#### Get sync info

```bash
bcnad status 2>&1 | jq .SyncInfo
```

#### Get node peer

```bash
echo $(bcnad tendermint show-node-id)'@'$(curl -s ifconfig.me)':'$(cat $HOME/.bcna/config/config.toml | sed -n '/Address to listen for incoming connection/{n;p;}' | sed 's/.*://; s/".*//')
```

#### Check if validator key is correct

```bash
[[ $(bcnad q staking validator $(bcnad keys show wallet --bech val -a) -oj | jq -r .consensus_pubkey.key) = $(bcnad status | jq -r .ValidatorInfo.PubKey.value) ]] && echo -e "\n\e[1m\e[32mTrue\e[0m\n" || echo -e "\n\e[1m\e[31mFalse\e[0m\n"
```

#### Get live peers

```bash
curl -sS http://localhost:14257/net_info | jq -r '.result.peers[] | "\(.node_info.id)@\(.remote_ip):\(.node_info.listen_addr)"' | awk -F ':' '{print $1":"$(NF)}'
```

#### Set minimum gas price

```bash
sed -i -e "s/^minimum-gas-prices *=.*/minimum-gas-prices = \"0ubcna\"/" $HOME/.bcna/config/app.toml
```

#### Enable prometheus

```bash
sed -i -e "s/prometheus = false/prometheus = true/" $HOME/.bcna/config/config.toml
```

#### Reset chain data

```bash
bcnad tendermint unsafe-reset-all --keep-addr-book --home $HOME/.bcna --keep-addr-book
```

#### Remove node

{% hint style='danger' %}
Please, before proceeding with the next step! All chain data will be lost! Make sure you have backed up your **priv_validator_key.json**!
{% endhint %}

```bash
cd $HOME
sudo systemctl stop bcnad
sudo systemctl disable bcnad
sudo rm /etc/systemd/system/bcnad.service
sudo systemctl daemon-reload
rm -f $(which bcnad)
rm -rf $HOME/.bcna
rm -rf $HOME/bcna
```

## ⚙️ Service Management

#### Reload service configuration

```bash
sudo systemctl daemon-reload
```

#### Enable service

```bash
sudo systemctl enable bcnad
```

#### Disable service

```bash
sudo systemctl disable bcnad
```

#### Start service

```bash
sudo systemctl start bcnad
```

#### Stop service

```bash
sudo systemctl stop bcnad
```

#### Restart service

```bash
sudo systemctl restart bcnad
```

#### Check service status

```bash
sudo systemctl status bcnad
```

#### Check service logs

```bash
sudo journalctl -u bcnad -f --no-hostname -o cat
```
