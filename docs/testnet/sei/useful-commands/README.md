---
description: Useful set of commands for node operators. From key management to chain governance.
---

# Useful commands

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/sei.png" width="150" alt=""><figcaption></figcaption></figure>

## 🔑 Key management

#### Add new key

```bash
seid keys add wallet
```

#### Recover existing key

```bash
seid keys add wallet --recover
```

#### List all keys

```bash
seid keys list
```

#### Delete key

```bash
seid keys delete wallet
```

#### Export key to the file

```bash
seid keys export wallet
```

#### Import key from the file

```bash
seid keys import wallet wallet.backup
```

#### Query wallet balance

```bash
seid q bank balances $(seid keys show wallet -a)
```

## 👷 Validator management

{% hint style="info" %}
Please make sure you have adjusted **moniker**, **identity**, **details** and **website** to match your values.
{% endhint %}

#### Create new validator

```bash
seid tx staking create-validator \
--amount 1000000usei \
--pubkey $(seid tendermint show-validator) \
--moniker "YOUR_MONIKER_NAME" \
--identity "YOUR_KEYBASE_ID" \
--details "YOUR_DETAILS" \
--website "YOUR_WEBSITE_URL" \
--chain-id atlantic-2 \
--commission-rate 0.05 \
--commission-max-rate 0.20 \
--commission-max-change-rate 0.01 \
--min-self-delegation 1 \
--from wallet \
--gas-adjustment 1.4 \
--gas auto \
--gas-prices 0.0001usei \
-y
```

#### Edit existing validator

```bash
seid tx staking edit-validator \
--new-moniker "YOUR_MONIKER_NAME" \
--identity "YOUR_KEYBASE_ID" \
--details "YOUR_DETAILS" \
--website "YOUR_WEBSITE_URL"
--chain-id atlantic-2 \
--commission-rate 0.05 \
--from wallet \
--gas-adjustment 1.4 \
--gas auto \
--gas-prices 0.0001usei \
-y
```

#### Unjail validator

```bash
seid tx slashing unjail --from wallet --chain-id atlantic-2 --gas-adjustment 1.4 --gas auto --gas-prices 0.0001usei -y
```

#### Jail reason

```bash
seid query slashing signing-info $(seid tendermint show-validator)
```

#### List all active validators

```bash
seid q staking validators -oj --limit=3000 | jq '.validators[] | select(.status=="BOND_STATUS_BONDED")' | jq -r '(.tokens|tonumber/pow(10; 6)|floor|tostring) + " \t " + .description.moniker' | sort -gr | nl
```

#### List all inactive validators

```bash
seid q staking validators -oj --limit=3000 | jq '.validators[] | select(.status=="BOND_STATUS_UNBONDED")' | jq -r '(.tokens|tonumber/pow(10; 6)|floor|tostring) + " \t " + .description.moniker' | sort -gr | nl
```

#### View validator details

```bash
seid q staking validator $(seid keys show wallet --bech val -a)
```

## 💲 Token management

#### Withdraw rewards from all validators

```bash
seid tx distribution withdraw-all-rewards --from wallet --chain-id atlantic-2 --gas-adjustment 1.4 --gas auto --gas-prices 0.0001usei -y
```

#### Withdraw commission and rewards from your validator

```bash
seid tx distribution withdraw-rewards $(seid keys show wallet --bech val -a) --commission --from wallet --chain-id atlantic-2 --gas-adjustment 1.4 --gas auto --gas-prices 0.0001usei -y
```

#### Delegate tokens to yourself

```bash
seid tx staking delegate $(seid keys show wallet --bech val -a) 1000000usei --from wallet --chain-id atlantic-2 --gas-adjustment 1.4 --gas auto --gas-prices 0.0001usei -y
```

#### Delegate tokens to validator

```bash
seid tx staking delegate <TO_VALOPER_ADDRESS> 1000000usei --from wallet --chain-id atlantic-2 --gas-adjustment 1.4 --gas auto --gas-prices 0.0001usei -y
```

#### Redelegate tokens to another validator

```bash
seid tx staking redelegate $(seid keys show wallet --bech val -a) <TO_VALOPER_ADDRESS> 1000000usei --from wallet --chain-id atlantic-2 --gas-adjustment 1.4 --gas auto --gas-prices 0.0001usei -y
```

#### Unbond tokens from your validator

```bash
seid tx staking unbond $(seid keys show wallet --bech val -a) 1000000usei --from wallet --chain-id atlantic-2 --gas-adjustment 1.4 --gas auto --gas-prices 0.0001usei -y
```

#### Send tokens to the wallet

```bash
seid tx bank send wallet <TO_WALLET_ADDRESS> 1000000usei --from wallet --chain-id atlantic-2 --gas-adjustment 1.4 --gas auto --gas-prices 0.0001usei -y
```

## 🗳 Governance

#### List all proposals

```bash
seid query gov proposals
```

#### View proposal by id

```bash
seid query gov proposal 1
```

#### Vote 'Yes'

```bash
seid tx gov vote 1 yes --from wallet --chain-id atlantic-2 --gas-adjustment 1.4 --gas auto --gas-prices 0.0001usei -y
```

#### Vote 'No'

```bash
seid tx gov vote 1 no --from wallet --chain-id atlantic-2 --gas-adjustment 1.4 --gas auto --gas-prices 0.0001usei -y
```

