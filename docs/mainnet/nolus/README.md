# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/nolus.png" alt=""><figcaption></figcaption></figure>

Nolus aims to be the leading DeFi Lease platform. The protocol  intends to become a tool for empowering people, simple to use, and highly efficient.

**Chain ID**: pirin-1 | **Latest Version Tag**: v0.3.0 | **Wasm**: ON

[Website](https://www.nolus.io) | [Discord](https://discord.gg/nolus-protocol) | [Twitter](https://twitter.com/NolusProtocol)



Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/nolus](https://explorer.kjnodes.com/nolus)

## Public endpoints

* api: [https://nolus.api.kjnodes.com](https://nolus.api.kjnodes.com)
* rpc: [https://nolus.rpc.kjnodes.com](https://nolus.rpc.kjnodes.com)
* grpc: nolus.grpc.kjnodes.com:14390

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@nolus.rpc.kjnodes.com:14356
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@nolus.rpc.kjnodes.com:14359
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/nolus/addrbook.json > $HOME/.nolus/config/addrbook.json
```

**live-peers** (10)
```bash
peers="89757803f40da51678451735445ad40d5b15e059@169.155.168.149:26656,c6be81e1757c31012ef201d396981d69d370f37a@162.19.237.150:26656,65d9be311c814f775eda349427d11a39eb6b8623@5.10.19.39:26656,97e4468ac589eac505a800411c635b14511a61bb@134.65.195.225:26656,d3f29b638d089a73651a290c3f2e27b8da663f92@65.109.122.105:60756,d2247f7b919f0781c90ee61958d7044665a22d38@164.152.160.230:26656,488c9ee36fc5ee54e662895dfed5e5df9a5ff2d5@136.243.39.118:26656,c124ce0b508e8b9ed1c5b6957f362225659b5343@134.65.193.172:26656,4868bb0024f54952ae5e2f191e1363ac29aab49c@65.108.71.163:2640,6cceba286b498d4a1931f85e35ea0fa433373057@169.155.170.20:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nolus/config/config.toml
```
