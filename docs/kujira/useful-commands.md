---
description: This page contains useful commands for validators
---

# Useful commands

### Key management

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

### Validator management

{% hint style="info" %}
Please make sure you have adjusted `moniker`, `identity`, `details` and `website` to match your values.
{% endhint %}

#### Create new validator

```bash
kujirad tx staking create-validator \
--amount=1000000unknown \
--pubkey=$(kujirad tendermint show-validator) \
--moniker="YOUR_MONIKER_NAME" \
--identity="YOUR_KEYBASE_ID" \
--details="YOUR_DETAILS" \
--website="YOUR_WEBSITE_URL"
--chain-id=kaiyo-1 \
--commission-rate=0.05 \
--commission-max-rate=0.20 \
--commission-max-change-rate=0.01 \
--min-self-delegation=1 \
--from=wallet \
--gas-adjustment=1.4 \
--gas=auto \
-y
```

#### Edit existing validator

```bash
kujirad tx staking edit-validator \
--moniker="YOUR_MONIKER_NAME" \
--identity="YOUR_KEYBASE_ID" \
--details="YOUR_DETAILS" \
--website="YOUR_WEBSITE_URL"
--chain-id=kaiyo-1 \
--commission-rate=0.05 \
--from=wallet \
--gas-adjustment=1.4 \
--gas=auto \
-y
```

#### Unjail validator

```bash
kujirad tx slashing unjail --from wallet --chain-id kaiyo-1 --gas auto --gas-adjustment 1.4 -y
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

### Token management

#### Withdraw rewards from all validators

```bash
kujirad tx distribution withdraw-all-rewards --from wallet --chain-id kaiyo-1 --gas-adjustment 1.4 --gas auto -y
```

#### Withdraw commission and rewards from your validator

```bash
kujirad tx distribution withdraw-rewards $(kujirad keys show wallet --bech val -a) --commission --from wallet --chain-id kaiyo-1 --gas-adjustment 1.4 --gas auto -y
```

#### Delegate tokens to yourself

```bash
kujirad tx staking delegate $(kujirad keys show wallet --bech val -a) 1000000unknown --from wallet --chain-id kaiyo-1 --gas-adjustment 1.4 --gas auto -y
```

#### Delegate tokens to validator

```bash
kujirad tx staking delegate <TO_VALOPER_ADDRESS> 1000000unknown --from wallet --chain-id kaiyo-1 --gas-adjustment 1.4 --gas auto -y
```

Redelegate tokens to another validator

```bash
kujirad tx staking redelegate $(kujirad keys show wallet --bech val -a) <TO_VALOPER_ADDRESS> 1000000unknown --from wallet --chain-id kaiyo-1 --gas-adjustment 1.4 --gas auto -y
```

Unbond tokens from your validator

```bash
kujirad tx staking unbond $(kujirad keys show wallet --bech val -a) 1000000unknown --from wallet --chain-id kaiyo-1 --gas-adjustment 1.4 --gas auto -y
```

Send tokens to the wallet

```bash
kujirad tx bank send wallet <TO_WALLET_ADDRESS> 1000000unknown --from wallet --chain-id kaiyo-1
```

### Governance

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
kujirad tx gov vote 1 yes --from wallet --chain-id kaiyo-1 --gas-adjustment 1.4 --gas auto -y
```

#### Vote 'No'

```bash
kujirad tx gov vote 1 no --from wallet --chain-id kaiyo-1 --gas-adjustment 1.4 --gas auto -y
```

#### Vote 'Abstain'

```bash
kujirad tx gov vote 1 abstain --from wallet --chain-id kaiyo-1 --gas-adjustment 1.4 --gas auto -y
```

#### Vote 'NoWithVeto'

```bash
kujirad tx gov vote 1 nowithveto --from wallet --chain-id kaiyo-1 --gas-adjustment 1.4 --gas auto -y
```

### Utility

#### Update ports

```bash
CUSTOM_PORT=10
sed -i.bak -e "s%^proxy_app = \"tcp://127.0.0.1:26658\"%proxy_app = \"tcp://127.0.0.1:${CUSTOM_PORT}658\"%; s%^laddr = \"tcp://127.0.0.1:26657\"%laddr = \"tcp://127.0.0.1:${CUSTOM_PORT}657\"%; s%^pprof_laddr = \"localhost:6060\"%pprof_laddr = \"localhost:${CUSTOM_PORT}060\"%; s%^laddr = \"tcp://0.0.0.0:26656\"%laddr = \"tcp://0.0.0.0:${CUSTOM_PORT}656\"%; s%^prometheus_listen_addr = \":26660\"%prometheus_listen_addr = \":${CUSTOM_PORT}660\"%" $HOME/.kujira/config/config.toml
sed -i.bak -e "s%^address = \"tcp://0.0.0.0:1317\"%address = \"tcp://0.0.0.0:${CUSTOM_PORT}317\"%; s%^address = \":8080\"%address = \":${CUSTOM_PORT}080\"%; s%^address = \"0.0.0.0:9090\"%address = \"0.0.0.0:${CUSTOM_PORT}090\"%; s%^address = \"0.0.0.0:9091\"%address = \"0.0.0.0:${CUSTOM_PORT}091\"%" $HOME/.kujira/config/app.toml
```

#### Update Indexer

Disable indexer

```bash
sed -i 's|^indexer *=.*|indexer = "null"|' $HOME/.kujira/config/config.toml
```

Enable indexer

```bash
sed -i 's|^indexer *=.*|indexer = "kv"|' $HOME/.kujira/config/config.toml
```

#### Update pruning

```bash
sed -i.bak -e 's|^pruning *=.*|pruning = "custom"|; s|^pruning-keep-recent *=.*|pruning-keep-recent = "100"|; s|^pruning-keep-every *=.*|pruning-keep-every = "0"|; s|^pruning-interval *=.*|pruning-interval = "10"|' $HOME/.kujira/config/app.toml
```

### Maintenance

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
curl -sS http://localhost:26657/net_info | jq -r '.result.peers[] | "\(.node_info.id)@\(.remote_ip):\(.node_info.listen_addr)"' | awk -F ':' '{print $1":"$(NF)}'
```

#### Set minimum gas price

```
sed -i -e "s/^minimum-gas-prices *=.*/minimum-gas-prices = \"0unknown\"/" $HOME/.kujira/config/app.toml
```

#### Enable prometheus

```
sed -i -e "s/prometheus = false/prometheus = true/" $HOME/.kujira/config/config.toml
```

#### Reset chain data

```bash
kujirad tendermint unsafe-reset-all --home $HOME/.kujira --keep-addr-book
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
rm -rf $HOME/.kujira
rm -rf $HOME/core
rm $(which kujirad) 
```

### Service Management

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
