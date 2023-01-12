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
peers="d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:19656,722b63e6c65628b929f22013dcbcde980210cb44@176.9.127.54:26656,bbc594f0a8424368b869fef47a18d6e35965db2e@176.9.188.21:53656,82ebb17ddac20928fb8107201dad9f5aea7f9132@198.244.200.3:26656,51eaf493facf36754411baa4f7b89355bd9cb3e7@195.201.63.87:42666,43da931d00da102c002e0a227de7258b8fb1871a@144.126.135.53:26656,3950af34da35ce3ff8c50ff3c47a43f5dfc93947@195.3.220.154:19656,920f32f409bbb18b641cdc9513545e2e016c2c62@142.132.203.60:26656,3594b73f909a9c4b87cfe6a361ef8b2b51124dd5@65.109.69.59:15956,856c165de82fbd0489df9ec6ffaa0958c620e073@198.244.179.127:26656,5a98d637a16b16bf425a4a785c9d11a7d1e5b8a0@65.21.131.215:26736,26175f13ada3d61c93bca342819fd5dc797bced0@65.109.58.226:28656,8ac41af54dfd91c41de71cde222a55670f2f405d@141.95.65.73:15956,46b7ae20e3cc4264076a91c3601f3894a021a80d@65.108.6.45:36656,0b27217386756577e1eadf00c4169dc8f041e522@51.210.7.219:26656,a25a3a218a699e71e2a64edaa45f457dfd8507ba@65.21.148.206:26656,d856120f262134ebf13e1d2632d778b69e704208@65.108.4.188:15956,942c99cb9ff717552f884639dda9f52ab66f9726@65.108.134.12:26656,5ab6437f73fe71f392d53566e037aa91087530ac@139.144.67.202:26656,ed747c9e39fc04fdbc7ab5fc4a4a7f7a298ee329@65.144.145.234:26656,4b04b3d164dc6dd5bb555a7a106a8d314f30516f@65.21.136.170:53656,89757803f40da51678451735445ad40d5b15e059@134.65.192.221:26656,ef54691ee6f731e49d58e7ee91cf42927f2d7947@144.126.136.227:26656,1e08fefb7e8851490d40e804df76d1ac33cb1f0a@38.146.3.175:15956,526d8c7c44f59be9a39d7463c576b68c0db23174@65.108.234.23:15956,406fc7fe86ba396cb7fc8616c546f21a1d3c51cd@89.58.57.158:26656,fffcd8c41a92e24d67b6d026f556c5afd49db092@45.77.41.21:26656,4bdef61228fe87e1257bfa5b19da146d4c333c7a@212.47.240.174:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.teritorid/config/config.toml
```
