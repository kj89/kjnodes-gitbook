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

**live-peers** (28)
```bash
peers="7075469d8ed68a423e065b67bcde29b6ca4266fd@142.132.248.253:65528,468db17f7fc0a3f87b72b4949a3ad9c0e6ecd1c9@94.16.117.238:26656,658f473c2399f87c5e5ff4d329c8c53ae9f399e0@46.101.232.154:26656,266d8a31a1cecf8d2f673e4cb65ea736173428e9@165.22.76.250:20656,aa269fc09dc0b73e45f1c6b514aea634fa0193c7@45.88.223.247:27656,8c6201e793348d8f89dedcae6df3cd36198477fd@94.46.187.220:26656,ec7e0b075202f836feac71f017a90e0d83674cb8@65.108.9.164:24556,0d9a4d351e9e88362f39bc50d7e12900d534dc47@134.209.104.239:27656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:49656,0c77942550c78ae8939b691b725a9dd7ffa4d864@185.219.142.182:27656,91b67dd0d2904d95748e1ec5311e39033cfeaabc@65.109.92.240:1076,dc3f2575d1ec7db2c22cab576018444cad896e5d@104.248.45.158:24556,b67aa6a7fe148c98575b80289bdef931813ed63d@185.217.127.138:49656,a9112494955b579ab18671281da88dd3f3f6cbca@139.59.170.199:26656,47971c889b727897dfc753ca93a15d8e1ce9cd5a@3.140.188.3:26656,866204caf5cdb5de403edf4ef4e43d57b9ada51d@143.198.145.207:24556,a76917f23b26c7c4918104d0e06a24c28f9077bd@5.161.50.28:26656,b9bec1902b4817dc07952078512fdb8fe0306bc4@89.58.45.204:60656,3535b3f6181b8ba413cd9391515b9840aafc4b2a@142.132.194.157:26256,cec1fdc272372d8254aaa33dcf12016c6ad1dbf6@65.109.24.121:26656,25a478432d5a16a0597124ecdad5ae6b706c2c32@185.252.234.212:24556,1b6164aab8350eeb71bd46ebfe641e5d103a3f8e@143.244.132.66:26656,bd38f8b14f549bc035eaf2f22e7832173f1fd761@198.199.74.16:20656,1946f4a7d7dd6b3ed49d8e3a64a16284a7f4fa11@85.214.116.96:24556,0c78af85c2fb11a4c5b09f357595bd671438e6eb@172.105.127.215:26656,9b68197830bb2833f3ad722a5460fe4d9ad4fbed@8.219.145.180:09656,746c2645f49602887cc6e38bb58c79860de93c1a@139.59.242.34:49656,7226702dd45f4bee9f35b6a20b5b4e51f963fae8@188.166.187.23:27656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.sao/config/config.toml
```
