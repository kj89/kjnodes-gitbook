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

**live-peers** (28)
```bash
peers="4cef2b81f82420434c6ce0dc43ca04ad18ef773f@65.108.75.107:15656,8e9624292123624e4eddc3f43189f08a0424127e@65.108.131.62:26656,6085c32b26fb1baa4b16b426f5d56f2fff81cfc7@135.181.165.246:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@134.65.192.81:26656,fefd8ffb33a5d6ae194f082a39c4bb713da3a06b@167.86.86.197:36656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:19656,fffcd8c41a92e24d67b6d026f556c5afd49db092@45.77.41.21:26656,920f32f409bbb18b641cdc9513545e2e016c2c62@142.132.203.60:26656,26175f13ada3d61c93bca342819fd5dc797bced0@65.109.58.226:28656,856c165de82fbd0489df9ec6ffaa0958c620e073@198.244.179.127:26656,a25a3a218a699e71e2a64edaa45f457dfd8507ba@65.21.148.206:26656,5a98d637a16b16bf425a4a785c9d11a7d1e5b8a0@65.21.131.215:26736,d856120f262134ebf13e1d2632d778b69e704208@65.108.4.188:15956,82ebb17ddac20928fb8107201dad9f5aea7f9132@198.244.200.3:26656,46b7ae20e3cc4264076a91c3601f3894a021a80d@65.108.6.45:36656,8ac41af54dfd91c41de71cde222a55670f2f405d@141.95.65.73:15956,0b27217386756577e1eadf00c4169dc8f041e522@51.210.7.219:26656,7d47faa64cef3eca57ed3f4eaf21f7a3981d512b@57.128.65.115:28656,b336b83d9bab0b8cf96a3833efcbc196fab63fdd@212.95.51.215:36656,51eaf493facf36754411baa4f7b89355bd9cb3e7@195.201.63.87:42666,b78dd48a9d34146f04801f479a82348a19a69ab7@51.159.185.141:26656,526d8c7c44f59be9a39d7463c576b68c0db23174@65.108.234.23:15956,942c99cb9ff717552f884639dda9f52ab66f9726@65.108.134.12:26656,ed747c9e39fc04fdbc7ab5fc4a4a7f7a298ee329@65.144.145.234:26656,4991cc04c48f96dec265464d5cf276e16f6b302c@188.217.162.92:26656,4740ad44e58f4f4a0e2b9c4353500009eb73a05a@176.191.97.120:26656,d956d6180e96c62315a777b1a3ed8f1ebf873e80@38.242.232.202:29656,8f75bd347c90fbaa2c96eb187a413bb3751b3a7e@51.81.208.70:15956"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.teritorid/config/config.toml
```
