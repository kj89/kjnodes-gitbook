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
peers="6011e62596d177073f3bed476622162652ab4310@164.68.105.143:26656,17e37a96af64a81bf6ee144850fd24442f9d4ec6@109.123.249.192:26656,8d5eac1042bac34cddd25d7601789fc03cb3f3a9@168.119.213.113:46656,b24974dd15a984f882438d907ee97c6baf1ae766@185.177.116.36:656,9e1ea4938f0112c1477827344e2f9d0792710575@185.252.232.189:30656,30ce17a86b30b43b7e64c47f8249add57d2ec576@217.21.53.107:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.54:27086,ba2ef45240cc997443df795b801a34602ba68b55@65.109.92.241:17886,a85420b25181bdb9b3a38741c48dafd5fb3b922f@209.34.205.57:26656,4d2ec1e61d61550fc5bfacc57e971ff9b6181152@135.181.180.29:26656,0ee31ef97ba6b6c13b25b5c528163f2092821c2d@65.21.132.27:24856,5d689e09a129c03c003f05850262f03b2433a384@51.79.30.141:26656,8eb8789ce687870a1c9b8ab7cc0f816c653ed56e@217.21.53.108:26656,5dbbb68e0c8a86bdc372cf1de0691f1cdc6a96ad@82.208.23.223:27656,8b5367df2b1287174ce8950654953d81a7d69a29@144.76.201.43:26556,ee2fa87279bc626f9c979093389bd1d6568d96ff@65.109.37.228:36656,708ff9955abd0e86b7873c1ec73311414bd1db24@217.21.53.106:26656,60f464943e6434579abdfa28a3122bd2d6008dec@139.99.68.119:26656,c6cdcc7f8e1a33f864956a8201c304741411f219@3.214.163.125:26656,3a1e280b47ba71e11c2f1d800d0dd837cd40ed08@38.242.246.215:26656,d2b841acdcabb622e9033fe685a395eef091f2fe@65.108.199.62:46656,22acf9a303e825ce04171ef26e2326c09aeb238b@47.147.226.228:55656,57a66a59cc291887f35e231b4469e2c957728862@46.4.5.45:20556,8e667c0759bfb20ec42b939956706301a4f2a10d@65.109.92.8:26656,c1008d2d05c56254e95d19ab7e9fe459dad2de3d@159.223.57.238:26656,62f5e5db360892ce0e8fc4cc5de7b880936e8410@82.208.23.204:04656,c26dc8486e8c4817e154812462993ce562cda221@65.108.231.124:32656,49d3bb4cc4913f928053513b9eb799be8ea33666@65.109.82.112:26656,fbc47b8193fba23bd6fcd79accfad38c20d74904@154.12.230.223:26656,281190aa44ca82fb47afe60ba1a8902bae469b2a@88.99.164.158:17086"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
