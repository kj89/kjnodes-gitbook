---
description: >-
  Snapshots allows a new node to join the network by recovering application state from a backup file. 
  It is compressed copy of chain data direcotry. To keep backup files small, snapshot server is periodically beeing state-synced.
---

# Snapshot

| BLOCK             | AGE             | DOWNLOAD                                                                         | SIZE             |
| ----------------- | --------------- | -------------------------------------------------------------------------------- | ---------------- |
| 4906405 | 9 minutes ago | [snapshot](https://snapshots.kjnodes.com/kujira/snapshot\_latest.tar.lz4) | 1.43 GB |

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
