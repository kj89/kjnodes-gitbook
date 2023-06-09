---
description: Useful set of commands for node operators. From key management to chain governance.
---

# Useful commands

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/kujira.png" alt=""><figcaption></figcaption></figure>

## 🔑 Key management

#### Add new key

```bash
kujirad keys add wallet
```

#### Recover existing key

```bash
kujirad keys add wallet --recover
```

#### List all keys

```bash
kujirad keys list
```

#### Delete key

```bash
kujirad keys delete wallet
```

#### Export key to the file

```bash
kujirad keys export wallet
```

#### Import key from the file

```bash
kujirad keys import wallet wallet.backup
```

#### Query wallet balance

```bash
kujirad q bank balances $(kujirad keys show wallet -a)
```

## 👷 Validator management

{% hint style="info" %}
Please make sure you have adjusted **moniker**, **identity**, **details** and **website** to match your values.
{% endhint %}

#### Create new validator

```bash
kujirad tx staking create-validator \
--amount 1000000ukuji \
--pubkey $(kujirad tendermint show-validator) \
--moniker "YOUR_MONIKER_NAME" \
--identity "YOUR_KEYBASE_ID" \
--details "YOUR_DETAILS" \
--website "YOUR_WEBSITE_URL" \
--chain-id kaiyo-1 \
--commission-rate 0.05 \
--commission-max-rate 0.20 \
--commission-max-change-rate 0.01 \
--min-self-delegation 1 \
--from wallet \
--gas-adjustment 1.4 \
--gas auto \
--gas-prices 0.00119ukuji \
-y
```

#### Edit existing validator

```bash
kujirad tx staking edit-validator \
--new-moniker "YOUR_MONIKER_NAME" \
--identity "YOUR_KEYBASE_ID" \
--details "YOUR_DETAILS" \
--website "YOUR_WEBSITE_URL" \
--chain-id kaiyo-1 \
--commission-rate 0.05 \
--from wallet \
--gas-adjustment 1.4 \
--gas auto \
--gas-prices 0.00119ukuji \
-y
```

#### Unjail validator

```bash
kujirad tx slashing unjail --from wallet --chain-id kaiyo-1 --gas-adjustment 1.4 --gas auto --gas-prices 0.00119ukuji -y
```

#### Jail reason

```bash
kujirad query slashing signing-info $(kujirad tendermint show-validator)
```

#### List all active validators

```bash
kujirad q staking validators -oj --limit=3000 | jq '.validators[] | select(.status=="BOND_STATUS_BONDED")' | jq -r '(.tokens|tonumber/pow(10; 6)|floor|tostring) + " \t " + .description.moniker' | sort -gr | nl
```

#### List all inactive validators

```bash
kujirad q staking validators -oj --limit=3000 | jq '.validators[] | select(.status=="BOND_STATUS_UNBONDED")' | jq -r '(.tokens|tonumber/pow(10; 6)|floor|tostring) + " \t " + .description.moniker' | sort -gr | nl
```

#### View validator details

```bash
kujirad q staking validator $(kujirad keys show wallet --bech val -a)
```

## 💲 Token management

#### Withdraw rewards from all validators

```bash
kujirad tx distribution withdraw-all-rewards --from wallet --chain-id kaiyo-1 --gas-adjustment 1.4 --gas auto --gas-prices 0.00119ukuji -y
```

#### Withdraw commission and rewards from your validator

```bash
kujirad tx distribution withdraw-rewards $(kujirad keys show wallet --bech val -a) --commission --from wallet --chain-id kaiyo-1 --gas-adjustment 1.4 --gas auto --gas-prices 0.00119ukuji -y
```

#### Delegate tokens to yourself

```bash
kujirad tx staking delegate $(kujirad keys show wallet --bech val -a) 1000000ukuji --from wallet --chain-id kaiyo-1 --gas-adjustment 1.4 --gas auto --gas-prices 0.00119ukuji -y
```

#### Delegate tokens to validator

```bash
kujirad tx staking delegate <TO_VALOPER_ADDRESS> 1000000ukuji --from wallet --chain-id kaiyo-1 --gas-adjustment 1.4 --gas auto --gas-prices 0.00119ukuji -y
```

#### Redelegate tokens to another validator

