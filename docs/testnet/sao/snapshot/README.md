---
description: Catch the latest block faster by using our daily snapshots.
---

# Snapshot

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/sao.png" width="150" alt=""><figcaption></figcaption></figure>

{% hint style='info' %}
Snapshots allows a new node to join the network by recovering application state from a backup file. 
Snapshot contains compressed copy of chain data directory. To keep backup files as small as plausible, 
snapshot server is periodically beeing state-synced.
{% endhint %}

Snapshots are taken automatically every 6 hours starting at **07:30 UTC**

**pruning**: 100/0/19 | **indexer**: null | **version tag**: v0.0.9

| BLOCK             | AGE             | DOWNLOAD                                                                                            |
| ----------------- | --------------- | --------------------------------------------------------------------------------------------------- |
| 363979 | 4 hours | [snapshot (0.35 GB)](https://snapshots.kjnodes.com/sao-testnet/snapshot\_latest.tar.lz4) |

## Instructions

### Stop the service and reset the data

```bash
sudo systemctl stop saod
cp $HOME/.sao/data/priv_validator_state.json $HOME/.sao/priv_validator_state.json.backup
rm -rf $HOME/.sao/data
```

### Download latest snapshot

```bash
curl -L https://snapshots.kjnodes.com/sao-testnet/snapshot_latest.tar.lz4 | tar -Ilz4 -xf - -C $HOME/.sao
mv $HOME/.sao/priv_validator_state.json.backup $HOME/.sao/data/priv_validator_state.json
```

### Restart the service and check the log

```bash
sudo systemctl start saod && sudo journalctl -u saod -f --no-hostname -o cat
```
