---
description: Catch the latest block faster by using our daily snapshots.
---

# Snapshot

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/nois.png" alt=""><figcaption></figcaption></figure>

{% hint style='info' %}
Snapshots allows a new node to join the network by recovering application state from a backup file. 
Snapshot contains compressed copy of chain data directory. To keep backup files as small as plausible, 
snapshot server is periodically beeing state-synced.
{% endhint %}

Snapshots are taken automatically every 6 hours starting at **08:00 UTC**

**pruning**: 100/0/19 | **indexer**: null | **version tag**: v1.0.3

| BLOCK             | AGE             | DOWNLOAD                                                                                            |
| ----------------- | --------------- | --------------------------------------------------------------------------------------------------- |
| 2895981 | 10 hours | [snapshot (1.86 GB)](https://snapshots.kjnodes.com/nois/snapshot\_latest.tar.lz4) |

## Instructions

### Stop the service and reset the data

```bash
sudo systemctl stop noisd
cp $HOME/.noisd/data/priv_validator_state.json $HOME/.noisd/priv_validator_state.json.backup
rm -rf $HOME/.noisd/data
```

### Download latest snapshot

```bash
curl -L https://snapshots.kjnodes.com/nois/snapshot_latest.tar.lz4 | tar -Ilz4 -xf - -C $HOME/.noisd
mv $HOME/.noisd/priv_validator_state.json.backup $HOME/.noisd/data/priv_validator_state.json
```

### Restart the service and check the log

```bash
sudo systemctl start noisd && sudo journalctl -u noisd -f --no-hostname -o cat
```
