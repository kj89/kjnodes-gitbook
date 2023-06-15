---
description: Catch the latest block faster by using our daily snapshots.
---

# Snapshot

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/hypersign.png" alt=""><figcaption></figcaption></figure>

{% hint style='info' %}
Snapshots allows a new node to join the network by recovering application state from a backup file. 
Snapshot contains compressed copy of chain data directory. To keep backup files as small as plausible, 
snapshot server is periodically beeing state-synced.
{% endhint %}

Snapshots are taken automatically every 6 hours starting at **00:30 UTC**

**pruning**: 100/0/19 | **indexer**: null | **version tag**: v017

| BLOCK             | AGE             | DOWNLOAD                                                                                            |
| ----------------- | --------------- | --------------------------------------------------------------------------------------------------- |
| 3847549 | 16 minutes | [snapshot (1.19 GB)](https://snapshots.kjnodes.com/hypersign-testnet/snapshot\_latest.tar.lz4) |

## Instructions

### Stop the service and reset the data

```bash
sudo systemctl stop hid-noded
cp $HOME/.hid-node/data/priv_validator_state.json $HOME/.hid-node/priv_validator_state.json.backup
rm -rf $HOME/.hid-node/data
```

### Download latest snapshot

```bash
curl -L https://snapshots.kjnodes.com/hypersign-testnet/snapshot_latest.tar.lz4 | tar -Ilz4 -xf - -C $HOME/.hid-node
mv $HOME/.hid-node/priv_validator_state.json.backup $HOME/.hid-node/data/priv_validator_state.json
```

### Restart the service and check the log

```bash
sudo systemctl start hid-noded && sudo journalctl -u hid-noded -f --no-hostname -o cat
```
