---
description: Catch the latest block faster by using our daily snapshots.
---

# Snapshot

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/mars.png" alt=""><figcaption></figcaption></figure>

{% hint style='info' %}
Snapshots allows a new node to join the network by recovering application state from a backup file. 
Snapshot contains compressed copy of chain data directory. To keep backup files as small as plausible, 
snapshot server is periodically beeing state-synced.
{% endhint %}

Snapshots are taken automatically every 6 hours starting at **06:00 UTC**

**pruning**: 100/0/19 | **indexer**: null | **version tag**: v1.0.2

| BLOCK             | AGE             | DOWNLOAD                                                                                            |
| ----------------- | --------------- | --------------------------------------------------------------------------------------------------- |
| 1900513 | 2 hours | [snapshot (0.84 GB)](https://snapshots.kjnodes.com/mars/snapshot\_latest.tar.lz4) |

## Instructions

### Stop the service and reset the data

```bash
sudo systemctl stop marsd
cp $HOME/.mars/data/priv_validator_state.json $HOME/.mars/priv_validator_state.json.backup
rm -rf $HOME/.mars/data
```

### Download latest snapshot

```bash
curl -L https://snapshots.kjnodes.com/mars/snapshot_latest.tar.lz4 | tar -Ilz4 -xf - -C $HOME/.mars
mv $HOME/.mars/priv_validator_state.json.backup $HOME/.mars/data/priv_validator_state.json
```

### Restart the service and check the log

```bash
sudo systemctl start marsd && sudo journalctl -u marsd -f --no-hostname -o cat
```
