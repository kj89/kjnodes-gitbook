# 💊 Snapshot

{% hint style='info' %}
Snapshots allows a new node to join the network by recovering application state from a backup file. 
Snapshot contains compressed copy of chain data directory. To keep backup files as small as plausible, 
snapshot server is periodically beeing state-synced.
{% endhint %}

| BLOCK             | AGE             | DOWNLOAD                                                                                            |
| ----------------- | --------------- | --------------------------------------------------------------------------------------------------- |
| 617708 | 7 hours ago | [snapshot (0.74 GB)](https://snapshots.kjnodes.com/quicksilver-testnet/snapshot\_latest.tar.lz4) |

## Instructions

### Stop the service and reset the data

```bash
sudo systemctl stop quicksilverd
cp $HOME/.quicksilverd/data/priv_validator_state.json $HOME/.quicksilverd/priv_validator_state.json.backup
rm -rf $HOME/.quicksilverd/data
```

### Download the latest snapshot

```bash
curl -L https://snapshots.kjnodes.com/quicksilver-testnet/snapshot_latest.tar.lz4 | lz4 -dc - | tar -xf - -C $HOME/.quicksilverd
mv $HOME/.quicksilverd/priv_validator_state.json.backup $HOME/.quicksilverd/data/priv_validator_state.json
```

### Restart the service and check the log

```bash
sudo systemctl start quicksilverd && journalctl -u quicksilverd -f --no-hostname -o cat
```
