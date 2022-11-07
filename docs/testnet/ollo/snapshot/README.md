---
description: >-
  Snapshots allows a new node to join the network by recovering application state from a backup file. 
  It is compressed copy of chain data direcotry. To keep backup files small, snapshot server is periodically beeing state-synced.
---

# Snapshot

| BLOCK             | AGE             | DOWNLOAD                                                                         | SIZE             |
| ----------------- | --------------- | -------------------------------------------------------------------------------- | ---------------- |
| 80507 | 20 hours ago | [snapshot](https://snapshots.kjnodes.com/ollo-testnet/snapshot\_latest.tar.lz4) | 0.15 GB |

### Stop the service and reset the data

```bash
sudo systemctl stop ollod
cp $HOME/.ollo/data/priv_validator_state.json $HOME/.ollo/priv_validator_state.json.backup
rm -rf $HOME/.ollo/data
```

### Download the latest snapshot

```bash
curl -L https://snapshots.kjnodes.com/ollo-testnet/snapshot_latest.tar.lz4 | lz4 -dc - | tar -xf - -C $HOME/.ollo
mv $HOME/.ollo/priv_validator_state.json.backup $HOME/.ollo/data/priv_validator_state.json
```

### Restart the service and check the log

```bash
sudo systemctl start ollod && journalctl -u ollod -f --no-hostname -o cat
```
