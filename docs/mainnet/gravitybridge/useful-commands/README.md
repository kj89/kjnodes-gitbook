---
description: Useful set of commands for node operators. From key management to chain governance.
---

# Useful commands

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/gravitybridge.png" width="150" alt=""><figcaption></figcaption></figure>

## 🔑 Key management

#### Add new key

```bash
gravityd keys add wallet
```

#### Recover existing key

```bash
gravityd keys add wallet --recover
```

#### List all keys

```bash
gravityd keys list
```

#### Delete key

```bash
gravityd keys delete wallet
```

#### Export key to the file

```bash
gravityd keys export wallet
```

#### Import key from the file

```bash
gravityd keys import wallet wallet.backup
```

#### Query wallet balance

```bash
gravityd q bank balances $(gravityd keys show wallet -a)
```

## 👷 Validator management

{% hint style="info" %}
Please make sure you have adjusted **moniker**, **identity**, **details** and **website** to match your values.
{% endhint %}

#### Create new validator

```bash
gravityd tx staking create-validator \
--amount 1000000ugraviton \
--pubkey $(gravityd tendermint show-validator) \
--moniker "YOUR_MONIKER_NAME" \
--identity "YOUR_KEYBASE_ID" \
--details "YOUR_DETAILS" \
--website "YOUR_WEBSITE_URL" \
--chain-id gravity-bridge-3 \
--commission-rate 0.05 \
--commission-max-rate 0.20 \
--commission-max-change-rate 0.01 \
--min-self-delegation 1 \
--from wallet \
--gas-adjustment 1.4 \
--gas auto \
--gas-prices 0ugraviton \
-y
```

#### Edit existing validator

```bash
gravityd tx staking edit-validator \
--new-moniker "YOUR_MONIKER_NAME" \
--identity "YOUR_KEYBASE_ID" \
--details "YOUR_DETAILS" \
--website "YOUR_WEBSITE_URL" \
--chain-id gravity-bridge-3 \
--commission-rate 0.05 \
--from wallet \
--gas-adjustment 1.4 \
--gas auto \
--gas-prices 0ugraviton \
-y
```

#### Unjail validator

```bash
gravityd tx slashing unjail --from wallet --chain-id gravity-bridge-3 --gas-adjustment 1.4 --gas auto --gas-prices 0ugraviton -y
```

#### Jail reason

```bash
gravityd query slashing signing-info $(gravityd tendermint show-validator)
```

#### List all active validators

```bash
gravityd q staking validators -oj --limit=3000 | jq '.validators[] | select(.status=="BOND_STATUS_BONDED")' | jq -r '(.tokens|tonumber/pow(10; 6)|floor|tostring) + " \t " + .description.moniker' | sort -gr | nl
```

#### List all inactive validators

```bash
gravityd q staking validators -oj --limit=3000 | jq '.validators[] | select(.status=="BOND_STATUS_UNBONDED")' | jq -r '(.tokens|tonumber/pow(10; 6)|floor|tostring) + " \t " + .description.moniker' | sort -gr | nl
```

#### View validator details

```bash
gravityd q staking validator $(gravityd keys show wallet --bech val -a)
```

## 💲 Token management

#### Withdraw rewards from all validators

```bash
gravityd tx distribution withdraw-all-rewards --from wallet --chain-id gravity-bridge-3 --gas-adjustment 1.4 --gas auto --gas-prices 0ugraviton -y
```

#### Withdraw commission and rewards from your validator

```bash
gravityd tx distribution withdraw-rewards $(gravityd keys show wallet --bech val -a) --commission --from wallet --chain-id gravity-bridge-3 --gas-adjustment 1.4 --gas auto --gas-prices 0ugraviton -y
```

#### Delegate tokens to yourself

```bash
gravityd tx staking delegate $(gravityd keys show wallet --bech val -a) 1000000ugraviton --from wallet --chain-id gravity-bridge-3 --gas-adjustment 1.4 --gas auto --gas-prices 0ugraviton -y
```

#### Delegate tokens to validator

```bash
gravityd tx staking delegate <TO_VALOPER_ADDRESS> 1000000ugraviton --from wallet --chain-id gravity-bridge-3 --gas-adjustment 1.4 --gas auto --gas-prices 0ugraviton -y
```

#### Redelegate tokens to another validator

```bash
gravityd tx staking redelegate $(gravityd keys show wallet --bech val -a) <TO_VALOPER_ADDRESS> 1000000ugraviton --from wallet --chain-id gravity-bridge-3 --gas-adjustment 1.4 --gas auto --gas-prices 0ugraviton -y
```

#### Unbond tokens from your validator

```bash
gravityd tx staking unbond $(gravityd keys show wallet --bech val -a) 1000000ugraviton --from wallet --chain-id gravity-bridge-3 --gas-adjustment 1.4 --gas auto --gas-prices 0ugraviton -y
```

#### Send tokens to the wallet

```bash
gravityd tx bank send wallet <TO_WALLET_ADDRESS> 1000000ugraviton --from wallet --chain-id gravity-bridge-3 --gas-adjustment 1.4 --gas auto --gas-prices 0ugraviton -y
```

## 🗳 Governance

#### List all proposals

```bash
gravityd query gov proposals
```

#### View proposal by id

```bash
gravityd query gov proposal 1
```

#### Vote 'Yes'

```bash
gravityd tx gov vote 1 yes --from wallet --chain-id gravity-bridge-3 --gas-adjustment 1.4 --gas auto --gas-prices 0ugraviton -y
```

#### Vote 'No'

