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

**pruning**: 100/0/19 | **indexer**: null | **version tag**: agoric-upgrade-8

| BLOCK             | AGE             | DOWNLOAD                                                                                            |
| ----------------- | --------------- | --------------------------------------------------------------------------------------------------- |
| 8143640 | 27 minutes | [snapshot (2.39 GB)](https://snapshots.kjnodes.com/agoric/snapshot\_latest.tar.lz4) |

## Instructions

### Stop the service and reset the data

```bash
sudo systemctl stop agd
cp $HOME/.agoric/data/priv_validator_state.json $HOME/.agoric/priv_validator_state.json.backup
rm -rf $HOME/.agoric/data
```

### Download latest snapshot

```bash
curl -L https://snapshots.kjnodes.com/agoric/snapshot_latest.tar.lz4 | tar -Ilz4 -xf - -C $HOME/.agoric
[[ -f $HOME/.agoric/data/upgrade-info.json ]] && cp $HOME/.agoric/data/upgrade-info.json $HOME/.agoric/cosmovisor/genesis/upgrade-info.json
mv $HOME/.agoric/priv_validator_state.json.backup $HOME/.agoric/data/priv_validator_state.json
```

### Restart the service and check the log

```bash
sudo systemctl start agd && sudo journalctl -u agd -f --no-hostname -o cat
```
