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

**live-peers** (27)
```bash
peers="526d8c7c44f59be9a39d7463c576b68c0db23174@65.108.234.23:15956,009e25e99e3f8fde86d283d4b8b0ce2f777cde53@138.201.8.248:53656,88a407d4749e1ccbb630f98ca44f304744d97864@38.242.141.168:26656,3bd3a20d7c8a26a20927289a7a6bffecf71de53e@51.81.155.97:10856,920f32f409bbb18b641cdc9513545e2e016c2c62@142.132.203.60:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:19656,0b27217386756577e1eadf00c4169dc8f041e522@51.210.7.219:26656,8ac41af54dfd91c41de71cde222a55670f2f405d@141.95.65.73:15956,d856120f262134ebf13e1d2632d778b69e704208@65.108.4.188:15956,48980875839186e08e12ebf0d9a2803b45206833@65.109.92.241:38026,fec9760fec02405039ee0e90f80322b893e4ccef@65.144.145.234:26656,856c165de82fbd0489df9ec6ffaa0958c620e073@198.244.179.127:26656,5a98d637a16b16bf425a4a785c9d11a7d1e5b8a0@65.21.131.215:26736,ce3baba928ae06cd3ff0af20aec888a82ddffef7@54.37.129.171:26656,26175f13ada3d61c93bca342819fd5dc797bced0@65.109.58.226:28656,ec4126b26336cd61b335345df4ff2a3fbb79338a@65.109.92.240:20026,d43c09d1734e2135102621305aa3d15117b5d1b6@13.209.213.117:26656,a25a3a218a699e71e2a64edaa45f457dfd8507ba@65.21.148.206:26656,6ef7a8bc7a3cc0856594f12570e8f2282a099dcf@65.109.93.152:26796,46b7ae20e3cc4264076a91c3601f3894a021a80d@65.108.6.45:36656,3594b73f909a9c4b87cfe6a361ef8b2b51124dd5@65.109.69.59:15956,51eaf493facf36754411baa4f7b89355bd9cb3e7@195.201.63.87:42666,2f93424bd346b857bd5164eaac0b2bfd5fd644c0@144.91.127.252:26656,9c5393bb5611f8c3aaa0abde1ce753284c1428d0@141.95.34.175:27656,34b87bdfc1f0b6a11724cf45dda3ee66c9a4691c@38.146.3.176:15956,a7d96dc929824613315dcc1c90fee119f28cc51f@164.152.161.254:26656,d956d6180e96c62315a777b1a3ed8f1ebf873e80@38.242.232.202:29656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.teritorid/config/config.toml
```
