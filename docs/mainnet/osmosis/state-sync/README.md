---
description: With our state sync services you will be able to catch up latest chain block in matter of minutes
---

# State sync

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/osmosis.png" width="150" alt=""><figcaption></figcaption></figure>

{% hint style='info' %}
State Sync allows a new node to join the network by fetching a snapshot of the application state 
at a recent height instead of fetching and replaying all historical blocks. Since the 
application state is generally much smaller than the blocks, and restoring it is much 
faster than replaying blocks, this can reduce the time to sync with the network from days to minutes.
{% endhint %}

## Instructions

### Stop the service and reset the data

```bash
sudo systemctl stop osmosisd
cp $HOME/.osmosisd/data/priv_validator_state.json $HOME/.osmosisd/priv_validator_state.json.backup
osmosisd tendermint unsafe-reset-all --home $HOME/.osmosisd
```

### Get and configure the state sync information

```bash
STATE_SYNC_RPC=https://osmosis.rpc.kjnodes.com:443
STATE_SYNC_PEER=d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@osmosis.rpc.kjnodes.com:29656
LATEST_HEIGHT=$(curl -s $STATE_SYNC_RPC/block | jq -r .result.block.header.height)
SYNC_BLOCK_HEIGHT=$(($LATEST_HEIGHT - 2000))
SYNC_BLOCK_HASH=$(curl -s "$STATE_SYNC_RPC/block?height=$SYNC_BLOCK_HEIGHT" | jq -r .result.block_id.hash)

sed -i.bak -e "s|^enable *=.*|enable = true|" $HOME/.osmosisd/config/config.toml
sed -i.bak -e "s|^rpc_servers *=.*|rpc_servers = \"$STATE_SYNC_RPC,$STATE_SYNC_RPC\"|" \
  $HOME/.osmosisd/config/config.toml
sed -i.bak -e "s|^trust_height *=.*|trust_height = $SYNC_BLOCK_HEIGHT|" \
  $HOME/.osmosisd/config/config.toml
sed -i.bak -e "s|^trust_hash *=.*|trust_hash = \"$SYNC_BLOCK_HASH\"|" \
  $HOME/.osmosisd/config/config.toml
sed -i.bak -e "s|^persistent_peers *=.*|persistent_peers = \"$STATE_SYNC_PEER\"|" \
  $HOME/.osmosisd/config/config.toml
mv $HOME/.osmosisd/priv_validator_state.json.backup $HOME/.osmosisd/data/priv_validator_state.json
```

### Restart the service and check the log

```bash
sudo systemctl start osmosisd && journalctl -u osmosisd -f --no-hostname -o cat
```
