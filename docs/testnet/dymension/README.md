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
peers="281190aa44ca82fb47afe60ba1a8902bae469b2a@88.99.164.158:17086,b1e1e5a9dbf2e03b456668c2f2d9164ae090ba0c@109.123.244.56:46656,62f5e5db360892ce0e8fc4cc5de7b880936e8410@82.208.23.204:04656,0ee31ef97ba6b6c13b25b5c528163f2092821c2d@65.21.132.27:24856,a85420b25181bdb9b3a38741c48dafd5fb3b922f@209.34.205.57:26656,ba2ef45240cc997443df795b801a34602ba68b55@65.109.92.241:17886,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656,3a1e280b47ba71e11c2f1d800d0dd837cd40ed08@38.242.246.215:26656,4d2ec1e61d61550fc5bfacc57e971ff9b6181152@135.181.180.29:26656,5dbbb68e0c8a86bdc372cf1de0691f1cdc6a96ad@82.208.23.223:27656,60f464943e6434579abdfa28a3122bd2d6008dec@139.99.68.119:26656,692189bd9936b767021d703b51d824e213cd9b92@89.252.21.37:60856,b24974dd15a984f882438d907ee97c6baf1ae766@185.177.116.36:656,98a03e1d03c1646e982b3379c0132d3828b0cacd@37.128.87.66:26656,8b5367df2b1287174ce8950654953d81a7d69a29@144.76.201.43:26556,0cc10d01b749a1e8b8d14c077140c776394d31e5@65.108.9.164:21456,1ed89bd1d280c4c6eb7d9134bb238d97fbb3f4b2@88.99.104.180:36656,acb69c31cac6140a1a9570e683de5e26dd008cff@51.222.44.116:32656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.54:27086,c6cdcc7f8e1a33f864956a8201c304741411f219@3.214.163.125:26656,8eb8789ce687870a1c9b8ab7cc0f816c653ed56e@217.21.53.108:26656,c1008d2d05c56254e95d19ab7e9fe459dad2de3d@159.223.57.238:26656,6204710a0d089566b6df85ae4aee595afdd23cbb@146.190.40.115:26656,917b34eb42fe8709700c7ee3afcfd5f8c72ddf32@31.220.75.4:26656,f433653cef597b3f0dd5f4e3e46c05fd121246bb@95.216.149.50:26656,43a46e2fbe871246e8fee045749d0a4677042b0c@95.217.216.88:46656,64acca240c1149f94b8986ffea3ee1b4e0bd5fbe@45.150.64.115:26656,3c937029e41e3f7b92b8b87d787be0ddc2a3f13c@70.34.214.236:26656,77791ee9b1eb56682335c451c296f450ee649c01@44.209.89.17:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
