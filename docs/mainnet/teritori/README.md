# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/teritori.png" width="150" alt=""><figcaption></figcaption></figure>

Teritori is a multi-chain hub designed to allow IBC and non IBC communities  to connect, trade services & NFTs, launch new projects & build further existing ones.

**Chain ID**: teritori-1 | **Latest Version Tag**: v1.3.0 | **Wasm**: ON

Website: [https://teritori.com](https://teritori.com)

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
peers="24b28cf013e6d7b5b88b6dba2701c5ddd2dd5ee1@65.109.58.225:28656,5ab6437f73fe71f392d53566e037aa91087530ac@139.144.67.202:26656,6bc9f80a5123d62c23aadb7b5d68b740a794b0c6@65.109.49.111:36656,ec4126b26336cd61b335345df4ff2a3fbb79338a@65.109.92.240:20026,4b04b3d164dc6dd5bb555a7a106a8d314f30516f@65.21.136.170:53656,0b27217386756577e1eadf00c4169dc8f041e522@51.210.7.219:26656,009e25e99e3f8fde86d283d4b8b0ce2f777cde53@138.201.8.248:53656,4aca2f1d6bb432596f5c3129165c42526320b3cb@78.110.161.68:26656,5a98d637a16b16bf425a4a785c9d11a7d1e5b8a0@65.21.131.215:26736,29b92a4020171c20fe70e5d60f9c5d07dc9f31f7@194.163.161.146:26656,406fc7fe86ba396cb7fc8616c546f21a1d3c51cd@89.58.57.158:26656,b0dcd078a40b8bca35f0cf873951b27e5dd45793@188.217.162.92:26656,2afdb9300c47e43e555fa572d033b2d68ac28506@65.109.70.68:26686,cdda30f407133027bf1322305e62ad968fad5348@96.69.133.222:26656,a191006e50d3af40fd253c23dae715a45fdd7415@95.179.217.1:26656,51eaf493facf36754411baa4f7b89355bd9cb3e7@195.201.63.87:42666,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:19656,14fa46dbadd79647ebf3e5bc82326d2debc5fd52@51.159.176.185:26656,3594b73f909a9c4b87cfe6a361ef8b2b51124dd5@65.109.69.59:15956,358f13bd95d91517053a58f4d30205842672837f@104.37.187.214:60656,6ef7a8bc7a3cc0856594f12570e8f2282a099dcf@65.109.93.152:26796,26175f13ada3d61c93bca342819fd5dc797bced0@65.109.58.226:28656,ed747c9e39fc04fdbc7ab5fc4a4a7f7a298ee329@65.144.145.234:26656,46b7ae20e3cc4264076a91c3601f3894a021a80d@65.108.6.45:36656,d956d6180e96c62315a777b1a3ed8f1ebf873e80@38.242.232.202:29656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.teritorid/config/config.toml
```
