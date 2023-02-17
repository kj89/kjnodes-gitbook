# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/nolus.png" width="150" alt=""><figcaption></figcaption></figure>

Nolus aims to be the leading DeFi Lease platform. The protocol  intends to become a tool for empowering people, simple to use, and highly efficient.

**Chain ID**: nolus-rila | **Latest Version Tag**: v0.1.39 | **Wasm**: ON

[Website](https://www.nolus.io) | [Discord](https://discord.gg/nolus-protocol) | [Twitter](https://twitter.com/NolusProtocol)




## Chain explorer
[https://explorer.kjnodes.com/nolus-testnet](https://explorer.kjnodes.com/nolus-testnet)

## Public endpoints

* api: [https://nolus-testnet.api.kjnodes.com](https://nolus-testnet.api.kjnodes.com)
* rpc: [https://nolus-testnet.rpc.kjnodes.com](https://nolus-testnet.rpc.kjnodes.com)
* grpc: [https://nolus-testnet.grpc.kjnodes.com](https://nolus-testnet.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@nolus-testnet.rpc.kjnodes.com:43656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@nolus-testnet.rpc.kjnodes.com:43659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/nolus-testnet/addrbook.json > $HOME/.nolus/config/addrbook.json
```

**live-peers** (28)
```bash
peers="5b7092ce1624e8a23a5d90897c4c5231fb7b1238@185.245.183.172:16656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:43656,fcb82df30d2056c3af024fb389e173d683fe8229@65.108.105.48:19756,d8088d91bdbf2ccdf59f0b3ee1c1b07e8cb60798@195.201.237.185:11656,7a1fc4d1cc0ffec7db6a2a15496136e62561b162@161.97.146.108:26656,387393e38531ac010f500d294505232a77c88766@45.33.32.8:26656,0005b1e2c88dbad64b71a706016b340f2afa982f@109.123.244.56:26686,33f4b7f56b6708526f0638162f020394de0ce5e9@65.21.229.33:28656,28cdf59b342cb19fe488e99fab754ccc90c379e3@185.196.21.104:26656,4b418e9dbc5e45c39ee8329b0d1bae42b7eface1@136.243.103.32:26656,367fb20ca2380ebbb73eb19b772564383b0f37ee@65.21.123.172:26656,e0aac09f3de68abf583b0e3994228ee8bd19d1eb@168.119.124.130:45659,33d485f51f413fd4bf83ef8a971c10228a39cffb@62.171.161.172:26656,8d636705234cc52f6cce11dc46fc826a47b622ff@65.109.84.215:36656,5289137e6134895c5b3b82a9847869f2a889cdc0@65.108.97.58:2776,8b0b427b4567a7a66f05fab1146ee97b52ad7958@93.189.30.119:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27016,0130c7e5dbc56f4a933215b2ea25cd1ac80efd41@95.31.16.222:26656,6cb8e63bf00d37399454ab24b6cf316062b90117@199.175.98.110:36656,a4113afdf9158e797d51b5c051009a0ec9e44ac7@5.78.67.32:26656,7d1ac536c8451d1b64e9702fb172ac5b1b725778@65.109.85.221:9000,d71f6a702561b08023810464a96668045dbabd9e@95.214.55.25:26656,096f508196d9e8e7c50937323a441307fbb82437@195.3.222.189:27656,26492b49c92ecc4f19a26cacc162d22f97a9d64b@85.239.233.164:26656,236a2626ad46bb671b200883b6105350310372ef@135.181.81.65:37656,5bf83be8dfe52fe2c204300f1e9b1449487ce5af@88.99.164.158:1176,df5523a9d35328716337343cbeea3063cd4fa9b3@65.108.206.118:61256,12b146cd82c7142e9d8aeb4f246499927ecb1c0f@217.13.223.167:36656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nolus/config/config.toml
```
