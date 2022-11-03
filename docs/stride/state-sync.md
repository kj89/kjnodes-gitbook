---
description: This page contain instructions to rapidly state sync your validator node
---

# State sync

### Basic information

#### RPC endpoint:

```bash
https://stride.rpc.kjnodes.com:443
```

#### Peer:

```bash
6f56d09b7d921e3520c1e7129b20a40dae2c7973@stride.rpc.kjnodes.com:16656
```

### Stop the service and reset the data

```bash
sudo systemctl stop strided
cp $HOME/.stride/data/priv_validator_state.json $HOME/.stride/priv_validator_state.json.backup
strided tendermint unsafe-reset-all --home $HOME/.stride
```

### Get and configure the state sync information

```bash
STATE_SYNC_RPC=https://stride.rpc.kjnodes.com:443
STATE_SYNC_PEER=6f56d09b7d921e3520c1e7129b20a40dae2c7973@stride.rpc.kjnodes.com:16656
LATEST_HEIGHT=$(curl -s $STATE_SYNC_RPC/block | jq -r .result.block.header.height)
SYNC_BLOCK_HEIGHT=$(($LATEST_HEIGHT - 2000))
SYNC_BLOCK_HASH=$(curl -s "$STATE_SYNC_RPC/block?height=$SYNC_BLOCK_HEIGHT" | jq -r .result.block_id.hash)

sed -i.bak -e "s|^enable *=.*|enable = true|" $HOME/.stride/config/config.toml
sed -i.bak -e "s|^rpc_servers *=.*|rpc_servers = \"$STATE_SYNC_RPC,$STATE_SYNC_RPC\"|" \
  $HOME/.stride/config/config.toml
sed -i.bak -e "s|^trust_height *=.*|trust_height = $SYNC_BLOCK_HEIGHT|" \
  $HOME/.stride/config/config.toml
sed -i.bak -e "s|^trust_hash *=.*|trust_hash = \"$SYNC_BLOCK_HASH\"|" \
  $HOME/.stride/config/config.toml
sed -i.bak -e "s|^persistent_peers *=.*|persistent_peers = \"$STATE_SYNC_PEER\"|" \
  $HOME/.stride/config/config.toml
mv $HOME/.stride/priv_validator_state.json.backup $HOME/.stride/data/priv_validator_state.json
```

### Restart the service and check the log

```bash
sudo systemctl start strided && journalctl -u strided -f --no-hostname -o cat
```
