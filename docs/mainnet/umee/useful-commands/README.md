---
description: Useful set of commands for node operators. From key management to chain governance.
---

# Useful commands

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/umee.png" alt=""><figcaption></figcaption></figure>

## 🔑 Key management

#### Add new key

```bash
umeed keys add wallet
```

#### Recover existing key

```bash
umeed keys add wallet --recover
```

#### List all keys

```bash
umeed keys list
```

#### Delete key

```bash
umeed keys delete wallet
```

#### Export key to the file

```bash
umeed keys export wallet
```

#### Import key from the file

```bash
umeed keys import wallet wallet.backup
```

#### Query wallet balance

```bash
umeed q bank balances $(umeed keys show wallet -a)
```

## 👷 Validator management

{% hint style="info" %}
Please make sure you have adjusted **moniker**, **identity**, **details** and **website** to match your values.
{% endhint %}

#### Create new validator

```bash
umeed tx staking create-validator \
--amount 1000000uumee \
--pubkey $(umeed tendermint show-validator) \
--moniker "YOUR_MONIKER_NAME" \
--identity "YOUR_KEYBASE_ID" \
--details "YOUR_DETAILS" \
--website "YOUR_WEBSITE_URL" \
--chain-id umee-1 \
--commission-rate 0.05 \
--commission-max-rate 0.20 \
--commission-max-change-rate 0.01 \
--min-self-delegation 1 \
--from wallet \
--gas-adjustment 1.4 \
--gas auto \
--gas-prices 0.1uumee \
-y
```

#### Edit existing validator

```bash
umeed tx staking edit-validator \
--new-moniker "YOUR_MONIKER_NAME" \
--identity "YOUR_KEYBASE_ID" \
--details "YOUR_DETAILS" \
--website "YOUR_WEBSITE_URL" \
--chain-id umee-1 \
--commission-rate 0.05 \
--from wallet \
--gas-adjustment 1.4 \
--gas auto \
--gas-prices 0.1uumee \
-y
```

#### Unjail validator

```bash
umeed tx slashing unjail --from wallet --chain-id umee-1 --gas-adjustment 1.4 --gas auto --gas-prices 0.1uumee -y
```

#### Jail reason

```bash
umeed query slashing signing-info $(umeed tendermint show-validator)
```

#### List all active validators

```bash
umeed q staking validators -oj --limit=3000 | jq '.validators[] | select(.status=="BOND_STATUS_BONDED")' | jq -r '(.tokens|tonumber/pow(10; 6)|floor|tostring) + " \t " + .description.moniker' | sort -gr | nl
```

#### List all inactive validators

```bash
umeed q staking validators -oj --limit=3000 | jq '.validators[] | select(.status=="BOND_STATUS_UNBONDED")' | jq -r '(.tokens|tonumber/pow(10; 6)|floor|tostring) + " \t " + .description.moniker' | sort -gr | nl
```

#### View validator details

```bash
umeed q staking validator $(umeed keys show wallet --bech val -a)
```

## 💲 Token management

#### Withdraw rewards from all validators

```bash
umeed tx distribution withdraw-all-rewards --from wallet --chain-id umee-1 --gas-adjustment 1.4 --gas auto --gas-prices 0.1uumee -y
```

#### Withdraw commission and rewards from your validator

```bash
umeed tx distribution withdraw-rewards $(umeed keys show wallet --bech val -a) --commission --from wallet --chain-id umee-1 --gas-adjustment 1.4 --gas auto --gas-prices 0.1uumee -y
```

#### Delegate tokens to yourself

```bash
umeed tx staking delegate $(umeed keys show wallet --bech val -a) 1000000uumee --from wallet --chain-id umee-1 --gas-adjustment 1.4 --gas auto --gas-prices 0.1uumee -y
```

#### Delegate tokens to validator

```bash
umeed tx staking delegate <TO_VALOPER_ADDRESS> 1000000uumee --from wallet --chain-id umee-1 --gas-adjustment 1.4 --gas auto --gas-prices 0.1uumee -y
```

#### Redelegate tokens to another validator

```bash
umeed tx staking redelegate $(umeed keys show wallet --bech val -a) <TO_VALOPER_ADDRESS> 1000000uumee --from wallet --chain-id umee-1 --gas-adjustment 1.4 --gas auto --gas-prices 0.1uumee -y
```

#### Unbond tokens from your validator

```bash
umeed tx staking unbond $(umeed keys show wallet --bech val -a) 1000000uumee --from wallet --chain-id umee-1 --gas-adjustment 1.4 --gas auto --gas-prices 0.1uumee -y
```

#### Send tokens to the wallet

```bash
umeed tx bank send wallet <TO_WALLET_ADDRESS> 1000000uumee --from wallet --chain-id umee-1 --gas-adjustment 1.4 --gas auto --gas-prices 0.1uumee -y
```

## 🗳 Governance

#### List all proposals

```bash
umeed query gov proposals
```

#### View proposal by id

```bash
umeed query gov proposal 1
```

#### Vote 'Yes'

```bash
umeed tx gov vote 1 yes --from wallet --chain-id umee-1 --gas-adjustment 1.4 --gas auto --gas-prices 0.1uumee -y
```

#### Vote 'No'

```bash
umeed tx gov vote 1 no --from wallet --chain-id umee-1 --gas-adjustment 1.4 --gas auto --gas-prices 0.1uumee -y
```

