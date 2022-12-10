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

**live-peers** (36)
```
peers="4b04b3d164dc6dd5bb555a7a106a8d314f30516f@65.21.136.170:53656,bbc594f0a8424368b869fef47a18d6e35965db2e@176.9.188.21:53656,106490318e51355bc6d72e7941a0080f8b8256b9@185.16.39.14:26656,3594b73f909a9c4b87cfe6a361ef8b2b51124dd5@65.109.69.59:15956,35cdec21668ac214c74a6e45d444f6933f094bc4@144.202.72.17:26646,526d8c7c44f59be9a39d7463c576b68c0db23174@65.108.234.23:15956,d956d6180e96c62315a777b1a3ed8f1ebf873e80@38.242.232.202:29656,ff8f8c1b4cf70f38e1c370af05a40c1845022ae8@51.79.103.43:26656,8f4db549de62fbb96cf4cf477e2af9c52f74a3dd@51.91.64.170:19656,a25a3a218a699e71e2a64edaa45f457dfd8507ba@65.21.148.206:26656,8e9624292123624e4eddc3f43189f08a0424127e@65.108.131.62:26656,5a98d637a16b16bf425a4a785c9d11a7d1e5b8a0@65.21.131.215:26736,40caa979c29a9930ea2b8a6249037924d308ae84@162.55.234.70:54256,787a6b318ebc4167fefb1d5ef9f88af6cb5a8b29@173.212.222.167:35656,45f2d4f8ed2ef8d71a257cdeed27123f5fe3bef4@141.94.109.71:10356,b336b83d9bab0b8cf96a3833efcbc196fab63fdd@212.95.51.215:36656,28456ac1dded17760432c3f1d759c7d50ab6ed3e@51.250.83.54:26656,808437b010f4663bf007b33433262d1495b0fbfe@35.90.134.158:28656,b906f0fdace24fb415254213644b51d4d6806d28@91.226.253.197:28756,24b28cf013e6d7b5b88b6dba2701c5ddd2dd5ee1@65.109.58.225:28656,29b92a4020171c20fe70e5d60f9c5d07dc9f31f7@194.163.161.146:26656,3950af34da35ce3ff8c50ff3c47a43f5dfc93947@195.3.220.154:19656,3180d715a3c650907cc78c51edf3926a72e7f364@146.19.24.43:30589,009e25e99e3f8fde86d283d4b8b0ce2f777cde53@138.201.8.248:53656,e01ab41f694c18226d827172934dd0c596cc92de@51.159.181.184:26656,7d47faa64cef3eca57ed3f4eaf21f7a3981d512b@57.128.65.115:28656,46b7ae20e3cc4264076a91c3601f3894a021a80d@65.108.6.45:36656,43da931d00da102c002e0a227de7258b8fb1871a@144.126.135.53:26656,39fc4816c6cf92a7813a277d918b3c2d5de54b02@95.217.88.61:28656,6fb98b9e316b2900fce2fd331621460a932f4d7d@65.108.15.183:51656,474a200a225ff771fb78897c1329b20b679ca74f@173.215.85.171:20010,16f90d350de14a596ebdc683ce5e703c14e40bb3@75.119.146.181:19656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:19656,ad347ea1ec920d12ccda2341348bcc89687739ef@88.99.164.158:38026,b52a6ec019dfa39bb052dec1406a043027e24fc8@65.144.145.234:26656,94b63fddfc78230f51aeb7ac34b9fb86bd042a77@95.217.89.23:30552"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.teritorid/config/config.toml
```
