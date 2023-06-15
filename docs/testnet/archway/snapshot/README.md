---
description: Catch the latest block faster by using our daily snapshots.
---

# Snapshot

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/archway.png" alt=""><figcaption></figcaption></figure>

{% hint style='info' %}
Snapshots allows a new node to join the network by recovering application state from a backup file. 
Snapshot contains compressed copy of chain data directory. To keep backup files as small as plausible, 
snapshot server is periodically beeing state-synced.
{% endhint %}

Snapshots are taken automatically every 6 hours starting at **09:15 UTC**

**pruning**: 100/0/19 | **indexer**: null | **version tag**: v0.6.0

| BLOCK             | AGE             | DOWNLOAD                                                                                            |
| ----------------- | --------------- | --------------------------------------------------------------------------------------------------- |
| 449155 | 9 hours | [snapshot (0.64 GB)](https://snapshots.kjnodes.com/archway-testnet/snapshot\_latest.tar.lz4) |

## Instructions

### Stop the service and reset the data

```bash
sudo systemctl stop archwayd
cp $HOME/.archway/data/priv_validator_state.json $HOME/.archway/priv_validator_state.json.backup
rm -rf $HOME/.archway/data
```

### Download latest snapshot

```bash
curl -L https://snapshots.kjnodes.com/archway-testnet/snapshot_latest.tar.lz4 | tar -Ilz4 -xf - -C $HOME/.archway
mv $HOME/.archway/priv_validator_state.json.backup $HOME/.archway/data/priv_validator_state.json
```

### Restart the service and check the log

```bash
sudo systemctl start archwayd && sudo journalctl -u archwayd -f --no-hostname -o cat
```
