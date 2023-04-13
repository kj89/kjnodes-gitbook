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

**live-peers** (29)
```bash
peers="5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.54:27086,d2b841acdcabb622e9033fe685a395eef091f2fe@65.108.199.62:46656,88e09de4c713ecb3497f39f6e6c599aea7a10750@65.109.38.111:20556,1ed89bd1d280c4c6eb7d9134bb238d97fbb3f4b2@88.99.104.180:36656,ba2ef45240cc997443df795b801a34602ba68b55@65.109.92.241:17886,a85420b25181bdb9b3a38741c48dafd5fb3b922f@209.34.205.57:26656,0ee31ef97ba6b6c13b25b5c528163f2092821c2d@65.21.132.27:24856,0cc10d01b749a1e8b8d14c077140c776394d31e5@65.108.9.164:21456,4d2ec1e61d61550fc5bfacc57e971ff9b6181152@135.181.180.29:26656,8b5367df2b1287174ce8950654953d81a7d69a29@144.76.201.43:26556,a6b148f8419992dd2a1c4733f0b707d489580ae8@109.238.12.65:27656,77791ee9b1eb56682335c451c296f450ee649c01@44.209.89.17:26656,98a03e1d03c1646e982b3379c0132d3828b0cacd@37.128.87.66:26656,c6cdcc7f8e1a33f864956a8201c304741411f219@3.214.163.125:26656,39794289e20cf80eba0a720eed58e7097e5686c1@136.243.103.53:46656,147a0021cff3c34251adb3ad7194574011fa3192@176.57.189.36:11656,ec843a4aea197837c13f13612a525bd7377443b1@167.235.250.107:26656,c26dc8486e8c4817e154812462993ce562cda221@65.108.231.124:32656,2d05753b4f5ac3bcd824afd96ea268d9c32ed84d@65.108.132.239:18656,b24974dd15a984f882438d907ee97c6baf1ae766@185.177.116.36:656,747d05bfe9f3e0c2e0462ac351c577699e1d9b8c@207.244.244.194:26656,25a43a4d1e9c0fd4aac087f24a79f2e296ac1c44@103.180.28.219:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656,78bc26c40c20715ca134b5d47a318a90dde95f12@78.46.61.117:04656,8f84d324a2d266e612d06db4a793b0d001ee62a0@38.146.3.200:20556,22acf9a303e825ce04171ef26e2326c09aeb238b@47.147.226.228:55656,7fc44e2651006fb2ddb4a56132e738da2845715f@65.108.6.45:61256,3a1e280b47ba71e11c2f1d800d0dd837cd40ed08@38.242.246.215:26656,488a1665d94f257733b04f7b4fbcef058cbb11cd@65.108.199.206:31656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
