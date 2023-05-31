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

**live-peers** (26)
```bash
peers="df49f4fee2fe62bc0ca8c27ee0dbae3f0abec98f@46.38.232.86:24656,de24eace0af969355bdc050d438e031bea311459@65.21.106.106:34656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15956,de2410e83b86e74a4569e0c120846b67c204f5bc@65.108.226.183:22256,f75c4ca083ff3ecc40777e63cb9a28d6458d1d1d@207.180.246.161:26616,eba3bc4613f3dac61201374ce09bee1fad00dc54@51.91.219.141:44003,4b689b965366ea2d9aad4bd1343ca37d6f18186a@65.109.92.240:21206,4b398ed5ecdd938ab8332b2722dfb6dbcd9a69fe@207.180.249.127:26616,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.21:26976,364b8245e72f083b0aa3e0d59b832020b66e9e9d@65.109.80.150:21500,4d3873e7d858f2cb710fea20c88445ef97d3ae60@37.27.17.146:19656,c2dbb5dbf1c9382e2eebe2a0ceeff0b4fc57f8ce@65.109.60.19:36656,8390e4faca502620c177edcb8ee6ef7e57b5fcab@65.109.33.48:21656,8f912ac69f9e36f7db9ec98879062f25b010484d@203.96.179.106:36656,d2deff06cf95c0d016d8f65822e1c74ce2af9def@95.217.58.111:26656,93418eb0d95d34dfda8818e7abf4cd4679f51e39@91.144.171.205:26656,89649e448f60b603a3a56205cd4a98d7ea141ab9@208.113.135.109:26656,33d01ca326bb21c3e02c6f05b9cb530eea93c39d@65.109.23.237:30536,72277f057ceace166b8c4ade796689cb1e394caf@89.179.33.100:15956,0851c005dd9aed50db962998989718987099f834@94.130.94.180:26656,5a331fc6afa9ae7cbd6c9ebf39358161052c962b@65.109.65.248:37656,3f0727b11da4dc792fe2dfb34214cf45fadd4a15@95.216.67.178:26656,783e682b38c0565082fe5d897b24feebf687c52b@65.108.13.154:37656,8bc61c9c1901a7f35adabaaf29fe05215bb77298@24.158.14.210:26656,ca3396dcbc8786df44fdc0d96726b8d1a2338856@116.202.227.117:15956,d9c51e0053fc0a0b1bcd0ba3880d8c70f49f496f@65.109.28.226:24656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.banksy/config/config.toml
```
