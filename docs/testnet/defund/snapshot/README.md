---
description: >-
  This page contains the latest snapshot to help validators rapidly recover node
  functionality.
---

# Snapshot

| BLOCK             | AGE             | DOWNLOAD                                                                         | SIZE             |
| ----------------- | --------------- | -------------------------------------------------------------------------------- | ---------------- |
| 121847 | 16 hours ago | [snapshot](https://snapshots.kjnodes.com/defund-testnet/snapshot\_latest.tar.lz4) | 1.86 GB |

### Stop the service and reset the data

```bash
sudo systemctl stop defundd
cp $HOME/.defund/data/priv_validator_state.json $HOME/.defund/priv_validator_state.json.backup
rm -rf $HOME/.defund/data
```

### Download the latest snapshot

```bash
curl -L https://snapshots.kjnodes.com/defund-testnet/snapshot_latest.tar.lz4 | lz4 -dc - | tar -xf - -C $HOME/.defund
mv $HOME/.defund/priv_validator_state.json.backup $HOME/.defund/data/priv_validator_state.json
```

### Restart the service and check the log

```bash
sudo systemctl start defundd && journalctl -u defundd -f --no-hostname -o cat
```
