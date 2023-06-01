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

**live-peers** (27)
```bash
peers="df49f4fee2fe62bc0ca8c27ee0dbae3f0abec98f@46.38.232.86:24656,0d8b80ff1f956385cecee2d1aef4730cc72fa6f4@146.190.40.139:15956,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15956,de2410e83b86e74a4569e0c120846b67c204f5bc@65.108.226.183:22256,eba3bc4613f3dac61201374ce09bee1fad00dc54@51.91.219.141:44003,de24eace0af969355bdc050d438e031bea311459@65.21.106.106:34656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.21:26976,e6a21ccb5175df638723eec2bc4f6ed95717acd3@135.181.216.54:3050,364b8245e72f083b0aa3e0d59b832020b66e9e9d@65.109.80.150:21500,0a147702eea1e80c46b9a565f558f70ec5110f4b@65.109.92.148:46656,d2deff06cf95c0d016d8f65822e1c74ce2af9def@95.217.58.111:26656,4d3873e7d858f2cb710fea20c88445ef97d3ae60@37.27.17.146:19656,8390e4faca502620c177edcb8ee6ef7e57b5fcab@65.109.33.48:21656,764fed363ddaa588c5bfaa43d5ef3177738bbc23@167.114.172.204:26656,c2dbb5dbf1c9382e2eebe2a0ceeff0b4fc57f8ce@65.109.60.19:36656,f86f691caf126ab0df6101d8748cf3313c99bbb6@78.31.64.11:26356,8f912ac69f9e36f7db9ec98879062f25b010484d@203.96.179.106:36656,4b398ed5ecdd938ab8332b2722dfb6dbcd9a69fe@207.180.249.127:26616,5a331fc6afa9ae7cbd6c9ebf39358161052c962b@65.109.65.248:37656,4b689b965366ea2d9aad4bd1343ca37d6f18186a@65.109.92.240:21206,7c064eeb99a5da5b1fe8ffc78c9ff8b5a9f3eda3@85.239.233.241:15956,33d01ca326bb21c3e02c6f05b9cb530eea93c39d@65.109.23.237:30536,0851c005dd9aed50db962998989718987099f834@94.130.94.180:26656,56bb737da7d2628b5c252e992c649489120838c7@65.21.178.202:26656,6b792ff5118ef1e141085af62ace3ad846d757b4@193.34.212.165:26656,783e682b38c0565082fe5d897b24feebf687c52b@65.108.13.154:37656,ce220cbf59df41af7bdd16f4c426c626c8a8619a@213.133.99.244:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.banksy/config/config.toml
```
