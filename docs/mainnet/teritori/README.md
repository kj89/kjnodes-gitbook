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

**live-peers** (34)
```bash
peers="1e08fefb7e8851490d40e804df76d1ac33cb1f0a@38.146.3.175:15956,1f858b8cc8e18ef05de79dd470ad29ba29ddbeb7@65.108.77.106:26889,82ebb17ddac20928fb8107201dad9f5aea7f9132@198.244.200.3:26656,3178ac8fffd269325500c95679d58d5e8ec61746@198.244.213.94:22956,920f32f409bbb18b641cdc9513545e2e016c2c62@142.132.203.60:26656,5ab6437f73fe71f392d53566e037aa91087530ac@139.144.67.202:26656,d43c09d1734e2135102621305aa3d15117b5d1b6@13.209.213.117:26656,46b7ae20e3cc4264076a91c3601f3894a021a80d@65.108.6.45:36656,a25a3a218a699e71e2a64edaa45f457dfd8507ba@65.21.148.206:26656,8e1e342208f400bb10677617d4f08b31a3b48877@138.201.61.159:26656,3950af34da35ce3ff8c50ff3c47a43f5dfc93947@195.3.220.154:19656,26175f13ada3d61c93bca342819fd5dc797bced0@65.109.58.226:28656,d856120f262134ebf13e1d2632d778b69e704208@65.108.4.188:15956,856c165de82fbd0489df9ec6ffaa0958c620e073@198.244.179.127:26656,5a98d637a16b16bf425a4a785c9d11a7d1e5b8a0@65.21.131.215:26736,6ef7a8bc7a3cc0856594f12570e8f2282a099dcf@65.109.93.152:26796,76ac8106e8b1169f1ef28f5c45558750db85d3dc@65.108.239.241:26656,0b27217386756577e1eadf00c4169dc8f041e522@51.210.7.219:26656,8ac41af54dfd91c41de71cde222a55670f2f405d@141.95.65.73:15956,526d8c7c44f59be9a39d7463c576b68c0db23174@65.108.234.23:15956,75d41a5ab4f826b7ba468a6c4912dbd8f4541428@65.108.200.142:26646,3594b73f909a9c4b87cfe6a361ef8b2b51124dd5@65.109.69.59:15956,c6f9573f0b5b7f986ec121e584465f2c6cd53de3@51.159.0.207:36656,7d47faa64cef3eca57ed3f4eaf21f7a3981d512b@57.128.65.115:28656,1f4e77295379ce0c928502d2b075157a8c8a9e64@51.83.96.150:26642,fffcd8c41a92e24d67b6d026f556c5afd49db092@45.77.41.21:26656,51345b444fb291c03cf18084bdfc51123de7b5ac@51.178.74.75:36656,d956d6180e96c62315a777b1a3ed8f1ebf873e80@38.242.232.202:29656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:19656,db730d0ca424c7deb2e8529735522b4e317298b5@65.108.108.42:26656,8f28518afd31a42ea81bb3232a50ab0cec4dcdf7@51.158.236.131:26656,942c99cb9ff717552f884639dda9f52ab66f9726@65.108.134.12:26656,51eaf493facf36754411baa4f7b89355bd9cb3e7@195.201.63.87:42666,4740ad44e58f4f4a0e2b9c4353500009eb73a05a@176.191.97.120:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.teritorid/config/config.toml
```
