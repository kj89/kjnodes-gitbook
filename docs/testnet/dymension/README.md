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

**live-peers** (29)
```bash
peers="8f84d324a2d266e612d06db4a793b0d001ee62a0@38.146.3.200:20556,747d05bfe9f3e0c2e0462ac351c577699e1d9b8c@207.244.244.194:26656,98a03e1d03c1646e982b3379c0132d3828b0cacd@37.128.87.66:26656,8b5367df2b1287174ce8950654953d81a7d69a29@144.76.201.43:26556,0cc10d01b749a1e8b8d14c077140c776394d31e5@65.108.9.164:21456,a85420b25181bdb9b3a38741c48dafd5fb3b922f@209.34.205.57:26656,4d2ec1e61d61550fc5bfacc57e971ff9b6181152@135.181.180.29:26656,60f464943e6434579abdfa28a3122bd2d6008dec@139.99.68.119:26656,ba2ef45240cc997443df795b801a34602ba68b55@65.109.92.241:17886,0ee31ef97ba6b6c13b25b5c528163f2092821c2d@65.21.132.27:24856,b24974dd15a984f882438d907ee97c6baf1ae766@185.177.116.36:656,f433653cef597b3f0dd5f4e3e46c05fd121246bb@95.216.149.50:26656,c6cdcc7f8e1a33f864956a8201c304741411f219@3.214.163.125:26656,acb69c31cac6140a1a9570e683de5e26dd008cff@51.222.44.116:32656,e678f78d3250fef1e6e0afcdb1ebdc5fe0d7138c@5.161.76.147:46656,b921655e6c66235915e7d4465ea2146e537f13e4@167.235.6.228:26636,5dbbb68e0c8a86bdc372cf1de0691f1cdc6a96ad@82.208.23.223:27656,43a46e2fbe871246e8fee045749d0a4677042b0c@95.217.216.88:46656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.54:27086,88e09de4c713ecb3497f39f6e6c599aea7a10750@65.109.38.111:20556,c17a4bcba59a0cbb10b91cd2cee0940c610d26ee@95.217.144.107:20556,d4a66d01b1d109d842a7f1d51f541033c653ea03@116.202.227.117:46656,ca2cfea3c48640c094ad740bb41c2aeb81b5dcc6@194.163.187.175:46656,94b63fddfc78230f51aeb7ac34b9fb86bd042a77@146.19.24.43:30585,3a1e280b47ba71e11c2f1d800d0dd837cd40ed08@38.242.246.215:26656,c36184fec2fb60bf7be775390c1cd6619c0201ef@209.126.81.240:26656,c26dc8486e8c4817e154812462993ce562cda221@65.108.231.124:32656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656,965694b051742c2da0ea66502dd9bfeea38de265@198.244.228.235:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
