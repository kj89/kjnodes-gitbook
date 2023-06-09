---
description: Useful set of commands for node operators. From key management to chain governance.
---

# Useful commands

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/defund.png" alt=""><figcaption></figcaption></figure>

## 🔑 Key management

#### Add new key

```bash
defundd keys add wallet
```

#### Recover existing key

```bash
defundd keys add wallet --recover
```

#### List all keys

```bash
defundd keys list
```

#### Delete key

```bash
defundd keys delete wallet
```

#### Export key to the file

```bash
defundd keys export wallet
```

#### Import key from the file

```bash
defundd keys import wallet wallet.backup
```

#### Query wallet balance

```bash
defundd q bank balances $(defundd keys show wallet -a)
```

## 👷 Validator management

{% hint style="info" %}
Please make sure you have adjusted **moniker**, **identity**, **details** and **website** to match your values.
{% endhint %}

#### Create new validator

```bash
defundd tx staking create-validator \
--amount 1000000ufetf \
--pubkey $(defundd tendermint show-validator) \
--moniker "YOUR_MONIKER_NAME" \
--identity "YOUR_KEYBASE_ID" \
--details "YOUR_DETAILS" \
--website "YOUR_WEBSITE_URL" \
--chain-id orbit-alpha-1 \
--commission-rate 0.05 \
--commission-max-rate 0.20 \
--commission-max-change-rate 0.01 \
--min-self-delegation 1 \
--from wallet \
--gas-adjustment 1.4 \
--gas auto \
--gas-prices 0ufetf \
-y
```

#### Edit existing validator

```bash
defundd tx staking edit-validator \
--new-moniker "YOUR_MONIKER_NAME" \
--identity "YOUR_KEYBASE_ID" \
--details "YOUR_DETAILS" \
--website "YOUR_WEBSITE_URL" \
--chain-id orbit-alpha-1 \
--commission-rate 0.05 \
--from wallet \
--gas-adjustment 1.4 \
--gas auto \
--gas-prices 0ufetf \
-y
```

#### Unjail validator

```bash
defundd tx slashing unjail --from wallet --chain-id orbit-alpha-1 --gas-adjustment 1.4 --gas auto --gas-prices 0ufetf -y
```

#### Jail reason

```bash
defundd query slashing signing-info $(defundd tendermint show-validator)
```

#### List all active validators

```bash
defundd q staking validators -oj --limit=3000 | jq '.validators[] | select(.status=="BOND_STATUS_BONDED")' | jq -r '(.tokens|tonumber/pow(10; 6)|floor|tostring) + " \t " + .description.moniker' | sort -gr | nl
```

#### List all inactive validators

```bash
defundd q staking validators -oj --limit=3000 | jq '.validators[] | select(.status=="BOND_STATUS_UNBONDED")' | jq -r '(.tokens|tonumber/pow(10; 6)|floor|tostring) + " \t " + .description.moniker' | sort -gr | nl
```

#### View validator details

```bash
defundd q staking validator $(defundd keys show wallet --bech val -a)
```

## 💲 Token management

#### Withdraw rewards from all validators

```bash
defundd tx distribution withdraw-all-rewards --from wallet --chain-id orbit-alpha-1 --gas-adjustment 1.4 --gas auto --gas-prices 0ufetf -y
```

#### Withdraw commission and rewards from your validator

```bash
defundd tx distribution withdraw-rewards $(defundd keys show wallet --bech val -a) --commission --from wallet --chain-id orbit-alpha-1 --gas-adjustment 1.4 --gas auto --gas-prices 0ufetf -y
```

#### Delegate tokens to yourself

```bash
defundd tx staking delegate $(defundd keys show wallet --bech val -a) 1000000ufetf --from wallet --chain-id orbit-alpha-1 --gas-adjustment 1.4 --gas auto --gas-prices 0ufetf -y
```

#### Delegate tokens to validator

```bash
defundd tx staking delegate <TO_VALOPER_ADDRESS> 1000000ufetf --from wallet --chain-id orbit-alpha-1 --gas-adjustment 1.4 --gas auto --gas-prices 0ufetf -y
```

#### Redelegate tokens to another validator

```bash
defundd tx staking redelegate $(defundd keys show wallet --bech val -a) <TO_VALOPER_ADDRESS> 1000000ufetf --from wallet --chain-id orbit-alpha-1 --gas-adjustment 1.4 --gas auto --gas-prices 0ufetf -y
```

#### Unbond tokens from your validator

```bash
defundd tx staking unbond $(defundd keys show wallet --bech val -a) 1000000ufetf --from wallet --chain-id orbit-alpha-1 --gas-adjustment 1.4 --gas auto --gas-prices 0ufetf -y
```

#### Send tokens to the wallet

```bash
defundd tx bank send wallet <TO_WALLET_ADDRESS> 1000000ufetf --from wallet --chain-id orbit-alpha-1 --gas-adjustment 1.4 --gas auto --gas-prices 0ufetf -y
```

## 🗳 Governance

#### List all proposals

```bash
defundd query gov proposals
```

#### View proposal by id

```bash
defundd query gov proposal 1
```

#### Vote 'Yes'

```bash
defundd tx gov vote 1 yes --from wallet --chain-id orbit-alpha-1 --gas-adjustment 1.4 --gas auto --gas-prices 0ufetf -y
```

#### Vote 'No'

