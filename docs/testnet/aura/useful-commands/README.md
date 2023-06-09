---
description: Useful set of commands for node operators. From key management to chain governance.
---

# Useful commands

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/aura.png" alt=""><figcaption></figcaption></figure>

## 🔑 Key management

#### Add new key

```bash
aurad keys add wallet
```

#### Recover existing key

```bash
aurad keys add wallet --recover
```

#### List all keys

```bash
aurad keys list
```

#### Delete key

```bash
aurad keys delete wallet
```

#### Export key to the file

```bash
aurad keys export wallet
```

#### Import key from the file

```bash
aurad keys import wallet wallet.backup
```

#### Query wallet balance

```bash
aurad q bank balances $(aurad keys show wallet -a)
```

## 👷 Validator management

{% hint style="info" %}
Please make sure you have adjusted **moniker**, **identity**, **details** and **website** to match your values.
{% endhint %}

#### Create new validator

```bash
aurad tx staking create-validator \
--amount 1000000ueaura \
--pubkey $(aurad tendermint show-validator) \
--moniker "YOUR_MONIKER_NAME" \
--identity "YOUR_KEYBASE_ID" \
--details "YOUR_DETAILS" \
--website "YOUR_WEBSITE_URL" \
--chain-id euphoria-2 \
--commission-rate 0.05 \
--commission-max-rate 0.20 \
--commission-max-change-rate 0.01 \
--min-self-delegation 1 \
--from wallet \
--gas-adjustment 1.4 \
--gas auto \
--gas-prices 0ueaura \
-y
```

#### Edit existing validator

```bash
aurad tx staking edit-validator \
--new-moniker "YOUR_MONIKER_NAME" \
--identity "YOUR_KEYBASE_ID" \
--details "YOUR_DETAILS" \
--website "YOUR_WEBSITE_URL" \
--chain-id euphoria-2 \
--commission-rate 0.05 \
--from wallet \
--gas-adjustment 1.4 \
--gas auto \
--gas-prices 0ueaura \
-y
```

#### Unjail validator

```bash
aurad tx slashing unjail --from wallet --chain-id euphoria-2 --gas-adjustment 1.4 --gas auto --gas-prices 0ueaura -y
```

#### Jail reason

```bash
aurad query slashing signing-info $(aurad tendermint show-validator)
```

#### List all active validators

```bash
aurad q staking validators -oj --limit=3000 | jq '.validators[] | select(.status=="BOND_STATUS_BONDED")' | jq -r '(.tokens|tonumber/pow(10; 6)|floor|tostring) + " \t " + .description.moniker' | sort -gr | nl
```

#### List all inactive validators

```bash
aurad q staking validators -oj --limit=3000 | jq '.validators[] | select(.status=="BOND_STATUS_UNBONDED")' | jq -r '(.tokens|tonumber/pow(10; 6)|floor|tostring) + " \t " + .description.moniker' | sort -gr | nl
```

#### View validator details

```bash
aurad q staking validator $(aurad keys show wallet --bech val -a)
```

## 💲 Token management

#### Withdraw rewards from all validators

```bash
aurad tx distribution withdraw-all-rewards --from wallet --chain-id euphoria-2 --gas-adjustment 1.4 --gas auto --gas-prices 0ueaura -y
```

#### Withdraw commission and rewards from your validator

```bash
aurad tx distribution withdraw-rewards $(aurad keys show wallet --bech val -a) --commission --from wallet --chain-id euphoria-2 --gas-adjustment 1.4 --gas auto --gas-prices 0ueaura -y
```

#### Delegate tokens to yourself

```bash
aurad tx staking delegate $(aurad keys show wallet --bech val -a) 1000000ueaura --from wallet --chain-id euphoria-2 --gas-adjustment 1.4 --gas auto --gas-prices 0ueaura -y
```

#### Delegate tokens to validator

```bash
aurad tx staking delegate <TO_VALOPER_ADDRESS> 1000000ueaura --from wallet --chain-id euphoria-2 --gas-adjustment 1.4 --gas auto --gas-prices 0ueaura -y
```

#### Redelegate tokens to another validator

```bash
aurad tx staking redelegate $(aurad keys show wallet --bech val -a) <TO_VALOPER_ADDRESS> 1000000ueaura --from wallet --chain-id euphoria-2 --gas-adjustment 1.4 --gas auto --gas-prices 0ueaura -y
```

#### Unbond tokens from your validator

```bash
aurad tx staking unbond $(aurad keys show wallet --bech val -a) 1000000ueaura --from wallet --chain-id euphoria-2 --gas-adjustment 1.4 --gas auto --gas-prices 0ueaura -y
```

#### Send tokens to the wallet

```bash
aurad tx bank send wallet <TO_WALLET_ADDRESS> 1000000ueaura --from wallet --chain-id euphoria-2 --gas-adjustment 1.4 --gas auto --gas-prices 0ueaura -y
```

## 🗳 Governance

#### List all proposals

```bash
aurad query gov proposals
```

#### View proposal by id

```bash
aurad query gov proposal 1
```

#### Vote 'Yes'

```bash
aurad tx gov vote 1 yes --from wallet --chain-id euphoria-2 --gas-adjustment 1.4 --gas auto --gas-prices 0ueaura -y
```

#### Vote 'No'

