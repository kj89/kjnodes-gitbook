---
description: >-
  This page contains the latest snapshot to help validators rapidly recover node
  functionality.
---

# Snapshot

| BLOCK             | AGE             | DOWNLOAD                                                                         | SIZE             |
| ----------------- | --------------- | -------------------------------------------------------------------------------- | ---------------- |
| 586227 | 22 minutes ago | [snapshot](https://snapshots.kjnodes.com/quicksilver-testnet/snapshot\_latest.tar.lz4) | 0.17 GB |

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
