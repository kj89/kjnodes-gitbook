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
* grpc: dymension-testnet.grpc.kjnodes.com:146090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@dymension-testnet.rpc.kjnodes.com:146656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@dymension-testnet.rpc.kjnodes.com:146659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/dymension-testnet/addrbook.json > $HOME/.dymension/config/addrbook.json
```

**live-peers** (29)
```bash
peers="869d03182da215ae0171ac37ee69a77ed59d1a38@135.181.253.11:46656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656,8eb8789ce687870a1c9b8ab7cc0f816c653ed56e@217.21.53.108:26656,60f464943e6434579abdfa28a3122bd2d6008dec@139.99.68.119:26656,b24974dd15a984f882438d907ee97c6baf1ae766@185.177.116.36:656,708ff9955abd0e86b7873c1ec73311414bd1db24@217.21.53.106:26656,3a1e280b47ba71e11c2f1d800d0dd837cd40ed08@38.242.246.215:26656,1ed89bd1d280c4c6eb7d9134bb238d97fbb3f4b2@88.99.104.180:36656,ba2ef45240cc997443df795b801a34602ba68b55@65.109.92.241:17886,4d2ec1e61d61550fc5bfacc57e971ff9b6181152@135.181.180.29:26656,146802c665668aa34647f55e2d97d682801bb40a@65.109.157.236:36656,0ee31ef97ba6b6c13b25b5c528163f2092821c2d@65.21.132.27:24856,a85420b25181bdb9b3a38741c48dafd5fb3b922f@209.34.205.57:26656,c1008d2d05c56254e95d19ab7e9fe459dad2de3d@159.223.57.238:26656,57a66a59cc291887f35e231b4469e2c957728862@46.4.5.45:20556,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.54:27086,8b5367df2b1287174ce8950654953d81a7d69a29@144.76.201.43:26556,30ce17a86b30b43b7e64c47f8249add57d2ec576@217.21.53.107:26656,c6cdcc7f8e1a33f864956a8201c304741411f219@3.214.163.125:26656,17e37a96af64a81bf6ee144850fd24442f9d4ec6@109.123.249.192:26656,e5226fa166386f9055908194a4942c06b7003ab5@65.108.192.123:42656,998b19ed2c580acaa2fdb5057e2930a38f041750@65.109.122.105:60556,5a0cee849e4a909b42c8b9b2df4a1e737ff2b715@194.233.90.134:26656,c17a4bcba59a0cbb10b91cd2cee0940c610d26ee@95.217.144.107:20556,965694b051742c2da0ea66502dd9bfeea38de265@198.244.228.235:26656,1c8386da0d839e71c217ee3a5e041983702db583@135.181.143.16:26656,4c23a702f7ba893cb6dc73e2e2c500aa22909dee@159.65.82.47:32656,c26dc8486e8c4817e154812462993ce562cda221@65.108.231.124:32656,e46b42d50947795f681cf9bfd601ae806e7a8d49@188.34.178.190:46656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
