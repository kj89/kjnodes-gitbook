# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/composable.png" alt=""><figcaption></figcaption></figure>

The complete infrastructure for cross-chain smart  contracts, applications, and modular functionality.

**Chain ID**: banksy-testnet-3 | **Latest Version Tag**: v2.3.5 | **Wasm**: OFF

[Website](https://www.composable.finance) | [Discord](https://discord.gg/composable) | [Twitter](https://twitter.com/ComposableFin)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/composable-testnet](https://explorer.kjnodes.com/composable-testnet)

## Public endpoints

* api: [https://composable-testnet.api.kjnodes.com](https://composable-testnet.api.kjnodes.com)
* rpc: [https://composable-testnet.rpc.kjnodes.com](https://composable-testnet.rpc.kjnodes.com)
* grpc: composable-testnet.grpc.kjnodes.com:15990

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@composable-testnet.rpc.kjnodes.com:15956
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@composable-testnet.rpc.kjnodes.com:15959
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/composable-testnet/addrbook.json > $HOME/.banksy/config/addrbook.json
```

**live-peers** (30)
```bash
peers="f86f691caf126ab0df6101d8748cf3313c99bbb6@78.31.64.11:26356,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15956,783e682b38c0565082fe5d897b24feebf687c52b@65.108.13.154:37656,f458da361f5934ee8d44e2ac1136bfa56f13b005@139.59.226.152:26656,117dea3045bce3a1bc4b0b59ed01a9be88df6815@65.108.124.121:60656,eabe1168dd224da0d17d84c18df235a836688204@94.41.17.212:36656,de2410e83b86e74a4569e0c120846b67c204f5bc@65.108.226.183:22256,0a147702eea1e80c46b9a565f558f70ec5110f4b@65.109.92.148:46656,eba3bc4613f3dac61201374ce09bee1fad00dc54@51.91.219.141:44003,f001e55f424e56e5eed28d4dfb4067856acb745c@143.198.148.41:15956,a3ddd1ffc5d24bd12fc4b2af5d2769776f5ce67d@65.109.92.240:21206,790b9221fd5e05957fba1fe186e3a0a6972ff7d6@65.109.99.216:15956,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.21:26976,e6a21ccb5175df638723eec2bc4f6ed95717acd3@135.181.216.54:3050,8390e4faca502620c177edcb8ee6ef7e57b5fcab@65.109.33.48:21656,1f3bc143690c465800406a7b6c2898d4f0adebe6@65.21.91.160:27111,364b8245e72f083b0aa3e0d59b832020b66e9e9d@65.109.80.150:21500,ab771b5501a129c0d26cdef4bd3db1638702a24b@65.109.99.156:26656,e9441db297752fb454f63d7f0f0c8eb5e067d528@34.124.143.97:26656,9bbbcb11861c2fe3c6459529af76f78cca32079e@93.115.28.169:46656,0038c200adc435ad9a21cde4e945fe2f48f405ff@65.108.233.102:34656,f2cafa15bd9e56c7c3f0190b0b5e0c99a91b4bbb@3.91.76.45:26656,d2deff06cf95c0d016d8f65822e1c74ce2af9def@95.217.58.111:26656,7c064eeb99a5da5b1fe8ffc78c9ff8b5a9f3eda3@85.239.233.241:15956,b932185cd8f4a3d8d0dd9a01a78e2d489a99c074@144.76.174.27:26656,46bd8f512d60a8ea2ed73a34e444d22f8436dc7d@104.218.55.110:27656,de24eace0af969355bdc050d438e031bea311459@65.21.106.106:34656,f306956520010c5ddd0e67c69f61f1de3fa91552@88.198.52.46:22256,bc59a32fa740e90d78a66dd5d671de81a5d4396c@138.2.74.78:15956,667703b3bdf291ec7774c0c46a54eddd2ccb6d36@46.17.250.108:61456"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.banksy/config/config.toml
```
