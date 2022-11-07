# Snapshot

{% hint style='info' %}
Snapshots allows a new node to join the network by recovering application state from a backup file. 
Snapshot contains compressed copy of chain data directory. To keep backup files as small as plausible, 
snapshot server is periodically beeing state-synced.
{% endhint %}

| BLOCK             | AGE             | DOWNLOAD                                                                                            |
| ----------------- | --------------- | --------------------------------------------------------------------------------------------------- |
| 4906405 | 54 minutes ago | [snapshot(1.43 GB)](https://snapshots.kjnodes.com/kujira/snapshot\_latest.tar.lz4) |

## Instructions

### Stop the service and reset the data

```bash
sudo systemctl stop kujirad
cp $HOME/.kujira/data/priv_validator_state.json $HOME/.kujira/priv_validator_state.json.backup
rm -rf $HOME/.kujira/data
```

### Download the latest snapshot

```bash
curl -L https://snapshots.kjnodes.com/kujira/snapshot_latest.tar.lz4 | lz4 -dc - | tar -xf - -C $HOME/.kujira
mv $HOME/.kujira/priv_validator_state.json.backup $HOME/.kujira/data/priv_validator_state.json
```

### Restart the service and check the log

```bash
sudo systemctl start kujirad && journalctl -u kujirad -f --no-hostname -o cat
```
