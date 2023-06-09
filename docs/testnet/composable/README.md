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
peers="0851c005dd9aed50db962998989718987099f834@94.130.94.180:26656,4b398ed5ecdd938ab8332b2722dfb6dbcd9a69fe@207.180.249.127:26616,8bfc2700b8ee3ccc87c7644232a56e934c47720e@65.108.238.147:34656,64196513969cdfc2e280ee25117c42031068f9ea@194.34.232.150:15956,f6bdd60edcc84f2f02d582dc411cef80c5176df1@38.242.133.188:26656,c241d021004ad9b0fe7fa2d967ff9f1f3b20c1f0@136.243.172.166:15956,f306956520010c5ddd0e67c69f61f1de3fa91552@88.198.52.46:22256,6f4d63f0cc74663cff1848c1eea2f389e2b1ef33@66.94.121.181:15956,c2dbb5dbf1c9382e2eebe2a0ceeff0b4fc57f8ce@65.109.60.19:36656,9e7270b955791bb00acd68856366ed5450134d29@82.208.22.64:26656,4491f06f803252917d69d053ed85adba5ad17474@5.166.240.95:15956,e9441db297752fb454f63d7f0f0c8eb5e067d528@34.124.143.97:26656,f4078136bacf232ff67c4ab0fdbe5c88fb1f2f94@31.220.72.179:26656,2a9225e33a3cd40d4f9118a111a463e4c11bc6c2@31.220.85.1:26656,3461731f09871909987fa3df99c9ac623ea303b3@207.180.241.219:26656,df49f4fee2fe62bc0ca8c27ee0dbae3f0abec98f@46.38.232.86:24656,8be7bfa6c270469971875cb6f23c957402654a14@207.180.194.162:26656,99010dd03737038ee115fd79dd59cb8231567080@185.249.227.39:26656,e083e1ee42159e3b57284d38530efc29c6f8a4c9@109.123.247.105:26656,1f3bc143690c465800406a7b6c2898d4f0adebe6@65.21.91.160:27111,b2a5b6c11e7d71c2a43d88a73b9dcff3352f4302@57.128.86.7:26656,c866bd14649bb402dcb08c861add820b152e39e3@173.212.233.177:15956,10a831b0641d1fd90c62cea6f49b839470bd07e0@185.217.126.187:15956,3bab9d5cfb23118e703e1c4b62820f35acf45521@144.76.174.27:26656,e56266b49ee4da55df14e1604fb80a14038639c1@161.97.145.13:15956,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15956,a3ddd1ffc5d24bd12fc4b2af5d2769776f5ce67d@65.109.92.240:21206,3172f3c8b62d31d4c6e69afbf6109d06f864d899@43.157.65.43:26656,dbb829ef71299064c717923f7e72e6aa51302eff@65.109.172.252:15956,0038c200adc435ad9a21cde4e945fe2f48f405ff@65.108.233.102:34656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.banksy/config/config.toml
```
