---
description: Catch the latest block faster by using our daily snapshots.
---

# Snapshot

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/quasar.png" alt=""><figcaption></figcaption></figure>

{% hint style='info' %}
Snapshots allows a new node to join the network by recovering application state from a backup file. 
Snapshot contains compressed copy of chain data directory. To keep backup files as small as plausible, 
snapshot server is periodically beeing state-synced.
{% endhint %}

Snapshots are taken automatically every 6 hours starting at **07:15 UTC**

**pruning**: 100/0/19 | **indexer**: null | **version tag**: v0.1.1

| BLOCK             | AGE             | DOWNLOAD                                                                                            |
| ----------------- | --------------- | --------------------------------------------------------------------------------------------------- |
| 1281994 | 11 hours | [snapshot (0.69 GB)](https://snapshots.kjnodes.com/quasar/snapshot\_latest.tar.lz4) |

## Instructions

### Stop the service and reset the data

```bash
sudo systemctl stop quasarnoded
cp $HOME/.quasarnode/data/priv_validator_state.json $HOME/.quasarnode/priv_validator_state.json.backup
rm -rf $HOME/.quasarnode/data
```

### Download latest snapshot

```bash
curl -L https://snapshots.kjnodes.com/quasar/snapshot_latest.tar.lz4 | tar -Ilz4 -xf - -C $HOME/.quasarnode
mv $HOME/.quasarnode/priv_validator_state.json.backup $HOME/.quasarnode/data/priv_validator_state.json
```

### Restart the service and check the log

```bash
sudo systemctl start quasarnoded && sudo journalctl -u quasarnoded -f --no-hostname -o cat
```
