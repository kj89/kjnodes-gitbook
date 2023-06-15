---
description: Catch the latest block faster by using our daily snapshots.
---

# Snapshot

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/althea.png" alt=""><figcaption></figcaption></figure>

{% hint style='info' %}
Snapshots allows a new node to join the network by recovering application state from a backup file. 
Snapshot contains compressed copy of chain data directory. To keep backup files as small as plausible, 
snapshot server is periodically beeing state-synced.
{% endhint %}

Snapshots are taken automatically every 6 hours starting at **08:15 UTC**

**pruning**: 100/0/19 | **indexer**: null | **version tag**: v0.3.2

| BLOCK             | AGE             | DOWNLOAD                                                                                            |
| ----------------- | --------------- | --------------------------------------------------------------------------------------------------- |
| 1836189 | 10 hours | [snapshot (9.84 GB)](https://snapshots.kjnodes.com/althea-testnet/snapshot\_latest.tar.lz4) |

## Instructions

### Stop the service and reset the data

```bash
sudo systemctl stop althea
cp $HOME/.althea/data/priv_validator_state.json $HOME/.althea/priv_validator_state.json.backup
rm -rf $HOME/.althea/data
```

### Download latest snapshot

```bash
curl -L https://snapshots.kjnodes.com/althea-testnet/snapshot_latest.tar.lz4 | tar -Ilz4 -xf - -C $HOME/.althea
mv $HOME/.althea/priv_validator_state.json.backup $HOME/.althea/data/priv_validator_state.json
```

### Restart the service and check the log

```bash
sudo systemctl start althea && sudo journalctl -u althea -f --no-hostname -o cat
```
