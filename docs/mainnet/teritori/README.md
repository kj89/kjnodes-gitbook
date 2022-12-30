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

**live-peers** (21)
```
peers="1d8e2fe7e235c8ca8a8054b3ded24c99702ea739@135.181.17.176:26656,24b28cf013e6d7b5b88b6dba2701c5ddd2dd5ee1@65.109.58.225:28656,b336b83d9bab0b8cf96a3833efcbc196fab63fdd@212.95.51.215:36656,0b27217386756577e1eadf00c4169dc8f041e522@51.210.7.219:26656,2b4f46e601fb4ede2a0c98976337e3afdaa50dac@65.108.238.102:15956,a7d96dc929824613315dcc1c90fee119f28cc51f@164.152.161.254:26656,5a98d637a16b16bf425a4a785c9d11a7d1e5b8a0@65.21.131.215:26736,3594b73f909a9c4b87cfe6a361ef8b2b51124dd5@65.109.69.59:15956,6ef7a8bc7a3cc0856594f12570e8f2282a099dcf@65.109.93.152:26796,bbc594f0a8424368b869fef47a18d6e35965db2e@176.9.188.21:53656,26175f13ada3d61c93bca342819fd5dc797bced0@65.109.58.226:28656,370bf5f5b9ce655403d05753c355798288c1f120@89.245.24.80:23356,4cef2b81f82420434c6ce0dc43ca04ad18ef773f@65.108.75.107:15656,46b7ae20e3cc4264076a91c3601f3894a021a80d@65.108.6.45:36656,8ac41af54dfd91c41de71cde222a55670f2f405d@141.95.65.73:15956,6fd88e2143e6d4ba02a7f745565120df18e84699@109.236.80.46:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:19656,51eaf493facf36754411baa4f7b89355bd9cb3e7@195.201.63.87:42666,29b92a4020171c20fe70e5d60f9c5d07dc9f31f7@194.163.161.146:26656,ad347ea1ec920d12ccda2341348bcc89687739ef@88.99.164.158:38026,d956d6180e96c62315a777b1a3ed8f1ebf873e80@38.242.232.202:29656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.teritorid/config/config.toml
```
