---
description: Useful set of commands for node operators. From key management to chain governance.
---

# Useful commands

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/haqq.png" alt=""><figcaption></figcaption></figure>

## 🔑 Key management

#### Add new key

```bash
haqqd keys add wallet
```

#### Recover existing key

```bash
haqqd keys add wallet --recover
```

#### List all keys

```bash
haqqd keys list
```

#### Delete key

```bash
haqqd keys delete wallet
```

#### Export key to the file

```bash
haqqd keys export wallet
```

#### Import key from the file

```bash
haqqd keys import wallet wallet.backup
```

#### Query wallet balance

```bash
haqqd q bank balances $(haqqd keys show wallet -a)
```

## 👷 Validator management

{% hint style="info" %}
Please make sure you have adjusted **moniker**, **identity**, **details** and **website** to match your values.
{% endhint %}

#### Create new validator

```bash
haqqd tx staking create-validator \
--amount 1000000aISLM \
--pubkey $(haqqd tendermint show-validator) \
--moniker "YOUR_MONIKER_NAME" \
--identity "YOUR_KEYBASE_ID" \
--details "YOUR_DETAILS" \
--website "YOUR_WEBSITE_URL" \
--chain-id haqq_54211-3 \
--commission-rate 0.05 \
--commission-max-rate 0.20 \
--commission-max-change-rate 0.01 \
--min-self-delegation 1 \
--from wallet \
--gas-adjustment 1.4 \
--gas auto \
--gas-prices 0aISLM \
-y
```

#### Edit existing validator

```bash
haqqd tx staking edit-validator \
--new-moniker "YOUR_MONIKER_NAME" \
--identity "YOUR_KEYBASE_ID" \
--details "YOUR_DETAILS" \
--website "YOUR_WEBSITE_URL" \
--chain-id haqq_54211-3 \
--commission-rate 0.05 \
--from wallet \
--gas-adjustment 1.4 \
--gas auto \
--gas-prices 0aISLM \
-y
```

#### Unjail validator

```bash
haqqd tx slashing unjail --from wallet --chain-id haqq_54211-3 --gas-adjustment 1.4 --gas auto --gas-prices 0aISLM -y
```

#### Jail reason

```bash
haqqd query slashing signing-info $(haqqd tendermint show-validator)
```

#### List all active validators

```bash
haqqd q staking validators -oj --limit=3000 | jq '.validators[] | select(.status=="BOND_STATUS_BONDED")' | jq -r '(.tokens|tonumber/pow(10; 6)|floor|tostring) + " \t " + .description.moniker' | sort -gr | nl
```

#### List all inactive validators

```bash
haqqd q staking validators -oj --limit=3000 | jq '.validators[] | select(.status=="BOND_STATUS_UNBONDED")' | jq -r '(.tokens|tonumber/pow(10; 6)|floor|tostring) + " \t " + .description.moniker' | sort -gr | nl
```

#### View validator details

```bash
haqqd q staking validator $(haqqd keys show wallet --bech val -a)
```

## 💲 Token management

#### Withdraw rewards from all validators

```bash
haqqd tx distribution withdraw-all-rewards --from wallet --chain-id haqq_54211-3 --gas-adjustment 1.4 --gas auto --gas-prices 0aISLM -y
```

#### Withdraw commission and rewards from your validator

```bash
haqqd tx distribution withdraw-rewards $(haqqd keys show wallet --bech val -a) --commission --from wallet --chain-id haqq_54211-3 --gas-adjustment 1.4 --gas auto --gas-prices 0aISLM -y
```

#### Delegate tokens to yourself

```bash
haqqd tx staking delegate $(haqqd keys show wallet --bech val -a) 1000000aISLM --from wallet --chain-id haqq_54211-3 --gas-adjustment 1.4 --gas auto --gas-prices 0aISLM -y
```

#### Delegate tokens to validator

```bash
haqqd tx staking delegate <TO_VALOPER_ADDRESS> 1000000aISLM --from wallet --chain-id haqq_54211-3 --gas-adjustment 1.4 --gas auto --gas-prices 0aISLM -y
```

#### Redelegate tokens to another validator

```bash
haqqd tx staking redelegate $(haqqd keys show wallet --bech val -a) <TO_VALOPER_ADDRESS> 1000000aISLM --from wallet --chain-id haqq_54211-3 --gas-adjustment 1.4 --gas auto --gas-prices 0aISLM -y
```

#### Unbond tokens from your validator

```bash
haqqd tx staking unbond $(haqqd keys show wallet --bech val -a) 1000000aISLM --from wallet --chain-id haqq_54211-3 --gas-adjustment 1.4 --gas auto --gas-prices 0aISLM -y
```

#### Send tokens to the wallet

```bash
haqqd tx bank send wallet <TO_WALLET_ADDRESS> 1000000aISLM --from wallet --chain-id haqq_54211-3 --gas-adjustment 1.4 --gas auto --gas-prices 0aISLM -y
```

## 🗳 Governance

#### List all proposals

```bash
haqqd query gov proposals
```

#### View proposal by id

```bash
haqqd query gov proposal 1
```

#### Vote 'Yes'

```bash
haqqd tx gov vote 1 yes --from wallet --chain-id haqq_54211-3 --gas-adjustment 1.4 --gas auto --gas-prices 0aISLM -y
```

#### Vote 'No'

```bash
haqqd tx gov vote 1 no --from wallet --chain-id haqq_54211-3 --gas-adjustment 1.4 --gas auto --gas-prices 0aISLM -y
```

