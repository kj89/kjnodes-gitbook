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
peers="54160abe97cd71abb3a83516fd8e4a47cb509fba@188.34.178.103:46656,eb524a9ed0e080ec4fa9a21df3f5f56e94e0e811@51.89.7.235:26652,e891edc820240a032c89a2ae8f17e3d1d44ecaf9@15.204.31.186:26656,dddc76ca6279ac90b12cf35b39c46a2fc2c2ce52@5.161.78.48:46656,39794289e20cf80eba0a720eed58e7097e5686c1@136.243.103.53:46656,c6cdcc7f8e1a33f864956a8201c304741411f219@3.214.163.125:26656,88e09de4c713ecb3497f39f6e6c599aea7a10750@65.109.38.111:20556,5dbbb68e0c8a86bdc372cf1de0691f1cdc6a96ad@82.208.23.223:27656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.54:27086,747d05bfe9f3e0c2e0462ac351c577699e1d9b8c@207.244.244.194:26656,a6b148f8419992dd2a1c4733f0b707d489580ae8@109.238.12.65:27656,f8f5bd34b9ee737646758120685d96656adcd2d8@18.207.225.212:26656,a85420b25181bdb9b3a38741c48dafd5fb3b922f@209.34.205.57:26656,877f82353e8cd6e2586ea37a6d16064eae081a74@192.95.30.128:31656,e6ea3444ac85302c336000ac036f4d86b97b3d3e@38.146.3.199:20556,0ee31ef97ba6b6c13b25b5c528163f2092821c2d@65.21.132.27:24856,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656,1a5b4c236f922a320eda3b86a661b6c8793d5df3@161.97.145.250:26656,4d2ec1e61d61550fc5bfacc57e971ff9b6181152@135.181.180.29:26656,98a03e1d03c1646e982b3379c0132d3828b0cacd@37.128.87.66:26656,b24974dd15a984f882438d907ee97c6baf1ae766@185.177.116.36:656,60f464943e6434579abdfa28a3122bd2d6008dec@139.99.68.119:26656,e8a706e3a81a36a6dded6cc02eabaf5d355f4c1d@80.79.5.171:28656,4c25618c9465c0aaea91d936be446d5db04be3d1@195.201.237.185:46656,8b5367df2b1287174ce8950654953d81a7d69a29@144.76.201.43:26556,0f64a6d52eec5563d2461ccc599e742c56cbcf4a@185.245.183.172:26656,36d734269c8e69fd60e9050a7f47733b2e570d1c@89.117.57.201:11656,ba2ef45240cc997443df795b801a34602ba68b55@65.109.92.241:17886,f9d5e36ecc66b48f9fb940a778dd0c3b6b7c3d1d@65.109.106.211:26656,6011e62596d177073f3bed476622162652ab4310@164.68.105.143:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