```bash
kujirad tx staking redelegate $(kujirad keys show wallet --bech val -a) <TO_VALOPER_ADDRESS> 1000000ukuji --from wallet --chain-id kaiyo-1 --gas-adjustment 1.4 --gas auto --gas-prices 0.00119ukuji -y
```

#### Unbond tokens from your validator

```bash
kujirad tx staking unbond $(kujirad keys show wallet --bech val -a) 1000000ukuji --from wallet --chain-id kaiyo-1 --gas-adjustment 1.4 --gas auto --gas-prices 0.00119ukuji -y
```

#### Send tokens to the wallet

```bash
kujirad tx bank send wallet <TO_WALLET_ADDRESS> 1000000ukuji --from wallet --chain-id kaiyo-1 --gas-adjustment 1.4 --gas auto --gas-prices 0.00119ukuji -y
```

## 🗳 Governance

#### List all proposals

```bash
kujirad query gov proposals
```

#### View proposal by id

```bash
kujirad query gov proposal 1
```

#### Vote 'Yes'

```bash
kujirad tx gov vote 1 yes --from wallet --chain-id kaiyo-1 --gas-adjustment 1.4 --gas auto --gas-prices 0.00119ukuji -y
```

#### Vote 'No'

```bash
kujirad tx gov vote 1 no --from wallet --chain-id kaiyo-1 --gas-adjustment 1.4 --gas auto --gas-prices 0.00119ukuji -y
```

#### Vote 'Abstain'

```bash
kujirad tx gov vote 1 abstain --from wallet --chain-id kaiyo-1 --gas-adjustment 1.4 --gas auto --gas-prices 0.00119ukuji -y
```

#### Vote 'NoWithVeto'

```bash
kujirad tx gov vote 1 NoWithVeto --from wallet --chain-id kaiyo-1 --gas-adjustment 1.4 --gas auto --gas-prices 0.00119ukuji -y
```

## ⚡️ Utility

#### Update ports

```bash
CUSTOM_PORT=110
sed -i -e "s%^proxy_app = \"tcp://127.0.0.1:26658\"%proxy_app = \"tcp://127.0.0.1:${CUSTOM_PORT}58\"%; s%^laddr = \"tcp://127.0.0.1:26657\"%laddr = \"tcp://127.0.0.1:${CUSTOM_PORT}57\"%; s%^pprof_laddr = \"localhost:6060\"%pprof_laddr = \"localhost:${CUSTOM_PORT}60\"%; s%^laddr = \"tcp://0.0.0.0:26656\"%laddr = \"tcp://0.0.0.0:${CUSTOM_PORT}56\"%; s%^prometheus_listen_addr = \":26660\"%prometheus_listen_addr = \":${CUSTOM_PORT}66\"%" $HOME/.kujira/config/config.toml
sed -i -e "s%^address = \"tcp://0.0.0.0:1317\"%address = \"tcp://0.0.0.0:${CUSTOM_PORT}17\"%; s%^address = \":8080\"%address = \":${CUSTOM_PORT}80\"%; s%^address = \"0.0.0.0:9090\"%address = \"0.0.0.0:${CUSTOM_PORT}90\"%; s%^address = \"0.0.0.0:9091\"%address = \"0.0.0.0:${CUSTOM_PORT}91\"%" $HOME/.kujira/config/app.toml
```

#### Update Indexer

**Disable indexer**

```bash
sed -i -e 's|^indexer *=.*|indexer = "null"|' $HOME/.kujira/config/config.toml
```

**Enable indexer**

```bash
sed -i -e 's|^indexer *=.*|indexer = "kv"|' $HOME/.kujira/config/config.toml
```

#### Update pruning

```bash
sed -i \
  -e 's|^pruning *=.*|pruning = "custom"|' \
  -e 's|^pruning-keep-recent *=.*|pruning-keep-recent = "100"|' \
  -e 's|^pruning-keep-every *=.*|pruning-keep-every = "0"|' \
  -e 's|^pruning-interval *=.*|pruning-interval = "19"|' \
  $HOME/.kujira/config/app.toml
```

## 🚨 Maintenance

#### Get validator info

```bash
kujirad status 2>&1 | jq .ValidatorInfo
```

#### Get sync info

