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

**live-peers** (28)
```bash
peers="de2410e83b86e74a4569e0c120846b67c204f5bc@65.108.226.183:22256,4d3873e7d858f2cb710fea20c88445ef97d3ae60@37.27.17.146:19656,e7fe7d8570fa647d738753cbad9935a0803c468a@65.109.96.93:60656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15956,e6a21ccb5175df638723eec2bc4f6ed95717acd3@135.181.216.54:3050,0a147702eea1e80c46b9a565f558f70ec5110f4b@65.109.92.148:46656,5a331fc6afa9ae7cbd6c9ebf39358161052c962b@65.109.65.248:37656,eba3bc4613f3dac61201374ce09bee1fad00dc54@51.91.219.141:44003,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.21:26976,d2deff06cf95c0d016d8f65822e1c74ce2af9def@95.217.58.111:26656,c2dbb5dbf1c9382e2eebe2a0ceeff0b4fc57f8ce@65.109.60.19:36656,364b8245e72f083b0aa3e0d59b832020b66e9e9d@65.109.80.150:21500,4b689b965366ea2d9aad4bd1343ca37d6f18186a@65.109.92.240:21206,56bb737da7d2628b5c252e992c649489120838c7@65.21.178.202:26656,f75c4ca083ff3ecc40777e63cb9a28d6458d1d1d@207.180.246.161:26616,8390e4faca502620c177edcb8ee6ef7e57b5fcab@65.109.33.48:21656,f306956520010c5ddd0e67c69f61f1de3fa91552@88.198.52.46:22256,8f912ac69f9e36f7db9ec98879062f25b010484d@203.96.179.106:36656,0038c200adc435ad9a21cde4e945fe2f48f405ff@65.108.233.102:34656,10a831b0641d1fd90c62cea6f49b839470bd07e0@185.217.126.187:15956,c66a2b8e76e30b87580d7f940dcee79ec5e1e5db@23.92.79.50:26856,4b398ed5ecdd938ab8332b2722dfb6dbcd9a69fe@207.180.249.127:26616,790b9221fd5e05957fba1fe186e3a0a6972ff7d6@65.109.99.216:15956,20e6ecaaadd8cad474b8312d935042811513f6ff@207.244.253.244:46656,99004e3251209542b30c7502a7c35b1d574cd3ae@195.3.221.16:26656,783e682b38c0565082fe5d897b24feebf687c52b@65.108.13.154:37656,df49f4fee2fe62bc0ca8c27ee0dbae3f0abec98f@46.38.232.86:24656,63a0e6bcd7045a2e3d21762bec9d70f399e886ab@43.157.47.45:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.banksy/config/config.toml
```
