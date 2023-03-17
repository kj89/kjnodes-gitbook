---
description: Catch the latest block faster by using our daily snapshots.
---

# Snapshot

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/sei.png" width="150" alt=""><figcaption></figcaption></figure>

{% hint style='info' %}
Snapshots allows a new node to join the network by recovering application state from a backup file. 
Snapshot contains compressed copy of chain data directory. To keep backup files as small as plausible, 
snapshot server is periodically beeing state-synced.
{% endhint %}

Snapshots are taken automatically every 6 hours starting at **01:45 UTC**

**pruning**: 100/0/19 | **indexer**: null | **version tag**: 1.2.2beta-postfix

| BLOCK             | AGE             | DOWNLOAD                                                                                            |
| ----------------- | --------------- | --------------------------------------------------------------------------------------------------- |
| 24753991 | 5 hours | [snapshot (13.16 GB)](https://snapshots.kjnodes.com/sei-testnet/snapshot\_latest.tar.lz4) |

## Instructions

### Stop the service and reset the data

```bash
sudo systemctl stop seid
cp $HOME/.sei/data/priv_validator_state.json $HOME/.sei/priv_validator_state.json.backup
rm -rf $HOME/.sei/data
```

### Download latest snapshot

```bash
curl -L https://snapshots.kjnodes.com/sei-testnet/snapshot_latest.tar.lz4 | tar -Ilz4 -xf - -C $HOME/.sei
mv $HOME/.sei/priv_validator_state.json.backup $HOME/.sei/data/priv_validator_state.json
```

### Restart the service and check the log

```bash
sudo systemctl start seid && sudo journalctl -u seid -f --no-hostname -o cat
```
