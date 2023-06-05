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
peers="2b674316ab230f0c814f3f9bb1772b78b2c20a0f@137.184.193.235:15956,f86f691caf126ab0df6101d8748cf3313c99bbb6@78.31.64.11:26356,1f3bc143690c465800406a7b6c2898d4f0adebe6@65.21.91.160:27111,01653b523732cf8f48225859d97f0b41e429079b@65.108.199.206:33656,46bd8f512d60a8ea2ed73a34e444d22f8436dc7d@104.218.55.110:27656,7c064eeb99a5da5b1fe8ffc78c9ff8b5a9f3eda3@85.239.233.241:15956,f458da361f5934ee8d44e2ac1136bfa56f13b005@139.59.226.152:26656,64196513969cdfc2e280ee25117c42031068f9ea@194.34.232.150:15956,117dea3045bce3a1bc4b0b59ed01a9be88df6815@65.108.124.121:60656,de2410e83b86e74a4569e0c120846b67c204f5bc@65.108.226.183:22256,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.21:26976,b932185cd8f4a3d8d0dd9a01a78e2d489a99c074@144.76.174.27:26656,0a147702eea1e80c46b9a565f558f70ec5110f4b@65.109.92.148:46656,364b8245e72f083b0aa3e0d59b832020b66e9e9d@65.109.80.150:21500,a3ddd1ffc5d24bd12fc4b2af5d2769776f5ce67d@65.109.92.240:21206,0038c200adc435ad9a21cde4e945fe2f48f405ff@65.108.233.102:34656,eba3bc4613f3dac61201374ce09bee1fad00dc54@51.91.219.141:44003,8bfc2700b8ee3ccc87c7644232a56e934c47720e@65.108.238.147:34656,e6a21ccb5175df638723eec2bc4f6ed95717acd3@135.181.216.54:3050,56bb737da7d2628b5c252e992c649489120838c7@65.21.178.202:26656,e9441db297752fb454f63d7f0f0c8eb5e067d528@34.124.143.97:26656,d2deff06cf95c0d016d8f65822e1c74ce2af9def@95.217.58.111:26656,8390e4faca502620c177edcb8ee6ef7e57b5fcab@65.109.33.48:21656,05ec13f804da91036f413ca57a61849c169acda3@195.3.223.182:15956,ab771b5501a129c0d26cdef4bd3db1638702a24b@65.109.99.156:26656,783e682b38c0565082fe5d897b24feebf687c52b@65.108.13.154:37656,4d3873e7d858f2cb710fea20c88445ef97d3ae60@37.27.17.146:19656,df49f4fee2fe62bc0ca8c27ee0dbae3f0abec98f@46.38.232.86:24656,de24eace0af969355bdc050d438e031bea311459@65.21.106.106:34656,04f369723e9134c674479451b523a4c695a00901@51.15.10.24:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.banksy/config/config.toml
```
