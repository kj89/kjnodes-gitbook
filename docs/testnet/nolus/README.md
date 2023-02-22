# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/nolus.png" width="150" alt=""><figcaption></figcaption></figure>

Nolus aims to be the leading DeFi Lease platform. The protocol  intends to become a tool for empowering people, simple to use, and highly efficient.

**Chain ID**: nolus-rila | **Latest Version Tag**: v0.1.43 | **Wasm**: ON

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

**live-peers** (27)
```bash
peers="ee7579d3dadb725ce0ed1e453fd72c2fcbb7b9af@142.132.208.26:26356,fac035258738be9be98957d5d012d24841d2e5eb@85.10.197.4:16656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27016,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:43656,387393e38531ac010f500d294505232a77c88766@45.33.32.8:26656,8b0b427b4567a7a66f05fab1146ee97b52ad7958@93.189.30.119:26656,19c6579ebb9d869e61c4dd082dc414cac6f799f3@46.4.122.235:26656,e0aac09f3de68abf583b0e3994228ee8bd19d1eb@168.119.124.130:45659,9951244a6f7cc04d30e7a122dfbee14c8ca5b542@185.239.208.142:656,33f4b7f56b6708526f0638162f020394de0ce5e9@65.21.229.33:28656,8c385e6c57a0f3d010437fbf4d5fd6db84d73a8d@185.215.165.0:26656,98907b8c92c003aa2d003bb5d47e5ae6e34b0732@77.51.200.79:46656,cb1d1e10c38fe276e3901efbbaa787f34b3f1a08@38.242.226.233:26656,3cadae7324e9bf129b76bc489cd080535d03f3d2@176.9.22.117:55656,1b4879af6ada4a05b2826212deee3747308d3f88@173.249.48.234:36656,2d500ae8bddfa548ee0fb0ed969709d78a4015af@144.168.47.230:26656,6cb8e63bf00d37399454ab24b6cf316062b90117@199.175.98.110:36656,03ec7af23216082eeccc690b7bdcbe497bf2dcf8@136.243.88.91:9000,6d5921160c688c2e4e3b510fcfa48496e74cf2c6@80.92.204.247:37656,dd8e8ca7c997b796a519363f58ecc5f670c6aba8@168.119.253.97:26656,12b146cd82c7142e9d8aeb4f246499927ecb1c0f@217.13.223.167:36656,0005b1e2c88dbad64b71a706016b340f2afa982f@109.123.244.56:26686,621c459c333de1a03250bb846647fc858b9c8638@38.242.142.83:26656,0130c7e5dbc56f4a933215b2ea25cd1ac80efd41@95.31.16.222:26656,fcb82df30d2056c3af024fb389e173d683fe8229@65.108.105.48:19756,55acbb36f6e18ce9d5034c1e0f615bf13ee1ae27@195.2.80.63:43656,b58f28536e9170b919a24242387e7c41b97371f1@113.161.144.108:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nolus/config/config.toml
```
