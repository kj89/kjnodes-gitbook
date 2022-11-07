---
description: >-
  Snapshots allows a new node to join the network by recovering application state from a backup file. 
  It is compressed copy of chain data direcotry. To keep backup files small, snapshot server is periodically beeing state-synced.
---

# Snapshot

| BLOCK             | AGE             | DOWNLOAD                                                                         | SIZE             |
| ----------------- | --------------- | -------------------------------------------------------------------------------- | ---------------- |
| 7309137 | 21 hours ago | [snapshot](https://snapshots.kjnodes.com/agoric/snapshot\_latest.tar.lz4) | 5.22 GB |

### Stop the service and reset the data

```bash
sudo systemctl stop agd
cp $HOME/.agoric/data/priv_validator_state.json $HOME/.agoric/priv_validator_state.json.backup
rm -rf $HOME/.agoric/data
```

### Download the latest snapshot

```bash
curl -L https://snapshots.kjnodes.com/agoric/snapshot_latest.tar.lz4 | lz4 -dc - | tar -xf - -C $HOME/.agoric
mv $HOME/.agoric/priv_validator_state.json.backup $HOME/.agoric/data/priv_validator_state.json
```

### Restart the service and check the log

```bash
sudo systemctl start agd && journalctl -u agd -f --no-hostname -o cat
```
