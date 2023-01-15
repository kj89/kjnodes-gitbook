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
* grpc: https://teritori.grpc.kjnodes.com:443

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

**live-peers** (32)
```bash
peers="1d8e2fe7e235c8ca8a8054b3ded24c99702ea739@135.181.17.176:26656,26175f13ada3d61c93bca342819fd5dc797bced0@65.109.58.226:28656,009e25e99e3f8fde86d283d4b8b0ce2f777cde53@138.201.8.248:53656,88a407d4749e1ccbb630f98ca44f304744d97864@38.242.141.168:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:19656,60d992aae7c708c097d41829bb3968bce16379e2@51.81.107.95:10756,2bb0801eb49b4ca346f4ee7755003b1663476dbd@95.216.220.113:26656,920f32f409bbb18b641cdc9513545e2e016c2c62@142.132.203.60:26656,856c165de82fbd0489df9ec6ffaa0958c620e073@198.244.179.127:26656,5a98d637a16b16bf425a4a785c9d11a7d1e5b8a0@65.21.131.215:26736,4b04b3d164dc6dd5bb555a7a106a8d314f30516f@65.21.136.170:53656,0b27217386756577e1eadf00c4169dc8f041e522@51.210.7.219:26656,46b7ae20e3cc4264076a91c3601f3894a021a80d@65.108.6.45:36656,a25a3a218a699e71e2a64edaa45f457dfd8507ba@65.21.148.206:26656,106490318e51355bc6d72e7941a0080f8b8256b9@185.16.39.14:26656,6085c32b26fb1baa4b16b426f5d56f2fff81cfc7@135.181.165.246:26656,3950af34da35ce3ff8c50ff3c47a43f5dfc93947@195.3.220.154:19656,8ac41af54dfd91c41de71cde222a55670f2f405d@141.95.65.73:15956,d856120f262134ebf13e1d2632d778b69e704208@65.108.4.188:15956,14fa46dbadd79647ebf3e5bc82326d2debc5fd52@51.159.176.185:26656,3bd3a20d7c8a26a20927289a7a6bffecf71de53e@51.81.155.97:10856,370bf5f5b9ce655403d05753c355798288c1f120@89.245.24.78:23356,44b2bf9d970aece0531d3d939c5c546a7ac9201a@34.219.76.190:26656,787a6b318ebc4167fefb1d5ef9f88af6cb5a8b29@173.212.222.167:35656,51eaf493facf36754411baa4f7b89355bd9cb3e7@195.201.63.87:42666,3594b73f909a9c4b87cfe6a361ef8b2b51124dd5@65.109.69.59:15956,ec4126b26336cd61b335345df4ff2a3fbb79338a@65.109.92.240:20026,94b63fddfc78230f51aeb7ac34b9fb86bd042a77@212.23.222.126:30552,942c99cb9ff717552f884639dda9f52ab66f9726@65.108.134.12:26656,526d8c7c44f59be9a39d7463c576b68c0db23174@65.108.234.23:15956,48980875839186e08e12ebf0d9a2803b45206833@65.109.92.241:38026,4740ad44e58f4f4a0e2b9c4353500009eb73a05a@176.191.97.120:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.teritorid/config/config.toml
```
