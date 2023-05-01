# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/dymension.png" alt=""><figcaption></figcaption></figure>

Dymension is a network of modular blockchains called RollApps  and at the center of it all is the Dymension Hub. Dymension  allows anyone to build and deploy their own consensus-free blockchain, a RollApp.

**Chain ID**: 35-C | **Latest Version Tag**: v0.2.0-beta | **Wasm**: OFF

[Website](https://dymension.xyz/) | [Discord](https://discord.gg/dymension) | [Twitter](https://twitter.com/dymensionXYZ)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/dymension-testnet](https://explorer.kjnodes.com/dymension-testnet)

## Public endpoints

* api: [https://dymension-testnet.api.kjnodes.com](https://dymension-testnet.api.kjnodes.com)
* rpc: [https://dymension-testnet.rpc.kjnodes.com](https://dymension-testnet.rpc.kjnodes.com)
* grpc: dymension-testnet.grpc.kjnodes.com:14690

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@dymension-testnet.rpc.kjnodes.com:14656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@dymension-testnet.rpc.kjnodes.com:14659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/dymension-testnet/addrbook.json > $HOME/.dymension/config/addrbook.json
```

**live-peers** (28)
```bash
peers="e46b42d50947795f681cf9bfd601ae806e7a8d49@188.34.178.190:46656,547cf669555bd611ba57b37bb0f288793ea4ec49@141.94.138.48:26673,80cce834fc749c0a9f47182665f833f97170ff4b@65.108.104.167:46656,3a1e280b47ba71e11c2f1d800d0dd837cd40ed08@38.242.246.215:26656,8b5367df2b1287174ce8950654953d81a7d69a29@144.76.201.43:26556,0ee31ef97ba6b6c13b25b5c528163f2092821c2d@65.21.132.27:24856,a85420b25181bdb9b3a38741c48dafd5fb3b922f@209.34.205.57:26656,4d2ec1e61d61550fc5bfacc57e971ff9b6181152@135.181.180.29:26656,146802c665668aa34647f55e2d97d682801bb40a@65.109.157.236:36656,ba2ef45240cc997443df795b801a34602ba68b55@65.109.92.241:17886,60f464943e6434579abdfa28a3122bd2d6008dec@139.99.68.119:26656,8eb8789ce687870a1c9b8ab7cc0f816c653ed56e@217.21.53.108:26656,30ce17a86b30b43b7e64c47f8249add57d2ec576@217.21.53.107:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.54:27086,708ff9955abd0e86b7873c1ec73311414bd1db24@217.21.53.106:26656,b24974dd15a984f882438d907ee97c6baf1ae766@185.177.116.36:656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656,17e37a96af64a81bf6ee144850fd24442f9d4ec6@109.123.249.192:26656,c6cdcc7f8e1a33f864956a8201c304741411f219@3.214.163.125:26656,1ed89bd1d280c4c6eb7d9134bb238d97fbb3f4b2@88.99.104.180:36656,57a66a59cc291887f35e231b4469e2c957728862@46.4.5.45:20556,c26dc8486e8c4817e154812462993ce562cda221@65.108.231.124:32656,af6787b3273dd60e0f809c7e5e2a2a9fd379045e@195.201.195.61:27656,e38aa6816fe5a0ac5acaa5f525d9ef7dc90905d1@194.126.173.150:29656,55f233c7c4bea21a47d266921ca5fce657f3adf7@168.119.240.200:26656,ee2fa87279bc626f9c979093389bd1d6568d96ff@65.109.37.228:36656,1c8386da0d839e71c217ee3a5e041983702db583@135.181.143.16:26656,281190aa44ca82fb47afe60ba1a8902bae469b2a@88.99.164.158:17086"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
