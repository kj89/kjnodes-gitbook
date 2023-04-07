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
peers="e5226fa166386f9055908194a4942c06b7003ab5@65.108.192.123:42656,44df333024cebe9b8e8361ac67feaa930ec6dc1f@65.109.85.170:54656,f8175ce7bc19d015ec17083fe19b80eae2bd2a9c@65.21.239.60:46656,98a03e1d03c1646e982b3379c0132d3828b0cacd@37.128.87.66:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.54:27086,a85420b25181bdb9b3a38741c48dafd5fb3b922f@209.34.205.57:26656,236b71988898dff63cef139f83a64f5fbfd9d8d7@135.181.18.112:55696,4d2ec1e61d61550fc5bfacc57e971ff9b6181152@135.181.180.29:26656,48ea1c8c62e9eb193a317096339b22f4a4452c8c@185.144.99.22:26656,8e667c0759bfb20ec42b939956706301a4f2a10d@65.109.92.8:26656,0ee31ef97ba6b6c13b25b5c528163f2092821c2d@65.21.132.27:24856,ba2ef45240cc997443df795b801a34602ba68b55@65.109.92.241:17886,b24974dd15a984f882438d907ee97c6baf1ae766@185.177.116.36:656,8b5367df2b1287174ce8950654953d81a7d69a29@144.76.201.43:26556,60f464943e6434579abdfa28a3122bd2d6008dec@139.99.68.119:26656,f9d5e36ecc66b48f9fb940a778dd0c3b6b7c3d1d@65.109.106.211:26656,1ed89bd1d280c4c6eb7d9134bb238d97fbb3f4b2@88.99.104.180:36656,88e09de4c713ecb3497f39f6e6c599aea7a10750@65.109.38.111:20556,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656,af6787b3273dd60e0f809c7e5e2a2a9fd379045e@195.201.195.61:27656,f433653cef597b3f0dd5f4e3e46c05fd121246bb@95.216.149.50:26656,a6b148f8419992dd2a1c4733f0b707d489580ae8@109.238.12.65:27656,0996622e0d51b51cdfb2e8bed752968693f87e10@109.205.180.254:26656,c6cdcc7f8e1a33f864956a8201c304741411f219@3.214.163.125:26656,747d05bfe9f3e0c2e0462ac351c577699e1d9b8c@207.244.244.194:26656,77791ee9b1eb56682335c451c296f450ee649c01@44.209.89.17:26656,7c720f2d079174ed7ce478b026ac3906a630d716@167.99.178.186:26656,6229800969107d039254a8e6888aaeb464cda44d@167.99.186.186:26656,5d689e09a129c03c003f05850262f03b2433a384@51.79.30.141:26656,281190aa44ca82fb47afe60ba1a8902bae469b2a@88.99.164.158:17086"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
