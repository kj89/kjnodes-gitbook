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

```
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@teritori.rpc.kjnodes.com:19656
```

**seed-node**

```
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@teritori.rpc.kjnodes.com:19659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/teritori/addrbook.json > $HOME/.teritorid/config/addrbook.json
```

**live-peers** (29)
```
peers="ec4126b26336cd61b335345df4ff2a3fbb79338a@65.109.92.240:20026,b212d5740b2e11e54f56b072dc13b6134650cfb5@134.65.192.81:26656,9c5393bb5611f8c3aaa0abde1ce753284c1428d0@141.95.34.175:27656,4d6c820a7d426ad934a5e51f2e020836f0378919@116.202.143.91:26656,317d9a102d4a04337c65571c18df0e98269dce87@141.94.193.12:13656,82ebb17ddac20928fb8107201dad9f5aea7f9132@198.244.200.3:26656,7d47faa64cef3eca57ed3f4eaf21f7a3981d512b@57.128.65.115:28656,8ac41af54dfd91c41de71cde222a55670f2f405d@141.95.65.73:15956,942c99cb9ff717552f884639dda9f52ab66f9726@65.108.134.12:26656,26175f13ada3d61c93bca342819fd5dc797bced0@65.109.58.226:28656,24b28cf013e6d7b5b88b6dba2701c5ddd2dd5ee1@65.109.58.225:28656,5a98d637a16b16bf425a4a785c9d11a7d1e5b8a0@65.21.131.215:26736,0b27217386756577e1eadf00c4169dc8f041e522@51.210.7.219:26656,5ab6437f73fe71f392d53566e037aa91087530ac@139.144.67.202:26656,51eaf493facf36754411baa4f7b89355bd9cb3e7@195.201.63.87:42666,89757803f40da51678451735445ad40d5b15e059@134.65.192.221:26656,3bd3a20d7c8a26a20927289a7a6bffecf71de53e@51.81.155.97:10856,571084dbc97e895d11f748fccdcd1a098d8f169a@15.235.115.156:10002,d856120f262134ebf13e1d2632d778b69e704208@65.108.4.188:15956,d956d6180e96c62315a777b1a3ed8f1ebf873e80@38.242.232.202:29656,526d8c7c44f59be9a39d7463c576b68c0db23174@65.108.234.23:15956,a7d96dc929824613315dcc1c90fee119f28cc51f@164.152.161.254:26656,1e08fefb7e8851490d40e804df76d1ac33cb1f0a@38.146.3.175:15956,46b7ae20e3cc4264076a91c3601f3894a021a80d@65.108.6.45:36656,a25a3a218a699e71e2a64edaa45f457dfd8507ba@65.21.148.206:26656,ad347ea1ec920d12ccda2341348bcc89687739ef@88.99.164.158:38026,94b63fddfc78230f51aeb7ac34b9fb86bd042a77@212.23.222.126:30552,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:19656,f97a75fb69d3a5fe893dca7c8d238ccc0bd66a8f@188.165.221.155:6969"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.teritorid/config/config.toml
```
