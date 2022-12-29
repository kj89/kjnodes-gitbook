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

**live-peers** (24)
```
peers="6bc9f80a5123d62c23aadb7b5d68b740a794b0c6@65.109.49.111:36656,ad347ea1ec920d12ccda2341348bcc89687739ef@88.99.164.158:38026,24b28cf013e6d7b5b88b6dba2701c5ddd2dd5ee1@65.109.58.225:28656,2afdb9300c47e43e555fa572d033b2d68ac28506@65.109.70.68:26686,26d6ee4138c7533c5541722c6e1ecc6d60d47a86@104.193.254.42:26656,009e25e99e3f8fde86d283d4b8b0ce2f777cde53@138.201.8.248:53656,40caa979c29a9930ea2b8a6249037924d308ae84@162.55.234.70:54256,5a98d637a16b16bf425a4a785c9d11a7d1e5b8a0@65.21.131.215:26736,406fc7fe86ba396cb7fc8616c546f21a1d3c51cd@89.58.57.158:26656,d29bed885306037dbe219278415025a2ea8880a4@51.159.160.140:26656,703714c82c94fc1c74b6ee0d1fc3417b932be5f3@169.155.168.57:26656,0b27217386756577e1eadf00c4169dc8f041e522@51.210.7.219:26656,d956d6180e96c62315a777b1a3ed8f1ebf873e80@38.242.232.202:29656,8ac41af54dfd91c41de71cde222a55670f2f405d@141.95.65.73:15956,4740ad44e58f4f4a0e2b9c4353500009eb73a05a@176.191.97.120:26656,a7d96dc929824613315dcc1c90fee119f28cc51f@164.152.161.254:26656,b336b83d9bab0b8cf96a3833efcbc196fab63fdd@212.95.51.215:36656,ec4126b26336cd61b335345df4ff2a3fbb79338a@65.109.92.240:20026,3594b73f909a9c4b87cfe6a361ef8b2b51124dd5@65.109.69.59:15956,e8cafb5a121c9fe322e554f5a7f489b2d25abd4c@51.159.153.113:26656,29b92a4020171c20fe70e5d60f9c5d07dc9f31f7@194.163.161.146:26656,ed747c9e39fc04fdbc7ab5fc4a4a7f7a298ee329@65.144.145.234:26656,46b7ae20e3cc4264076a91c3601f3894a021a80d@65.108.6.45:36656,26175f13ada3d61c93bca342819fd5dc797bced0@65.109.58.226:28656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.teritorid/config/config.toml
```
