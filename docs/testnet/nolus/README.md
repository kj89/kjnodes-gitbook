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

**live-peers** (33)
```bash
peers="7a1fc4d1cc0ffec7db6a2a15496136e62561b162@161.97.146.108:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:43656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27016,e0aac09f3de68abf583b0e3994228ee8bd19d1eb@168.119.124.130:45659,387393e38531ac010f500d294505232a77c88766@45.33.32.8:26656,236a2626ad46bb671b200883b6105350310372ef@135.181.81.65:37656,c6e7b095d965209c8d15086c2a173627fb9b29e1@161.97.169.22:26656,5b7092ce1624e8a23a5d90897c4c5231fb7b1238@185.245.183.172:16656,5bf83be8dfe52fe2c204300f1e9b1449487ce5af@88.99.164.158:1176,8b0b427b4567a7a66f05fab1146ee97b52ad7958@93.189.30.119:26656,8c5de077ed97fea13f822e0afa9d5720b1ff7e1d@178.63.8.245:26656,805f69593aeb23e78ae19b4adca24d0ddd513e12@38.242.141.147:26656,db05aaa5ee2d67f3418cd77df4307f2bb412ee40@65.108.199.62:19656,98907b8c92c003aa2d003bb5d47e5ae6e34b0732@77.51.200.79:46656,33f4b7f56b6708526f0638162f020394de0ce5e9@65.21.229.33:28656,c2c7344a10a39040592a8aa156ef9da17700d9a2@45.84.0.252:26656,0130c7e5dbc56f4a933215b2ea25cd1ac80efd41@95.31.16.222:26656,28cdf59b342cb19fe488e99fab754ccc90c379e3@185.196.21.104:26656,03ec7af23216082eeccc690b7bdcbe497bf2dcf8@136.243.88.91:9000,367fb20ca2380ebbb73eb19b772564383b0f37ee@65.21.123.172:26656,55acbb36f6e18ce9d5034c1e0f615bf13ee1ae27@195.2.80.63:43656,f77c45399c1dea69fcc48ff15995e8387169249a@80.85.242.54:26656,9951244a6f7cc04d30e7a122dfbee14c8ca5b542@185.239.208.142:656,6cf1dbaf1cfee65f14421ba5ac5b165ebe7b0d0a@5.9.97.58:26656,f000cd749de3af6d4d8d21e310ee69a61a66ebdb@138.201.204.5:34656,cb1d1e10c38fe276e3901efbbaa787f34b3f1a08@38.242.226.233:26656,fcb82df30d2056c3af024fb389e173d683fe8229@65.108.105.48:19756,f11e044189963552bee155956a9a0f14f08936fe@117.5.227.60:26656,19c6579ebb9d869e61c4dd082dc414cac6f799f3@46.4.122.235:26656,2f733fee182504c70f38be10f083263ead4a579e@14.238.7.58:26656,5365635387f1effc39473e19dace5a0ea2c3a4de@14.173.140.22:26656,38d46c87a7b7c7ea8ba9b50a6f87331fdf77a36c@45.14.194.209:26656,12b146cd82c7142e9d8aeb4f246499927ecb1c0f@217.13.223.167:36656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nolus/config/config.toml
```
