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
peers="ff09fa406702cb607a0ca7389d5c1ccf9d09c8b3@65.109.53.22:54056,b3ba407aef9e18e16e8e9a3b523a1b026dabeab3@84.46.248.174:26656,b244dfc19293103040d4bdad359534d0990a9070@45.140.185.181:26656,0bcc8119877ba0c701cd230e35c5477da2657bef@5.78.102.204:26656,e5bee82a116c174abf0981c20c34d0e13a7f6c1d@81.0.221.57:26656,9581fadb9a32f2af89d575bb0f2661b9bb216d41@46.4.23.108:26656,99c890c97afc8abfdfeff662d539af5c504a0baf@88.99.67.234:26656,08c242d4505c5db223647069fdc0acb6e90079aa@65.109.106.214:26656,cb8a1e9e12ac06dbd565311137f6c93d66fd96f8@104.167.221.18:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:11056"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.paloma/config/config.toml
```
