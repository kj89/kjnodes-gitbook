---
description: >-
  This page contains the latest snapshot to help validators rapidly recover node
  functionality.
---

# Snapshot

| BLOCK  | TIMESTAMP  | SIZE    | DOWNLOAD                                                                                                                  |
| ------ | ---------- | ------- | ------------------------------------------------------------------------------------------------------------------------- |
| 865090 | 11 hours ago | 6.14 GB | [snapshot\_latest.tar.lz4](https://snapshots.kjnodes.com/stride/snapshot\_latest.tar.lz4) |


<style>
table th:first-of-type {
    width: 10%;
}
table th:nth-of-type(2) {
    width: 10%;
}
table th:nth-of-type(3) {
    width: 50%;
}
table th:nth-of-type(4) {
    width: 30%;
}
</style>


+---------+---------+---------+----------+
| Header1 | header2 | header3 | header4  |
+---------+---------+---------+----------+
| Bar     | bar     | bar     | bar      |
+---------+---------+---------+----------+

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
