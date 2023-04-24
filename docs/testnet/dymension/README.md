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
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656,8b5367df2b1287174ce8950654953d81a7d69a29@144.76.201.43:26556,4c25618c9465c0aaea91d936be446d5db04be3d1@195.201.237.185:46656,30ce17a86b30b43b7e64c47f8249add57d2ec576@217.21.53.107:26656,0cc10d01b749a1e8b8d14c077140c776394d31e5@65.108.9.164:21456,a85420b25181bdb9b3a38741c48dafd5fb3b922f@209.34.205.57:26656,0ee31ef97ba6b6c13b25b5c528163f2092821c2d@65.21.132.27:24856,ba2ef45240cc997443df795b801a34602ba68b55@65.109.92.241:17886,4d2ec1e61d61550fc5bfacc57e971ff9b6181152@135.181.180.29:26656,c6cdcc7f8e1a33f864956a8201c304741411f219@3.214.163.125:26656,a6b148f8419992dd2a1c4733f0b707d489580ae8@109.238.12.65:27656,8eb8789ce687870a1c9b8ab7cc0f816c653ed56e@217.21.53.108:26656,b24974dd15a984f882438d907ee97c6baf1ae766@185.177.116.36:656,877f82353e8cd6e2586ea37a6d16064eae081a74@192.95.30.128:31656,36d734269c8e69fd60e9050a7f47733b2e570d1c@89.117.57.201:11656,57a66a59cc291887f35e231b4469e2c957728862@46.4.5.45:20556,6ee2e6550cd3510c0fc912bf0632a894148a79a7@38.242.202.174:31656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.54:27086,708ff9955abd0e86b7873c1ec73311414bd1db24@217.21.53.106:26656,60f464943e6434579abdfa28a3122bd2d6008dec@139.99.68.119:26656,5dbbb68e0c8a86bdc372cf1de0691f1cdc6a96ad@82.208.23.223:27656,5a0cee849e4a909b42c8b9b2df4a1e737ff2b715@194.233.90.134:26656,7fc44e2651006fb2ddb4a56132e738da2845715f@65.108.6.45:61256,c1008d2d05c56254e95d19ab7e9fe459dad2de3d@159.223.57.238:26656,c36184fec2fb60bf7be775390c1cd6619c0201ef@209.126.81.240:26656,0d30a0790a216d01c9759ab48192d9154381e6c0@136.243.88.91:3240,cb1cc6b4c48b3e311f18b606c663c2dc0fb89b75@74.96.207.62:26656,c26dc8486e8c4817e154812462993ce562cda221@65.108.231.124:32656,6229800969107d039254a8e6888aaeb464cda44d@167.99.186.186:26656,281190aa44ca82fb47afe60ba1a8902bae469b2a@88.99.164.158:17086"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
