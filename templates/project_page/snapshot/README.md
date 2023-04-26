---
description: Catch the latest block faster by using our daily snapshots.
---

# Snapshot

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/${PROJECT_NAME}.png" alt=""><figcaption></figcaption></figure>

{% hint style='info' %}
Snapshots allows a new node to join the network by recovering application state from a backup file. 
Snapshot contains compressed copy of chain data directory. To keep backup files as small as plausible, 
snapshot server is periodically beeing state-synced.
{% endhint %}

Snapshots are taken automatically every 6 hours starting at **${CHAIN_SNAPSHOT_TIME}**

**pruning**: 100/0/19 | **indexer**: null | **version tag**: ${SNAPSHOT_VERSION}

| BLOCK             | AGE             | DOWNLOAD                                                                                            |
| ----------------- | --------------- | --------------------------------------------------------------------------------------------------- |
| ${SNAPSHOT_BLOCK} | ${SNAPSHOT_AGE} | [snapshot (${SNAPSHOT_SIZE})](https://snapshots.kjnodes.com/${CHAIN_NAME}/snapshot\_latest.tar.lz4) |

## Instructions

### Stop the service and reset the data

```bash
sudo systemctl stop ${CHAIN_APP}
cp $HOME/${CHAIN_DIR}/data/priv_validator_state.json $HOME/${CHAIN_DIR}/priv_validator_state.json.backup
rm -rf $HOME/${CHAIN_DIR}/data
```

### Download latest snapshot

```bash
curl -L https://snapshots.kjnodes.com/${CHAIN_NAME}/snapshot_latest.tar.lz4 | tar -Ilz4 -xf - -C $HOME/${CHAIN_DIR}
mv $HOME/${CHAIN_DIR}/priv_validator_state.json.backup $HOME/${CHAIN_DIR}/data/priv_validator_state.json
```

### Restart the service and check the log

```bash
sudo systemctl start ${CHAIN_APP} && sudo journalctl -u ${CHAIN_APP} -f --no-hostname -o cat
```
