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
peers="fe02e0280c6aedfeaea6f0d8e828dbc53f34e69a@91.107.232.129:26656,f433653cef597b3f0dd5f4e3e46c05fd121246bb@95.216.149.50:26656,0996622e0d51b51cdfb2e8bed752968693f87e10@109.205.180.254:26656,e678f78d3250fef1e6e0afcdb1ebdc5fe0d7138c@5.161.76.147:46656,a85420b25181bdb9b3a38741c48dafd5fb3b922f@209.34.205.57:26656,98a03e1d03c1646e982b3379c0132d3828b0cacd@185.70.181.103:26656,ba2ef45240cc997443df795b801a34602ba68b55@65.109.92.241:17886,7fc44e2651006fb2ddb4a56132e738da2845715f@65.108.6.45:61256,0ee31ef97ba6b6c13b25b5c528163f2092821c2d@65.21.132.27:24856,4d2ec1e61d61550fc5bfacc57e971ff9b6181152@135.181.180.29:26656,b24974dd15a984f882438d907ee97c6baf1ae766@185.177.116.36:656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656,7c720f2d079174ed7ce478b026ac3906a630d716@167.99.178.186:26656,1a5b4c236f922a320eda3b86a661b6c8793d5df3@161.97.145.250:26656,88e09de4c713ecb3497f39f6e6c599aea7a10750@65.109.38.111:20556,a6b148f8419992dd2a1c4733f0b707d489580ae8@109.238.12.65:27656,60f464943e6434579abdfa28a3122bd2d6008dec@139.99.68.119:26656,2d05753b4f5ac3bcd824afd96ea268d9c32ed84d@65.108.132.239:18656,c6cdcc7f8e1a33f864956a8201c304741411f219@3.214.163.125:26656,8e0c3fc76a3c7510d28fff02d452ccf952450ca9@89.117.48.191:26656,5dbbb68e0c8a86bdc372cf1de0691f1cdc6a96ad@82.208.23.223:27656,d189f9eaf48a551c4ae2ddc47e5c8ab757dac3f5@65.109.94.10:26656,8b5367df2b1287174ce8950654953d81a7d69a29@144.76.201.43:26556,4e2984edd9da237b189d51a49f36dfb03b2d23f1@65.108.105.48:20556,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.54:27086,8f84d324a2d266e612d06db4a793b0d001ee62a0@38.146.3.200:20556,e6ea3444ac85302c336000ac036f4d86b97b3d3e@38.146.3.199:20556,77791ee9b1eb56682335c451c296f450ee649c01@44.209.89.17:26656,acb69c31cac6140a1a9570e683de5e26dd008cff@51.222.44.116:32656,c26dc8486e8c4817e154812462993ce562cda221@65.108.231.124:32656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
