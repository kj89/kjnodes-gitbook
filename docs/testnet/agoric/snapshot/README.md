---
description: Catch the latest block faster by using our daily snapshots.
---

# Snapshot

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/agoric.png" width="150" alt=""><figcaption></figcaption></figure>

{% hint style='info' %}
Snapshots allows a new node to join the network by recovering application state from a backup file. 
Snapshot contains compressed copy of chain data directory. To keep backup files as small as plausible, 
snapshot server is periodically beeing state-synced.
{% endhint %}

Snapshots are taken automatically every 6 hours starting at **04:15 UTC**

**pruning**: 100/0/19 | **indexer**: null | **version tag**: agorictest-upgrade-9

| BLOCK             | AGE             | DOWNLOAD                                                                                            |
| ----------------- | --------------- | --------------------------------------------------------------------------------------------------- |
| 3134300 | 4 hours | [snapshot (1.77 GB)](https://snapshots.kjnodes.com/agoric-testnet/snapshot\_latest.tar.lz4) |

## Instructions

### Stop the service and reset the data

```bash
sudo systemctl stop agd
cp $HOME/.agoric/data/priv_validator_state.json $HOME/.agoric/priv_validator_state.json.backup
rm -rf $HOME/.agoric/data
```

### Download latest snapshot

```bash
curl -L https://snapshots.kjnodes.com/agoric-testnet/snapshot_latest.tar.lz4 | tar -Ilz4 -xf - -C $HOME/.agoric
mv $HOME/.agoric/priv_validator_state.json.backup $HOME/.agoric/data/priv_validator_state.json
```

### Restart the service and check the log

```bash
sudo systemctl start agd && sudo journalctl -u agd -f --no-hostname -o cat
```
