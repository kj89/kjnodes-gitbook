# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/paloma.png" alt=""><figcaption></figcaption></figure>

Paloma is a fast, permissionless, Cosmos-SDK blockchain that  moves messages securely, between any other blockchains.

**Chain ID**: messenger | **Latest Version Tag**: v0.11.6 | **Wasm**: ON

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
peers="dfa0d66a3713bf6b49bc509a2a4fc75bee042a30@23.88.77.188:20009,e833844c00b8ce60ce6826f170becfa18e6172c2@46.4.27.59:26656,99c890c97afc8abfdfeff662d539af5c504a0baf@88.99.67.234:26656,b3ba407aef9e18e16e8e9a3b523a1b026dabeab3@84.46.248.174:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:11056,1a0232b9426aa1c7a78c92a2136b69d050bb6942@65.108.224.126:26656,87b4221770495e66e772a53bbea92a15aff288c2@144.126.158.0:26656,7e93f6409ade895fe301b502d6fb9dfb96343a34@135.125.5.34:54056,60066422d3b70fbf7571012b267dc2cccd9603d5@149.102.156.223:26656,19165f3248f358ded53c3f51cf97a22123560b86@65.109.69.154:38656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.paloma/config/config.toml
```
