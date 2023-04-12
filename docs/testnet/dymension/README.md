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
peers="d4a66d01b1d109d842a7f1d51f541033c653ea03@116.202.227.117:46656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.54:27086,7c720f2d079174ed7ce478b026ac3906a630d716@167.99.178.186:26656,a85420b25181bdb9b3a38741c48dafd5fb3b922f@209.34.205.57:26656,8b5367df2b1287174ce8950654953d81a7d69a29@144.76.201.43:26556,ba2ef45240cc997443df795b801a34602ba68b55@65.109.92.241:17886,0ee31ef97ba6b6c13b25b5c528163f2092821c2d@65.21.132.27:24856,4d2ec1e61d61550fc5bfacc57e971ff9b6181152@135.181.180.29:26656,c26dc8486e8c4817e154812462993ce562cda221@65.108.231.124:32656,e46b42d50947795f681cf9bfd601ae806e7a8d49@188.34.178.190:46656,3a1e280b47ba71e11c2f1d800d0dd837cd40ed08@38.242.246.215:26656,88e09de4c713ecb3497f39f6e6c599aea7a10750@65.109.38.111:20556,60f464943e6434579abdfa28a3122bd2d6008dec@139.99.68.119:26656,0cc10d01b749a1e8b8d14c077140c776394d31e5@65.108.9.164:21456,98a03e1d03c1646e982b3379c0132d3828b0cacd@37.128.87.66:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656,c6cdcc7f8e1a33f864956a8201c304741411f219@3.214.163.125:26656,b24974dd15a984f882438d907ee97c6baf1ae766@185.177.116.36:656,a6b148f8419992dd2a1c4733f0b707d489580ae8@109.238.12.65:27656,d2b841acdcabb622e9033fe685a395eef091f2fe@65.108.199.62:46656,ee2fa87279bc626f9c979093389bd1d6568d96ff@65.109.37.228:36656,3a8bb83d5c5afb13ae2c1c3b91c97928e277f6a5@142.132.205.94:15658,1ed89bd1d280c4c6eb7d9134bb238d97fbb3f4b2@88.99.104.180:36656,43a46e2fbe871246e8fee045749d0a4677042b0c@95.217.216.88:46656,77791ee9b1eb56682335c451c296f450ee649c01@44.209.89.17:26656,22acf9a303e825ce04171ef26e2326c09aeb238b@47.147.226.228:55656,965694b051742c2da0ea66502dd9bfeea38de265@198.244.228.235:26656,b8d08951d68da03af8f9272bf77684811197c289@95.216.41.160:26656,e6ea3444ac85302c336000ac036f4d86b97b3d3e@38.146.3.199:20556,1cb9a04206e2f7a0b2524d4598072e2d275a0cbc@109.123.244.233:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
