---
description: Useful set of commands for node operators. From key management to chain governance.
---

# Useful commands

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/agoricdev.png" width="150" alt=""><figcaption></figcaption></figure>

## 🔑 Key management

#### Add new key

```bash
agd keys add wallet
```

#### Recover existing key

```bash
agd keys add wallet --recover
```

#### List all keys

```bash
agd keys list
```

#### Delete key

```bash
agd keys delete wallet
```

#### Export key to the file

```bash
agd keys export wallet
```

#### Import key from the file

```bash
agd keys import wallet wallet.backup
```

#### Query wallet balance

```bash
agd q bank balances $(agd keys show wallet -a)
```

## 👷 Validator management

{% hint style="info" %}
Please make sure you have adjusted **moniker**, **identity**, **details** and **website** to match your values.
{% endhint %}

#### Create new validator

```bash
agd tx staking create-validator \
--amount 1000000ubld \
--pubkey $(agd tendermint show-validator) \
--moniker "YOUR_MONIKER_NAME" \
--identity "YOUR_KEYBASE_ID" \
--details "YOUR_DETAILS" \
--website "YOUR_WEBSITE_URL" \
--chain-id agoricdev-17 \
--commission-rate 0.05 \
--commission-max-rate 0.20 \
--commission-max-change-rate 0.01 \
--min-self-delegation 1 \
--from wallet \
--gas-adjustment 1.4 \
--gas auto \
--gas-prices 0.025ubld \
-y
```

#### Edit existing validator

```bash
agd tx staking edit-validator \
--new-moniker "YOUR_MONIKER_NAME" \
--identity "YOUR_KEYBASE_ID" \
--details "YOUR_DETAILS" \
--website "YOUR_WEBSITE_URL" \
--chain-id agoricdev-17 \
--commission-rate 0.05 \
--from wallet \
--gas-adjustment 1.4 \
--gas auto \
--gas-prices 0.025ubld \
-y
```

#### Unjail validator

```bash
agd tx slashing unjail --from wallet --chain-id agoricdev-17 --gas-adjustment 1.4 --gas auto --gas-prices 0.025ubld -y
```

#### Jail reason

```bash
agd query slashing signing-info $(agd tendermint show-validator)
```

#### List all active validators

```bash
agd q staking validators -oj --limit=3000 | jq '.validators[] | select(.status=="BOND_STATUS_BONDED")' | jq -r '(.tokens|tonumber/pow(10; 6)|floor|tostring) + " \t " + .description.moniker' | sort -gr | nl
```

#### List all inactive validators

```bash
agd q staking validators -oj --limit=3000 | jq '.validators[] | select(.status=="BOND_STATUS_UNBONDED")' | jq -r '(.tokens|tonumber/pow(10; 6)|floor|tostring) + " \t " + .description.moniker' | sort -gr | nl
```

#### View validator details

```bash
agd q staking validator $(agd keys show wallet --bech val -a)
```

## 💲 Token management

#### Withdraw rewards from all validators

```bash
agd tx distribution withdraw-all-rewards --from wallet --chain-id agoricdev-17 --gas-adjustment 1.4 --gas auto --gas-prices 0.025ubld -y
```

#### Withdraw commission and rewards from your validator

```bash
agd tx distribution withdraw-rewards $(agd keys show wallet --bech val -a) --commission --from wallet --chain-id agoricdev-17 --gas-adjustment 1.4 --gas auto --gas-prices 0.025ubld -y
```

#### Delegate tokens to yourself

```bash
agd tx staking delegate $(agd keys show wallet --bech val -a) 1000000ubld --from wallet --chain-id agoricdev-17 --gas-adjustment 1.4 --gas auto --gas-prices 0.025ubld -y
```

#### Delegate tokens to validator

```bash
agd tx staking delegate <TO_VALOPER_ADDRESS> 1000000ubld --from wallet --chain-id agoricdev-17 --gas-adjustment 1.4 --gas auto --gas-prices 0.025ubld -y
```

#### Redelegate tokens to another validator

```bash
agd tx staking redelegate $(agd keys show wallet --bech val -a) <TO_VALOPER_ADDRESS> 1000000ubld --from wallet --chain-id agoricdev-17 --gas-adjustment 1.4 --gas auto --gas-prices 0.025ubld -y
```

#### Unbond tokens from your validator

```bash
agd tx staking unbond $(agd keys show wallet --bech val -a) 1000000ubld --from wallet --chain-id agoricdev-17 --gas-adjustment 1.4 --gas auto --gas-prices 0.025ubld -y
```

#### Send tokens to the wallet

```bash
agd tx bank send wallet <TO_WALLET_ADDRESS> 1000000ubld --from wallet --chain-id agoricdev-17 --gas-adjustment 1.4 --gas auto --gas-prices 0.025ubld -y
```

## 🗳 Governance

#### List all proposals

```bash
agd query gov proposals
```

#### View proposal by id

```bash
agd query gov proposal 1
```

#### Vote 'Yes'

```bash
agd tx gov vote 1 yes --from wallet --chain-id agoricdev-17 --gas-adjustment 1.4 --gas auto --gas-prices 0.025ubld -y
```

#### Vote 'No'

```bash
agd tx gov vote 1 no --from wallet --chain-id agoricdev-17 --gas-adjustment 1.4 --gas auto --gas-prices 0.025ubld -y
```

