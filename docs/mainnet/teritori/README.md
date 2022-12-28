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
peers="28456ac1dded17760432c3f1d759c7d50ab6ed3e@51.250.83.54:26656,40caa979c29a9930ea2b8a6249037924d308ae84@162.55.234.70:54256,82ebb17ddac20928fb8107201dad9f5aea7f9132@198.244.200.3:26656,88a407d4749e1ccbb630f98ca44f304744d97864@38.242.141.168:26656,d956d6180e96c62315a777b1a3ed8f1ebf873e80@38.242.232.202:29656,0b27217386756577e1eadf00c4169dc8f041e522@51.210.7.219:26656,5ab6437f73fe71f392d53566e037aa91087530ac@139.144.67.202:26656,5a98d637a16b16bf425a4a785c9d11a7d1e5b8a0@65.21.131.215:26736,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:19656,76ac8106e8b1169f1ef28f5c45558750db85d3dc@65.108.239.241:26656,8ac41af54dfd91c41de71cde222a55670f2f405d@141.95.65.73:15956,4b04b3d164dc6dd5bb555a7a106a8d314f30516f@65.21.136.170:53656,1e08fefb7e8851490d40e804df76d1ac33cb1f0a@38.146.3.175:15956,317d9a102d4a04337c65571c18df0e98269dce87@141.94.193.12:13656,3178ac8fffd269325500c95679d58d5e8ec61746@198.244.213.94:22956,81bd965baf90d49b9ff3e122394150fcdc935e64@65.144.145.234:26604,89757803f40da51678451735445ad40d5b15e059@134.65.192.221:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@134.65.192.81:26656,3594b73f909a9c4b87cfe6a361ef8b2b51124dd5@65.109.69.59:15956,51eaf493facf36754411baa4f7b89355bd9cb3e7@195.201.63.87:42666,26175f13ada3d61c93bca342819fd5dc797bced0@65.109.58.226:28656,a7d96dc929824613315dcc1c90fee119f28cc51f@164.152.161.254:26656,44b2bf9d970aece0531d3d939c5c546a7ac9201a@34.219.76.190:26656,14fa46dbadd79647ebf3e5bc82326d2debc5fd52@51.159.176.185:26656,46b7ae20e3cc4264076a91c3601f3894a021a80d@65.108.6.45:36656,ad347ea1ec920d12ccda2341348bcc89687739ef@88.99.164.158:38026,4740ad44e58f4f4a0e2b9c4353500009eb73a05a@176.191.97.120:26656,ade4d8bc8cbe014af6ebdf3cb7b1e9ad36f412c0@135.181.5.219:15956,f97a75fb69d3a5fe893dca7c8d238ccc0bd66a8f@188.165.221.155:6969"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.teritorid/config/config.toml
```
