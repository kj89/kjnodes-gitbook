---
description: Catch the latest block faster by using our daily snapshots.
---

# Snapshot

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/bitcanna.png" alt=""><figcaption></figcaption></figure>

{% hint style='info' %}
Snapshots allows a new node to join the network by recovering application state from a backup file. 
Snapshot contains compressed copy of chain data directory. To keep backup files as small as plausible, 
snapshot server is periodically beeing state-synced.
{% endhint %}

Snapshots are taken automatically every 6 hours starting at **05:15 UTC**

**pruning**: 100/0/19 | **indexer**: null | **version tag**: vigorous-grow-huckleberry

| BLOCK             | AGE             | DOWNLOAD                                                                                            |
| ----------------- | --------------- | --------------------------------------------------------------------------------------------------- |
| 8998824 | 1 hours | [snapshot (0.77 GB)](https://snapshots.kjnodes.com/bitcanna/snapshot\_latest.tar.lz4) |

## Instructions

### Stop the service and reset the data

```bash
sudo systemctl stop bcnad
cp $HOME/.bcna/data/priv_validator_state.json $HOME/.bcna/priv_validator_state.json.backup
rm -rf $HOME/.bcna/data
```

### Download latest snapshot

```bash
curl -L https://snapshots.kjnodes.com/bitcanna/snapshot_latest.tar.lz4 | tar -Ilz4 -xf - -C $HOME/.bcna
mv $HOME/.bcna/priv_validator_state.json.backup $HOME/.bcna/data/priv_validator_state.json
```

### Restart the service and check the log

```bash
sudo systemctl start bcnad && sudo journalctl -u bcnad -f --no-hostname -o cat
```
