---
description: Catch the latest block faster by using our daily snapshots.
---

# Snapshot

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/umee.png" alt=""><figcaption></figcaption></figure>

{% hint style='info' %}
Snapshots allows a new node to join the network by recovering application state from a backup file. 
Snapshot contains compressed copy of chain data directory. To keep backup files as small as plausible, 
snapshot server is periodically beeing state-synced.
{% endhint %}

Snapshots are taken automatically every 6 hours starting at **11:00 UTC**

**pruning**: 100/0/19 | **indexer**: null | **version tag**: 

| BLOCK             | AGE             | DOWNLOAD                                                                                            |
| ----------------- | --------------- | --------------------------------------------------------------------------------------------------- |
|  |  | [snapshot ()](https://snapshots.kjnodes.com/umee/snapshot\_latest.tar.lz4) |

## Instructions

### Stop the service and reset the data

```bash
sudo systemctl stop umeed
cp $HOME/.umee/data/priv_validator_state.json $HOME/.umee/priv_validator_state.json.backup
rm -rf $HOME/.umee/data
```

### Download latest snapshot

```bash
curl -L https://snapshots.kjnodes.com/umee/snapshot_latest.tar.lz4 | tar -Ilz4 -xf - -C $HOME/.umee
mv $HOME/.umee/priv_validator_state.json.backup $HOME/.umee/data/priv_validator_state.json
```

### Restart the service and check the log

```bash
sudo systemctl start umeed && sudo journalctl -u umeed -f --no-hostname -o cat
```
