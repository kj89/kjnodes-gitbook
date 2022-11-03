---
description: >-
  This page contains the latest snapshot to help validators rapidly recover node
  functionality.
---

# Snapshot

| BLOCK  | TIMESTAMP  | SIZE    | DOWNLOAD                                                                                                                       |
| ------ | ---------- | ------- | ------------------------------------------------------------------------------------------------------------------------------ |
| 1623670 | 28 minutes ago | 4.36 GB | [https://snapshots.kjnodes.com/rebus/snapshot\_latest.tar.lz4](https://snapshots.kjnodes.com/rebus/snapshot\_latest.tar.lz4) |

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
