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

**live-peers** (28)
```
peers="5a98d637a16b16bf425a4a785c9d11a7d1e5b8a0@65.21.131.215:26736,b336b83d9bab0b8cf96a3833efcbc196fab63fdd@212.95.51.215:36656,e3b906fefa58783395fcf72086c698707908a558@141.95.65.26:27736,29b92a4020171c20fe70e5d60f9c5d07dc9f31f7@194.163.161.146:26656,20e1000e88125698264454a884812746c2eb4807@65.108.227.217:15956,0b27217386756577e1eadf00c4169dc8f041e522@51.210.7.219:26656,51eaf493facf36754411baa4f7b89355bd9cb3e7@195.201.63.87:42666,d2247f7b919f0781c90ee61958d7044665a22d38@169.155.44.201:26656,a7d96dc929824613315dcc1c90fee119f28cc51f@164.152.161.254:26656,526d8c7c44f59be9a39d7463c576b68c0db23174@65.108.234.23:15956,82ebb17ddac20928fb8107201dad9f5aea7f9132@198.244.200.3:26656,3594b73f909a9c4b87cfe6a361ef8b2b51124dd5@65.109.69.59:15956,89757803f40da51678451735445ad40d5b15e059@134.65.192.221:26656,d29bed885306037dbe219278415025a2ea8880a4@51.159.160.140:26656,88a407d4749e1ccbb630f98ca44f304744d97864@38.242.141.168:26656,370bf5f5b9ce655403d05753c355798288c1f120@89.245.24.66:23356,7fb5a1a53f481f037487920ed08b0495158e2041@148.251.53.202:26796,b212d5740b2e11e54f56b072dc13b6134650cfb5@134.65.192.81:26656,6ef7a8bc7a3cc0856594f12570e8f2282a099dcf@65.109.93.152:26796,c124ce0b508e8b9ed1c5b6957f362225659b5343@169.155.168.57:26656,40caa979c29a9930ea2b8a6249037924d308ae84@162.55.234.70:54256,d956d6180e96c62315a777b1a3ed8f1ebf873e80@38.242.232.202:29656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:19656,46b7ae20e3cc4264076a91c3601f3894a021a80d@65.108.6.45:36656,14fa46dbadd79647ebf3e5bc82326d2debc5fd52@51.159.176.185:26656,ad347ea1ec920d12ccda2341348bcc89687739ef@88.99.164.158:38026,4740ad44e58f4f4a0e2b9c4353500009eb73a05a@176.191.97.120:26656,26175f13ada3d61c93bca342819fd5dc797bced0@65.109.58.226:28656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.teritorid/config/config.toml
```
