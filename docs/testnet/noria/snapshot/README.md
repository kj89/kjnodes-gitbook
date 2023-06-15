---
description: Catch the latest block faster by using our daily snapshots.
---

# Snapshot

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/noria.png" alt=""><figcaption></figcaption></figure>

{% hint style='info' %}
Snapshots allows a new node to join the network by recovering application state from a backup file. 
Snapshot contains compressed copy of chain data directory. To keep backup files as small as plausible, 
snapshot server is periodically beeing state-synced.
{% endhint %}

Snapshots are taken automatically every 6 hours starting at **10:45 UTC**

**pruning**: 100/0/19 | **indexer**: null | **version tag**: v1.2.0

| BLOCK             | AGE             | DOWNLOAD                                                                                            |
| ----------------- | --------------- | --------------------------------------------------------------------------------------------------- |
| 1301619 | 8 hours | [snapshot (0.25 GB)](https://snapshots.kjnodes.com/noria-testnet/snapshot\_latest.tar.lz4) |

## Instructions

### Stop the service and reset the data

```bash
sudo systemctl stop noriad
cp $HOME/.noria/data/priv_validator_state.json $HOME/.noria/priv_validator_state.json.backup
rm -rf $HOME/.noria/data
```

### Download latest snapshot

```bash
curl -L https://snapshots.kjnodes.com/noria-testnet/snapshot_latest.tar.lz4 | tar -Ilz4 -xf - -C $HOME/.noria
mv $HOME/.noria/priv_validator_state.json.backup $HOME/.noria/data/priv_validator_state.json
```

### Restart the service and check the log

```bash
sudo systemctl start noriad && sudo journalctl -u noriad -f --no-hostname -o cat
```
