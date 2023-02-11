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
peers="7a1fc4d1cc0ffec7db6a2a15496136e62561b162@161.97.146.108:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27016,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:43656,387393e38531ac010f500d294505232a77c88766@45.33.32.8:26656,4b418e9dbc5e45c39ee8329b0d1bae42b7eface1@136.243.103.32:26656,e0ab3276d94a8fbdf04b0b9eb95df22f7037eb89@167.235.31.186:34656,56268f0d71ff5a6380ca82c2f741a240d6ec91da@45.151.122.213:26656,f09a8ba06a00d1edc517995040313732f94c2b56@95.214.55.155:18656,2e80da0046dd3f2205a207dd435b6c9b0f9bfc04@65.109.93.152:27656,db05aaa5ee2d67f3418cd77df4307f2bb412ee40@65.108.199.62:19656,d71f6a702561b08023810464a96668045dbabd9e@95.214.55.25:26656,0bc65a562eff399463fcf18f54716e32054e4cf4@188.166.88.185:26656,33f4b7f56b6708526f0638162f020394de0ce5e9@65.21.229.33:28656,5b7092ce1624e8a23a5d90897c4c5231fb7b1238@185.245.183.172:16656,12b146cd82c7142e9d8aeb4f246499927ecb1c0f@217.13.223.167:36656,0130c7e5dbc56f4a933215b2ea25cd1ac80efd41@95.31.16.222:26656,6cf1dbaf1cfee65f14421ba5ac5b165ebe7b0d0a@5.9.97.58:26656,f77c45399c1dea69fcc48ff15995e8387169249a@80.85.242.54:26656,048df3fd3100c57b1a661aef3336a7c681657928@185.193.17.226:26656,67be97f5ef69a4f149fbef7970ba888e5b2c2cff@65.108.231.124:16656,fcb82df30d2056c3af024fb389e173d683fe8229@65.108.105.48:19756,c2c7344a10a39040592a8aa156ef9da17700d9a2@45.84.0.252:26656,fc9d9ae98a5f12d8be9b2b4eb7c6376dbe500062@148.51.139.47:36656,654e76e7d4b27fdb3a931fe2d44c51184d8a5731@5.161.78.48:26656,3be781c50aac85518bb3cfb8620528cbc5dacd67@146.190.45.222:26656,d8088d91bdbf2ccdf59f0b3ee1c1b07e8cb60798@195.201.237.185:11656,03ec7af23216082eeccc690b7bdcbe497bf2dcf8@136.243.88.91:9000,e62dd608a302ba4f815a7cd3cf3d7facafa0e171@135.181.123.154:16656,8b0b427b4567a7a66f05fab1146ee97b52ad7958@93.189.30.119:26656,e0aac09f3de68abf583b0e3994228ee8bd19d1eb@168.119.124.130:45659,1278e67b0f6523c20e665109dd092ef20d6fd70e@45.67.230.23:26656,5e2ac913af7420f19157b5f0258dcec5df3511e3@49.37.250.208:26656,5bf83be8dfe52fe2c204300f1e9b1449487ce5af@88.99.164.158:1176"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nolus/config/config.toml
```
