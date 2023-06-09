---
description: Useful set of commands for node operators. From key management to chain governance.
---

# Useful commands

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/hypersign.png" alt=""><figcaption></figcaption></figure>

## 🔑 Key management

#### Add new key

```bash
hid-noded keys add wallet
```

#### Recover existing key

```bash
hid-noded keys add wallet --recover
```

#### List all keys

```bash
hid-noded keys list
```

#### Delete key

```bash
hid-noded keys delete wallet
```

#### Export key to the file

```bash
hid-noded keys export wallet
```

#### Import key from the file

```bash
hid-noded keys import wallet wallet.backup
```

#### Query wallet balance

```bash
hid-noded q bank balances $(hid-noded keys show wallet -a)
```

## 👷 Validator management

{% hint style="info" %}
Please make sure you have adjusted **moniker**, **identity**, **details** and **website** to match your values.
{% endhint %}

#### Create new validator

```bash
hid-noded tx staking create-validator \
--amount=1000000uhid \
--pubkey=$(hid-noded tendermint show-validator) \
--moniker="YOUR_MONIKER_NAME" \
--identity="YOUR_KEYBASE_ID" \
--details="YOUR_DETAILS" \
--website="YOUR_WEBSITE_URL"
--chain-id=jagrat \
--commission-rate=0.05 \
--commission-max-rate=0.20 \
--commission-max-change-rate=0.01 \
--min-self-delegation=1 \
--from=wallet \
--gas-adjustment=1.4 \
--gas=auto \
--node=tcp://localhost:13157 \
-y
```

#### Edit existing validator

```bash
hid-noded tx staking edit-validator \
--new-moniker="YOUR_MONIKER_NAME" \
--identity="YOUR_KEYBASE_ID" \
--details="YOUR_DETAILS" \
--website="YOUR_WEBSITE_URL"
--chain-id=jagrat \
--commission-rate=0.05 \
--from=wallet \
--gas-adjustment=1.4 \
--gas=auto \
--node=tcp://localhost:13157 \
-y
```

#### Unjail validator

```bash
hid-noded tx slashing unjail --from wallet --chain-id jagrat --gas-adjustment 1.4 --gas auto --node=tcp://localhost:13157 -y
```

#### Jail reason

```bash
hid-noded query slashing signing-info $(hid-noded tendermint show-validator)
```

#### List all active validators

```bash
hid-noded q staking validators -oj --limit=3000 | jq '.validators[] | select(.status=="BOND_STATUS_BONDED")' | jq -r '(.tokens|tonumber/pow(10; 6)|floor|tostring) + " \t " + .description.moniker' | sort -gr | nl
```

#### List all inactive validators

```bash
hid-noded q staking validators -oj --limit=3000 | jq '.validators[] | select(.status=="BOND_STATUS_UNBONDED")' | jq -r '(.tokens|tonumber/pow(10; 6)|floor|tostring) + " \t " + .description.moniker' | sort -gr | nl
```

#### View validator details

```bash
hid-noded q staking validator $(hid-noded keys show wallet --bech val -a)
```

## 💲 Token management

#### Withdraw rewards from all validators

```bash
hid-noded tx distribution withdraw-all-rewards --from wallet --chain-id jagrat --gas-adjustment 1.4 --gas auto --node=tcp://localhost:13157 -y
```

#### Withdraw commission and rewards from your validator

```bash
hid-noded tx distribution withdraw-rewards $(hid-noded keys show wallet --bech val -a) --commission --from wallet --chain-id jagrat --gas-adjustment 1.4 --gas auto --node=tcp://localhost:13157 -y
```

#### Delegate tokens to yourself

```bash
hid-noded tx staking delegate $(hid-noded keys show wallet --bech val -a) 1000000uhid --from wallet --chain-id jagrat --gas-adjustment 1.4 --gas auto --node=tcp://localhost:13157 -y
```

#### Delegate tokens to validator

```bash
hid-noded tx staking delegate <TO_VALOPER_ADDRESS> 1000000uhid --from wallet --chain-id jagrat --gas-adjustment 1.4 --gas auto --node=tcp://localhost:13157 -y
```

#### Redelegate tokens to another validator

```bash
hid-noded tx staking redelegate $(hid-noded keys show wallet --bech val -a) <TO_VALOPER_ADDRESS> 1000000uhid --from wallet --chain-id jagrat --gas-adjustment 1.4 --gas auto --node=tcp://localhost:13157 -y
```

#### Unbond tokens from your validator

```bash
hid-noded tx staking unbond $(hid-noded keys show wallet --bech val -a) 1000000uhid --from wallet --chain-id jagrat --gas-adjustment 1.4 --gas auto --node=tcp://localhost:13157 -y
```

#### Send tokens to the wallet

```bash
hid-noded tx bank send wallet <TO_WALLET_ADDRESS> 1000000uhid --from wallet --chain-id jagrat
```

## 🗳 Governance

#### List all proposals

```bash
hid-noded query gov proposals
```

#### View proposal by id

```bash
hid-noded query gov proposal 1
```

#### Vote 'Yes'

```bash
hid-noded tx gov vote 1 yes --from wallet --chain-id jagrat --gas-adjustment 1.4 --gas auto --node=tcp://localhost:13157 -y
```

#### Vote 'No'

```bash
hid-noded tx gov vote 1 no --from wallet --chain-id jagrat --gas-adjustment 1.4 --gas auto --node=tcp://localhost:13157 -y
```