```bash
defundd tx gov vote 1 no --from wallet --chain-id orbit-alpha-1 --gas-adjustment 1.4 --gas auto --gas-prices 0ufetf -y
```

#### Vote 'Abstain'

```bash
defundd tx gov vote 1 abstain --from wallet --chain-id orbit-alpha-1 --gas-adjustment 1.4 --gas auto --gas-prices 0ufetf -y
```

#### Vote 'NoWithVeto'

```bash
defundd tx gov vote 1 NoWithVeto --from wallet --chain-id orbit-alpha-1 --gas-adjustment 1.4 --gas auto --gas-prices 0ufetf -y
```

## ⚡️ Utility

#### Update ports

```bash
CUSTOM_PORT=110
sed -i -e "s%^proxy_app = \"tcp://127.0.0.1:26658\"%proxy_app = \"tcp://127.0.0.1:${CUSTOM_PORT}58\"%; s%^laddr = \"tcp://127.0.0.1:26657\"%laddr = \"tcp://127.0.0.1:${CUSTOM_PORT}57\"%; s%^pprof_laddr = \"localhost:6060\"%pprof_laddr = \"localhost:${CUSTOM_PORT}60\"%; s%^laddr = \"tcp://0.0.0.0:26656\"%laddr = \"tcp://0.0.0.0:${CUSTOM_PORT}56\"%; s%^prometheus_listen_addr = \":26660\"%prometheus_listen_addr = \":${CUSTOM_PORT}66\"%" $HOME/.defund/config/config.toml
sed -i -e "s%^address = \"tcp://0.0.0.0:1317\"%address = \"tcp://0.0.0.0:${CUSTOM_PORT}17\"%; s%^address = \":8080\"%address = \":${CUSTOM_PORT}80\"%; s%^address = \"0.0.0.0:9090\"%address = \"0.0.0.0:${CUSTOM_PORT}90\"%; s%^address = \"0.0.0.0:9091\"%address = \"0.0.0.0:${CUSTOM_PORT}91\"%" $HOME/.defund/config/app.toml
```

#### Update Indexer

**Disable indexer**

```bash
sed -i -e 's|^indexer *=.*|indexer = "null"|' $HOME/.defund/config/config.toml
```

**Enable indexer**

```bash
sed -i -e 's|^indexer *=.*|indexer = "kv"|' $HOME/.defund/config/config.toml
```

#### Update pruning

```bash
sed -i \
  -e 's|^pruning *=.*|pruning = "custom"|' \
  -e 's|^pruning-keep-recent *=.*|pruning-keep-recent = "100"|' \
  -e 's|^pruning-keep-every *=.*|pruning-keep-every = "0"|' \
  -e 's|^pruning-interval *=.*|pruning-interval = "19"|' \
  $HOME/.defund/config/app.toml
```

## 🚨 Maintenance

#### Get validator info

```bash
defundd status 2>&1 | jq .ValidatorInfo
```

#### Get sync info

```bash
defundd status 2>&1 | jq .SyncInfo
```

#### Get node peer

```bash
echo $(defundd tendermint show-node-id)'@'$(curl -s ifconfig.me)':'$(cat $HOME/.defund/config/config.toml | sed -n '/Address to listen for incoming connection/{n;p;}' | sed 's/.*://; s/".*//')
```

#### Check if validator key is correct

```bash
[[ $(defundd q staking validator $(defundd keys show wallet --bech val -a) -oj | jq -r .consensus_pubkey.key) = $(defundd status | jq -r .ValidatorInfo.PubKey.value) ]] && echo -e "\n\e[1m\e[32mTrue\e[0m\n" || echo -e "\n\e[1m\e[31mFalse\e[0m\n"
```

#### Get live peers

```bash
curl -sS http://localhost:14057/net_info | jq -r '.result.peers[] | "\(.node_info.id)@\(.remote_ip):\(.node_info.listen_addr)"' | awk -F ':' '{print $1":"$(NF)}'
```

#### Set minimum gas price

```bash
sed -i -e "s/^minimum-gas-prices *=.*/minimum-gas-prices = \"0ufetf\"/" $HOME/.defund/config/app.toml
```

#### Enable prometheus

```bash
sed -i -e "s/prometheus = false/prometheus = true/" $HOME/.defund/config/config.toml
```

#### Reset chain data

```bash
defundd tendermint unsafe-reset-all --keep-addr-book --home $HOME/.defund --keep-addr-book
```

#### Remove node

{% hint style='danger' %}
Please, before proceeding with the next step! All chain data will be lost! Make sure you have backed up your **priv_validator_key.json**!
{% endhint %}

```bash
cd $HOME
sudo systemctl stop defundd
sudo systemctl disable defundd
sudo rm /etc/systemd/system/defundd.service
sudo systemctl daemon-reload
rm -f $(which defundd)
rm -rf $HOME/.defund
rm -rf $HOME/defund
```

## ⚙️ Service Management

#### Reload service configuration

```bash
sudo systemctl daemon-reload
```

#### Enable service

```bash
sudo systemctl enable defundd
```

#### Disable service

```bash
sudo systemctl disable defundd
```

#### Start service

```bash
sudo systemctl start defundd
```

#### Stop service

```bash
sudo systemctl stop defundd
```

#### Restart service

```bash
sudo systemctl restart defundd
```

#### Check service status

```bash
sudo systemctl status defundd
```

#### Check service logs

```bash
sudo journalctl -u defundd -f --no-hostname -o cat
```