#### Vote 'Abstain'

```bash
seid tx gov vote 1 abstain --from wallet --chain-id atlantic-2 --gas-adjustment 1.4 --gas auto --gas-prices 0.0001usei -y
```

#### Vote 'NoWithVeto'

```bash
seid tx gov vote 1 NoWithVeto --from wallet --chain-id atlantic-2 --gas-adjustment 1.4 --gas auto --gas-prices 0.0001usei -y
```

## ⚡️ Utility

#### Update ports

```bash
CUSTOM_PORT=10
sed -i -e "s%^proxy_app = \"tcp://127.0.0.1:26658\"%proxy_app = \"tcp://127.0.0.1:${CUSTOM_PORT}658\"%; s%^laddr = \"tcp://127.0.0.1:26657\"%laddr = \"tcp://127.0.0.1:${CUSTOM_PORT}657\"%; s%^pprof_laddr = \"localhost:6060\"%pprof_laddr = \"localhost:${CUSTOM_PORT}060\"%; s%^laddr = \"tcp://0.0.0.0:26656\"%laddr = \"tcp://0.0.0.0:${CUSTOM_PORT}656\"%; s%^prometheus_listen_addr = \":26660\"%prometheus_listen_addr = \":${CUSTOM_PORT}660\"%" $HOME/.sei/config/config.toml
sed -i -e "s%^address = \"tcp://0.0.0.0:1317\"%address = \"tcp://0.0.0.0:${CUSTOM_PORT}317\"%; s%^address = \":8080\"%address = \":${CUSTOM_PORT}080\"%; s%^address = \"0.0.0.0:9090\"%address = \"0.0.0.0:${CUSTOM_PORT}090\"%; s%^address = \"0.0.0.0:9091\"%address = \"0.0.0.0:${CUSTOM_PORT}091\"%" $HOME/.sei/config/app.toml
```

#### Update Indexer

##### Disable indexer

```bash
sed -i -e 's|^indexer *=.*|indexer = "null"|' $HOME/.sei/config/config.toml
```

##### Enable indexer

```bash
sed -i -e 's|^indexer *=.*|indexer = "kv"|' $HOME/.sei/config/config.toml
```

#### Update pruning

```bash
sed -i \
  -e 's|^pruning *=.*|pruning = "custom"|' \
  -e 's|^pruning-keep-recent *=.*|pruning-keep-recent = "100"|' \
  -e 's|^pruning-keep-every *=.*|pruning-keep-every = "0"|' \
  -e 's|^pruning-interval *=.*|pruning-interval = "19"|' \
  $HOME/.sei/config/app.toml
```

## 🚨 Maintenance

#### Get validator info

```bash
seid status 2>&1 | jq .ValidatorInfo
```

#### Get sync info

```bash
seid status 2>&1 | jq .SyncInfo
```

#### Get node peer

```bash
echo $(seid tendermint show-node-id)'@'$(curl -s ifconfig.me)':'$(cat $HOME/.sei/config/config.toml | sed -n '/Address to listen for incoming connection/{n;p;}' | sed 's/.*://; s/".*//')
```

#### Check if validator key is correct

```bash
[[ $(seid q staking validator $(seid keys show wallet --bech val -a) -oj | jq -r .consensus_pubkey.key) = $(seid status | jq -r .ValidatorInfo.PubKey.value) ]] && echo -e "\n\e[1m\e[32mTrue\e[0m\n" || echo -e "\n\e[1m\e[31mFalse\e[0m\n"
```

#### Get live peers

```bash
curl -sS http://localhost:12657/net_info | jq -r '.result.peers[] | "\(.node_info.id)@\(.remote_ip):\(.node_info.listen_addr)"' | awk -F ':' '{print $1":"$(NF)}'
```

#### Set minimum gas price

```bash
sed -i -e "s/^minimum-gas-prices *=.*/minimum-gas-prices = \"0.0001usei\"/" $HOME/.sei/config/app.toml
```

#### Enable prometheus

```bash
sed -i -e "s/prometheus = false/prometheus = true/" $HOME/.sei/config/config.toml
```

#### Reset chain data

```bash
seid tendermint unsafe-reset-all --home $HOME/.sei --keep-addr-book
```

#### Remove node

{% hint style='danger' %}
Please, before proceeding with the next step! All chain data will be lost! Make sure you have backed up your **priv_validator_key.json**!
{% endhint %}

```bash
cd $HOME
sudo systemctl stop seid
sudo systemctl disable seid
sudo rm /etc/systemd/system/seid.service
sudo systemctl daemon-reload
rm -f $(which seid)
rm -rf $HOME/.sei
rm -rf $HOME/sei-chain
```

## ⚙️ Service Management

#### Reload service configuration

```bash
sudo systemctl daemon-reload
```

#### Enable service

```bash
sudo systemctl enable seid
```

#### Disable service

```bash
sudo systemctl disable seid
```

#### Start service

```bash
sudo systemctl start seid
```

#### Stop service

```bash
sudo systemctl stop seid
```

#### Restart service

```bash
sudo systemctl restart seid
```

#### Check service status

```bash
sudo systemctl status seid
```

#### Check service logs

```bash
sudo journalctl -u seid -f --no-hostname -o cat
```
