---
description: Catch the latest block faster by using our daily snapshots.
---

# Snapshot

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/osmosis.png" alt=""><figcaption></figcaption></figure>

{% hint style='info' %}
Snapshots allows a new node to join the network by recovering application state from a backup file. 
Snapshot contains compressed copy of chain data directory. To keep backup files as small as plausible, 
snapshot server is periodically beeing state-synced.
{% endhint %}

Snapshots are taken automatically every 6 hours starting at **02:30 UTC**

**pruning**: 100/0/19 | **indexer**: null | **version tag**: v15

| BLOCK             | AGE             | DOWNLOAD                                                                                            |
| ----------------- | --------------- | --------------------------------------------------------------------------------------------------- |
| 10093485 | 3 hours | [snapshot (13.3 GB)](https://snapshots.kjnodes.com/osmosis/snapshot\_latest.tar.lz4) |

## Instructions

### Stop the service and reset the data

```bash
sudo systemctl stop osmosisd
cp $HOME/.osmosisd/data/priv_validator_state.json $HOME/.osmosisd/priv_validator_state.json.backup
rm -rf $HOME/.osmosisd/data
```

### Download latest snapshot

```bash
curl -L https://snapshots.kjnodes.com/osmosis/snapshot_latest.tar.lz4 | tar -Ilz4 -xf - -C $HOME/.osmosisd
mv $HOME/.osmosisd/priv_validator_state.json.backup $HOME/.osmosisd/data/priv_validator_state.json
```

### Restart the service and check the log

```bash
sudo systemctl start osmosisd && sudo journalctl -u osmosisd -f --no-hostname -o cat
```
