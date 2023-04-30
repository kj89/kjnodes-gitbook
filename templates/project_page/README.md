# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/${PROJECT_NAME}.png" alt=""><figcaption></figcaption></figure>

${CHAIN_SHORT_DESCRIPTION}
**Chain ID**: ${CHAIN_ID} | **Latest Version Tag**: ${LATEST_VERSION_TAG} | **Wasm**: ${CHAIN_WASM}

[Website](${CHAIN_WEBSITE}) | [Discord](${CHAIN_DISCORD}) | [Twitter](${CHAIN_TWITTER})

${STAKE_BUTTON}

${PROPOSAL_BOT}

${RESTAKE}
## Chain explorer
[https://explorer.kjnodes.com/${CHAIN_SERVICE}](https://explorer.kjnodes.com/${CHAIN_SERVICE})

## Public endpoints

* api: [https://${CHAIN_NAME}.api.kjnodes.com](https://${CHAIN_NAME}.api.kjnodes.com)
* rpc: [https://${CHAIN_NAME}.rpc.kjnodes.com](https://${CHAIN_NAME}.rpc.kjnodes.com)
* grpc: ${CHAIN_NAME}.grpc.kjnodes.com:${CHAIN_PORT}90

## Peering

**state-sync**

```text
${CHAIN_PEER}@${CHAIN_NAME}.rpc.kjnodes.com:${CHAIN_PORT}56
```

**seed-node**

```text
${CHAIN_TENDERSEED_PEER}@${CHAIN_NAME}.rpc.kjnodes.com:${CHAIN_PORT}59
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/${CHAIN_NAME}/addrbook.json > $HOME/${CHAIN_DIR}/config/addrbook.json
```

**live-peers** (${CHAIN_LIVE_PEERS_COUNT})
```bash
peers="${CHAIN_LIVE_PEERS}"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/${CHAIN_DIR}/config/config.toml
```
