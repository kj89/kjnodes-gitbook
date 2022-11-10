# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/${PROJECT_NAME}.png" width="150" alt=""><figcaption></figcaption></figure>

${CHAIN_SHORT_DESCRIPTION}
**Chain ID**: ${CHAIN_ID} | **Latest Version Tag**: ${LATEST_VERSION} | **Wasm**: ${CHAIN_WASM}

Website: [${CHAIN_WEBSITE}](${CHAIN_WEBSITE})

${RESTAKE}
## Public endpoints

* rpc: [https://${CHAIN_NAME}.rpc.kjnodes.com](https://${CHAIN_NAME}.rpc.kjnodes.com)
* api: [https://${CHAIN_NAME}.api.kjnodes.com](https://${CHAIN_NAME}.api.kjnodes.com)

## Peering

**state-sync**

```
${CHAIN_PEER}@${CHAIN_NAME}.rpc.kjnodes.com:${CHAIN_PORT}656
```

**seed-node**

```
${CHAIN_TENDERSEED_PEER}@${CHAIN_NAME}.rpc.kjnodes.com:${CHAIN_PORT}659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/${CHAIN_NAME}/addrbook.json > $HOME/${CHAIN_DIR}/config/addrbook.json
```

**live-peers** (${CHAIN_LIVE_PEERS_COUNT})
```
peers="${CHAIN_LIVE_PEERS}"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/${CHAIN_DIR}/config/config.toml
```
