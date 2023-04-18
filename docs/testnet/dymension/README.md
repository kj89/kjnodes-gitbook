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
peers="f433653cef597b3f0dd5f4e3e46c05fd121246bb@95.216.149.50:26656,0ee31ef97ba6b6c13b25b5c528163f2092821c2d@65.21.132.27:24856,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656,43a46e2fbe871246e8fee045749d0a4677042b0c@95.217.216.88:46656,4d2ec1e61d61550fc5bfacc57e971ff9b6181152@135.181.180.29:26656,a85420b25181bdb9b3a38741c48dafd5fb3b922f@209.34.205.57:26656,62f5e5db360892ce0e8fc4cc5de7b880936e8410@82.208.23.204:04656,ba2ef45240cc997443df795b801a34602ba68b55@65.109.92.241:17886,8eb8789ce687870a1c9b8ab7cc0f816c653ed56e@217.21.53.108:26656,d2b841acdcabb622e9033fe685a395eef091f2fe@65.108.199.62:46656,5d689e09a129c03c003f05850262f03b2433a384@51.79.30.141:26656,8b5367df2b1287174ce8950654953d81a7d69a29@144.76.201.43:26556,b24974dd15a984f882438d907ee97c6baf1ae766@185.177.116.36:656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.54:27086,c6cdcc7f8e1a33f864956a8201c304741411f219@3.214.163.125:26656,98a03e1d03c1646e982b3379c0132d3828b0cacd@37.128.87.66:26656,747d05bfe9f3e0c2e0462ac351c577699e1d9b8c@207.244.244.194:26656,0cc10d01b749a1e8b8d14c077140c776394d31e5@65.108.9.164:21456,09927421cd3aa47bc81f8f981e15c547bc490121@5.9.83.110:26656,e891edc820240a032c89a2ae8f17e3d1d44ecaf9@15.204.31.186:26656,88e09de4c713ecb3497f39f6e6c599aea7a10750@65.109.38.111:20556,7fc44e2651006fb2ddb4a56132e738da2845715f@65.108.6.45:61256,db0264c412618949ce3a63cb07328d027e433372@146.19.24.101:26646,965694b051742c2da0ea66502dd9bfeea38de265@198.244.228.235:26656,bb8615bb51139c05fd59020fc2aa7eac210690b4@135.181.221.186:27656,692189bd9936b767021d703b51d824e213cd9b92@89.252.21.37:60856,60f464943e6434579abdfa28a3122bd2d6008dec@139.99.68.119:26656,6011e62596d177073f3bed476622162652ab4310@164.68.105.143:26656,c26dc8486e8c4817e154812462993ce562cda221@65.108.231.124:32656,c5db84267f7dce8fa249b0d5365d59a7abeb0164@95.217.211.32:46656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
