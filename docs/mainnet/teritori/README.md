# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/teritori.png" width="150" alt=""><figcaption></figcaption></figure>

Teritori is a multi-chain hub designed to allow IBC and non IBC communities  to connect, trade services & NFTs, launch new projects & build further existing ones.

**Chain ID**: teritori-1 | **Latest Version Tag**: v1.3.0 | **Wasm**: ON

[Website](https://teritori.com) | [Discord](https://discord.gg/teritori) | [Twitter](https://twitter.com/TeritoriNetwork)

## Restake

[Restake with kjnodes](https://restake.app/teritori/torivaloper184ln03hkpt75uhrrr26f66kvcqvf4yn4nc2xjm) (every day at 08:00, 20:00)
## Public endpoints

* rpc: [https://teritori.rpc.kjnodes.com](https://teritori.rpc.kjnodes.com)
* api: [https://teritori.api.kjnodes.com](https://teritori.api.kjnodes.com)

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@teritori.rpc.kjnodes.com:19656
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@teritori.rpc.kjnodes.com:19659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/teritori/addrbook.json > $HOME/.teritorid/config/addrbook.json
```

**live-peers** (24)
```bash
peers="d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:19656,26175f13ada3d61c93bca342819fd5dc797bced0@65.109.58.226:28656,e3374c3d25a36f06662fa150043e5e6529d11570@88.198.32.17:31656,0b27217386756577e1eadf00c4169dc8f041e522@51.210.7.219:26656,82ebb17ddac20928fb8107201dad9f5aea7f9132@198.244.200.3:26656,a25a3a218a699e71e2a64edaa45f457dfd8507ba@65.21.148.206:26656,3bd3a20d7c8a26a20927289a7a6bffecf71de53e@51.81.155.97:10856,920f32f409bbb18b641cdc9513545e2e016c2c62@142.132.203.60:26656,856c165de82fbd0489df9ec6ffaa0958c620e073@198.244.179.127:26656,ef54691ee6f731e49d58e7ee91cf42927f2d7947@144.126.136.227:26656,526d8c7c44f59be9a39d7463c576b68c0db23174@65.108.234.23:15956,ed747c9e39fc04fdbc7ab5fc4a4a7f7a298ee329@65.144.145.234:26656,8ac41af54dfd91c41de71cde222a55670f2f405d@141.95.65.73:15956,fffcd8c41a92e24d67b6d026f556c5afd49db092@45.77.41.21:26656,5a98d637a16b16bf425a4a785c9d11a7d1e5b8a0@65.21.131.215:26736,46b7ae20e3cc4264076a91c3601f3894a021a80d@65.108.6.45:36656,d856120f262134ebf13e1d2632d778b69e704208@65.108.4.188:15956,317d9a102d4a04337c65571c18df0e98269dce87@141.94.193.12:13656,e01ab41f694c18226d827172934dd0c596cc92de@51.159.181.184:26656,3594b73f909a9c4b87cfe6a361ef8b2b51124dd5@65.109.69.59:15956,6085c32b26fb1baa4b16b426f5d56f2fff81cfc7@135.181.165.246:26656,942c99cb9ff717552f884639dda9f52ab66f9726@65.108.134.12:26656,4740ad44e58f4f4a0e2b9c4353500009eb73a05a@176.191.97.120:26656,f97a75fb69d3a5fe893dca7c8d238ccc0bd66a8f@188.165.221.155:6969"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.teritorid/config/config.toml
```
