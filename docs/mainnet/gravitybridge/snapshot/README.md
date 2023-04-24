---
description: Catch the latest block faster by using our daily snapshots.
---

# Snapshot

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/gravitybridge.png" width="150" alt=""><figcaption></figcaption></figure>

{% hint style='info' %}
Snapshots allows a new node to join the network by recovering application state from a backup file. 
Snapshot contains compressed copy of chain data directory. To keep backup files as small as plausible, 
snapshot server is periodically beeing state-synced.
{% endhint %}

Snapshots are taken automatically every 6 hours starting at **03:45 UTC**

**pruning**: 100/0/19 | **indexer**: null | **version tag**: pleiades2

| BLOCK             | AGE             | DOWNLOAD                                                                                            |
| ----------------- | --------------- | --------------------------------------------------------------------------------------------------- |
| 6654499 | 1 hours | [snapshot (1.49 GB)](https://snapshots.kjnodes.com/gravitybridge/snapshot\_latest.tar.lz4) |

## Instructions

### Stop the service and reset the data

```bash
sudo systemctl stop gravityd
cp $HOME/.gravity/data/priv_validator_state.json $HOME/.gravity/priv_validator_state.json.backup
rm -rf $HOME/.gravity/data
```

### Download latest snapshot

```bash
curl -L https://snapshots.kjnodes.com/gravitybridge/snapshot_latest.tar.lz4 | tar -Ilz4 -xf - -C $HOME/.gravity
mv $HOME/.gravity/priv_validator_state.json.backup $HOME/.gravity/data/priv_validator_state.json
```

### Restart the service and check the log

```bash
sudo systemctl start gravityd && sudo journalctl -u gravityd -f --no-hostname -o cat
```
