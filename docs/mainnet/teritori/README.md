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

**live-peers** (25)
```
peers="5a98d637a16b16bf425a4a785c9d11a7d1e5b8a0@65.21.131.215:26736,ec4126b26336cd61b335345df4ff2a3fbb79338a@65.109.92.240:20026,b212d5740b2e11e54f56b072dc13b6134650cfb5@134.65.192.81:26656,89757803f40da51678451735445ad40d5b15e059@134.65.192.221:26656,26d6ee4138c7533c5541722c6e1ecc6d60d47a86@104.193.254.42:26656,e627e9bbff303c96e859de00e5deaaf5104911cd@51.15.228.89:26656,26175f13ada3d61c93bca342819fd5dc797bced0@65.109.58.226:28656,942c99cb9ff717552f884639dda9f52ab66f9726@65.108.134.12:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:19656,d956d6180e96c62315a777b1a3ed8f1ebf873e80@38.242.232.202:29656,0b27217386756577e1eadf00c4169dc8f041e522@51.210.7.219:26656,a8f99d0bf134cf0e5127c851059f60901a27d06d@95.216.220.113:26656,94b63fddfc78230f51aeb7ac34b9fb86bd042a77@212.23.222.126:30552,406fc7fe86ba396cb7fc8616c546f21a1d3c51cd@89.58.57.158:26656,a7d96dc929824613315dcc1c90fee119f28cc51f@164.152.161.254:26656,8ac41af54dfd91c41de71cde222a55670f2f405d@141.95.65.73:15956,526d8c7c44f59be9a39d7463c576b68c0db23174@65.108.234.23:15956,d856120f262134ebf13e1d2632d778b69e704208@65.108.4.188:15956,e3374c3d25a36f06662fa150043e5e6529d11570@88.198.32.17:31656,1f9293a286df733dac6303aad3c39240ad3b3796@178.211.139.24:46656,3594b73f909a9c4b87cfe6a361ef8b2b51124dd5@65.109.69.59:15956,a35dc0cd0efd7e04d3334d781112bae0698a8f57@164.92.131.1:26656,46b7ae20e3cc4264076a91c3601f3894a021a80d@65.108.6.45:36656,29b92a4020171c20fe70e5d60f9c5d07dc9f31f7@194.163.161.146:26656,ad347ea1ec920d12ccda2341348bcc89687739ef@88.99.164.158:38026"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.teritorid/config/config.toml
```
