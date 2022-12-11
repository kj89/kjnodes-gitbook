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

**live-peers** (33)
```
peers="2afdb9300c47e43e555fa572d033b2d68ac28506@65.109.70.68:26686,a191006e50d3af40fd253c23dae715a45fdd7415@95.179.217.1:26656,82ebb17ddac20928fb8107201dad9f5aea7f9132@198.244.200.3:26656,4b04b3d164dc6dd5bb555a7a106a8d314f30516f@65.21.136.170:53656,48980875839186e08e12ebf0d9a2803b45206833@65.109.92.241:38026,b906f0fdace24fb415254213644b51d4d6806d28@91.226.253.197:28756,d43c09d1734e2135102621305aa3d15117b5d1b6@13.209.213.117:26656,ebacd77faa91ee858496a79250adff93480ce64b@158.69.188.117:26656,3178ac8fffd269325500c95679d58d5e8ec61746@198.244.213.94:22956,106490318e51355bc6d72e7941a0080f8b8256b9@185.16.39.14:26656,43da931d00da102c002e0a227de7258b8fb1871a@144.126.135.53:26656,6085c32b26fb1baa4b16b426f5d56f2fff81cfc7@135.181.165.246:26656,40caa979c29a9930ea2b8a6249037924d308ae84@162.55.234.70:54256,76ac8106e8b1169f1ef28f5c45558750db85d3dc@65.108.239.241:26656,1f4e77295379ce0c928502d2b075157a8c8a9e64@51.83.96.150:26642,787a6b318ebc4167fefb1d5ef9f88af6cb5a8b29@173.212.222.167:35656,3594b73f909a9c4b87cfe6a361ef8b2b51124dd5@65.109.69.59:15956,35cdec21668ac214c74a6e45d444f6933f094bc4@144.202.72.17:26646,a25a3a218a699e71e2a64edaa45f457dfd8507ba@65.21.148.206:26656,6fb98b9e316b2900fce2fd331621460a932f4d7d@65.108.15.183:51656,b336b83d9bab0b8cf96a3833efcbc196fab63fdd@212.95.51.215:36656,3768b801461e9934afc8cee642f8e5c10f823348@89.245.24.72:23356,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:19656,d956d6180e96c62315a777b1a3ed8f1ebf873e80@38.242.232.202:29656,2434c1dbf0c04bb50e17a39a77c317512b5c1dc4@65.109.35.66:51656,24b28cf013e6d7b5b88b6dba2701c5ddd2dd5ee1@65.109.58.225:28656,ad347ea1ec920d12ccda2341348bcc89687739ef@88.99.164.158:38026,6ef7a8bc7a3cc0856594f12570e8f2282a099dcf@65.109.93.152:26796,4740ad44e58f4f4a0e2b9c4353500009eb73a05a@176.191.97.120:26656,b52a6ec019dfa39bb052dec1406a043027e24fc8@65.144.145.234:26656,46b7ae20e3cc4264076a91c3601f3894a021a80d@65.108.6.45:36656,29b92a4020171c20fe70e5d60f9c5d07dc9f31f7@194.163.161.146:26656,5ab6437f73fe71f392d53566e037aa91087530ac@139.144.67.202:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.teritorid/config/config.toml
```
