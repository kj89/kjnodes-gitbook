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
peers="9e1ea4938f0112c1477827344e2f9d0792710575@185.252.232.189:30656,55f233c7c4bea21a47d266921ca5fce657f3adf7@168.119.240.200:26656,281190aa44ca82fb47afe60ba1a8902bae469b2a@88.99.164.158:17086,c6cdcc7f8e1a33f864956a8201c304741411f219@3.214.163.125:26656,a85420b25181bdb9b3a38741c48dafd5fb3b922f@209.34.205.57:26656,869d03182da215ae0171ac37ee69a77ed59d1a38@135.181.253.11:46656,708ff9955abd0e86b7873c1ec73311414bd1db24@217.21.53.106:26656,ba2ef45240cc997443df795b801a34602ba68b55@65.109.92.241:17886,454ce7fae2800bfbf53d73131e8d9ba3a384e8c4@43.248.96.60:26656,4d2ec1e61d61550fc5bfacc57e971ff9b6181152@135.181.180.29:26656,0ee31ef97ba6b6c13b25b5c528163f2092821c2d@65.21.132.27:24856,b24974dd15a984f882438d907ee97c6baf1ae766@185.177.116.36:656,8eb8789ce687870a1c9b8ab7cc0f816c653ed56e@217.21.53.108:26656,30ce17a86b30b43b7e64c47f8249add57d2ec576@217.21.53.107:26656,60f464943e6434579abdfa28a3122bd2d6008dec@139.99.68.119:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.54:27086,8b5367df2b1287174ce8950654953d81a7d69a29@144.76.201.43:26556,36d734269c8e69fd60e9050a7f47733b2e570d1c@89.117.57.201:11656,57a66a59cc291887f35e231b4469e2c957728862@46.4.5.45:20556,64acca240c1149f94b8986ffea3ee1b4e0bd5fbe@45.150.64.115:26656,17e37a96af64a81bf6ee144850fd24442f9d4ec6@109.123.249.192:26656,d2b841acdcabb622e9033fe685a395eef091f2fe@65.108.199.62:46656,be789ab36bc298b491735f2313d5f99abf452d1f@162.55.246.165:26656,22acf9a303e825ce04171ef26e2326c09aeb238b@47.147.226.228:55656,2afd537c6cca30a46393545a6aa69235d3fdb398@38.242.241.117:26656,1ed89bd1d280c4c6eb7d9134bb238d97fbb3f4b2@88.99.104.180:36656,b921655e6c66235915e7d4465ea2146e537f13e4@167.235.6.228:26636,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656,c26dc8486e8c4817e154812462993ce562cda221@65.108.231.124:32656,09927421cd3aa47bc81f8f981e15c547bc490121@5.9.83.110:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
