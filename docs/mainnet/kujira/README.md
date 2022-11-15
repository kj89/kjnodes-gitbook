# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/kujira.png" width="150" alt=""><figcaption></figcaption></figure>

Kujira is a Layer 1 protocol built on Cosmos, which can be used for  hosting community-selected projects.

**Chain ID**: kaiyo-1 | **Latest Version Tag**: v0.7.1 | **Wasm**: ON

Website: [https://kujira.app](https://kujira.app)

## Restake

[Restake with kjnodes](https://restake.app/kujira/kujiravaloper1tnuqj73jfn3724lqz34c27tuv80nv336sadqym) (every day at 08:00, 20:00)
## Public endpoints

* rpc: [https://kujira.rpc.kjnodes.com](https://kujira.rpc.kjnodes.com)
* api: [https://kujira.api.kjnodes.com](https://kujira.api.kjnodes.com)

## Peering

**state-sync**

```
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@kujira.rpc.kjnodes.com:13656
```

**seed-node**

```
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@kujira.rpc.kjnodes.com:13659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/kujira/addrbook.json > $HOME/.kujira/config/addrbook.json
```

**live-peers** (11)
```
peers="bbd504c2ab489671b948faab56f309c764fb23bb@65.108.108.179:9556,610b8e096b4d8f923b1f41f7bdf92d5b63e033dc@162.55.243.82:4060,ed71d6328a0228cd2eac7d71451509813c660b5d@116.202.164.206:26656,5ef740383b8a490c1bee7f9e61bf03c43427b182@83.149.102.56:32095,35629bef4cc1a0be69ebd053ff4e16de82970add@5.79.79.80:30095,d6f2eee997d108d4fde5683e31d678427376dfce@77.68.27.75:26656,de08e6178779ff3b19a8b6d22a05664392cb2b35@185.216.179.205:26656,fc593f5f9fcf7f88790bd8274ebc791f612d3efe@65.21.89.54:26655,f35e499b047c1aa78fe04a16705b508610b7a896@135.181.57.223:26656,4c1f4d9358118cb8917567702c12ca4f31714b32@65.108.132.107:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@144.76.163.233:13656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.kujira/config/config.toml
```
