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
peers="c1008d2d05c56254e95d19ab7e9fe459dad2de3d@159.223.57.238:26656,1ed89bd1d280c4c6eb7d9134bb238d97fbb3f4b2@88.99.104.180:36656,8b5367df2b1287174ce8950654953d81a7d69a29@144.76.201.43:26556,9e1ea4938f0112c1477827344e2f9d0792710575@185.252.232.189:30656,708ff9955abd0e86b7873c1ec73311414bd1db24@217.21.53.106:26656,60f464943e6434579abdfa28a3122bd2d6008dec@139.99.68.119:26656,0cc10d01b749a1e8b8d14c077140c776394d31e5@65.108.9.164:21456,ba2ef45240cc997443df795b801a34602ba68b55@65.109.92.241:17886,a85420b25181bdb9b3a38741c48dafd5fb3b922f@209.34.205.57:26656,0ee31ef97ba6b6c13b25b5c528163f2092821c2d@65.21.132.27:24856,4d2ec1e61d61550fc5bfacc57e971ff9b6181152@135.181.180.29:26656,b24974dd15a984f882438d907ee97c6baf1ae766@185.177.116.36:656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.54:27086,30ce17a86b30b43b7e64c47f8249add57d2ec576@217.21.53.107:26656,c6cdcc7f8e1a33f864956a8201c304741411f219@3.214.163.125:26656,8eb8789ce687870a1c9b8ab7cc0f816c653ed56e@217.21.53.108:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656,57a66a59cc291887f35e231b4469e2c957728862@46.4.5.45:20556,d4a66d01b1d109d842a7f1d51f541033c653ea03@116.202.227.117:46656,b8d08951d68da03af8f9272bf77684811197c289@95.216.41.160:26656,36d734269c8e69fd60e9050a7f47733b2e570d1c@89.117.57.201:11656,af97c76448e6a5d7671c6523f38fc48cc7273da7@217.76.59.46:26656,17e37a96af64a81bf6ee144850fd24442f9d4ec6@109.123.249.192:26656,2dff9bc18d3717b733bddea2625470a019e86231@65.108.129.104:24656,5dbbb68e0c8a86bdc372cf1de0691f1cdc6a96ad@82.208.23.223:27656,affa469df41a5b58c23a7c8c1e11247d09c60452@108.175.1.130:26656,7f928378eecafe22fe1e93d9f63db181cec3f8a3@145.239.143.76:11256,0d30a0790a216d01c9759ab48192d9154381e6c0@136.243.88.91:3240,af6787b3273dd60e0f809c7e5e2a2a9fd379045e@195.201.195.61:27656,c26dc8486e8c4817e154812462993ce562cda221@65.108.231.124:32656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
