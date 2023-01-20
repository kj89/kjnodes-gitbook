# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/teritori.png" width="150" alt=""><figcaption></figcaption></figure>

Teritori is a multi-chain hub designed to allow IBC and non IBC communities  to connect, trade services & NFTs, launch new projects & build further existing ones.

**Chain ID**: teritori-1 | **Latest Version Tag**: v1.3.0 | **Wasm**: ON

[Website](https://teritori.com) | [Discord](https://discord.gg/teritori) | [Twitter](https://twitter.com/TeritoriNetwork)

## Restake

[Restake with kjnodes](https://restake.app/teritori/torivaloper184ln03hkpt75uhrrr26f66kvcqvf4yn4nc2xjm) (every day at 08:00, 20:00)
## Public endpoints

* api: [https://teritori.api.kjnodes.com](https://teritori.api.kjnodes.com)
* rpc: [https://teritori.rpc.kjnodes.com](https://teritori.rpc.kjnodes.com)
* grpc: [https://teritori.grpc.kjnodes.com](https://teritori.grpc.kjnodes.com)

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

**live-peers** (26)
```bash
peers="6fd88e2143e6d4ba02a7f745565120df18e84699@109.236.80.46:26656,1e08fefb7e8851490d40e804df76d1ac33cb1f0a@38.146.3.175:15956,43da931d00da102c002e0a227de7258b8fb1871a@144.126.135.53:26656,920f32f409bbb18b641cdc9513545e2e016c2c62@142.132.203.60:26656,46b7ae20e3cc4264076a91c3601f3894a021a80d@65.108.6.45:36656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:19656,48980875839186e08e12ebf0d9a2803b45206833@65.109.92.241:38026,0b27217386756577e1eadf00c4169dc8f041e522@51.210.7.219:26656,ce3baba928ae06cd3ff0af20aec888a82ddffef7@54.37.129.171:26656,856c165de82fbd0489df9ec6ffaa0958c620e073@198.244.179.127:26656,5a98d637a16b16bf425a4a785c9d11a7d1e5b8a0@65.21.131.215:26736,efe721a953196d8c5f2375b86dcd54285aec565c@51.158.231.48:26656,8ac41af54dfd91c41de71cde222a55670f2f405d@141.95.65.73:15956,2f93424bd346b857bd5164eaac0b2bfd5fd644c0@144.91.127.252:26656,a25a3a218a699e71e2a64edaa45f457dfd8507ba@65.21.148.206:26656,3594b73f909a9c4b87cfe6a361ef8b2b51124dd5@65.109.69.59:15956,526d8c7c44f59be9a39d7463c576b68c0db23174@65.108.234.23:15956,d856120f262134ebf13e1d2632d778b69e704208@65.108.4.188:15956,3bd3a20d7c8a26a20927289a7a6bffecf71de53e@51.81.155.97:10856,fec9760fec02405039ee0e90f80322b893e4ccef@65.144.145.234:26656,24b28cf013e6d7b5b88b6dba2701c5ddd2dd5ee1@65.109.58.225:28656,ec4126b26336cd61b335345df4ff2a3fbb79338a@65.109.92.240:20026,a8abf12f9b69a7d80999efe0aaafe5fcb28294d4@52.35.72.210:26656,34b87bdfc1f0b6a11724cf45dda3ee66c9a4691c@38.146.3.176:15956,d43c09d1734e2135102621305aa3d15117b5d1b6@13.209.213.117:26656,f97a75fb69d3a5fe893dca7c8d238ccc0bd66a8f@188.165.221.155:6969"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.teritorid/config/config.toml
```
