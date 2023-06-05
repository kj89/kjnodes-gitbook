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

**live-peers** (10)
```bash
peers="ff09fa406702cb607a0ca7389d5c1ccf9d09c8b3@65.109.53.22:54056,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:11056,b3ba407aef9e18e16e8e9a3b523a1b026dabeab3@84.46.248.174:26656,e833844c00b8ce60ce6826f170becfa18e6172c2@46.4.27.59:26656,60066422d3b70fbf7571012b267dc2cccd9603d5@149.102.156.223:26656,0bcc8119877ba0c701cd230e35c5477da2657bef@5.78.102.204:26656,1a0232b9426aa1c7a78c92a2136b69d050bb6942@65.108.224.126:26656,7eae755c119f538e0dc99f3c37289de628bc9526@209.182.239.169:26656,9319a0981d4baab6dbd6c4eaecf530f016ccfff9@37.120.191.47:60656,317141e329bc214a76ba92201f6818574ebe5323@135.181.114.98:36656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.paloma/config/config.toml
```
