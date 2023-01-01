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
peers="6046cec27c36f0a7596cb9fa9f2c5decbd4e87cb@151.115.53.172:26656,d2247f7b919f0781c90ee61958d7044665a22d38@169.155.44.201:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:19656,6ef7a8bc7a3cc0856594f12570e8f2282a099dcf@65.109.93.152:26796,703714c82c94fc1c74b6ee0d1fc3417b932be5f3@169.155.168.57:26656,24b28cf013e6d7b5b88b6dba2701c5ddd2dd5ee1@65.109.58.225:28656,5a98d637a16b16bf425a4a785c9d11a7d1e5b8a0@65.21.131.215:26736,808437b010f4663bf007b33433262d1495b0fbfe@35.90.134.158:28656,0b27217386756577e1eadf00c4169dc8f041e522@51.210.7.219:26656,a25a3a218a699e71e2a64edaa45f457dfd8507ba@65.21.148.206:26656,571084dbc97e895d11f748fccdcd1a098d8f169a@15.235.115.156:10002,88a407d4749e1ccbb630f98ca44f304744d97864@38.242.141.168:26656,a7d96dc929824613315dcc1c90fee119f28cc51f@164.152.161.254:26656,8ac41af54dfd91c41de71cde222a55670f2f405d@141.95.65.73:15956,89757803f40da51678451735445ad40d5b15e059@134.65.192.221:26656,00bcdf330421f3834c6dd279342d0c935b2f353f@95.217.117.99:26656,526d8c7c44f59be9a39d7463c576b68c0db23174@65.108.234.23:15956,b212d5740b2e11e54f56b072dc13b6134650cfb5@134.65.192.81:26656,787a6b318ebc4167fefb1d5ef9f88af6cb5a8b29@173.212.222.167:35656,ad347ea1ec920d12ccda2341348bcc89687739ef@88.99.164.158:38026,34b87bdfc1f0b6a11724cf45dda3ee66c9a4691c@38.146.3.176:15956,d956d6180e96c62315a777b1a3ed8f1ebf873e80@38.242.232.202:29656,317d9a102d4a04337c65571c18df0e98269dce87@141.94.193.12:13656,fefd8ffb33a5d6ae194f082a39c4bb713da3a06b@167.86.86.197:36656,29b92a4020171c20fe70e5d60f9c5d07dc9f31f7@194.163.161.146:26656,51eaf493facf36754411baa4f7b89355bd9cb3e7@195.201.63.87:42666,4740ad44e58f4f4a0e2b9c4353500009eb73a05a@176.191.97.120:26656,46b7ae20e3cc4264076a91c3601f3894a021a80d@65.108.6.45:36656,26175f13ada3d61c93bca342819fd5dc797bced0@65.109.58.226:28656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.teritorid/config/config.toml
```
