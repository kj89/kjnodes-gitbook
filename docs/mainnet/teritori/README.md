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

**live-peers** (36)
```bash
peers="6060a7c4f09dd7315f2c59b0c516f71e6e719a76@51.89.7.234:26642,703714c82c94fc1c74b6ee0d1fc3417b932be5f3@169.155.168.57:26656,88a407d4749e1ccbb630f98ca44f304744d97864@38.242.141.168:26656,920f32f409bbb18b641cdc9513545e2e016c2c62@142.132.203.60:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:19656,46b7ae20e3cc4264076a91c3601f3894a021a80d@65.108.6.45:36656,26175f13ada3d61c93bca342819fd5dc797bced0@65.109.58.226:28656,8ac41af54dfd91c41de71cde222a55670f2f405d@141.95.65.73:15956,5a98d637a16b16bf425a4a785c9d11a7d1e5b8a0@65.21.131.215:26736,4740ad44e58f4f4a0e2b9c4353500009eb73a05a@176.191.97.120:26656,a7d96dc929824613315dcc1c90fee119f28cc51f@164.152.161.254:26656,60d992aae7c708c097d41829bb3968bce16379e2@51.81.107.95:10756,a25a3a218a699e71e2a64edaa45f457dfd8507ba@65.21.148.206:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@134.65.192.81:26656,0b27217386756577e1eadf00c4169dc8f041e522@51.210.7.219:26656,106490318e51355bc6d72e7941a0080f8b8256b9@185.16.39.14:26656,94b63fddfc78230f51aeb7ac34b9fb86bd042a77@212.23.222.126:30552,fffcd8c41a92e24d67b6d026f556c5afd49db092@45.77.41.21:26656,856c165de82fbd0489df9ec6ffaa0958c620e073@198.244.179.127:26656,526d8c7c44f59be9a39d7463c576b68c0db23174@65.108.234.23:15956,406fc7fe86ba396cb7fc8616c546f21a1d3c51cd@89.58.57.158:26656,89757803f40da51678451735445ad40d5b15e059@134.65.192.221:26656,7d47faa64cef3eca57ed3f4eaf21f7a3981d512b@57.128.65.115:28656,6085c32b26fb1baa4b16b426f5d56f2fff81cfc7@135.181.165.246:26656,1f858b8cc8e18ef05de79dd470ad29ba29ddbeb7@65.108.77.106:26889,bc8734c4c81fc1d0543b311914963be3954255bf@222.252.2.167:26656,1e08fefb7e8851490d40e804df76d1ac33cb1f0a@38.146.3.175:15956,82ebb17ddac20928fb8107201dad9f5aea7f9132@198.244.200.3:26656,4991cc04c48f96dec265464d5cf276e16f6b302c@188.217.162.92:26656,d956d6180e96c62315a777b1a3ed8f1ebf873e80@38.242.232.202:29656,942c99cb9ff717552f884639dda9f52ab66f9726@65.108.134.12:26656,3594b73f909a9c4b87cfe6a361ef8b2b51124dd5@65.109.69.59:15956,35cdec21668ac214c74a6e45d444f6933f094bc4@144.202.72.17:26646,d856120f262134ebf13e1d2632d778b69e704208@65.108.4.188:15956,8f4db549de62fbb96cf4cf477e2af9c52f74a3dd@51.91.64.170:19656,ad347ea1ec920d12ccda2341348bcc89687739ef@88.99.164.158:38026"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.teritorid/config/config.toml
```
