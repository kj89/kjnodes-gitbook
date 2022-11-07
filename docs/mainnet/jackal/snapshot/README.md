---
description: >-
  This page contains the latest snapshot to help validators rapidly recover node
  functionality.
---

# Snapshot

| BLOCK             | AGE             | DOWNLOAD                                                                         | SIZE             |
| ----------------- | --------------- | -------------------------------------------------------------------------------- | ---------------- |
| 45381 | 2 hours ago | [snapshot](https://snapshots.kjnodes.com/jackal/snapshot\_latest.tar.lz4) | 0.31 GB |

### Stop the service and reset the data

```bash
sudo systemctl stop canined
cp $HOME/.canine/data/priv_validator_state.json $HOME/.canine/priv_validator_state.json.backup
rm -rf $HOME/.canine/data
```

### Download the latest snapshot

```bash
curl -L https://snapshots.kjnodes.com/jackal/snapshot_latest.tar.lz4 | lz4 -dc - | tar -xf - -C $HOME/.canine
mv $HOME/.canine/priv_validator_state.json.backup $HOME/.canine/data/priv_validator_state.json
```

### Restart the service and check the log

```bash
sudo systemctl start canined && journalctl -u canined -f --no-hostname -o cat
```
