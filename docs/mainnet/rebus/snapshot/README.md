# 💊 Snapshot

{% hint style='info' %}
Snapshots allows a new node to join the network by recovering application state from a backup file. 
Snapshot contains compressed copy of chain data directory. To keep backup files as small as plausible, 
snapshot server is periodically beeing state-synced.
{% endhint %}

| BLOCK             | AGE             | DOWNLOAD                                                                                            |
| ----------------- | --------------- | --------------------------------------------------------------------------------------------------- |
| 1746821 | 36 minutes ago | [snapshot (1.81 GB)](https://snapshots.kjnodes.com/rebus/snapshot\_latest.tar.lz4) |

## Instructions

### Stop the service and reset the data

```bash
sudo systemctl stop rebusd
cp $HOME/.rebusd/data/priv_validator_state.json $HOME/.rebusd/priv_validator_state.json.backup
rm -rf $HOME/.rebusd/data
```

### Download the latest snapshot

```bash
curl -L https://snapshots.kjnodes.com/rebus/snapshot_latest.tar.lz4 | lz4 -dc - | tar -xf - -C $HOME/.rebusd
mv $HOME/.rebusd/priv_validator_state.json.backup $HOME/.rebusd/data/priv_validator_state.json
```

### Restart the service and check the log

```bash
sudo systemctl start rebusd && journalctl -u rebusd -f --no-hostname -o cat
```
