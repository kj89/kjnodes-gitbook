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
peers="b921655e6c66235915e7d4465ea2146e537f13e4@167.235.6.228:26636,9e1ea4938f0112c1477827344e2f9d0792710575@185.252.232.189:30656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656,8b5367df2b1287174ce8950654953d81a7d69a29@144.76.201.43:26556,c6cdcc7f8e1a33f864956a8201c304741411f219@3.214.163.125:26656,b24974dd15a984f882438d907ee97c6baf1ae766@185.177.116.36:656,55f233c7c4bea21a47d266921ca5fce657f3adf7@168.119.240.200:26656,3a1e280b47ba71e11c2f1d800d0dd837cd40ed08@38.242.246.215:26656,a85420b25181bdb9b3a38741c48dafd5fb3b922f@209.34.205.57:26656,ba2ef45240cc997443df795b801a34602ba68b55@65.109.92.241:17886,0ee31ef97ba6b6c13b25b5c528163f2092821c2d@65.21.132.27:24856,62f5e5db360892ce0e8fc4cc5de7b880936e8410@82.208.23.204:04656,4d2ec1e61d61550fc5bfacc57e971ff9b6181152@135.181.180.29:26656,8eb8789ce687870a1c9b8ab7cc0f816c653ed56e@217.21.53.108:26656,236b71988898dff63cef139f83a64f5fbfd9d8d7@135.181.18.112:55696,708ff9955abd0e86b7873c1ec73311414bd1db24@217.21.53.106:26656,60f464943e6434579abdfa28a3122bd2d6008dec@139.99.68.119:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.54:27086,0cc10d01b749a1e8b8d14c077140c776394d31e5@65.108.9.164:21456,30ce17a86b30b43b7e64c47f8249add57d2ec576@217.21.53.107:26656,1ed89bd1d280c4c6eb7d9134bb238d97fbb3f4b2@88.99.104.180:36656,96ffe4b68c3f97cbeae4b4362634bf1054c7aeeb@142.132.151.99:15658,0d30a0790a216d01c9759ab48192d9154381e6c0@136.243.88.91:3240,5a0cee849e4a909b42c8b9b2df4a1e737ff2b715@194.233.90.134:26656,cb1cc6b4c48b3e311f18b606c663c2dc0fb89b75@74.96.207.62:26656,47921c153041fb2f048c1e174b6d02ac0efab7a9@38.242.207.16:26656,877f82353e8cd6e2586ea37a6d16064eae081a74@192.95.30.128:31656,c26dc8486e8c4817e154812462993ce562cda221@65.108.231.124:32656,98a03e1d03c1646e982b3379c0132d3828b0cacd@37.128.87.66:26656,2afd537c6cca30a46393545a6aa69235d3fdb398@38.242.241.117:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