```bash
aurad tx gov vote 1 no --from wallet --chain-id euphoria-2 --gas-adjustment 1.4 --gas auto --gas-prices 0ueaura -y
```

#### Vote 'Abstain'

```bash
aurad tx gov vote 1 abstain --from wallet --chain-id euphoria-2 --gas-adjustment 1.4 --gas auto --gas-prices 0ueaura -y
```

#### Vote 'NoWithVeto'

```bash
aurad tx gov vote 1 NoWithVeto --from wallet --chain-id euphoria-2 --gas-adjustment 1.4 --gas auto --gas-prices 0ueaura -y
```

## ⚡️ Utility

#### Update ports

```bash
CUSTOM_PORT=110
sed -i -e "s%^proxy_app = \"tcp://127.0.0.1:26658\"%proxy_app = \"tcp://127.0.0.1:${CUSTOM_PORT}58\"%; s%^laddr = \"tcp://127.0.0.1:26657\"%laddr = \"tcp://127.0.0.1:${CUSTOM_PORT}57\"%; s%^pprof_laddr = \"localhost:6060\"%pprof_laddr = \"localhost:${CUSTOM_PORT}60\"%; s%^laddr = \"tcp://0.0.0.0:26656\"%laddr = \"tcp://0.0.0.0:${CUSTOM_PORT}56\"%; s%^prometheus_listen_addr = \":26660\"%prometheus_listen_addr = \":${CUSTOM_PORT}66\"%" $HOME/.aura/config/config.toml
sed -i -e "s%^address = \"tcp://0.0.0.0:1317\"%address = \"tcp://0.0.0.0:${CUSTOM_PORT}17\"%; s%^address = \":8080\"%address = \":${CUSTOM_PORT}80\"%; s%^address = \"0.0.0.0:9090\"%address = \"0.0.0.0:${CUSTOM_PORT}90\"%; s%^address = \"0.0.0.0:9091\"%address = \"0.0.0.0:${CUSTOM_PORT}91\"%" $HOME/.aura/config/app.toml
```

#### Update Indexer

**Disable indexer**

```bash
sed -i -e 's|^indexer *=.*|indexer = "null"|' $HOME/.aura/config/config.toml
```

**Enable indexer**

```bash
sed -i -e 's|^indexer *=.*|indexer = "kv"|' $HOME/.aura/config/config.toml
```

#### Update pruning

```bash
sed -i \
  -e 's|^pruning *=.*|pruning = "custom"|' \
  -e 's|^pruning-keep-recent *=.*|pruning-keep-recent = "100"|' \
  -e 's|^pruning-keep-every *=.*|pruning-keep-every = "0"|' \
  -e 's|^pruning-interval *=.*|pruning-interval = "19"|' \
  $HOME/.aura/config/app.toml
```

## 🚨 Maintenance

#### Get validator info

```bash
aurad status 2>&1 | jq .ValidatorInfo
```

#### Get sync info

```bash
aurad status 2>&1 | jq .SyncInfo
```

#### Get node peer

```bash
echo $(aurad tendermint show-node-id)'@'$(curl -s ifconfig.me)':'$(cat $HOME/.aura/config/config.toml | sed -n '/Address to listen for incoming connection/{n;p;}' | sed 's/.*://; s/".*//')
```

#### Check if validator key is correct

```bash
[[ $(aurad q staking validator $(aurad keys show wallet --bech val -a) -oj | jq -r .consensus_pubkey.key) = $(aurad status | jq -r .ValidatorInfo.PubKey.value) ]] && echo -e "\n\e[1m\e[32mTrue\e[0m\n" || echo -e "\n\e[1m\e[31mFalse\e[0m\n"
```

#### Get live peers

```bash
curl -sS http://localhost:11757/net_info | jq -r '.result.peers[] | "\(.node_info.id)@\(.remote_ip):\(.node_info.listen_addr)"' | awk -F ':' '{print $1":"$(NF)}'
```

#### Set minimum gas price

```bash
sed -i -e "s/^minimum-gas-prices *=.*/minimum-gas-prices = \"0ueaura\"/" $HOME/.aura/config/app.toml
```

#### Enable prometheus

```bash
sed -i -e "s/prometheus = false/prometheus = true/" $HOME/.aura/config/config.toml
```

#### Reset chain data

```bash
aurad tendermint unsafe-reset-all --keep-addr-book --home $HOME/.aura --keep-addr-book
```

#### Remove node

{% hint style='danger' %}
Please, before proceeding with the next step! All chain data will be lost! Make sure you have backed up your **priv_validator_key.json**!
{% endhint %}

```bash
cd $HOME
sudo systemctl stop aurad
sudo systemctl disable aurad
sudo rm /etc/systemd/system/aurad.service
sudo systemctl daemon-reload
rm -f $(which aurad)
rm -rf $HOME/.aura
rm -rf $HOME/aura
```

## ⚙️ Service Management

#### Reload service configuration

```bash
sudo systemctl daemon-reload
```

#### Enable service

```bash
sudo systemctl enable aurad
```

#### Disable service

```bash
sudo systemctl disable aurad
```

#### Start service

```bash
sudo systemctl start aurad
```

#### Stop service

```bash
sudo systemctl stop aurad
```

#### Restart service

```bash
sudo systemctl restart aurad
```

#### Check service status

```bash
sudo systemctl status aurad
```

#### Check service logs

```bash
sudo journalctl -u aurad -f --no-hostname -o cat
```
