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
peers="33d01ca326bb21c3e02c6f05b9cb530eea93c39d@65.109.23.237:30536,99004e3251209542b30c7502a7c35b1d574cd3ae@195.3.221.16:26656,8bfc2700b8ee3ccc87c7644232a56e934c47720e@65.108.238.147:34656,56bb737da7d2628b5c252e992c649489120838c7@65.21.178.202:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15956,8f912ac69f9e36f7db9ec98879062f25b010484d@203.96.179.106:36656,0a147702eea1e80c46b9a565f558f70ec5110f4b@65.109.92.148:46656,f458da361f5934ee8d44e2ac1136bfa56f13b005@139.59.226.152:26656,364b8245e72f083b0aa3e0d59b832020b66e9e9d@65.109.80.150:21500,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.21:26976,de2410e83b86e74a4569e0c120846b67c204f5bc@65.108.226.183:22256,a3ddd1ffc5d24bd12fc4b2af5d2769776f5ce67d@65.109.92.240:21206,d2deff06cf95c0d016d8f65822e1c74ce2af9def@95.217.58.111:26656,f306956520010c5ddd0e67c69f61f1de3fa91552@88.198.52.46:22256,f75c4ca083ff3ecc40777e63cb9a28d6458d1d1d@207.180.246.161:26616,eba3bc4613f3dac61201374ce09bee1fad00dc54@51.91.219.141:44003,e6a21ccb5175df638723eec2bc4f6ed95717acd3@135.181.216.54:3050,b2ab46fe515d0ede14bbe37b16a24bfdf67c8a5b@167.235.7.34:56656,b932185cd8f4a3d8d0dd9a01a78e2d489a99c074@144.76.174.27:26656,c2dbb5dbf1c9382e2eebe2a0ceeff0b4fc57f8ce@65.109.60.19:36656,0038c200adc435ad9a21cde4e945fe2f48f405ff@65.108.233.102:34656,4b398ed5ecdd938ab8332b2722dfb6dbcd9a69fe@207.180.249.127:26616,8390e4faca502620c177edcb8ee6ef7e57b5fcab@65.109.33.48:21656,790b9221fd5e05957fba1fe186e3a0a6972ff7d6@65.109.99.216:15956,117dea3045bce3a1bc4b0b59ed01a9be88df6815@65.108.124.121:60656,783e682b38c0565082fe5d897b24feebf687c52b@65.108.13.154:37656,5fcb4e8ac8d621d165a6616ae56ef5d5fd4f57bf@84.54.23.37:15956,e56266b49ee4da55df14e1604fb80a14038639c1@161.97.145.13:15956,4d3873e7d858f2cb710fea20c88445ef97d3ae60@37.27.17.146:19656,8020b85930cf42ca1dc3ed71e12c1620a3a8ce2e@65.108.129.94:46656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.banksy/config/config.toml
```
