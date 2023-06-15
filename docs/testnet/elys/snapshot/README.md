---
description: Catch the latest block faster by using our daily snapshots.
---

# Snapshot

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/elys.png" alt=""><figcaption></figcaption></figure>

{% hint style='info' %}
Snapshots allows a new node to join the network by recovering application state from a backup file. 
Snapshot contains compressed copy of chain data directory. To keep backup files as small as plausible, 
snapshot server is periodically beeing state-synced.
{% endhint %}

Snapshots are taken automatically every 6 hours starting at **08:30 UTC**

**pruning**: 100/0/19 | **indexer**: null | **version tag**: v0.6.0

| BLOCK             | AGE             | DOWNLOAD                                                                                            |
| ----------------- | --------------- | --------------------------------------------------------------------------------------------------- |
| 1013641 | 10 hours | [snapshot (2.52 GB)](https://snapshots.kjnodes.com/elys-testnet/snapshot\_latest.tar.lz4) |

## Instructions

### Stop the service and reset the data

```bash
sudo systemctl stop elysd
cp $HOME/.elys/data/priv_validator_state.json $HOME/.elys/priv_validator_state.json.backup
rm -rf $HOME/.elys/data
```

### Download latest snapshot

```bash
curl -L https://snapshots.kjnodes.com/elys-testnet/snapshot_latest.tar.lz4 | tar -Ilz4 -xf - -C $HOME/.elys
mv $HOME/.elys/priv_validator_state.json.backup $HOME/.elys/data/priv_validator_state.json
```

### Restart the service and check the log

```bash
sudo systemctl start elysd && sudo journalctl -u elysd -f --no-hostname -o cat
```
