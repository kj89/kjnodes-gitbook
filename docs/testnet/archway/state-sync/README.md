---
description: With our state sync services you will be able to catch up latest chain block in matter of minutes
---

# State sync

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/archway.png" alt=""><figcaption></figcaption></figure>

{% hint style='info' %}
State Sync allows a new node to join the network by fetching a snapshot of the application state 
at a recent height instead of fetching and replaying all historical blocks. Since the 
application state is generally much smaller than the blocks, and restoring it is much 
faster than replaying blocks, this can reduce the time to sync with the network from days to minutes.
{% endhint %}

## Instructions

### Stop the service and reset the data

```bash
sudo systemctl stop archwayd
cp $HOME/.archway/data/priv_validator_state.json $HOME/.archway/priv_validator_state.json.backup
archwayd tendermint unsafe-reset-all --keep-addr-book --home $HOME/.archway
```

### Get and configure the state sync information

```bash
STATE_SYNC_RPC=https://archway-testnet.rpc.kjnodes.com:443
STATE_SYNC_PEER=d5519e378247dfb61dfe90652d1fe3e2b3005a5b@archway-testnet.rpc.kjnodes.com:15656
LATEST_HEIGHT=$(curl -s $STATE_SYNC_RPC/block | jq -r .result.block.header.height)
SYNC_BLOCK_HEIGHT=$(($LATEST_HEIGHT - 1000))
SYNC_BLOCK_HASH=$(curl -s "$STATE_SYNC_RPC/block?height=$SYNC_BLOCK_HEIGHT" | jq -r .result.block_id.hash)

sed -i \
  -e "s|^enable *=.*|enable = true|" \
  -e "s|^rpc_servers *=.*|rpc_servers = \"$STATE_SYNC_RPC,$STATE_SYNC_RPC\"|" \
  -e "s|^trust_height *=.*|trust_height = $SYNC_BLOCK_HEIGHT|" \
  -e "s|^trust_hash *=.*|trust_hash = \"$SYNC_BLOCK_HASH\"|" \
  -e "s|^persistent_peers *=.*|persistent_peers = \"$STATE_SYNC_PEER\"|" \
  $HOME/.archway/config/config.toml

mv $HOME/.archway/priv_validator_state.json.backup $HOME/.archway/data/priv_validator_state.json
```

### Download latest wasm

{% hint style='info' %}
Currently state sync does not support copy of the `wasm` folder. Therefore, you will have to download it manually.
{% endhint %}

```bash
curl -L https://snapshots.kjnodes.com/archway-testnet/wasm_latest.tar.lz4 | lz4 -dc - | tar -xf - -C $HOME/.archway
```

### Restart the service and check the log

```bash
sudo systemctl start archwayd && sudo journalctl -u archwayd -f --no-hostname -o cat
```
