---
description: Catch the latest block faster by using our daily snapshots.
---

# Snapshot

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/migaloo.png" alt=""><figcaption></figcaption></figure>

{% hint style='info' %}
Snapshots allows a new node to join the network by recovering application state from a backup file. 
Snapshot contains compressed copy of chain data directory. To keep backup files as small as plausible, 
snapshot server is periodically beeing state-synced.
{% endhint %}

Snapshots are taken automatically every 6 hours starting at **07:30 UTC**

**pruning**: 100/0/19 | **indexer**: null | **version tag**: v2

| BLOCK             | AGE             | DOWNLOAD                                                                                            |
| ----------------- | --------------- | --------------------------------------------------------------------------------------------------- |
| 1819290 | 11 hours | [snapshot (0.83 GB)](https://snapshots.kjnodes.com/migaloo/snapshot\_latest.tar.lz4) |

## Instructions

### Stop the service and reset the data

```bash
sudo systemctl stop migalood
cp $HOME/.migalood/data/priv_validator_state.json $HOME/.migalood/priv_validator_state.json.backup
rm -rf $HOME/.migalood/data
```

### Download latest snapshot

```bash
curl -L https://snapshots.kjnodes.com/migaloo/snapshot_latest.tar.lz4 | tar -Ilz4 -xf - -C $HOME/.migalood
mv $HOME/.migalood/priv_validator_state.json.backup $HOME/.migalood/data/priv_validator_state.json
```

### Restart the service and check the log

```bash
sudo systemctl start migalood && sudo journalctl -u migalood -f --no-hostname -o cat
```
