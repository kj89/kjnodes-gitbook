---
description: Catch the latest block faster by using our daily snapshots.
---

# Snapshot

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/gitopia.png" alt=""><figcaption></figcaption></figure>

{% hint style='info' %}
Snapshots allows a new node to join the network by recovering application state from a backup file. 
Snapshot contains compressed copy of chain data directory. To keep backup files as small as plausible, 
snapshot server is periodically beeing state-synced.
{% endhint %}

Snapshots are taken automatically every 6 hours starting at **04:00 UTC**

**pruning**: 100/0/19 | **indexer**: null | **version tag**: v2.1.1

| BLOCK             | AGE             | DOWNLOAD                                                                                            |
| ----------------- | --------------- | --------------------------------------------------------------------------------------------------- |
| 1425497 | 33 minutes | [snapshot (1.48 GB)](https://snapshots.kjnodes.com/gitopia/snapshot\_latest.tar.lz4) |

## Instructions

### Stop the service and reset the data

```bash
sudo systemctl stop gitopiad
cp $HOME/.gitopia/data/priv_validator_state.json $HOME/.gitopia/priv_validator_state.json.backup
rm -rf $HOME/.gitopia/data
```

### Download latest snapshot

```bash
curl -L https://snapshots.kjnodes.com/gitopia/snapshot_latest.tar.lz4 | tar -Ilz4 -xf - -C $HOME/.gitopia
mv $HOME/.gitopia/priv_validator_state.json.backup $HOME/.gitopia/data/priv_validator_state.json
```

### Restart the service and check the log

```bash
sudo systemctl start gitopiad && sudo journalctl -u gitopiad -f --no-hostname -o cat
```
