---
description: >-
  This page contains the latest snapshot to help validators rapidly recover node
  functionality.
---

# Snapshot

| BLOCK             | AGE             | DOWNLOAD                                                                         | SIZE             |
| ----------------- | --------------- | -------------------------------------------------------------------------------- | ---------------- |
| 874851 | 47 minutes ago | [snapshot](https://snapshots.kjnodes.com/stride/snapshot\_latest.tar.lz4) | 0.21 GB |

### Stop the service and reset the data

```bash
sudo systemctl stop strided
cp $HOME/.stride/data/priv_validator_state.json $HOME/.stride/priv_validator_state.json.backup
rm -rf $HOME/.stride/data
```

### Download the latest snapshot

```bash
curl -L https://snapshots.kjnodes.com/stride/snapshot_latest.tar.lz4 | lz4 -dc - | tar -xf - -C $HOME/.stride
mv $HOME/.stride/priv_validator_state.json.backup $HOME/.stride/data/priv_validator_state.json
```

### Restart the service and check the log

```bash
sudo systemctl start strided && journalctl -u strided -f --no-hostname -o cat
```
