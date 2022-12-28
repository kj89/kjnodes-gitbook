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
peers="0b27217386756577e1eadf00c4169dc8f041e522@51.210.7.219:26656,88a407d4749e1ccbb630f98ca44f304744d97864@38.242.141.168:26656,40caa979c29a9930ea2b8a6249037924d308ae84@162.55.234.70:54256,bbc594f0a8424368b869fef47a18d6e35965db2e@176.9.188.21:53656,82ebb17ddac20928fb8107201dad9f5aea7f9132@198.244.200.3:26656,722b63e6c65628b929f22013dcbcde980210cb44@176.9.127.54:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:19656,d956d6180e96c62315a777b1a3ed8f1ebf873e80@38.242.232.202:29656,5a98d637a16b16bf425a4a785c9d11a7d1e5b8a0@65.21.131.215:26736,3594b73f909a9c4b87cfe6a361ef8b2b51124dd5@65.109.69.59:15956,b336b83d9bab0b8cf96a3833efcbc196fab63fdd@212.95.51.215:36656,a191006e50d3af40fd253c23dae715a45fdd7415@95.179.217.1:26656,5ab6437f73fe71f392d53566e037aa91087530ac@139.144.67.202:26656,ebacd77faa91ee858496a79250adff93480ce64b@158.69.188.117:26656,a7d96dc929824613315dcc1c90fee119f28cc51f@164.152.161.254:26656,cdda30f407133027bf1322305e62ad968fad5348@96.69.133.222:26656,46b7ae20e3cc4264076a91c3601f3894a021a80d@65.108.6.45:36656,4b04b3d164dc6dd5bb555a7a106a8d314f30516f@65.21.136.170:53656,b212d5740b2e11e54f56b072dc13b6134650cfb5@134.65.192.81:26656,26175f13ada3d61c93bca342819fd5dc797bced0@65.109.58.226:28656,4740ad44e58f4f4a0e2b9c4353500009eb73a05a@176.191.97.120:26656,ad347ea1ec920d12ccda2341348bcc89687739ef@88.99.164.158:38026,29b92a4020171c20fe70e5d60f9c5d07dc9f31f7@194.163.161.146:26656,ade4d8bc8cbe014af6ebdf3cb7b1e9ad36f412c0@135.181.5.219:15956"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.teritorid/config/config.toml
```
