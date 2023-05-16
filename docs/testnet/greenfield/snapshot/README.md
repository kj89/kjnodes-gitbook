---
description: Catch the latest block faster by using our daily snapshots.
---

# Snapshot

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/greenfield.png" alt=""><figcaption></figcaption></figure>

{% hint style='info' %}
Snapshots allows a new node to join the network by recovering application state from a backup file. 
Snapshot contains compressed copy of chain data directory. To keep backup files as small as plausible, 
snapshot server is periodically beeing state-synced.
{% endhint %}

Snapshots are taken automatically every 6 hours starting at **08:45 UTC**

**pruning**: 100/0/19 | **indexer**: null | **version tag**: v0.1.1

| BLOCK             | AGE             | DOWNLOAD                                                                                            |
| ----------------- | --------------- | --------------------------------------------------------------------------------------------------- |
| 884702 | 1 days | [snapshot (1.08 GB)](https://snapshots.kjnodes.com/greenfield-testnet/snapshot\_latest.tar.lz4) |

## Instructions

### Stop the service and reset the data

```bash
sudo systemctl stop gnfd
cp $HOME/.gnfd/data/priv_validator_state.json $HOME/.gnfd/priv_validator_state.json.backup
rm -rf $HOME/.gnfd/data
```

### Download latest snapshot

```bash
curl -L https://snapshots.kjnodes.com/greenfield-testnet/snapshot_latest.tar.lz4 | tar -Ilz4 -xf - -C $HOME/.gnfd
mv $HOME/.gnfd/priv_validator_state.json.backup $HOME/.gnfd/data/priv_validator_state.json
```

### Restart the service and check the log

```bash
sudo systemctl start gnfd && sudo journalctl -u gnfd -f --no-hostname -o cat
```
