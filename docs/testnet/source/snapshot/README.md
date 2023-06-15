---
description: Catch the latest block faster by using our daily snapshots.
---

# Snapshot

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/source.png" alt=""><figcaption></figcaption></figure>

{% hint style='info' %}
Snapshots allows a new node to join the network by recovering application state from a backup file. 
Snapshot contains compressed copy of chain data directory. To keep backup files as small as plausible, 
snapshot server is periodically beeing state-synced.
{% endhint %}

Snapshots are taken automatically every 6 hours starting at **06:30 UTC**

**pruning**: 100/0/19 | **indexer**: null | **version tag**: v1.0.0

| BLOCK             | AGE             | DOWNLOAD                                                                                            |
| ----------------- | --------------- | --------------------------------------------------------------------------------------------------- |
| 6420177 | 17 minutes | [snapshot (0.43 GB)](https://snapshots.kjnodes.com/source-testnet/snapshot\_latest.tar.lz4) |

## Instructions

### Stop the service and reset the data

```bash
sudo systemctl stop sourced
cp $HOME/.source/data/priv_validator_state.json $HOME/.source/priv_validator_state.json.backup
rm -rf $HOME/.source/data
```

### Download latest snapshot

```bash
curl -L https://snapshots.kjnodes.com/source-testnet/snapshot_latest.tar.lz4 | tar -Ilz4 -xf - -C $HOME/.source
mv $HOME/.source/priv_validator_state.json.backup $HOME/.source/data/priv_validator_state.json
```

### Restart the service and check the log

```bash
sudo systemctl start sourced && sudo journalctl -u sourced -f --no-hostname -o cat
```
