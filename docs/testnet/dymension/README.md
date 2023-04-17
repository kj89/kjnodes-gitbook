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
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.54:27086,98a03e1d03c1646e982b3379c0132d3828b0cacd@37.128.87.66:26656,62f5e5db360892ce0e8fc4cc5de7b880936e8410@82.208.23.204:04656,0cc10d01b749a1e8b8d14c077140c776394d31e5@65.108.9.164:21456,4d2ec1e61d61550fc5bfacc57e971ff9b6181152@135.181.180.29:26656,a85420b25181bdb9b3a38741c48dafd5fb3b922f@209.34.205.57:26656,0ee31ef97ba6b6c13b25b5c528163f2092821c2d@65.21.132.27:24856,c6cdcc7f8e1a33f864956a8201c304741411f219@3.214.163.125:26656,8b5367df2b1287174ce8950654953d81a7d69a29@144.76.201.43:26556,60f464943e6434579abdfa28a3122bd2d6008dec@139.99.68.119:26656,55f233c7c4bea21a47d266921ca5fce657f3adf7@168.119.240.200:26656,48ea1c8c62e9eb193a317096339b22f4a4452c8c@185.144.99.22:26656,0d30a0790a216d01c9759ab48192d9154381e6c0@136.243.88.91:3240,ba2ef45240cc997443df795b801a34602ba68b55@65.109.92.241:17886,43a46e2fbe871246e8fee045749d0a4677042b0c@95.217.216.88:46656,88e09de4c713ecb3497f39f6e6c599aea7a10750@65.109.38.111:20556,b24974dd15a984f882438d907ee97c6baf1ae766@185.177.116.36:656,63996f52b1dc68259ff64bb2546625c71fc9d546@176.9.48.38:26656,77791ee9b1eb56682335c451c296f450ee649c01@44.209.89.17:26656,c26dc8486e8c4817e154812462993ce562cda221@65.108.231.124:32656,747d05bfe9f3e0c2e0462ac351c577699e1d9b8c@207.244.244.194:26656,965694b051742c2da0ea66502dd9bfeea38de265@198.244.228.235:26656,af6787b3273dd60e0f809c7e5e2a2a9fd379045e@195.201.195.61:27656,692189bd9936b767021d703b51d824e213cd9b92@89.252.21.37:60856,5dbbb68e0c8a86bdc372cf1de0691f1cdc6a96ad@82.208.23.223:27656,281190aa44ca82fb47afe60ba1a8902bae469b2a@88.99.164.158:17086,e891edc820240a032c89a2ae8f17e3d1d44ecaf9@15.204.31.186:26656,b921655e6c66235915e7d4465ea2146e537f13e4@167.235.6.228:26636,6011e62596d177073f3bed476622162652ab4310@164.68.105.143:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
