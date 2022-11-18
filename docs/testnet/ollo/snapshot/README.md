---
description: Catch the latest block faster by using our daily snapshots.
---

# Snapshot

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/ollo.png" width="150" alt=""><figcaption></figcaption></figure>

{% hint style='info' %}
Snapshots allows a new node to join the network by recovering application state from a backup file. 
Snapshot contains compressed copy of chain data directory. To keep backup files as small as plausible, 
snapshot server is periodically beeing state-synced.
{% endhint %}

**pruning**: 100/0/19 | **indexer**: null | **version tag**: v0.0.1

| BLOCK             | AGE             | DOWNLOAD                                                                                            |
| ----------------- | --------------- | --------------------------------------------------------------------------------------------------- |
| 253802 | 14 hours ago | [snapshot (1.11 GB)](https://snapshots.kjnodes.com/ollo-testnet/snapshot\_latest.tar.lz4) |

## Instructions

### Stop the service and reset the data

```bash
sudo systemctl stop ollod
cp $HOME/.ollo/data/priv_validator_state.json $HOME/.ollo/priv_validator_state.json.backup
rm -rf $HOME/.ollo/data
```

### Download latest snapshot

```bash
curl -L https://snapshots.kjnodes.com/ollo-testnet/snapshot_latest.tar.lz4 | lz4 -dc - | tar -xf - -C $HOME/.ollo
mv $HOME/.ollo/priv_validator_state.json.backup $HOME/.ollo/data/priv_validator_state.json
```

### Restart the service and check the log

```bash
sudo systemctl start ollod && journalctl -u ollod -f --no-hostname -o cat
```
