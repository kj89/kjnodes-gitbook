---
description: >-
  This page contains the latest snapshot to help validators rapidly recover node
  functionality.
---

# Snapshot

| BLOCK  | TIMESTAMP  | SIZE    | DOWNLOAD                                                                                                                       |
| ------ | ---------- | ------- | ------------------------------------------------------------------------------------------------------------------------------ |
| 458714 | 12 hours ago | 3.11 GB | [https://snapshots.kjnodes.com/teritori/snapshot\_latest.tar.lz4](https://snapshots.kjnodes.com/teritori/snapshot\_latest.tar.lz4) |

### Stop the service and reset the data

```bash
sudo systemctl stop teritorid
cp $HOME/.teritorid/data/priv_validator_state.json $HOME/.teritorid/priv_validator_state.json.backup
rm -rf $HOME/.teritorid/data
```

### Download the latest snapshot

```bash
curl -L https://snapshots.kjnodes.com/teritori/snapshot_latest.tar.lz4 | lz4 -dc - | tar -xf - -C $HOME/.teritorid
mv $HOME/.teritorid/priv_validator_state.json.backup $HOME/.teritorid/data/priv_validator_state.json
```

### Restart the service and check the log

```bash
sudo systemctl start teritorid && journalctl -u teritorid -f --no-hostname -o cat
```
