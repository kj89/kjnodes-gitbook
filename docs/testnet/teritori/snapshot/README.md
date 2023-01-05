---
description: Catch the latest block faster by using our daily snapshots.
---

# Snapshot

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/teritori.png" width="150" alt=""><figcaption></figcaption></figure>

{% hint style='info' %}
Snapshots allows a new node to join the network by recovering application state from a backup file. 
Snapshot contains compressed copy of chain data directory. To keep backup files as small as plausible, 
snapshot server is periodically beeing state-synced.
{% endhint %}

Snapshots are taken automatically every 6 hours starting at **01:15 UTC**

**pruning**: 100/0/19 | **indexer**: null | **version tag**: v1.3.0

| BLOCK             | AGE             | DOWNLOAD                                                                                            |
| ----------------- | --------------- | --------------------------------------------------------------------------------------------------- |
| 2713079 | 51 minutes | [snapshot (0.33 GB)](https://snapshots.kjnodes.com/teritori-testnet/snapshot\_latest.tar.lz4) |

## Instructions

### Stop the service and reset the data

```bash
sudo systemctl stop teritorid
cp $HOME/.teritorid/data/priv_validator_state.json $HOME/.teritorid/priv_validator_state.json.backup
rm -rf $HOME/.teritorid/data
```

### Download latest snapshot

```bash
curl -L https://snapshots.kjnodes.com/teritori-testnet/snapshot_latest.tar.lz4 | lz4 -dc - | tar -xf - -C $HOME/.teritorid
mv $HOME/.teritorid/priv_validator_state.json.backup $HOME/.teritorid/data/priv_validator_state.json
```

### Restart the service and check the log

```bash
sudo systemctl start teritorid && journalctl -u teritorid -f --no-hostname -o cat
```
