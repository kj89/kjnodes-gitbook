---
description: >-
  This page contains the latest snapshot to help validators rapidly recover node
  functionality.
---

# Snapshot

| BLOCK             | AGE             | DOWNLOAD                                                                         | SIZE             |
| ----------------- | --------------- | -------------------------------------------------------------------------------- | ---------------- |
| 223394 | 16 hours ago | [snapshot](https://snapshots.kjnodes.com/nibiru-testnet/snapshot\_latest.tar.lz4) | 0.47 GB |

### Stop the service and reset the data

```bash
sudo systemctl stop nibid
cp $HOME/.nibid/data/priv_validator_state.json $HOME/.nibid/priv_validator_state.json.backup
rm -rf $HOME/.nibid/data
```

### Download the latest snapshot

```bash
curl -L https://snapshots.kjnodes.com/nibiru-testnet/snapshot_latest.tar.lz4 | lz4 -dc - | tar -xf - -C $HOME/.nibid
mv $HOME/.nibid/priv_validator_state.json.backup $HOME/.nibid/data/priv_validator_state.json
```

### Restart the service and check the log

```bash
sudo systemctl start nibid && journalctl -u nibid -f --no-hostname -o cat
```
