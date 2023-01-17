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

**live-peers** (32)
```bash
peers="e627e9bbff303c96e859de00e5deaaf5104911cd@51.15.228.89:26656,14fa46dbadd79647ebf3e5bc82326d2debc5fd52@51.159.176.185:26656,e3b906fefa58783395fcf72086c698707908a558@141.95.65.26:27736,4d6c820a7d426ad934a5e51f2e020836f0378919@116.202.143.91:26656,88a407d4749e1ccbb630f98ca44f304744d97864@38.242.141.168:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:19656,920f32f409bbb18b641cdc9513545e2e016c2c62@142.132.203.60:26656,46b7ae20e3cc4264076a91c3601f3894a021a80d@65.108.6.45:36656,a25a3a218a699e71e2a64edaa45f457dfd8507ba@65.21.148.206:26656,ec4126b26336cd61b335345df4ff2a3fbb79338a@65.109.92.240:20026,48980875839186e08e12ebf0d9a2803b45206833@65.109.92.241:38026,26175f13ada3d61c93bca342819fd5dc797bced0@65.109.58.226:28656,ce3baba928ae06cd3ff0af20aec888a82ddffef7@54.37.129.171:26656,d856120f262134ebf13e1d2632d778b69e704208@65.108.4.188:15956,856c165de82fbd0489df9ec6ffaa0958c620e073@198.244.179.127:26656,16f90d350de14a596ebdc683ce5e703c14e40bb3@75.119.146.181:19656,0b27217386756577e1eadf00c4169dc8f041e522@51.210.7.219:26656,8ac41af54dfd91c41de71cde222a55670f2f405d@141.95.65.73:15956,4991cc04c48f96dec265464d5cf276e16f6b302c@31.156.233.3:26656,1d8e2fe7e235c8ca8a8054b3ded24c99702ea739@135.181.17.176:26656,3594b73f909a9c4b87cfe6a361ef8b2b51124dd5@65.109.69.59:15956,5a98d637a16b16bf425a4a785c9d11a7d1e5b8a0@65.21.131.215:26736,82ebb17ddac20928fb8107201dad9f5aea7f9132@198.244.200.3:26656,593b8319d1d4b1958e7daba8c3bbb56795cb59ba@146.59.81.92:51656,571084dbc97e895d11f748fccdcd1a098d8f169a@15.235.115.156:10002,b212d5740b2e11e54f56b072dc13b6134650cfb5@134.65.192.81:26656,526d8c7c44f59be9a39d7463c576b68c0db23174@65.108.234.23:15956,a35dc0cd0efd7e04d3334d781112bae0698a8f57@164.92.131.1:26656,b336b83d9bab0b8cf96a3833efcbc196fab63fdd@212.95.51.215:36656,1f858b8cc8e18ef05de79dd470ad29ba29ddbeb7@65.108.77.106:26889,6ef7a8bc7a3cc0856594f12570e8f2282a099dcf@65.109.93.152:26796,8f75bd347c90fbaa2c96eb187a413bb3751b3a7e@51.81.208.70:15956"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.teritorid/config/config.toml
```