#### Vote 'Abstain'

```bash
haqqd tx gov vote 1 abstain --from wallet --chain-id haqq_54211-3 --gas-adjustment 1.4 --gas auto --gas-prices 0aISLM -y
```

#### Vote 'NoWithVeto'

```bash
haqqd tx gov vote 1 NoWithVeto --from wallet --chain-id haqq_54211-3 --gas-adjustment 1.4 --gas auto --gas-prices 0aISLM -y
```

## ⚡️ Utility

#### Update ports

```bash
CUSTOM_PORT=110
sed -i -e "s%^proxy_app = \"tcp://127.0.0.1:26658\"%proxy_app = \"tcp://127.0.0.1:${CUSTOM_PORT}58\"%; s%^laddr = \"tcp://127.0.0.1:26657\"%laddr = \"tcp://127.0.0.1:${CUSTOM_PORT}57\"%; s%^pprof_laddr = \"localhost:6060\"%pprof_laddr = \"localhost:${CUSTOM_PORT}60\"%; s%^laddr = \"tcp://0.0.0.0:26656\"%laddr = \"tcp://0.0.0.0:${CUSTOM_PORT}56\"%; s%^prometheus_listen_addr = \":26660\"%prometheus_listen_addr = \":${CUSTOM_PORT}66\"%" $HOME/.haqqd/config/config.toml
sed -i -e "s%^address = \"tcp://0.0.0.0:1317\"%address = \"tcp://0.0.0.0:${CUSTOM_PORT}17\"%; s%^address = \":8080\"%address = \":${CUSTOM_PORT}80\"%; s%^address = \"0.0.0.0:9090\"%address = \"0.0.0.0:${CUSTOM_PORT}90\"%; s%^address = \"0.0.0.0:9091\"%address = \"0.0.0.0:${CUSTOM_PORT}91\"%" $HOME/.haqqd/config/app.toml
```

#### Update Indexer

**Disable indexer**

```bash
sed -i -e 's|^indexer *=.*|indexer = "null"|' $HOME/.haqqd/config/config.toml
```

**Enable indexer**

```bash
sed -i -e 's|^indexer *=.*|indexer = "kv"|' $HOME/.haqqd/config/config.toml
```

#### Update pruning

```bash
sed -i \
  -e 's|^pruning *=.*|pruning = "custom"|' \
  -e 's|^pruning-keep-recent *=.*|pruning-keep-recent = "100"|' \
  -e 's|^pruning-keep-every *=.*|pruning-keep-every = "0"|' \
  -e 's|^pruning-interval *=.*|pruning-interval = "19"|' \
  $HOME/.haqqd/config/app.toml
```

## 🚨 Maintenance

#### Get validator info

```bash
haqqd status 2>&1 | jq .ValidatorInfo
```

#### Get sync info

```bash
haqqd status 2>&1 | jq .SyncInfo
```

#### Get node peer

```bash
echo $(haqqd tendermint show-node-id)'@'$(curl -s ifconfig.me)':'$(cat $HOME/.haqqd/config/config.toml | sed -n '/Address to listen for incoming connection/{n;p;}' | sed 's/.*://; s/".*//')
```

#### Check if validator key is correct

```bash
[[ $(haqqd q staking validator $(haqqd keys show wallet --bech val -a) -oj | jq -r .consensus_pubkey.key) = $(haqqd status | jq -r .ValidatorInfo.PubKey.value) ]] && echo -e "\n\e[1m\e[32mTrue\e[0m\n" || echo -e "\n\e[1m\e[31mFalse\e[0m\n"
```

#### Get live peers

```bash
curl -sS http://localhost:13557/net_info | jq -r '.result.peers[] | "\(.node_info.id)@\(.remote_ip):\(.node_info.listen_addr)"' | awk -F ':' '{print $1":"$(NF)}'
```

#### Set minimum gas price

```bash
sed -i -e "s/^minimum-gas-prices *=.*/minimum-gas-prices = \"0aISLM\"/" $HOME/.haqqd/config/app.toml
```

#### Enable prometheus

```bash
sed -i -e "s/prometheus = false/prometheus = true/" $HOME/.haqqd/config/config.toml
```

#### Reset chain data

```bash
haqqd tendermint unsafe-reset-all --home $HOME/.haqqd --keep-addr-book
```

#### Remove node

{% hint style='danger' %}
Please, before proceeding with the next step! All chain data will be lost! Make sure you have backed up your **priv_validator_key.json**!
{% endhint %}

```bash
cd $HOME
sudo systemctl stop haqqd
sudo systemctl disable haqqd
sudo rm /etc/systemd/system/haqqd.service
sudo systemctl daemon-reload
rm -f $(which haqqd)
rm -rf $HOME/.haqqd
rm -rf $HOME/haqq
```

## ⚙️ Service Management

#### Reload service configuration

```bash
sudo systemctl daemon-reload
```

#### Enable service

```bash
sudo systemctl enable haqqd
```

#### Disable service

```bash
sudo systemctl disable haqqd
```

#### Start service

```bash
sudo systemctl start haqqd
```

#### Stop service

```bash
sudo systemctl stop haqqd
```

#### Restart service

```bash
sudo systemctl restart haqqd
```

#### Check service status

```bash
sudo systemctl status haqqd
```

#### Check service logs

```bash
sudo journalctl -u haqqd -f --no-hostname -o cat
```