#### Vote 'Abstain'

```bash
umeed tx gov vote 1 abstain --from wallet --chain-id umee-1 --gas-adjustment 1.4 --gas auto --gas-prices 0.1uumee -y
```

#### Vote 'NoWithVeto'

```bash
umeed tx gov vote 1 NoWithVeto --from wallet --chain-id umee-1 --gas-adjustment 1.4 --gas auto --gas-prices 0.1uumee -y
```

## ⚡️ Utility

#### Update ports

```bash
CUSTOM_PORT=110
sed -i -e "s%^proxy_app = \"tcp://127.0.0.1:26658\"%proxy_app = \"tcp://127.0.0.1:${CUSTOM_PORT}58\"%; s%^laddr = \"tcp://127.0.0.1:26657\"%laddr = \"tcp://127.0.0.1:${CUSTOM_PORT}57\"%; s%^pprof_laddr = \"localhost:6060\"%pprof_laddr = \"localhost:${CUSTOM_PORT}60\"%; s%^laddr = \"tcp://0.0.0.0:26656\"%laddr = \"tcp://0.0.0.0:${CUSTOM_PORT}56\"%; s%^prometheus_listen_addr = \":26660\"%prometheus_listen_addr = \":${CUSTOM_PORT}66\"%" $HOME/.umee/config/config.toml
sed -i -e "s%^address = \"tcp://0.0.0.0:1317\"%address = \"tcp://0.0.0.0:${CUSTOM_PORT}17\"%; s%^address = \":8080\"%address = \":${CUSTOM_PORT}80\"%; s%^address = \"0.0.0.0:9090\"%address = \"0.0.0.0:${CUSTOM_PORT}90\"%; s%^address = \"0.0.0.0:9091\"%address = \"0.0.0.0:${CUSTOM_PORT}91\"%" $HOME/.umee/config/app.toml
```

#### Update Indexer

**Disable indexer**

```bash
sed -i -e 's|^indexer *=.*|indexer = "null"|' $HOME/.umee/config/config.toml
```

**Enable indexer**

```bash
sed -i -e 's|^indexer *=.*|indexer = "kv"|' $HOME/.umee/config/config.toml
```

#### Update pruning

```bash
sed -i \
  -e 's|^pruning *=.*|pruning = "custom"|' \
  -e 's|^pruning-keep-recent *=.*|pruning-keep-recent = "100"|' \
  -e 's|^pruning-keep-every *=.*|pruning-keep-every = "0"|' \
  -e 's|^pruning-interval *=.*|pruning-interval = "19"|' \
  $HOME/.umee/config/app.toml
```

## 🚨 Maintenance

#### Get validator info

```bash
umeed status 2>&1 | jq .ValidatorInfo
```

#### Get sync info

```bash
umeed status 2>&1 | jq .SyncInfo
```

#### Get node peer

```bash
echo $(umeed tendermint show-node-id)'@'$(curl -s ifconfig.me)':'$(cat $HOME/.umee/config/config.toml | sed -n '/Address to listen for incoming connection/{n;p;}' | sed 's/.*://; s/".*//')
```

#### Check if validator key is correct

```bash
[[ $(umeed q staking validator $(umeed keys show wallet --bech val -a) -oj | jq -r .consensus_pubkey.key) = $(umeed status | jq -r .ValidatorInfo.PubKey.value) ]] && echo -e "\n\e[1m\e[32mTrue\e[0m\n" || echo -e "\n\e[1m\e[31mFalse\e[0m\n"
```

#### Get live peers

```bash
curl -sS http://localhost:16257/net_info | jq -r '.result.peers[] | "\(.node_info.id)@\(.remote_ip):\(.node_info.listen_addr)"' | awk -F ':' '{print $1":"$(NF)}'
```

#### Set minimum gas price

```bash
sed -i -e "s/^minimum-gas-prices *=.*/minimum-gas-prices = \"0.1uumee\"/" $HOME/.umee/config/app.toml
```

#### Enable prometheus

```bash
sed -i -e "s/prometheus = false/prometheus = true/" $HOME/.umee/config/config.toml
```

#### Reset chain data

```bash
umeed tendermint unsafe-reset-all --keep-addr-book --home $HOME/.umee --keep-addr-book
```

#### Remove node

{% hint style='danger' %}
Please, before proceeding with the next step! All chain data will be lost! Make sure you have backed up your **priv_validator_key.json**!
{% endhint %}

```bash
cd $HOME
sudo systemctl stop umeed
sudo systemctl disable umeed
sudo rm /etc/systemd/system/umeed.service
sudo systemctl daemon-reload
rm -f $(which umeed)
rm -rf $HOME/.umee
rm -rf $HOME/umee
```

## ⚙️ Service Management

#### Reload service configuration

```bash
sudo systemctl daemon-reload
```

#### Enable service

```bash
sudo systemctl enable umeed
```

#### Disable service

```bash
sudo systemctl disable umeed
```

#### Start service

```bash
sudo systemctl start umeed
```

#### Stop service

```bash
sudo systemctl stop umeed
```

#### Restart service

```bash
sudo systemctl restart umeed
```

#### Check service status

```bash
sudo systemctl status umeed
```

#### Check service logs

```bash
sudo journalctl -u umeed -f --no-hostname -o cat
```
