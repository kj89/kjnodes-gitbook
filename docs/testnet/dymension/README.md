# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/dymension.png" width="150" alt=""><figcaption></figcaption></figure>

Dymension is a network of modular blockchains called RollApps  and at the center of it all is the Dymension Hub. Dymension  allows anyone to build and deploy their own consensus-free blockchain, a RollApp.

**Chain ID**: 35-C | **Latest Version Tag**: v0.2.0-beta | **Wasm**: OFF

[Website](https://dymension.xyz/) | [Discord](https://discord.gg/dymension) | [Twitter](https://twitter.com/dymensionXYZ)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/dymension-testnet](https://explorer.kjnodes.com/dymension-testnet)

## Public endpoints

* api: [https://dymension-testnet.api.kjnodes.com](https://dymension-testnet.api.kjnodes.com)
* rpc: [https://dymension-testnet.rpc.kjnodes.com](https://dymension-testnet.rpc.kjnodes.com)
* grpc: dymension-testnet.grpc.kjnodes.com:46090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@dymension-testnet.rpc.kjnodes.com:46656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@dymension-testnet.rpc.kjnodes.com:46659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/dymension-testnet/addrbook.json > $HOME/.dymension/config/addrbook.json
```

**live-peers** (30)
```bash
peers="94b63fddfc78230f51aeb7ac34b9fb86bd042a77@146.19.24.43:30585,b1e1e5a9dbf2e03b456668c2f2d9164ae090ba0c@109.123.244.56:46656,b24974dd15a984f882438d907ee97c6baf1ae766@185.177.116.36:656,1ed89bd1d280c4c6eb7d9134bb238d97fbb3f4b2@88.99.104.180:36656,998b19ed2c580acaa2fdb5057e2930a38f041750@65.109.122.105:60556,98a03e1d03c1646e982b3379c0132d3828b0cacd@37.128.87.66:26656,a85420b25181bdb9b3a38741c48dafd5fb3b922f@209.34.205.57:26656,0ee31ef97ba6b6c13b25b5c528163f2092821c2d@65.21.132.27:24856,0cc10d01b749a1e8b8d14c077140c776394d31e5@65.108.9.164:21456,b921655e6c66235915e7d4465ea2146e537f13e4@167.235.6.228:26636,4d2ec1e61d61550fc5bfacc57e971ff9b6181152@135.181.180.29:26656,ba2ef45240cc997443df795b801a34602ba68b55@65.109.92.241:17886,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.54:27086,c6cdcc7f8e1a33f864956a8201c304741411f219@3.214.163.125:26656,88e09de4c713ecb3497f39f6e6c599aea7a10750@65.109.38.111:20556,5f235b399033f1841f77e233d38eaf707087e275@38.242.248.195:26656,8b5367df2b1287174ce8950654953d81a7d69a29@144.76.201.43:26556,747d05bfe9f3e0c2e0462ac351c577699e1d9b8c@207.244.244.194:26656,3a1e280b47ba71e11c2f1d800d0dd837cd40ed08@38.242.246.215:26656,60f464943e6434579abdfa28a3122bd2d6008dec@139.99.68.119:26656,7fc44e2651006fb2ddb4a56132e738da2845715f@65.108.6.45:61256,80cce834fc749c0a9f47182665f833f97170ff4b@65.108.104.167:46656,dddc76ca6279ac90b12cf35b39c46a2fc2c2ce52@5.161.78.48:46656,b8d08951d68da03af8f9272bf77684811197c289@95.216.41.160:26656,48bdb78c51e56b651c938d075e1077dab2c6197c@43.157.22.223:26656,5dbbb68e0c8a86bdc372cf1de0691f1cdc6a96ad@82.208.23.223:27656,63996f52b1dc68259ff64bb2546625c71fc9d546@176.9.48.38:26656,62f5e5db360892ce0e8fc4cc5de7b880936e8410@82.208.23.204:04656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656,281190aa44ca82fb47afe60ba1a8902bae469b2a@88.99.164.158:17086"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
