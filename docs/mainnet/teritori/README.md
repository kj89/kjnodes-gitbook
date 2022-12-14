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

**live-peers** (35)
```
peers="b336b83d9bab0b8cf96a3833efcbc196fab63fdd@212.95.51.215:36656,76ac8106e8b1169f1ef28f5c45558750db85d3dc@65.108.239.241:26656,e3b906fefa58783395fcf72086c698707908a558@141.95.65.26:27736,45f2d4f8ed2ef8d71a257cdeed27123f5fe3bef4@141.94.109.71:10356,4740ad44e58f4f4a0e2b9c4353500009eb73a05a@176.191.97.120:26656,fefd8ffb33a5d6ae194f082a39c4bb713da3a06b@167.86.86.197:36656,c58613003b7f2e2a5de7fd0035552bb2afa6c1ab@31.186.64.5:19656,34b87bdfc1f0b6a11724cf45dda3ee66c9a4691c@38.146.3.176:15956,009e25e99e3f8fde86d283d4b8b0ce2f777cde53@138.201.8.248:53656,ebacd77faa91ee858496a79250adff93480ce64b@158.69.188.117:26656,1f4e77295379ce0c928502d2b075157a8c8a9e64@51.83.96.150:26642,7f9773971291b77b2d65364a8928cb31c40aa70f@65.108.73.124:13656,b906f0fdace24fb415254213644b51d4d6806d28@91.226.253.197:28756,2f93424bd346b857bd5164eaac0b2bfd5fd644c0@144.91.127.252:26656,bbc594f0a8424368b869fef47a18d6e35965db2e@176.9.188.21:53656,3594b73f909a9c4b87cfe6a361ef8b2b51124dd5@65.109.69.59:15956,722b63e6c65628b929f22013dcbcde980210cb44@176.9.127.54:26656,370bf5f5b9ce655403d05753c355798288c1f120@89.245.24.67:23356,106490318e51355bc6d72e7941a0080f8b8256b9@185.16.39.14:26656,81bd965baf90d49b9ff3e122394150fcdc935e64@65.144.145.234:26604,e73e8cefd738de437775f9621a8bd76f1e6ff954@3.144.73.184:26656,36c2418b7aed4e585ac3e8f138a2e5ccf0f8278f@198.244.228.17:28766,1e08fefb7e8851490d40e804df76d1ac33cb1f0a@38.146.3.175:15956,5ab6437f73fe71f392d53566e037aa91087530ac@139.144.67.202:26656,40caa979c29a9930ea2b8a6249037924d308ae84@162.55.234.70:54256,26175f13ada3d61c93bca342819fd5dc797bced0@65.109.58.226:28656,358f13bd95d91517053a58f4d30205842672837f@104.37.187.214:60656,51eaf493facf36754411baa4f7b89355bd9cb3e7@195.201.63.87:42666,526d8c7c44f59be9a39d7463c576b68c0db23174@65.108.234.23:15956,46b7ae20e3cc4264076a91c3601f3894a021a80d@65.108.6.45:36656,d956d6180e96c62315a777b1a3ed8f1ebf873e80@38.242.232.202:29656,6ef7a8bc7a3cc0856594f12570e8f2282a099dcf@65.109.93.152:26796,8ac41af54dfd91c41de71cde222a55670f2f405d@141.95.65.73:15956,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:19656,29b92a4020171c20fe70e5d60f9c5d07dc9f31f7@194.163.161.146:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.teritorid/config/config.toml
```
