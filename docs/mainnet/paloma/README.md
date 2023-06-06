# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/paloma.png" alt=""><figcaption></figcaption></figure>

Paloma is a fast, permissionless, Cosmos-SDK blockchain that  moves messages securely, between any other blockchains.

**Chain ID**: messenger | **Latest Version Tag**: v1.1.0 | **Wasm**: ON

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

**live-peers** (11)
```bash
peers="1a0232b9426aa1c7a78c92a2136b69d050bb6942@65.108.224.126:26656,8af8dfa817359036f55f6793b0ed4bcce8884027@85.14.245.70:26656,ff09fa406702cb607a0ca7389d5c1ccf9d09c8b3@65.109.53.22:54056,dfa0d66a3713bf6b49bc509a2a4fc75bee042a30@23.88.77.188:20009,b244dfc19293103040d4bdad359534d0990a9070@45.140.185.181:26656,d62eda97bc071f1b91106f484e0784928985f50e@207.180.196.234:26656,471a09da6fafb67bff3aa1f01e00fd1830e53262@136.243.94.138:26656,0bcc8119877ba0c701cd230e35c5477da2657bef@5.78.102.204:26656,317141e329bc214a76ba92201f6818574ebe5323@135.181.114.98:36656,8ed8cddfac504d986a2c6545def0e57b2c6aa5db@65.109.106.172:38656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:11056"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.paloma/config/config.toml
```
