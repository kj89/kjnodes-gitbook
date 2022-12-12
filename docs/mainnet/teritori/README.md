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

**live-peers** (30)
```
peers="76ac8106e8b1169f1ef28f5c45558750db85d3dc@65.108.239.241:26656,4d6c820a7d426ad934a5e51f2e020836f0378919@116.202.143.91:26656,fe8765a154fc336ab284f28cdabc0bcb50a7afae@95.111.252.207:19656,ebacd77faa91ee858496a79250adff93480ce64b@158.69.188.117:26656,8ac41af54dfd91c41de71cde222a55670f2f405d@141.95.65.73:15956,16f90d350de14a596ebdc683ce5e703c14e40bb3@75.119.146.181:19656,ec4126b26336cd61b335345df4ff2a3fbb79338a@65.109.92.240:20026,4740ad44e58f4f4a0e2b9c4353500009eb73a05a@176.191.97.120:26656,808437b010f4663bf007b33433262d1495b0fbfe@35.90.134.158:28656,39fc4816c6cf92a7813a277d918b3c2d5de54b02@95.217.88.61:28656,574479abf5b0ed001519c60042bd88a97ce80a48@18.236.38.205:26656,8f4db549de62fbb96cf4cf477e2af9c52f74a3dd@51.91.64.170:19656,b336b83d9bab0b8cf96a3833efcbc196fab63fdd@212.95.51.215:36656,3577bc3c96ad809d7a89de999019db192ed85560@149.102.135.118:26656,97838a0c8a5035398f696dd29f28fe66b20b6a8d@46.4.81.204:44656,a25a3a218a699e71e2a64edaa45f457dfd8507ba@65.21.148.206:26656,0f0c7b23d2bde7f70b3e7b22f8664cd71186075c@95.216.228.231:26653,b906f0fdace24fb415254213644b51d4d6806d28@91.226.253.197:28756,3594b73f909a9c4b87cfe6a361ef8b2b51124dd5@65.109.69.59:15956,40caa979c29a9930ea2b8a6249037924d308ae84@162.55.234.70:54256,d43c09d1734e2135102621305aa3d15117b5d1b6@13.209.213.117:26656,e3b906fefa58783395fcf72086c698707908a558@141.95.65.26:27736,d956d6180e96c62315a777b1a3ed8f1ebf873e80@38.242.232.202:29656,6060a7c4f09dd7315f2c59b0c516f71e6e719a76@51.89.7.234:26642,5ab6437f73fe71f392d53566e037aa91087530ac@139.144.67.202:26656,bd6b1d4e82f21bb44fe11e2a1215e08da725e2c8@51.159.138.231:26656,bbc594f0a8424368b869fef47a18d6e35965db2e@176.9.188.21:53656,2da1141f27d403e9d0cd0ecf3f02d71a3ed5031a@49.12.132.167:30553,46b7ae20e3cc4264076a91c3601f3894a021a80d@65.108.6.45:36656,29b92a4020171c20fe70e5d60f9c5d07dc9f31f7@194.163.161.146:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.teritorid/config/config.toml
```