#### Vote 'Abstain'

```bash
hid-noded tx gov vote 1 abstain --from wallet --chain-id jagrat --gas-adjustment 1.4 --gas auto --node=tcp://localhost:13157 -y
```

#### Vote 'NoWithVeto'

```bash
hid-noded tx gov vote 1 NoWithVeto --from wallet --chain-id jagrat --gas-adjustment 1.4 --gas auto --node=tcp://localhost:13157 -y
```

## ⚡️ Utility

#### Update ports

```bash
CUSTOM_PORT=110
sed -i -e "s%^proxy_app = \"tcp://127.0.0.1:26658\"%proxy_app = \"tcp://127.0.0.1:${CUSTOM_PORT}58\"%; s%^laddr = \"tcp://127.0.0.1:26657\"%laddr = \"tcp://127.0.0.1:${CUSTOM_PORT}57\"%; s%^pprof_laddr = \"localhost:6060\"%pprof_laddr = \"localhost:${CUSTOM_PORT}60\"%; s%^laddr = \"tcp://0.0.0.0:26656\"%laddr = \"tcp://0.0.0.0:${CUSTOM_PORT}56\"%; s%^prometheus_listen_addr = \":26660\"%prometheus_listen_addr = \":${CUSTOM_PORT}66\"%" $HOME/.hid-node/config/config.toml
sed -i -e "s%^address = \"tcp://0.0.0.0:1317\"%address = \"tcp://0.0.0.0:${CUSTOM_PORT}17\"%; s%^address = \":8080\"%address = \":${CUSTOM_PORT}80\"%; s%^address = \"0.0.0.0:9090\"%address = \"0.0.0.0:${CUSTOM_PORT}90\"%; s%^address = \"0.0.0.0:9091\"%address = \"0.0.0.0:${CUSTOM_PORT}91\"%" $HOME/.hid-node/config/app.toml
```

#### Update Indexer

**Disable indexer**

```bash
sed -i -e 's|^indexer *=.*|indexer = "null"|' $HOME/.hid-node/config/config.toml
```

**Enable indexer**

```bash
sed -i -e 's|^indexer *=.*|indexer = "kv"|' $HOME/.hid-node/config/config.toml
```

#### Update pruning

```bash
sed -i \
  -e 's|^pruning *=.*|pruning = "custom"|' \
  -e 's|^pruning-keep-recent *=.*|pruning-keep-recent = "100"|' \
  -e 's|^pruning-keep-every *=.*|pruning-keep-every = "0"|' \
  -e 's|^pruning-interval *=.*|pruning-interval = "19"|' \
  $HOME/.hid-node/config/app.toml
```

## 🚨 Maintenance

#### Get validator info

```bash
hid-noded status 2>&1 | jq .ValidatorInfo
```

#### Get sync info

```bash
hid-noded status 2>&1 | jq .SyncInfo
```

#### Get node peer

```bash
echo $(hid-noded tendermint show-node-id)'@'$(curl -s ifconfig.me)':'$(cat $HOME/.hid-node/config/config.toml | sed -n '/Address to listen for incoming connection/{n;p;}' | sed 's/.*://; s/".*//')
```

#### Check if validator key is correct

```bash
[[ $(hid-noded q staking validator $(hid-noded keys show wallet --bech val -a) -oj | jq -r .consensus_pubkey.key) = $(hid-noded status | jq -r .ValidatorInfo.PubKey.value) ]] && echo -e "\n\e[1m\e[32mTrue\e[0m\n" || echo -e "\n\e[1m\e[31mFalse\e[0m\n"
```

#### Get live peers

```bash
curl -sS http://localhost:13157/net_info | jq -r '.result.peers[] | "\(.node_info.id)@\(.remote_ip):\(.node_info.listen_addr)"' | awk -F ':' '{print $1":"$(NF)}'
```

#### Set minimum gas price

```bash
sed -i -e "s/^minimum-gas-prices *=.*/minimum-gas-prices = \"0uhid\"/" $HOME/.hid-node/config/app.toml
```

#### Enable prometheus

```bash
sed -i -e "s/prometheus = false/prometheus = true/" $HOME/.hid-node/config/config.toml
```

#### Reset chain data

```bash
hid-noded tendermint unsafe-reset-all --keep-addr-book --home $HOME/.hid-node --keep-addr-book
```

#### Remove node

{% hint style='danger' %}
Please, before proceeding with the next step! All chain data will be lost! Make sure you have backed up your **priv_validator_key.json**!
{% endhint %}

```bash
cd $HOME
sudo systemctl stop hid-noded
sudo systemctl disable hid-noded
sudo rm /etc/systemd/system/hid-noded.service
sudo systemctl daemon-reload
rm -f $(which hid-noded)
rm -rf $HOME/.hid-node
rm -rf $HOME/hid-node
```

## ⚙️ Service Management

#### Reload service configuration

```bash
sudo systemctl daemon-reload
```

#### Enable service

```bash
sudo systemctl enable hid-noded
```

#### Disable service

```bash
sudo systemctl disable hid-noded
```

#### Start service

```bash
sudo systemctl start hid-noded
```

#### Stop service

```bash
sudo systemctl stop hid-noded
```

#### Restart service

```bash
sudo systemctl restart hid-noded
```

#### Check service status

```bash
sudo systemctl status hid-noded
```

#### Check service logs

```bash
sudo journalctl -u hid-noded -f --no-hostname -o cat
```
