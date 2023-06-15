---
description: Catch the latest block faster by using our daily snapshots.
---

# Snapshot

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/humans.png" alt=""><figcaption></figcaption></figure>

{% hint style='info' %}
Snapshots allows a new node to join the network by recovering application state from a backup file. 
Snapshot contains compressed copy of chain data directory. To keep backup files as small as plausible, 
snapshot server is periodically beeing state-synced.
{% endhint %}

Snapshots are taken automatically every 6 hours starting at **10:00 UTC**

**pruning**: 100/0/19 | **indexer**: null | **version tag**: v1.0.0

| BLOCK             | AGE             | DOWNLOAD                                                                                            |
| ----------------- | --------------- | --------------------------------------------------------------------------------------------------- |
| 242353 | 8 hours | [snapshot (0.22 GB)](https://snapshots.kjnodes.com/humans/snapshot\_latest.tar.lz4) |

## Instructions

### Stop the service and reset the data

```bash
sudo systemctl stop humansd
cp $HOME/.humansd/data/priv_validator_state.json $HOME/.humansd/priv_validator_state.json.backup
rm -rf $HOME/.humansd/data
```

### Download latest snapshot

```bash
curl -L https://snapshots.kjnodes.com/humans/snapshot_latest.tar.lz4 | tar -Ilz4 -xf - -C $HOME/.humansd
mv $HOME/.humansd/priv_validator_state.json.backup $HOME/.humansd/data/priv_validator_state.json
```

### Restart the service and check the log

```bash
sudo systemctl start humansd && sudo journalctl -u humansd -f --no-hostname -o cat
```
