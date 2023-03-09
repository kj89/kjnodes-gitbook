# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/sao.png" width="150" alt=""><figcaption></figcaption></figure>

SAO Network is a secure and decentralized Web3 storage infrastructure  based on Cosmos SDK and IPFS protocol. It aims to facilitate the adoption  of Web3 storage, support the growing demand for Web3 applications and  allow for a more decentralized way of storing and accessing data.

**Chain ID**: sao-testnet0 | **Latest Version Tag**: v0.0.9 | **Wasm**: OFF

[Website](https://www.sao.network) | [Discord](https://discord.gg/f4xzfvPhhA) | [Twitter](https://twitter.com/SAONetwork)




## Chain explorer
[https://explorer.kjnodes.com/sao-testnet](https://explorer.kjnodes.com/sao-testnet)

## Public endpoints

* api: [https://sao-testnet.api.kjnodes.com](https://sao-testnet.api.kjnodes.com)
* rpc: [https://sao-testnet.rpc.kjnodes.com](https://sao-testnet.rpc.kjnodes.com)
* grpc: [https://sao-testnet.grpc.kjnodes.com](https://sao-testnet.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@sao-testnet.rpc.kjnodes.com:49656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@sao-testnet.rpc.kjnodes.com:49659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/sao-testnet/addrbook.json > $HOME/.sao/config/addrbook.json
```

**live-peers** (38)
```bash
peers="7075469d8ed68a423e065b67bcde29b6ca4266fd@142.132.248.253:65528,61e9e3927c1d25d91e8fefbdc880791e7974bfb5@159.223.19.154:27656,9943703d74b9ce0fa43e45dd3a96f40141131b48@213.239.216.252:49656,658f473c2399f87c5e5ff4d329c8c53ae9f399e0@46.101.232.154:26656,ada0a0b4b5b3d290cae51b946b33a1079d00df72@185.197.250.35:27656,25a478432d5a16a0597124ecdad5ae6b706c2c32@185.252.234.212:24556,48e35ce9a6e794a6d292d2df74eafc2c1c754678@185.207.251.105:26656,b67aa6a7fe148c98575b80289bdef931813ed63d@185.217.127.138:49656,a9112494955b579ab18671281da88dd3f3f6cbca@139.59.170.199:26656,ec7e0b075202f836feac71f017a90e0d83674cb8@65.108.9.164:24556,0c78af85c2fb11a4c5b09f357595bd671438e6eb@172.105.127.215:26656,22cb6793d2bc029121f9e1dffddeb6eae74a466c@178.128.24.92:20656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:49656,0c77942550c78ae8939b691b725a9dd7ffa4d864@185.219.142.182:27656,91b67dd0d2904d95748e1ec5311e39033cfeaabc@65.109.92.240:1076,cec1fdc272372d8254aaa33dcf12016c6ad1dbf6@65.109.24.121:26656,266d8a31a1cecf8d2f673e4cb65ea736173428e9@165.22.76.250:20656,e96613a87f825269bf81ece62a9c53e611f0143c@91.201.113.194:46656,a4a02db4e2753ebb13a77eb53531d87e566cae7b@27.71.128.102:26656,1b6164aab8350eeb71bd46ebfe641e5d103a3f8e@143.244.132.66:26656,ee0f6da4f64970738cdbb01d21c9ce5240c92ca4@157.245.150.110:20656,b9bec1902b4817dc07952078512fdb8fe0306bc4@89.58.45.204:60656,a76917f23b26c7c4918104d0e06a24c28f9077bd@5.161.50.28:26656,dc3f2575d1ec7db2c22cab576018444cad896e5d@104.248.45.158:24556,3535b3f6181b8ba413cd9391515b9840aafc4b2a@142.132.194.157:26256,0a661ed79b169c7c2b0f289c436e35900bb0de90@157.97.108.38:24556,f78bcf0cd9f48b511f1e0087ae0a73d2b35de2d8@84.46.246.248:27656,bd39c2d10d1f11881d1baca9caa25f721a36ce97@65.109.92.148:26656,346a26e47244ce188e808a53e1d85e60dd58a114@109.123.243.68:26656,2391c496886d549eaef56eec922193b23e48119f@65.108.12.181:26756,866204caf5cdb5de403edf4ef4e43d57b9ada51d@143.198.145.207:24556,9b68197830bb2833f3ad722a5460fe4d9ad4fbed@8.219.145.180:09656,14e4a9a565508d0aac31f270d898fb6df82f1146@1.53.109.68:49656,8ed1fa8c260b74441bdb9c0ad32587b0a6081b3f@20.46.153.249:26656,04f9bad9b3b5c657dc7c11b341074028fb2faf2c@203.23.128.181:26656,af7259853f202391e624c612ff9d3de1142b4ca4@175.41.187.192:26656,a5298771c624a376fdb83c48cc6c630e58092c62@192.18.136.151:26656,b89f7fa190362f2bd328184fb0bed7ce5e2c79c3@172.104.50.65:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.sao/config/config.toml
```
