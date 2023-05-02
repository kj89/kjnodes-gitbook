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
* grpc: dymension-testnet.grpc.kjnodes.com:14690

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@dymension-testnet.rpc.kjnodes.com:14656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@dymension-testnet.rpc.kjnodes.com:14659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/dymension-testnet/addrbook.json > $HOME/.dymension/config/addrbook.json
```

**live-peers** (28)
```bash
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.54:27086,708ff9955abd0e86b7873c1ec73311414bd1db24@217.21.53.106:26656,8eb8789ce687870a1c9b8ab7cc0f816c653ed56e@217.21.53.108:26656,3a1e280b47ba71e11c2f1d800d0dd837cd40ed08@38.242.246.215:26656,747d05bfe9f3e0c2e0462ac351c577699e1d9b8c@207.244.244.194:26656,30ce17a86b30b43b7e64c47f8249add57d2ec576@217.21.53.107:26656,0ee31ef97ba6b6c13b25b5c528163f2092821c2d@65.21.132.27:24856,4d2ec1e61d61550fc5bfacc57e971ff9b6181152@135.181.180.29:26656,146802c665668aa34647f55e2d97d682801bb40a@65.109.157.236:36656,a85420b25181bdb9b3a38741c48dafd5fb3b922f@209.34.205.57:26656,ba2ef45240cc997443df795b801a34602ba68b55@65.109.92.241:17886,17e37a96af64a81bf6ee144850fd24442f9d4ec6@109.123.249.192:26656,60f464943e6434579abdfa28a3122bd2d6008dec@139.99.68.119:26656,8b5367df2b1287174ce8950654953d81a7d69a29@144.76.201.43:26556,e46b42d50947795f681cf9bfd601ae806e7a8d49@188.34.178.190:46656,b24974dd15a984f882438d907ee97c6baf1ae766@185.177.116.36:656,b921655e6c66235915e7d4465ea2146e537f13e4@167.235.6.228:26636,c6cdcc7f8e1a33f864956a8201c304741411f219@3.214.163.125:26656,ca2cfea3c48640c094ad740bb41c2aeb81b5dcc6@194.163.187.175:46656,0d7ec1ea841e763267f197e2e0aa89467da24064@94.19.249.187:35656,c1008d2d05c56254e95d19ab7e9fe459dad2de3d@159.223.57.238:26656,1fa5bb085e8f52c21bc71c39afbba2851bee3e18@43.157.48.181:26656,965694b051742c2da0ea66502dd9bfeea38de265@198.244.228.235:26656,9e1ea4938f0112c1477827344e2f9d0792710575@185.252.232.189:30656,e891edc820240a032c89a2ae8f17e3d1d44ecaf9@15.204.31.186:26656,d4a66d01b1d109d842a7f1d51f541033c653ea03@116.202.227.117:46656,f433653cef597b3f0dd5f4e3e46c05fd121246bb@95.216.149.50:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
