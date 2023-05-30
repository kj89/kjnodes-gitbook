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
peers="0851c005dd9aed50db962998989718987099f834@94.130.94.180:26656,3172f3c8b62d31d4c6e69afbf6109d06f864d899@43.157.65.43:26656,5a331fc6afa9ae7cbd6c9ebf39358161052c962b@65.109.65.248:37656,364b8245e72f083b0aa3e0d59b832020b66e9e9d@65.109.80.150:21500,de2410e83b86e74a4569e0c120846b67c204f5bc@65.108.226.183:22256,4d3873e7d858f2cb710fea20c88445ef97d3ae60@37.27.17.146:19656,e6a21ccb5175df638723eec2bc4f6ed95717acd3@135.181.216.54:3050,764fed363ddaa588c5bfaa43d5ef3177738bbc23@167.114.172.204:26656,05ec13f804da91036f413ca57a61849c169acda3@195.3.223.182:15956,eba3bc4613f3dac61201374ce09bee1fad00dc54@51.91.219.141:44003,6b792ff5118ef1e141085af62ace3ad846d757b4@193.34.212.165:26656,99004e3251209542b30c7502a7c35b1d574cd3ae@195.3.221.16:26656,cb524c20d23b743dcf59a2caa4b0c5ac604af1ef@95.165.107.241:15956,4b689b965366ea2d9aad4bd1343ca37d6f18186a@65.109.92.240:21206,8390e4faca502620c177edcb8ee6ef7e57b5fcab@65.109.33.48:21656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.21:26976,211bebc24e286a973d3038f2fbbf5f673badc190@51.250.4.215:27656,8020b85930cf42ca1dc3ed71e12c1620a3a8ce2e@65.108.129.94:46656,f86f691caf126ab0df6101d8748cf3313c99bbb6@78.31.64.11:26356,de24eace0af969355bdc050d438e031bea311459@65.21.106.106:34656,d0f54e60e10ca4d657b48c9cfc5549fb2a8c7a96@65.109.31.55:25656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15956,022221b7dc3be873a5b7b24682154f32c07e96cc@194.163.167.138:52656,df49f4fee2fe62bc0ca8c27ee0dbae3f0abec98f@46.38.232.86:24656,ab2ba40e4f9dff8e09ac1734dce6eba1aa8770a8@65.109.55.186:656,415ed8fdb8f4408ee4ab4c7ac57a66282184fa7d@144.91.124.126:30656,33d01ca326bb21c3e02c6f05b9cb530eea93c39d@65.109.23.237:30536,02ea9a908729d6c7a846a535a63fd47131c59b88@65.109.60.19:36656,e7fe7d8570fa647d738753cbad9935a0803c468a@65.109.96.93:60656,783e682b38c0565082fe5d897b24feebf687c52b@65.108.13.154:37656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.banksy/config/config.toml
```
