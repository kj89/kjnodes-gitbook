# ♻ State sync

{% hint style='info' %}
State Sync allows a new node to join the network by fetching a snapshot of the application state 
at a recent height instead of fetching and replaying all historical blocks. Since the 
application state is generally much smaller than the blocks, and restoring it is much 
faster than replaying blocks, this can reduce the time to sync with the network from days to minutes.
{% endhint %}

## Instructions

### Stop the service and reset the data

```bash
sudo systemctl stop aurad
cp $HOME/.aura/data/priv_validator_state.json $HOME/.aura/priv_validator_state.json.backup
aurad tendermint unsafe-reset-all --home $HOME/.aura
```

### Get and configure the state sync information

```bash
STATE_SYNC_RPC=https://aura-testnet.rpc.kjnodes.com:443
STATE_SYNC_PEER=d5519e378247dfb61dfe90652d1fe3e2b3005a5b@aura-testnet.rpc.kjnodes.com:17656
LATEST_HEIGHT=$(curl -s $STATE_SYNC_RPC/block | jq -r .result.block.header.height)
SYNC_BLOCK_HEIGHT=$(($LATEST_HEIGHT - 2000))
SYNC_BLOCK_HASH=$(curl -s "$STATE_SYNC_RPC/block?height=$SYNC_BLOCK_HEIGHT" | jq -r .result.block_id.hash)

sed -i.bak -e "s|^enable *=.*|enable = true|" $HOME/.aura/config/config.toml
sed -i.bak -e "s|^rpc_servers *=.*|rpc_servers = \"$STATE_SYNC_RPC,$STATE_SYNC_RPC\"|" \
  $HOME/.aura/config/config.toml
sed -i.bak -e "s|^trust_height *=.*|trust_height = $SYNC_BLOCK_HEIGHT|" \
  $HOME/.aura/config/config.toml
sed -i.bak -e "s|^trust_hash *=.*|trust_hash = \"$SYNC_BLOCK_HASH\"|" \
  $HOME/.aura/config/config.toml
sed -i.bak -e "s|^persistent_peers *=.*|persistent_peers = \"$STATE_SYNC_PEER\"|" \
  $HOME/.aura/config/config.toml
mv $HOME/.aura/priv_validator_state.json.backup $HOME/.aura/data/priv_validator_state.json
```

### Restart the service and check the log

```bash
sudo systemctl start aurad && journalctl -u aurad -f --no-hostname -o cat
```
