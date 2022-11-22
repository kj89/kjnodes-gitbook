---
description: Catch the latest block faster by using our daily snapshots.
---

# Snapshot

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/aura.png" width="150" alt=""><figcaption></figcaption></figure>

{% hint style='info' %}
Snapshots allows a new node to join the network by recovering application state from a backup file. 
Snapshot contains compressed copy of chain data directory. To keep backup files as small as plausible, 
snapshot server is periodically beeing state-synced.
{% endhint %}

**pruning**: 100/0/19 | **indexer**: null | **version tag**: euphoria_v0.3.3

| BLOCK             | AGE             | DOWNLOAD                                                                                            |
| ----------------- | --------------- | --------------------------------------------------------------------------------------------------- |
| 1989454 | 11 hours ago | [snapshot (1.1 GB)](https://snapshots.kjnodes.com/aura-testnet/snapshot\_latest.tar.lz4) |

## Instructions

### Stop the service and reset the data

```bash
sudo systemctl stop aurad
cp $HOME/.aura/data/priv_validator_state.json $HOME/.aura/priv_validator_state.json.backup
rm -rf $HOME/.aura/data
```

### Download latest snapshot

```bash
curl -L https://snapshots.kjnodes.com/aura-testnet/snapshot_latest.tar.lz4 | lz4 -dc - | tar -xf - -C $HOME/.aura
mv $HOME/.aura/priv_validator_state.json.backup $HOME/.aura/data/priv_validator_state.json
```

### Restart the service and check the log

```bash
sudo systemctl start aurad && journalctl -u aurad -f --no-hostname -o cat
```
