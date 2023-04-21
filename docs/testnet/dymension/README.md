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
peers="77791ee9b1eb56682335c451c296f450ee649c01@44.209.89.17:26656,11fe4c887e890c03cd109f61e8a80ecb77873013@134.209.184.190:26656,9e1ea4938f0112c1477827344e2f9d0792710575@185.252.232.189:30656,62f5e5db360892ce0e8fc4cc5de7b880936e8410@82.208.23.204:04656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.54:27086,60f464943e6434579abdfa28a3122bd2d6008dec@139.99.68.119:26656,f433653cef597b3f0dd5f4e3e46c05fd121246bb@95.216.149.50:26656,cb1cc6b4c48b3e311f18b606c663c2dc0fb89b75@74.96.207.62:26656,8eb8789ce687870a1c9b8ab7cc0f816c653ed56e@217.21.53.108:26656,b24974dd15a984f882438d907ee97c6baf1ae766@185.177.116.36:656,a85420b25181bdb9b3a38741c48dafd5fb3b922f@209.34.205.57:26656,ba2ef45240cc997443df795b801a34602ba68b55@65.109.92.241:17886,4d2ec1e61d61550fc5bfacc57e971ff9b6181152@135.181.180.29:26656,0ee31ef97ba6b6c13b25b5c528163f2092821c2d@65.21.132.27:24856,0cc10d01b749a1e8b8d14c077140c776394d31e5@65.108.9.164:21456,5dbbb68e0c8a86bdc372cf1de0691f1cdc6a96ad@82.208.23.223:27656,47921c153041fb2f048c1e174b6d02ac0efab7a9@38.242.207.16:26656,c6cdcc7f8e1a33f864956a8201c304741411f219@3.214.163.125:26656,30ce17a86b30b43b7e64c47f8249add57d2ec576@217.21.53.107:26656,8b5367df2b1287174ce8950654953d81a7d69a29@144.76.201.43:26556,98a03e1d03c1646e982b3379c0132d3828b0cacd@37.128.87.66:26656,617214edc6dbd3d82765d66767ca56deb9660851@134.209.21.58:26656,708ff9955abd0e86b7873c1ec73311414bd1db24@217.21.53.106:26656,b8d08951d68da03af8f9272bf77684811197c289@95.216.41.160:26656,7fc44e2651006fb2ddb4a56132e738da2845715f@65.108.6.45:61256,55f233c7c4bea21a47d266921ca5fce657f3adf7@168.119.240.200:26656,e02df942761178c2896fffde327f41c6cb0d2c4d@64.227.125.163:46656,43a46e2fbe871246e8fee045749d0a4677042b0c@95.217.216.88:46656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656,3a1e280b47ba71e11c2f1d800d0dd837cd40ed08@38.242.246.215:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
