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

**live-peers** (34)
```
peers="4b04b3d164dc6dd5bb555a7a106a8d314f30516f@65.21.136.170:53656,1f9293a286df733dac6303aad3c39240ad3b3796@178.211.139.24:46656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:19656,6fb98b9e316b2900fce2fd331621460a932f4d7d@65.108.15.183:51656,76ac8106e8b1169f1ef28f5c45558750db85d3dc@65.108.239.241:26656,5a98d637a16b16bf425a4a785c9d11a7d1e5b8a0@65.21.131.215:26736,d856120f262134ebf13e1d2632d778b69e704208@65.108.4.188:15956,7d47faa64cef3eca57ed3f4eaf21f7a3981d512b@57.128.65.115:28656,3950af34da35ce3ff8c50ff3c47a43f5dfc93947@195.3.220.154:19656,16f90d350de14a596ebdc683ce5e703c14e40bb3@75.119.146.181:19656,ebacd77faa91ee858496a79250adff93480ce64b@158.69.188.117:26656,3bd3a20d7c8a26a20927289a7a6bffecf71de53e@51.81.155.97:10856,c669be4c7c0e44a3da941f4b97a8ee4ef39f7d6e@51.159.106.145:26656,bbc594f0a8424368b869fef47a18d6e35965db2e@176.9.188.21:53656,b336b83d9bab0b8cf96a3833efcbc196fab63fdd@212.95.51.215:36656,2da1141f27d403e9d0cd0ecf3f02d71a3ed5031a@49.12.132.167:30553,5ab6437f73fe71f392d53566e037aa91087530ac@139.144.67.202:26656,b906f0fdace24fb415254213644b51d4d6806d28@91.226.253.197:28756,26175f13ada3d61c93bca342819fd5dc797bced0@65.109.58.226:28656,3594b73f909a9c4b87cfe6a361ef8b2b51124dd5@65.109.69.59:15956,fefd8ffb33a5d6ae194f082a39c4bb713da3a06b@167.86.86.197:36656,40caa979c29a9930ea2b8a6249037924d308ae84@162.55.234.70:54256,d956d6180e96c62315a777b1a3ed8f1ebf873e80@38.242.232.202:29656,7fbfea037bd7962199ffbfd25986c014bab05298@155.133.22.9:22956,ed747c9e39fc04fdbc7ab5fc4a4a7f7a298ee329@65.144.145.234:26656,7cd5a57fb2194297952f62b2632c04d8e1222485@65.108.226.58:26656,35cdec21668ac214c74a6e45d444f6933f094bc4@144.202.72.17:26646,a043a97266360ff45781a9fc9392aedc16494c59@65.108.97.58:19656,647bbbc30d26fbbb2f7d19aafe30ed77a92c4748@65.108.130.171:26656,44b2bf9d970aece0531d3d939c5c546a7ac9201a@34.219.76.190:26656,29b92a4020171c20fe70e5d60f9c5d07dc9f31f7@194.163.161.146:26656,4740ad44e58f4f4a0e2b9c4353500009eb73a05a@176.191.97.120:26656,46b7ae20e3cc4264076a91c3601f3894a021a80d@65.108.6.45:36656,4991cc04c48f96dec265464d5cf276e16f6b302c@188.217.162.92:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.teritorid/config/config.toml
```
