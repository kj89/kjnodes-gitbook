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

**live-peers** (28)
```bash
peers="26175f13ada3d61c93bca342819fd5dc797bced0@65.109.58.226:28656,b212d5740b2e11e54f56b072dc13b6134650cfb5@134.65.192.81:26656,722b63e6c65628b929f22013dcbcde980210cb44@176.9.127.54:26656,16f90d350de14a596ebdc683ce5e703c14e40bb3@75.119.146.181:19656,406fc7fe86ba396cb7fc8616c546f21a1d3c51cd@89.58.57.158:26656,ec4126b26336cd61b335345df4ff2a3fbb79338a@65.109.92.240:20026,920f32f409bbb18b641cdc9513545e2e016c2c62@142.132.203.60:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:19656,fec9760fec02405039ee0e90f80322b893e4ccef@65.144.145.234:26656,8ac41af54dfd91c41de71cde222a55670f2f405d@141.95.65.73:15956,2f93424bd346b857bd5164eaac0b2bfd5fd644c0@144.91.127.252:26656,48980875839186e08e12ebf0d9a2803b45206833@65.109.92.241:38026,5a98d637a16b16bf425a4a785c9d11a7d1e5b8a0@65.21.131.215:26736,ce3baba928ae06cd3ff0af20aec888a82ddffef7@54.37.129.171:26656,46b7ae20e3cc4264076a91c3601f3894a021a80d@65.108.6.45:36656,d856120f262134ebf13e1d2632d778b69e704208@65.108.4.188:15956,856c165de82fbd0489df9ec6ffaa0958c620e073@198.244.179.127:26656,a25a3a218a699e71e2a64edaa45f457dfd8507ba@65.21.148.206:26656,f813a00f52de54a49aea3211b89a65ae6133eac2@88.99.167.148:26686,4b04b3d164dc6dd5bb555a7a106a8d314f30516f@65.21.136.170:53656,7cd5a57fb2194297952f62b2632c04d8e1222485@65.108.226.58:26656,0b27217386756577e1eadf00c4169dc8f041e522@51.210.7.219:26656,526d8c7c44f59be9a39d7463c576b68c0db23174@65.108.234.23:15956,28456ac1dded17760432c3f1d759c7d50ab6ed3e@51.250.83.54:26656,bca4b3fe8dec2f48a00e7e8eb09c662a2d37274c@65.109.37.58:10656,d956d6180e96c62315a777b1a3ed8f1ebf873e80@38.242.232.202:29656,b336b83d9bab0b8cf96a3833efcbc196fab63fdd@212.95.51.215:36656,ade4d8bc8cbe014af6ebdf3cb7b1e9ad36f412c0@135.181.5.219:15956"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.teritorid/config/config.toml
```
