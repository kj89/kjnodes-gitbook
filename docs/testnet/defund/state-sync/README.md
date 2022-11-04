---
description: This page contain instructions to rapidly state sync your validator node
---

# State sync

### Basic information

#### RPC endpoint:

```bash
https://defund-testnet.rpc.kjnodes.com:443
```

#### Peer:

```bash
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@defund-testnet.rpc.kjnodes.com:40656
```

### Stop the service and reset the data

```bash
sudo systemctl stop defundd
cp $HOME/.defund/data/priv_validator_state.json $HOME/.defund/priv_validator_state.json.backup
defundd tendermint unsafe-reset-all --home $HOME/.defund
```

### Get and configure the state sync information

```bash
STATE_SYNC_RPC=https://defund-testnet.rpc.kjnodes.com:443
STATE_SYNC_PEER=d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@defund-testnet.rpc.kjnodes.com:40656
LATEST_HEIGHT=$(curl -s $STATE_SYNC_RPC/block | jq -r .result.block.header.height)
SYNC_BLOCK_HEIGHT=$(($LATEST_HEIGHT - 2000))
SYNC_BLOCK_HASH=$(curl -s "$STATE_SYNC_RPC/block?height=$SYNC_BLOCK_HEIGHT" | jq -r .result.block_id.hash)

sed -i.bak -e "s|^enable *=.*|enable = true|" $HOME/.defund/config/config.toml
sed -i.bak -e "s|^rpc_servers *=.*|rpc_servers = \"$STATE_SYNC_RPC,$STATE_SYNC_RPC\"|" \
  $HOME/.defund/config/config.toml
sed -i.bak -e "s|^trust_height *=.*|trust_height = $SYNC_BLOCK_HEIGHT|" \
  $HOME/.defund/config/config.toml
sed -i.bak -e "s|^trust_hash *=.*|trust_hash = \"$SYNC_BLOCK_HASH\"|" \
  $HOME/.defund/config/config.toml
sed -i.bak -e "s|^persistent_peers *=.*|persistent_peers = \"$STATE_SYNC_PEER\"|" \
  $HOME/.defund/config/config.toml
mv $HOME/.defund/priv_validator_state.json.backup $HOME/.defund/data/priv_validator_state.json
```

### Restart the service and check the log

```bash
sudo systemctl start defundd && journalctl -u defundd -f --no-hostname -o cat
```