```bash
gravityd tx gov vote 1 no --from wallet --chain-id gravity-bridge-3 --gas-adjustment 1.4 --gas auto --gas-prices 0ugraviton -y
```

#### Vote 'Abstain'

```bash
gravityd tx gov vote 1 abstain --from wallet --chain-id gravity-bridge-3 --gas-adjustment 1.4 --gas auto --gas-prices 0ugraviton -y
```

#### Vote 'NoWithVeto'

```bash
gravityd tx gov vote 1 NoWithVeto --from wallet --chain-id gravity-bridge-3 --gas-adjustment 1.4 --gas auto --gas-prices 0ugraviton -y
```

## ⚡️ Utility

#### Update ports

```bash
CUSTOM_PORT=10
sed -i -e "s%^proxy_app = \"tcp://127.0.0.1:26658\"%proxy_app = \"tcp://127.0.0.1:${CUSTOM_PORT}658\"%; s%^laddr = \"tcp://127.0.0.1:26657\"%laddr = \"tcp://127.0.0.1:${CUSTOM_PORT}657\"%; s%^pprof_laddr = \"localhost:6060\"%pprof_laddr = \"localhost:${CUSTOM_PORT}060\"%; s%^laddr = \"tcp://0.0.0.0:26656\"%laddr = \"tcp://0.0.0.0:${CUSTOM_PORT}656\"%; s%^prometheus_listen_addr = \":26660\"%prometheus_listen_addr = \":${CUSTOM_PORT}660\"%" $HOME/.gravity/config/config.toml
sed -i -e "s%^address = \"tcp://0.0.0.0:1317\"%address = \"tcp://0.0.0.0:${CUSTOM_PORT}317\"%; s%^address = \":8080\"%address = \":${CUSTOM_PORT}080\"%; s%^address = \"0.0.0.0:9090\"%address = \"0.0.0.0:${CUSTOM_PORT}090\"%; s%^address = \"0.0.0.0:9091\"%address = \"0.0.0.0:${CUSTOM_PORT}091\"%" $HOME/.gravity/config/app.toml
```

#### Update Indexer

**Disable indexer**

```bash
sed -i -e 's|^indexer *=.*|indexer = "null"|' $HOME/.gravity/config/config.toml
```

**Enable indexer**

```bash
sed -i -e 's|^indexer *=.*|indexer = "kv"|' $HOME/.gravity/config/config.toml
```

#### Update pruning

```bash
sed -i \
  -e 's|^pruning *=.*|pruning = "custom"|' \
  -e 's|^pruning-keep-recent *=.*|pruning-keep-recent = "100"|' \
  -e 's|^pruning-keep-every *=.*|pruning-keep-every = "0"|' \
  -e 's|^pruning-interval *=.*|pruning-interval = "19"|' \
  $HOME/.gravity/config/app.toml
```

## 🚨 Maintenance

#### Get validator info

```bash
gravityd status 2>&1 | jq .ValidatorInfo
```

#### Get sync info

```bash
gravityd status 2>&1 | jq .SyncInfo
```

#### Get node peer

```bash
echo $(gravityd tendermint show-node-id)'@'$(curl -s ifconfig.me)':'$(cat $HOME/.gravity/config/config.toml | sed -n '/Address to listen for incoming connection/{n;p;}' | sed 's/.*://; s/".*//')
```

#### Check if validator key is correct

```bash
[[ $(gravityd q staking validator $(gravityd keys show wallet --bech val -a) -oj | jq -r .consensus_pubkey.key) = $(gravityd status | jq -r .ValidatorInfo.PubKey.value) ]] && echo -e "\n\e[1m\e[32mTrue\e[0m\n" || echo -e "\n\e[1m\e[31mFalse\e[0m\n"
```

#### Get live peers

```bash
curl -sS http://localhost:26657/net_info | jq -r '.result.peers[] | "\(.node_info.id)@\(.remote_ip):\(.node_info.listen_addr)"' | awk -F ':' '{print $1":"$(NF)}'
```

#### Set minimum gas price

```bash
sed -i -e "s/^minimum-gas-prices *=.*/minimum-gas-prices = \"0ugraviton\"/" $HOME/.gravity/config/app.toml
```

#### Enable prometheus

```bash
sed -i -e "s/prometheus = false/prometheus = true/" $HOME/.gravity/config/config.toml
```

#### Reset chain data

```bash
gravityd tendermint unsafe-reset-all --home $HOME/.gravity --keep-addr-book
```

#### Remove node

{% hint style='danger' %}
Please, before proceeding with the next step! All chain data will be lost! Make sure you have backed up your **priv_validator_key.json**!
{% endhint %}

```bash
cd $HOME
sudo systemctl stop gravityd
sudo systemctl disable gravityd
sudo rm /etc/systemd/system/gravityd.service
sudo systemctl daemon-reload
rm -f $(which gravityd)
rm -rf $HOME/.gravity
rm -rf $HOME/gravity-bin
```

## ⚙️ Service Management

#### Reload service configuration

```bash
sudo systemctl daemon-reload
```

#### Enable service

```bash
sudo systemctl enable gravityd
```

#### Disable service

```bash
sudo systemctl disable gravityd
```

#### Start service

```bash
sudo systemctl start gravityd
```

#### Stop service

```bash
sudo systemctl stop gravityd
```

#### Restart service

```bash
sudo systemctl restart gravityd
```

#### Check service status

```bash
sudo systemctl status gravityd
```

#### Check service logs

```bash
sudo journalctl -u gravityd -f --no-hostname -o cat
```
