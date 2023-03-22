---
description: Useful set of commands for node operators. From key management to chain governance.
---

# Useful commands

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/quasar.png" width="150" alt=""><figcaption></figcaption></figure>

## 🔑 Key management

#### Add new key

```bash
quasard keys add wallet
```

#### Recover existing key

```bash
quasard keys add wallet --recover
```

#### List all keys

```bash
quasard keys list
```

#### Delete key

```bash
quasard keys delete wallet
```

#### Export key to the file

```bash
quasard keys export wallet
```

#### Import key from the file

```bash
quasard keys import wallet wallet.backup
```

#### Query wallet balance

```bash
quasard q bank balances $(quasard keys show wallet -a)
```

## 👷 Validator management

{% hint style="info" %}
Please make sure you have adjusted **moniker**, **identity**, **details** and **website** to match your values.
{% endhint %}

#### Create new validator

```bash
quasard tx staking create-validator \
--amount 1000000uqsr \
--pubkey $(quasard tendermint show-validator) \
--moniker "YOUR_MONIKER_NAME" \
--identity "YOUR_KEYBASE_ID" \
--details "YOUR_DETAILS" \
--website "YOUR_WEBSITE_URL" \
--chain-id qsr-questnet-04 \
--commission-rate 0.05 \
--commission-max-rate 0.20 \
--commission-max-change-rate 0.01 \
--min-self-delegation 1 \
--from wallet \
--gas-adjustment 1.4 \
--gas auto \
--gas-prices 0uqsr \
-y
```

#### Edit existing validator

```bash
quasard tx staking edit-validator \
--new-moniker "YOUR_MONIKER_NAME" \
--identity "YOUR_KEYBASE_ID" \
--details "YOUR_DETAILS" \
--website "YOUR_WEBSITE_URL"
--chain-id qsr-questnet-04 \
--commission-rate 0.05 \
--from wallet \
--gas-adjustment 1.4 \
--gas auto \
--gas-prices 0uqsr \
-y
```

#### Unjail validator

```bash
quasard tx slashing unjail --from wallet --chain-id qsr-questnet-04 --gas-adjustment 1.4 --gas auto --gas-prices 0uqsr -y
```

#### Jail reason

```bash
quasard query slashing signing-info $(quasard tendermint show-validator)
```

#### List all active validators

```bash
quasard q staking validators -oj --limit=3000 | jq '.validators[] | select(.status=="BOND_STATUS_BONDED")' | jq -r '(.tokens|tonumber/pow(10; 6)|floor|tostring) + " \t " + .description.moniker' | sort -gr | nl
```

#### List all inactive validators

```bash
quasard q staking validators -oj --limit=3000 | jq '.validators[] | select(.status=="BOND_STATUS_UNBONDED")' | jq -r '(.tokens|tonumber/pow(10; 6)|floor|tostring) + " \t " + .description.moniker' | sort -gr | nl
```

#### View validator details

```bash
quasard q staking validator $(quasard keys show wallet --bech val -a)
```

## 💲 Token management

#### Withdraw rewards from all validators

```bash
quasard tx distribution withdraw-all-rewards --from wallet --chain-id qsr-questnet-04 --gas-adjustment 1.4 --gas auto --gas-prices 0uqsr -y
```

#### Withdraw commission and rewards from your validator

```bash
quasard tx distribution withdraw-rewards $(quasard keys show wallet --bech val -a) --commission --from wallet --chain-id qsr-questnet-04 --gas-adjustment 1.4 --gas auto --gas-prices 0uqsr -y
```

#### Delegate tokens to yourself

```bash
quasard tx staking delegate $(quasard keys show wallet --bech val -a) 1000000uqsr --from wallet --chain-id qsr-questnet-04 --gas-adjustment 1.4 --gas auto --gas-prices 0uqsr -y
```

#### Delegate tokens to validator

```bash
quasard tx staking delegate <TO_VALOPER_ADDRESS> 1000000uqsr --from wallet --chain-id qsr-questnet-04 --gas-adjustment 1.4 --gas auto --gas-prices 0uqsr -y
```

#### Redelegate tokens to another validator

```bash
quasard tx staking redelegate $(quasard keys show wallet --bech val -a) <TO_VALOPER_ADDRESS> 1000000uqsr --from wallet --chain-id qsr-questnet-04 --gas-adjustment 1.4 --gas auto --gas-prices 0uqsr -y
```

#### Unbond tokens from your validator

```bash
quasard tx staking unbond $(quasard keys show wallet --bech val -a) 1000000uqsr --from wallet --chain-id qsr-questnet-04 --gas-adjustment 1.4 --gas auto --gas-prices 0uqsr -y
```

#### Send tokens to the wallet

```bash
quasard tx bank send wallet <TO_WALLET_ADDRESS> 1000000uqsr --from wallet --chain-id qsr-questnet-04 --gas-adjustment 1.4 --gas auto --gas-prices 0uqsr -y
```

## 🗳 Governance

#### List all proposals

```bash
quasard query gov proposals
```

#### View proposal by id

```bash
quasard query gov proposal 1
```

#### Vote 'Yes'

