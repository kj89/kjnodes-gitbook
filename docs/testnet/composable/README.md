# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/composable.png" alt=""><figcaption></figcaption></figure>

The complete infrastructure for cross-chain smart  contracts, applications, and modular functionality.

**Chain ID**: banksy-testnet-3 | **Latest Version Tag**: v3.0.0 | **Wasm**: OFF

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
peers="f75c4ca083ff3ecc40777e63cb9a28d6458d1d1d@207.180.246.161:26616,de2410e83b86e74a4569e0c120846b67c204f5bc@65.108.226.183:22256,f458da361f5934ee8d44e2ac1136bfa56f13b005@139.59.226.152:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15956,1f3bc143690c465800406a7b6c2898d4f0adebe6@65.21.91.160:27111,aa679f4f160f5ad84faf4b9baae11b6149379363@161.97.108.208:28656,d2deff06cf95c0d016d8f65822e1c74ce2af9def@95.217.58.111:26656,a3ddd1ffc5d24bd12fc4b2af5d2769776f5ce67d@65.109.92.240:21206,8f912ac69f9e36f7db9ec98879062f25b010484d@203.96.179.106:36656,eabe1168dd224da0d17d84c18df235a836688204@94.41.17.212:36656,b2ab46fe515d0ede14bbe37b16a24bfdf67c8a5b@167.235.7.34:56656,e9441db297752fb454f63d7f0f0c8eb5e067d528@34.124.143.97:26656,364b8245e72f083b0aa3e0d59b832020b66e9e9d@65.109.80.150:21500,4d3873e7d858f2cb710fea20c88445ef97d3ae60@37.27.17.146:19656,8390e4faca502620c177edcb8ee6ef7e57b5fcab@65.109.33.48:21656,117dea3045bce3a1bc4b0b59ed01a9be88df6815@65.108.124.121:60656,c2dbb5dbf1c9382e2eebe2a0ceeff0b4fc57f8ce@65.109.60.19:36656,8bc61c9c1901a7f35adabaaf29fe05215bb77298@24.158.14.210:26656,9a8b06a3b594fdbceaeeaf3d46aa97d302ed0303@185.255.131.27:26656,5a331fc6afa9ae7cbd6c9ebf39358161052c962b@65.109.65.248:37656,df49f4fee2fe62bc0ca8c27ee0dbae3f0abec98f@46.38.232.86:24656,42c6370c3608fcfc49b95d411efd4db34a7ad838@65.108.75.107:31656,e6a21ccb5175df638723eec2bc4f6ed95717acd3@135.181.216.54:3050,de24eace0af969355bdc050d438e031bea311459@65.21.106.106:34656,0038c200adc435ad9a21cde4e945fe2f48f405ff@65.108.233.102:34656,783e682b38c0565082fe5d897b24feebf687c52b@65.108.13.154:37656,7b603a86d79fb21aa9b4b6f8ea561bdbdf5cd223@75.119.154.2:15956,0a147702eea1e80c46b9a565f558f70ec5110f4b@65.109.92.148:46656,c866bd14649bb402dcb08c861add820b152e39e3@173.212.233.177:15956,790b9221fd5e05957fba1fe186e3a0a6972ff7d6@65.109.99.216:15956"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.banksy/config/config.toml
```
