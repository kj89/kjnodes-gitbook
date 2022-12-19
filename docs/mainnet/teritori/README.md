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

**live-peers** (32)
```
peers="fefd8ffb33a5d6ae194f082a39c4bb713da3a06b@167.86.86.197:36656,fec9760fec02405039ee0e90f80322b893e4ccef@65.144.145.234:26656,a191006e50d3af40fd253c23dae715a45fdd7415@95.179.217.1:26656,48980875839186e08e12ebf0d9a2803b45206833@65.109.92.241:38026,b906f0fdace24fb415254213644b51d4d6806d28@91.226.253.197:28756,593b8319d1d4b1958e7daba8c3bbb56795cb59ba@146.59.81.92:51656,d856120f262134ebf13e1d2632d778b69e704208@65.108.4.188:15956,0b27217386756577e1eadf00c4169dc8f041e522@51.210.7.219:26656,787a6b318ebc4167fefb1d5ef9f88af6cb5a8b29@173.212.222.167:35656,1e08fefb7e8851490d40e804df76d1ac33cb1f0a@38.146.3.175:15956,b336b83d9bab0b8cf96a3833efcbc196fab63fdd@212.95.51.215:36656,45f2d4f8ed2ef8d71a257cdeed27123f5fe3bef4@141.94.109.71:10356,3950af34da35ce3ff8c50ff3c47a43f5dfc93947@195.3.220.154:19656,24b28cf013e6d7b5b88b6dba2701c5ddd2dd5ee1@65.109.58.225:28656,1f4e77295379ce0c928502d2b075157a8c8a9e64@51.83.96.150:26642,40caa979c29a9930ea2b8a6249037924d308ae84@162.55.234.70:54256,6bc9f80a5123d62c23aadb7b5d68b740a794b0c6@65.109.49.111:36656,8480ce1f929a9410567d315a5b3fc2709c2807a7@93.115.25.106:51656,29b92a4020171c20fe70e5d60f9c5d07dc9f31f7@194.163.161.146:26656,5ab6437f73fe71f392d53566e037aa91087530ac@139.144.67.202:26656,5a98d637a16b16bf425a4a785c9d11a7d1e5b8a0@65.21.131.215:26736,d29bed885306037dbe219278415025a2ea8880a4@51.159.160.140:26656,009e25e99e3f8fde86d283d4b8b0ce2f777cde53@138.201.8.248:53656,26175f13ada3d61c93bca342819fd5dc797bced0@65.109.58.226:28656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:19656,3594b73f909a9c4b87cfe6a361ef8b2b51124dd5@65.109.69.59:15956,59d7b82880f319283d8f0314f20ddc98aa7b2cf8@174.45.46.27:26626,106490318e51355bc6d72e7941a0080f8b8256b9@185.16.39.14:26656,6ef7a8bc7a3cc0856594f12570e8f2282a099dcf@65.109.93.152:26796,46b7ae20e3cc4264076a91c3601f3894a021a80d@65.108.6.45:36656,4991cc04c48f96dec265464d5cf276e16f6b302c@188.217.162.92:26656,4740ad44e58f4f4a0e2b9c4353500009eb73a05a@176.191.97.120:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.teritorid/config/config.toml
```
