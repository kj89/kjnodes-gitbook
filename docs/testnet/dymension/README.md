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
peers="7fc44e2651006fb2ddb4a56132e738da2845715f@65.108.6.45:61256,877f82353e8cd6e2586ea37a6d16064eae081a74@192.95.30.128:31656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656,30ce17a86b30b43b7e64c47f8249add57d2ec576@217.21.53.107:26656,60f464943e6434579abdfa28a3122bd2d6008dec@139.99.68.119:26656,708ff9955abd0e86b7873c1ec73311414bd1db24@217.21.53.106:26656,a6b148f8419992dd2a1c4733f0b707d489580ae8@109.238.12.65:27656,6229800969107d039254a8e6888aaeb464cda44d@167.99.186.186:26656,b1e1e5a9dbf2e03b456668c2f2d9164ae090ba0c@109.123.244.56:46656,5a0cee849e4a909b42c8b9b2df4a1e737ff2b715@194.233.90.134:26656,0cc10d01b749a1e8b8d14c077140c776394d31e5@65.108.9.164:21456,0ee31ef97ba6b6c13b25b5c528163f2092821c2d@65.21.132.27:24856,a85420b25181bdb9b3a38741c48dafd5fb3b922f@209.34.205.57:26656,4d2ec1e61d61550fc5bfacc57e971ff9b6181152@135.181.180.29:26656,ba2ef45240cc997443df795b801a34602ba68b55@65.109.92.241:17886,b24974dd15a984f882438d907ee97c6baf1ae766@185.177.116.36:656,36d734269c8e69fd60e9050a7f47733b2e570d1c@89.117.57.201:11656,8eb8789ce687870a1c9b8ab7cc0f816c653ed56e@217.21.53.108:26656,22acf9a303e825ce04171ef26e2326c09aeb238b@47.147.226.228:55656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.54:27086,c6cdcc7f8e1a33f864956a8201c304741411f219@3.214.163.125:26656,11fe4c887e890c03cd109f61e8a80ecb77873013@134.209.184.190:26656,8b5367df2b1287174ce8950654953d81a7d69a29@144.76.201.43:26556,57a66a59cc291887f35e231b4469e2c957728862@46.4.5.45:20556,48ea1c8c62e9eb193a317096339b22f4a4452c8c@185.144.99.22:26656,0d30a0790a216d01c9759ab48192d9154381e6c0@136.243.88.91:3240,5dbbb68e0c8a86bdc372cf1de0691f1cdc6a96ad@82.208.23.223:27656,17e37a96af64a81bf6ee144850fd24442f9d4ec6@109.123.249.192:26656,e891edc820240a032c89a2ae8f17e3d1d44ecaf9@15.204.31.186:26656,72b721d31cba4935ecb2b2f7e7fec8a695f4b8d5@149.102.131.176:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
