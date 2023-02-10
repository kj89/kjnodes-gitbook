# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/paloma.png" width="150" alt=""><figcaption></figcaption></figure>

Paloma is a fast, permissionless, Cosmos-SDK blockchain that  moves messages securely, between any other blockchains.

**Chain ID**: messenger | **Latest Version Tag**: v0.11.6 | **Wasm**: ON

[Website](https://www.palomachain.com) | [Discord](https://discord.gg/tKVFpfdSw4) | [Twitter](https://twitter.com/paloma_chain)




## Chain explorer
[https://explorer.kjnodes.com/paloma](https://explorer.kjnodes.com/paloma)

## Public endpoints

* api: [https://paloma.api.kjnodes.com](https://paloma.api.kjnodes.com)
* rpc: [https://paloma.rpc.kjnodes.com](https://paloma.rpc.kjnodes.com)
* grpc: [https://paloma.grpc.kjnodes.com](https://paloma.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@paloma.rpc.kjnodes.com:10656
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@paloma.rpc.kjnodes.com:10659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/paloma/addrbook.json > $HOME/.paloma/config/addrbook.json
```

**live-peers** (9)
```bash
peers="d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:10656,e833844c00b8ce60ce6826f170becfa18e6172c2@46.4.27.59:26656,4569193b58dfc6d9ca9acd4e2bcabf596e5b6b3c@65.21.7.251:10656,124cbe860f1eaa8084444587928db17c78ebd8f3@34.147.54.231:26656,7eae755c119f538e0dc99f3c37289de628bc9526@209.182.239.169:26656,b244dfc19293103040d4bdad359534d0990a9070@45.140.185.181:26656,e4b7cdd48c39c355e9a3480f4f4d5afab8fb0e08@46.0.203.78:26637,b3ba407aef9e18e16e8e9a3b523a1b026dabeab3@84.46.248.174:26656,dfa0d66a3713bf6b49bc509a2a4fc75bee042a30@23.88.77.188:20009"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.paloma/config/config.toml
```
