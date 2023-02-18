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

**live-peers** (30)
```bash
peers="12b146cd82c7142e9d8aeb4f246499927ecb1c0f@217.13.223.167:36656,5b7092ce1624e8a23a5d90897c4c5231fb7b1238@185.245.183.172:16656,387393e38531ac010f500d294505232a77c88766@45.33.32.8:26656,7a1fc4d1cc0ffec7db6a2a15496136e62561b162@161.97.146.108:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:43656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27016,785789b6574c45b8cfefff08344fdfeda345c7e1@135.125.5.34:55666,8b0b427b4567a7a66f05fab1146ee97b52ad7958@93.189.30.119:26656,e0aac09f3de68abf583b0e3994228ee8bd19d1eb@168.119.124.130:45659,33f4b7f56b6708526f0638162f020394de0ce5e9@65.21.229.33:28656,d8088d91bdbf2ccdf59f0b3ee1c1b07e8cb60798@195.201.237.185:11656,67be97f5ef69a4f149fbef7970ba888e5b2c2cff@65.108.231.124:16656,076aa0f1516b2250b045be2889ef3bda904d3906@5.78.83.14:26656,db05aaa5ee2d67f3418cd77df4307f2bb412ee40@65.108.199.62:19656,df5523a9d35328716337343cbeea3063cd4fa9b3@65.108.206.118:61256,389158fdbbdda215898d01231d47e66964ee1ae1@154.26.135.231:26656,0130c7e5dbc56f4a933215b2ea25cd1ac80efd41@95.31.16.222:26656,367fb20ca2380ebbb73eb19b772564383b0f37ee@65.21.123.172:26656,0005b1e2c88dbad64b71a706016b340f2afa982f@109.123.244.56:26686,8d636705234cc52f6cce11dc46fc826a47b622ff@65.109.84.215:36656,98907b8c92c003aa2d003bb5d47e5ae6e34b0732@77.51.200.79:46656,28cdf59b342cb19fe488e99fab754ccc90c379e3@185.196.21.104:26656,7c2ea36064077da73d0ad5b60d8ef215acbee50b@161.97.79.100:36656,0e24f9b374ebc0c76d2ad71f8f3db240ba02a097@155.133.27.251:26656,1278e67b0f6523c20e665109dd092ef20d6fd70e@45.67.230.23:26656,a12f0c225332ab006fbc46d58706669bf44f52e0@123.31.73.177:26656,9951244a6f7cc04d30e7a122dfbee14c8ca5b542@185.239.208.142:656,26492b49c92ecc4f19a26cacc162d22f97a9d64b@85.239.233.164:26656,3526133f0428910922f9ce2ac9a08b2836bbc9c1@217.76.61.183:26656,5bf83be8dfe52fe2c204300f1e9b1449487ce5af@88.99.164.158:1176"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nolus/config/config.toml
```
