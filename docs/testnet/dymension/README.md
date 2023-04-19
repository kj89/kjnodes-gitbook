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
peers="bb8615bb51139c05fd59020fc2aa7eac210690b4@135.181.221.186:27656,ee2fa87279bc626f9c979093389bd1d6568d96ff@65.109.37.228:36656,cb1cc6b4c48b3e311f18b606c663c2dc0fb89b75@74.96.207.62:26656,c1008d2d05c56254e95d19ab7e9fe459dad2de3d@159.223.57.238:26656,3a1e280b47ba71e11c2f1d800d0dd837cd40ed08@38.242.246.215:26656,8eb8789ce687870a1c9b8ab7cc0f816c653ed56e@217.21.53.108:26656,8b5367df2b1287174ce8950654953d81a7d69a29@144.76.201.43:26556,a85420b25181bdb9b3a38741c48dafd5fb3b922f@209.34.205.57:26656,0cc10d01b749a1e8b8d14c077140c776394d31e5@65.108.9.164:21456,62f5e5db360892ce0e8fc4cc5de7b880936e8410@82.208.23.204:04656,ba2ef45240cc997443df795b801a34602ba68b55@65.109.92.241:17886,60f464943e6434579abdfa28a3122bd2d6008dec@139.99.68.119:26656,0ee31ef97ba6b6c13b25b5c528163f2092821c2d@65.21.132.27:24856,4d2ec1e61d61550fc5bfacc57e971ff9b6181152@135.181.180.29:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.54:27086,4c25618c9465c0aaea91d936be446d5db04be3d1@195.201.237.185:46656,98a03e1d03c1646e982b3379c0132d3828b0cacd@37.128.87.66:26656,c6cdcc7f8e1a33f864956a8201c304741411f219@3.214.163.125:26656,b24974dd15a984f882438d907ee97c6baf1ae766@185.177.116.36:656,43a46e2fbe871246e8fee045749d0a4677042b0c@95.217.216.88:46656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656,5dbbb68e0c8a86bdc372cf1de0691f1cdc6a96ad@82.208.23.223:27656,7fc44e2651006fb2ddb4a56132e738da2845715f@65.108.6.45:61256,692189bd9936b767021d703b51d824e213cd9b92@89.252.21.37:60856,77791ee9b1eb56682335c451c296f450ee649c01@44.209.89.17:26656,5a0cee849e4a909b42c8b9b2df4a1e737ff2b715@194.233.90.134:26656,1cb9a04206e2f7a0b2524d4598072e2d275a0cbc@109.123.244.233:26656,88e09de4c713ecb3497f39f6e6c599aea7a10750@65.109.38.111:20556,64acca240c1149f94b8986ffea3ee1b4e0bd5fbe@45.150.64.115:26656,877f82353e8cd6e2586ea37a6d16064eae081a74@192.95.30.128:31656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