```bash
quasard tx gov vote 1 yes --from wallet --chain-id qsr-questnet-04 --gas-adjustment 1.4 --gas auto --gas-prices 0uqsr -y
```

#### Vote 'No'

```bash
quasard tx gov vote 1 no --from wallet --chain-id qsr-questnet-04 --gas-adjustment 1.4 --gas auto --gas-prices 0uqsr -y
```

#### Vote 'Abstain'

```bash
quasard tx gov vote 1 abstain --from wallet --chain-id qsr-questnet-04 --gas-adjustment 1.4 --gas auto --gas-prices 0uqsr -y
```

#### Vote 'NoWithVeto'

```bash
quasard tx gov vote 1 NoWithVeto --from wallet --chain-id qsr-questnet-04 --gas-adjustment 1.4 --gas auto --gas-prices 0uqsr -y
```

## ⚡️ Utility

#### Update ports

```bash
CUSTOM_PORT=10
sed -i -e "s%^proxy_app = \"tcp://127.0.0.1:26658\"%proxy_app = \"tcp://127.0.0.1:${CUSTOM_PORT}658\"%; s%^laddr = \"tcp://127.0.0.1:26657\"%laddr = \"tcp://127.0.0.1:${CUSTOM_PORT}657\"%; s%^pprof_laddr = \"localhost:6060\"%pprof_laddr = \"localhost:${CUSTOM_PORT}060\"%; s%^laddr = \"tcp://0.0.0.0:26656\"%laddr = \"tcp://0.0.0.0:${CUSTOM_PORT}656\"%; s%^prometheus_listen_addr = \":26660\"%prometheus_listen_addr = \":${CUSTOM_PORT}660\"%" $HOME/.quasarnode/config/config.toml
sed -i -e "s%^address = \"tcp://0.0.0.0:1317\"%address = \"tcp://0.0.0.0:${CUSTOM_PORT}317\"%; s%^address = \":8080\"%address = \":${CUSTOM_PORT}080\"%; s%^address = \"0.0.0.0:9090\"%address = \"0.0.0.0:${CUSTOM_PORT}090\"%; s%^address = \"0.0.0.0:9091\"%address = \"0.0.0.0:${CUSTOM_PORT}091\"%" $HOME/.quasarnode/config/app.toml
```

#### Update Indexer

##### Disable indexer

```bash
sed -i -e 's|^indexer *=.*|indexer = "null"|' $HOME/.quasarnode/config/config.toml
```

##### Enable indexer

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
quasard status 2>&1 | jq .ValidatorInfo
```

#### Get sync info

```bash
quasard status 2>&1 | jq .SyncInfo
```

#### Get node peer

```bash
echo $(quasard tendermint show-node-id)'@'$(curl -s ifconfig.me)':'$(cat $HOME/.quasarnode/config/config.toml | sed -n '/Address to listen for incoming connection/{n;p;}' | sed 's/.*://; s/".*//')
```

#### Check if validator key is correct

```bash
[[ $(quasard q staking validator $(quasard keys show wallet --bech val -a) -oj | jq -r .consensus_pubkey.key) = $(quasard status | jq -r .ValidatorInfo.PubKey.value) ]] && echo -e "\n\e[1m\e[32mTrue\e[0m\n" || echo -e "\n\e[1m\e[31mFalse\e[0m\n"
```

#### Get live peers

```bash
curl -sS http://localhost:48657/net_info | jq -r '.result.peers[] | "\(.node_info.id)@\(.remote_ip):\(.node_info.listen_addr)"' | awk -F ':' '{print $1":"$(NF)}'
```

#### Set minimum gas price

```bash
sed -i -e "s/^minimum-gas-prices *=.*/minimum-gas-prices = \"0uqsr\"/" $HOME/.quasarnode/config/app.toml
```

#### Enable prometheus

```bash
sed -i -e "s/prometheus = false/prometheus = true/" $HOME/.quasarnode/config/config.toml
```

#### Reset chain data

```bash
quasard tendermint unsafe-reset-all --home $HOME/.quasarnode --keep-addr-book
```

#### Remove node

{% hint style='danger' %}
Please, before proceeding with the next step! All chain data will be lost! Make sure you have backed up your **priv_validator_key.json**!
{% endhint %}

```bash
cd $HOME
sudo systemctl stop quasard
sudo systemctl disable quasard
sudo rm /etc/systemd/system/quasard.service
sudo systemctl daemon-reload
rm -f $(which quasard)
rm -rf $HOME/.quasarnode
rm -rf $HOME/gravity-bin
```

## ⚙️ Service Management

#### Reload service configuration

```bash
sudo systemctl daemon-reload
```

#### Enable service

```bash
sudo systemctl enable quasard
```

#### Disable service

```bash
sudo systemctl disable quasard
```

#### Start service

```bash
sudo systemctl start quasard
```

#### Stop service

```bash
sudo systemctl stop quasard
```

#### Restart service

```bash
sudo systemctl restart quasard
```

#### Check service status

```bash
sudo systemctl status quasard
```

#### Check service logs

```bash
sudo journalctl -u quasard -f --no-hostname -o cat
```
