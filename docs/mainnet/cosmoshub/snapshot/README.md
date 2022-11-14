---
description: Catch the latest block faster by using our daily snapshots.
---

# Snapshot

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/cosmoshub.png" width="150" alt=""><figcaption></figcaption></figure>

{% hint style='info' %}
Snapshots allows a new node to join the network by recovering application state from a backup file. 
Snapshot contains compressed copy of chain data directory. To keep backup files as small as plausible, 
snapshot server is periodically beeing state-synced.
{% endhint %}

**pruning**: 100/0/19 | **indexer**: null | **version tag**: v7.1.0

| BLOCK             | AGE             | DOWNLOAD                                                                                            |
| ----------------- | --------------- | --------------------------------------------------------------------------------------------------- |
| 12839991 | 6 hours ago | [snapshot (5.1 GB)](https://snapshots.kjnodes.com/cosmoshub/snapshot\_latest.tar.lz4) |

## Instructions

### Stop the service and reset the data

```bash
sudo systemctl stop gaiad
cp $HOME/.gaiad/data/priv_validator_state.json $HOME/.gaiad/priv_validator_state.json.backup
rm -rf $HOME/.gaiad/data
```

### Download latest snapshot

```bash
curl -L https://snapshots.kjnodes.com/cosmoshub/snapshot_latest.tar.lz4 | lz4 -dc - | tar -xf - -C $HOME/.gaiad
mv $HOME/.gaiad/priv_validator_state.json.backup $HOME/.gaiad/data/priv_validator_state.json
```

### Restart the service and check the log

```bash
sudo systemctl start gaiad && journalctl -u gaiad -f --no-hostname -o cat
```
