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
peers="3172f3c8b62d31d4c6e69afbf6109d06f864d899@43.157.65.43:26656,99004e3251209542b30c7502a7c35b1d574cd3ae@195.3.221.16:26656,e7fe7d8570fa647d738753cbad9935a0803c468a@65.109.96.93:60656,de24eace0af969355bdc050d438e031bea311459@65.21.106.106:34656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15956,e6a21ccb5175df638723eec2bc4f6ed95717acd3@135.181.216.54:3050,de2410e83b86e74a4569e0c120846b67c204f5bc@65.108.226.183:22256,eba3bc4613f3dac61201374ce09bee1fad00dc54@51.91.219.141:44003,211bebc24e286a973d3038f2fbbf5f673badc190@51.250.4.215:27656,33d01ca326bb21c3e02c6f05b9cb530eea93c39d@65.109.23.237:30536,9ae49a070ea985784830da8050769ad6791caef5@164.92.64.61:15956,42c6370c3608fcfc49b95d411efd4db34a7ad838@65.108.75.107:31656,61d192daf2e2877f25d90705eccab95d2ccc5d28@164.92.112.252:15956,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.21:26976,f86f691caf126ab0df6101d8748cf3313c99bbb6@78.31.64.11:26356,364b8245e72f083b0aa3e0d59b832020b66e9e9d@65.109.80.150:21500,2915075181a61869aba8b38b40782090548117c6@146.19.24.101:23466,4b689b965366ea2d9aad4bd1343ca37d6f18186a@65.109.92.240:21206,8f912ac69f9e36f7db9ec98879062f25b010484d@203.96.179.106:36656,0851c005dd9aed50db962998989718987099f834@94.130.94.180:26656,3f0727b11da4dc792fe2dfb34214cf45fadd4a15@95.216.67.178:26656,4f45caee0a7627640f931baae588d10094072d12@143.198.198.204:15956,8390e4faca502620c177edcb8ee6ef7e57b5fcab@65.109.33.48:21656,764fed363ddaa588c5bfaa43d5ef3177738bbc23@167.114.172.204:26656,c2dbb5dbf1c9382e2eebe2a0ceeff0b4fc57f8ce@65.109.60.19:36656,0a68e21ab47c15f634a97019c2a0b8d3bea09622@185.190.142.177:26656,5a331fc6afa9ae7cbd6c9ebf39358161052c962b@65.109.65.248:37656,0cde9b12f47913678e4fd6eeed1f93711613baa7@65.108.11.234:15656,4d3873e7d858f2cb710fea20c88445ef97d3ae60@37.27.17.146:19656,783e682b38c0565082fe5d897b24feebf687c52b@65.108.13.154:37656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.banksy/config/config.toml
```
