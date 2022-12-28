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

**live-peers** (26)
```
peers="cdda30f407133027bf1322305e62ad968fad5348@96.69.133.222:26656,634a29ae2bd7ad8165d6ef66a6dea02d04c9bbed@65.108.77.250:26641,1e08fefb7e8851490d40e804df76d1ac33cb1f0a@38.146.3.175:15956,b212d5740b2e11e54f56b072dc13b6134650cfb5@134.65.192.81:26656,0b27217386756577e1eadf00c4169dc8f041e522@51.210.7.219:26656,ebacd77faa91ee858496a79250adff93480ce64b@158.69.188.117:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:19656,8ac41af54dfd91c41de71cde222a55670f2f405d@141.95.65.73:15956,88a407d4749e1ccbb630f98ca44f304744d97864@38.242.141.168:26656,ff8f8c1b4cf70f38e1c370af05a40c1845022ae8@51.79.103.43:26656,3178ac8fffd269325500c95679d58d5e8ec61746@198.244.213.94:22956,ed747c9e39fc04fdbc7ab5fc4a4a7f7a298ee329@65.144.145.234:26656,4b04b3d164dc6dd5bb555a7a106a8d314f30516f@65.21.136.170:53656,5ab6437f73fe71f392d53566e037aa91087530ac@139.144.67.202:26656,b336b83d9bab0b8cf96a3833efcbc196fab63fdd@212.95.51.215:36656,89757803f40da51678451735445ad40d5b15e059@134.65.192.221:26656,46b7ae20e3cc4264076a91c3601f3894a021a80d@65.108.6.45:36656,3594b73f909a9c4b87cfe6a361ef8b2b51124dd5@65.109.69.59:15956,a8f99d0bf134cf0e5127c851059f60901a27d06d@95.216.220.113:26656,a7d96dc929824613315dcc1c90fee119f28cc51f@164.152.161.254:26656,29b92a4020171c20fe70e5d60f9c5d07dc9f31f7@194.163.161.146:26656,4740ad44e58f4f4a0e2b9c4353500009eb73a05a@176.191.97.120:26656,26175f13ada3d61c93bca342819fd5dc797bced0@65.109.58.226:28656,ad347ea1ec920d12ccda2341348bcc89687739ef@88.99.164.158:38026,5a98d637a16b16bf425a4a785c9d11a7d1e5b8a0@65.21.131.215:26736,f97a75fb69d3a5fe893dca7c8d238ccc0bd66a8f@188.165.221.155:6969"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.teritorid/config/config.toml
```
