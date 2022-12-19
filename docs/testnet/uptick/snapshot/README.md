---
description: Catch the latest block faster by using our daily snapshots.
---

# Snapshot

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/uptick.png" width="150" alt=""><figcaption></figcaption></figure>

{% hint style='info' %}
Snapshots allows a new node to join the network by recovering application state from a backup file. 
Snapshot contains compressed copy of chain data directory. To keep backup files as small as plausible, 
snapshot server is periodically beeing state-synced.
{% endhint %}

Snapshots are taken automatically each day at **06:30 UTC**

**pruning**: 100/0/19 | **indexer**: null | **version tag**: v0.2.4

| BLOCK             | AGE             | DOWNLOAD                                                                                            |
| ----------------- | --------------- | --------------------------------------------------------------------------------------------------- |
| 1233691 | 5 hours ago | [snapshot (1.51 GB)](https://snapshots.kjnodes.com/uptick-testnet/snapshot\_latest.tar.lz4) |

## Instructions

### Stop the service and reset the data

```bash
sudo systemctl stop uptickd
cp $HOME/.uptickd/data/priv_validator_state.json $HOME/.uptickd/priv_validator_state.json.backup
rm -rf $HOME/.uptickd/data
```

### Download latest snapshot

```bash
curl -L https://snapshots.kjnodes.com/uptick-testnet/snapshot_latest.tar.lz4 | lz4 -dc - | tar -xf - -C $HOME/.uptickd
mv $HOME/.uptickd/priv_validator_state.json.backup $HOME/.uptickd/data/priv_validator_state.json
```

### Restart the service and check the log

```bash
sudo systemctl start uptickd && journalctl -u uptickd -f --no-hostname -o cat
```
