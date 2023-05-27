# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/paloma.png" alt=""><figcaption></figcaption></figure>

Paloma is a fast, permissionless, Cosmos-SDK blockchain that  moves messages securely, between any other blockchains.

**Chain ID**: messenger | **Latest Version Tag**: v1.0.0 | **Wasm**: ON

[Website](https://www.palomachain.com) | [Discord](https://discord.gg/tKVFpfdSw4) | [Twitter](https://twitter.com/paloma_chain)



Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/paloma](https://explorer.kjnodes.com/paloma)

## Public endpoints

* api: [https://paloma.api.kjnodes.com](https://paloma.api.kjnodes.com)
* rpc: [https://paloma.rpc.kjnodes.com](https://paloma.rpc.kjnodes.com)
* grpc: paloma.grpc.kjnodes.com:11090

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@paloma.rpc.kjnodes.com:11056
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@paloma.rpc.kjnodes.com:11059
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/paloma/addrbook.json > $HOME/.paloma/config/addrbook.json
```

**live-peers** (10)
```bash
peers="e7117b41395352d5d3555153598744f2c963d5ee@65.109.8.247:26656,98b54cd6696e616fe966008ebf2bac409e3e0773@65.108.194.44:26656,471a09da6fafb67bff3aa1f01e00fd1830e53262@136.243.94.138:26656,06e9c9d5c07755d36241249a568b51ec8476fe65@135.181.220.168:26656,9581fadb9a32f2af89d575bb0f2661b9bb216d41@46.4.23.108:26656,e5bee82a116c174abf0981c20c34d0e13a7f6c1d@81.0.221.57:26656,cb8a1e9e12ac06dbd565311137f6c93d66fd96f8@104.167.221.18:26656,317141e329bc214a76ba92201f6818574ebe5323@135.181.114.98:36656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:11056,999dd829036eb4a2c4024b0d35d0fa7c02562770@84.54.23.3:34656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.paloma/config/config.toml
```