#### Vote 'Abstain'

```bash
agd tx gov vote 1 abstain --from wallet --chain-id agoricdev-17 --gas-adjustment 1.4 --gas auto --gas-prices 0.025ubld -y
```

#### Vote 'NoWithVeto'

```bash
agd tx gov vote 1 NoWithVeto --from wallet --chain-id agoricdev-17 --gas-adjustment 1.4 --gas auto --gas-prices 0.025ubld -y
```

## ⚡️ Utility

#### Update ports

```bash
CUSTOM_PORT=10
sed -i -e "s%^proxy_app = \"tcp://127.0.0.1:26658\"%proxy_app = \"tcp://127.0.0.1:${CUSTOM_PORT}658\"%; s%^laddr = \"tcp://127.0.0.1:26657\"%laddr = \"tcp://127.0.0.1:${CUSTOM_PORT}657\"%; s%^pprof_laddr = \"localhost:6060\"%pprof_laddr = \"localhost:${CUSTOM_PORT}060\"%; s%^laddr = \"tcp://0.0.0.0:26656\"%laddr = \"tcp://0.0.0.0:${CUSTOM_PORT}656\"%; s%^prometheus_listen_addr = \":26660\"%prometheus_listen_addr = \":${CUSTOM_PORT}660\"%" $HOME/.agoric/config/config.toml
sed -i -e "s%^address = \"tcp://0.0.0.0:1317\"%address = \"tcp://0.0.0.0:${CUSTOM_PORT}317\"%; s%^address = \":8080\"%address = \":${CUSTOM_PORT}080\"%; s%^address = \"0.0.0.0:9090\"%address = \"0.0.0.0:${CUSTOM_PORT}090\"%; s%^address = \"0.0.0.0:9091\"%address = \"0.0.0.0:${CUSTOM_PORT}091\"%" $HOME/.agoric/config/app.toml
```

#### Update Indexer

**Disable indexer**

```bash
sed -i -e 's|^indexer *=.*|indexer = "null"|' $HOME/.agoric/config/config.toml
```

**Enable indexer**

```bash
sed -i -e 's|^indexer *=.*|indexer = "kv"|' $HOME/.agoric/config/config.toml
```

#### Update pruning

```bash
sed -i \
  -e 's|^pruning *=.*|pruning = "custom"|' \
  -e 's|^pruning-keep-recent *=.*|pruning-keep-recent = "100"|' \
  -e 's|^pruning-keep-every *=.*|pruning-keep-every = "0"|' \
  -e 's|^pruning-interval *=.*|pruning-interval = "19"|' \
  $HOME/.agoric/config/app.toml
```

## 🚨 Maintenance

#### Get validator info

```bash
agd status 2>&1 | jq .ValidatorInfo
```

#### Get sync info

```bash
agd status 2>&1 | jq .SyncInfo
```

#### Get node peer

```bash
echo $(agd tendermint show-node-id)'@'$(curl -s ifconfig.me)':'$(cat $HOME/.agoric/config/config.toml | sed -n '/Address to listen for incoming connection/{n;p;}' | sed 's/.*://; s/".*//')
```

#### Check if validator key is correct

```bash
[[ $(agd q staking validator $(agd keys show wallet --bech val -a) -oj | jq -r .consensus_pubkey.key) = $(agd status | jq -r .ValidatorInfo.PubKey.value) ]] && echo -e "\n\e[1m\e[32mTrue\e[0m\n" || echo -e "\n\e[1m\e[31mFalse\e[0m\n"
```

#### Get live peers

```bash
curl -sS http://localhost:14657/net_info | jq -r '.result.peers[] | "\(.node_info.id)@\(.remote_ip):\(.node_info.listen_addr)"' | awk -F ':' '{print $1":"$(NF)}'
```

#### Set minimum gas price

```bash
sed -i -e "s/^minimum-gas-prices *=.*/minimum-gas-prices = \"0.025ubld\"/" $HOME/.agoric/config/app.toml
```

#### Enable prometheus

```bash
sed -i -e "s/prometheus = false/prometheus = true/" $HOME/.agoric/config/config.toml
```

#### Reset chain data

```bash
agd tendermint unsafe-reset-all --home $HOME/.agoric --keep-addr-book
```

#### Remove node

{% hint style='danger' %}
Please, before proceeding with the next step! All chain data will be lost! Make sure you have backed up your **priv_validator_key.json**!
{% endhint %}

```bash
cd $HOME
sudo systemctl stop agd
sudo systemctl disable agd
sudo rm /etc/systemd/system/agd.service
sudo systemctl daemon-reload
rm -f $(which agd)
rm -rf $HOME/.agoric
rm -rf $HOME/agoric-sdk
```

## ⚙️ Service Management

#### Reload service configuration

```bash
sudo systemctl daemon-reload
```

#### Enable service

```bash
sudo systemctl enable agd
```

#### Disable service

```bash
sudo systemctl disable agd
```

#### Start service

```bash
sudo systemctl start agd
```

#### Stop service

```bash
sudo systemctl stop agd
```

#### Restart service

```bash
sudo systemctl restart agd
```

#### Check service status

```bash
sudo systemctl status agd
```

#### Check service logs

```bash
sudo journalctl -u agd -f --no-hostname -o cat
```
