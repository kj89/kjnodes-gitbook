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
peers="c36184fec2fb60bf7be775390c1cd6619c0201ef@209.126.81.240:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.54:27086,8b5367df2b1287174ce8950654953d81a7d69a29@144.76.201.43:26556,60f464943e6434579abdfa28a3122bd2d6008dec@139.99.68.119:26656,a85420b25181bdb9b3a38741c48dafd5fb3b922f@209.34.205.57:26656,4d2ec1e61d61550fc5bfacc57e971ff9b6181152@135.181.180.29:26656,0ee31ef97ba6b6c13b25b5c528163f2092821c2d@65.21.132.27:24856,0cc10d01b749a1e8b8d14c077140c776394d31e5@65.108.9.164:21456,62f5e5db360892ce0e8fc4cc5de7b880936e8410@82.208.23.204:04656,ba2ef45240cc997443df795b801a34602ba68b55@65.109.92.241:17886,c1008d2d05c56254e95d19ab7e9fe459dad2de3d@159.223.57.238:26656,b24974dd15a984f882438d907ee97c6baf1ae766@185.177.116.36:656,30ce17a86b30b43b7e64c47f8249add57d2ec576@217.21.53.107:26656,c6cdcc7f8e1a33f864956a8201c304741411f219@3.214.163.125:26656,708ff9955abd0e86b7873c1ec73311414bd1db24@217.21.53.106:26656,998b19ed2c580acaa2fdb5057e2930a38f041750@65.109.122.105:60556,5dbbb68e0c8a86bdc372cf1de0691f1cdc6a96ad@82.208.23.223:27656,8eb8789ce687870a1c9b8ab7cc0f816c653ed56e@217.21.53.108:26656,547cf669555bd611ba57b37bb0f288793ea4ec49@141.94.138.48:26673,ec843a4aea197837c13f13612a525bd7377443b1@167.235.250.107:26656,a6b148f8419992dd2a1c4733f0b707d489580ae8@109.238.12.65:27656,488a1665d94f257733b04f7b4fbcef058cbb11cd@65.108.199.206:31656,7f645435ae8ed3287fd0a099d29b7637ed7f8b67@65.109.116.110:26656,b921655e6c66235915e7d4465ea2146e537f13e4@167.235.6.228:26636,44df333024cebe9b8e8361ac67feaa930ec6dc1f@65.109.85.170:54656,6204710a0d089566b6df85ae4aee595afdd23cbb@146.190.40.115:26656,55f233c7c4bea21a47d266921ca5fce657f3adf7@168.119.240.200:26656,b8d08951d68da03af8f9272bf77684811197c289@95.216.41.160:26656,22acf9a303e825ce04171ef26e2326c09aeb238b@47.147.226.228:55656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