```bash
kujirad status 2>&1 | jq .SyncInfo
```

#### Get node peer

```bash
echo $(kujirad tendermint show-node-id)'@'$(curl -s ifconfig.me)':'$(cat $HOME/.kujira/config/config.toml | sed -n '/Address to listen for incoming connection/{n;p;}' | sed 's/.*://; s/".*//')
```

#### Check if validator key is correct

```bash
[[ $(kujirad q staking validator $(kujirad keys show wallet --bech val -a) -oj | jq -r .consensus_pubkey.key) = $(kujirad status | jq -r .ValidatorInfo.PubKey.value) ]] && echo -e "\n\e[1m\e[32mTrue\e[0m\n" || echo -e "\n\e[1m\e[31mFalse\e[0m\n"
```

#### Get live peers

```bash
curl -sS http://localhost:11357/net_info | jq -r '.result.peers[] | "\(.node_info.id)@\(.remote_ip):\(.node_info.listen_addr)"' | awk -F ':' '{print $1":"$(NF)}'
```

#### Set minimum gas price

```bash
sed -i -e "s/^minimum-gas-prices *=.*/minimum-gas-prices = \"0.00119ukuji,0.00150factory/kujira1qk00h5atutpsv900x202pxx42npjr9thg58dnqpa72f2p7m2luase444a7/uusk,0.00150ibc/295548A78785A1007F232DE286149A6FF512F180AF5657780FC89C009E2C348F,0.000125ibc/27394FB092D2ECCD56123C74F36E4C1F926001CEADA9CA97EA622B25F41E5EB2,0.00126ibc/47BD209179859CDE4A2806763D7189B6E6FE13A17880FE2B42DE1E6C1E329E23,0.00652ibc/3607EB5B5E64DD1C0E12E07F077FF470D5BC4706AFCBC98FE1BA960E5AE4CE07,617283951ibc/F3AA7EF362EC5E791FE78A0F4CCC69FEE1F9A7485EB1A8CAB3F6601C00522F10,0.000288ibc/EFF323CC632EC4F747C61BCE238A758EFDB7699C3226565F7C20DA06509D59A5,0.000125ibc/DA59C009A0B3B95E0549E6BF7B075C8239285989FF457A8EDDBB56F10B2A6986,0.00137ibc/A358D7F19237777AF6D8AD0E0F53268F8B18AE8A53ED318095C14D6D7F3B2DB5,0.0488ibc/4F393C3FCA4190C0A6756CE7F6D897D5D1BE57D6CCB80D0BC87393566A7B6602,78492936ibc/004EBF085BBED1029326D56BE8A2E67C08CECE670A94AC1947DF413EF5130EB2,964351ibc/1B38805B1C75352B28169284F96DF56BDEBD9E8FAC005BDCC8CF0378C82AA8E7\"/" $HOME/.kujira/config/app.toml
```

#### Enable prometheus

```bash
sed -i -e "s/prometheus = false/prometheus = true/" $HOME/.kujira/config/config.toml
```

#### Reset chain data

```bash
kujirad tendermint unsafe-reset-all --keep-addr-book --home $HOME/.kujira --keep-addr-book
```

#### Remove node

{% hint style='danger' %}
Please, before proceeding with the next step! All chain data will be lost! Make sure you have backed up your **priv_validator_key.json**!
{% endhint %}

```bash
cd $HOME
sudo systemctl stop kujirad
sudo systemctl disable kujirad
sudo rm /etc/systemd/system/kujirad.service
sudo systemctl daemon-reload
rm -f $(which kujirad)
rm -rf $HOME/.kujira
rm -rf $HOME/core
```

## ⚙️ Service Management

#### Reload service configuration

```bash
sudo systemctl daemon-reload
```

#### Enable service

```bash
sudo systemctl enable kujirad
```

#### Disable service

```bash
sudo systemctl disable kujirad
```

#### Start service

```bash
sudo systemctl start kujirad
```

#### Stop service

```bash
sudo systemctl stop kujirad
```

#### Restart service

```bash
sudo systemctl restart kujirad
```

#### Check service status

```bash
sudo systemctl status kujirad
```

#### Check service logs

```bash
sudo journalctl -u kujirad -f --no-hostname -o cat
```
