---
description: Catch the latest block faster by using our daily snapshots.
---

# Snapshot

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/zetachain.png" alt=""><figcaption></figcaption></figure>

{% hint style='info' %}
Snapshots allows a new node to join the network by recovering application state from a backup file. 
Snapshot contains compressed copy of chain data directory. To keep backup files as small as plausible, 
snapshot server is periodically beeing state-synced.
{% endhint %}

Snapshots are taken automatically every 6 hours starting at **10:30 UTC**

**pruning**: 100/0/19 | **indexer**: null | **version tag**: latest

| BLOCK             | AGE             | DOWNLOAD                                                                                            |
| ----------------- | --------------- | --------------------------------------------------------------------------------------------------- |
| 319522 | 8 hours | [snapshot (2.29 GB)](https://snapshots.kjnodes.com/zetachain-testnet/snapshot\_latest.tar.lz4) |

## Instructions

### Stop the service and reset the data

```bash
sudo systemctl stop zetacored
cp $HOME/.zetacored/data/priv_validator_state.json $HOME/.zetacored/priv_validator_state.json.backup
rm -rf $HOME/.zetacored/data
```

### Download latest snapshot

```bash
curl -L https://snapshots.kjnodes.com/zetachain-testnet/snapshot_latest.tar.lz4 | tar -Ilz4 -xf - -C $HOME/.zetacored
mv $HOME/.zetacored/priv_validator_state.json.backup $HOME/.zetacored/data/priv_validator_state.json
```

### Restart the service and check the log

```bash
sudo systemctl start zetacored && sudo journalctl -u zetacored -f --no-hostname -o cat
```
