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

**live-peers** (29)
```bash
peers="634a29ae2bd7ad8165d6ef66a6dea02d04c9bbed@65.108.77.250:26641,d43c09d1734e2135102621305aa3d15117b5d1b6@13.209.213.117:26656,8ac41af54dfd91c41de71cde222a55670f2f405d@141.95.65.73:15956,722b63e6c65628b929f22013dcbcde980210cb44@176.9.127.54:26656,efe721a953196d8c5f2375b86dcd54285aec565c@51.158.231.48:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:19656,920f32f409bbb18b641cdc9513545e2e016c2c62@142.132.203.60:26656,ec4126b26336cd61b335345df4ff2a3fbb79338a@65.109.92.240:20026,48980875839186e08e12ebf0d9a2803b45206833@65.109.92.241:38026,0b27217386756577e1eadf00c4169dc8f041e522@51.210.7.219:26656,856c165de82fbd0489df9ec6ffaa0958c620e073@198.244.179.127:26656,106490318e51355bc6d72e7941a0080f8b8256b9@185.16.39.14:26656,d856120f262134ebf13e1d2632d778b69e704208@65.108.4.188:15956,46b7ae20e3cc4264076a91c3601f3894a021a80d@65.108.6.45:36656,5a98d637a16b16bf425a4a785c9d11a7d1e5b8a0@65.21.131.215:26736,a25a3a218a699e71e2a64edaa45f457dfd8507ba@65.21.148.206:26656,9c5393bb5611f8c3aaa0abde1ce753284c1428d0@141.95.34.175:27656,ce3baba928ae06cd3ff0af20aec888a82ddffef7@54.37.129.171:26656,26175f13ada3d61c93bca342819fd5dc797bced0@65.109.58.226:28656,3178ac8fffd269325500c95679d58d5e8ec61746@198.244.213.94:22956,3594b73f909a9c4b87cfe6a361ef8b2b51124dd5@65.109.69.59:15956,526d8c7c44f59be9a39d7463c576b68c0db23174@65.108.234.23:15956,6ef7a8bc7a3cc0856594f12570e8f2282a099dcf@65.109.93.152:26796,4740ad44e58f4f4a0e2b9c4353500009eb73a05a@176.191.97.120:26656,a191006e50d3af40fd253c23dae715a45fdd7415@95.179.217.1:26656,1e08fefb7e8851490d40e804df76d1ac33cb1f0a@38.146.3.175:15956,ed747c9e39fc04fdbc7ab5fc4a4a7f7a298ee329@65.144.145.234:26656,d956d6180e96c62315a777b1a3ed8f1ebf873e80@38.242.232.202:29656,51eaf493facf36754411baa4f7b89355bd9cb3e7@195.201.63.87:42666"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.teritorid/config/config.toml
```
