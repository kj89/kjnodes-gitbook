---
description: Catch the latest block faster by using our daily snapshots.
---

# Snapshot

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/stargaze.png" alt=""><figcaption></figcaption></figure>

{% hint style='info' %}
Snapshots allows a new node to join the network by recovering application state from a backup file. 
Snapshot contains compressed copy of chain data directory. To keep backup files as small as plausible, 
snapshot server is periodically beeing state-synced.
{% endhint %}

Snapshots are taken automatically every 6 hours starting at **09:45 UTC**

**pruning**: 100/0/19 | **indexer**: null | **version tag**: v9

| BLOCK             | AGE             | DOWNLOAD                                                                                            |
| ----------------- | --------------- | --------------------------------------------------------------------------------------------------- |
| 8439209 | 2 hours | [snapshot (2.37 GB)](https://snapshots.kjnodes.com/stargaze/snapshot\_latest.tar.lz4) |

## Instructions

### Stop the service and reset the data

```bash
sudo systemctl stop starsd
cp $HOME/.starsd/data/priv_validator_state.json $HOME/.starsd/priv_validator_state.json.backup
rm -rf $HOME/.starsd/data
```

### Download latest snapshot

```bash
curl -L https://snapshots.kjnodes.com/stargaze/snapshot_latest.tar.lz4 | tar -Ilz4 -xf - -C $HOME/.starsd
mv $HOME/.starsd/priv_validator_state.json.backup $HOME/.starsd/data/priv_validator_state.json
```

### Restart the service and check the log

```bash
sudo systemctl start starsd && sudo journalctl -u starsd -f --no-hostname -o cat
```
