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

**live-peers** (31)
```bash
peers="8c5de077ed97fea13f822e0afa9d5720b1ff7e1d@178.63.8.245:26656,8b0b427b4567a7a66f05fab1146ee97b52ad7958@93.189.30.119:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:43656,88723de4de92b0fae5cc551bc39cb7b05e1b2c18@217.76.62.110:26656,6d5921160c688c2e4e3b510fcfa48496e74cf2c6@80.92.204.247:37656,c6e7b095d965209c8d15086c2a173627fb9b29e1@161.97.169.22:26656,50d786a2d242839fe2bdb69bee694d7ffa455824@5.161.60.42:18656,236a2626ad46bb671b200883b6105350310372ef@135.181.81.65:37656,df5523a9d35328716337343cbeea3063cd4fa9b3@65.108.206.118:61256,5365635387f1effc39473e19dace5a0ea2c3a4de@14.173.140.22:26656,dd22261eb9101fb33110a715056bc949066b4113@79.137.33.26:16656,e0aac09f3de68abf583b0e3994228ee8bd19d1eb@168.119.124.130:45659,fcb82df30d2056c3af024fb389e173d683fe8229@65.108.105.48:19756,9951244a6f7cc04d30e7a122dfbee14c8ca5b542@185.239.208.142:656,03ec7af23216082eeccc690b7bdcbe497bf2dcf8@136.243.88.91:9000,4b418e9dbc5e45c39ee8329b0d1bae42b7eface1@136.243.103.32:26656,0130c7e5dbc56f4a933215b2ea25cd1ac80efd41@95.31.16.222:26656,33401059ff4b2bc38d7f30930e1a8d82e22def4f@167.235.235.80:26656,cb1d1e10c38fe276e3901efbbaa787f34b3f1a08@38.242.226.233:26656,ac86c1678e20a87bf2f036741932910869726337@135.181.222.185:15656,387393e38531ac010f500d294505232a77c88766@45.33.32.8:26656,2d500ae8bddfa548ee0fb0ed969709d78a4015af@144.168.47.230:26656,a12f0c225332ab006fbc46d58706669bf44f52e0@123.31.73.177:26656,0939a3593877d6cd2896eb94047fc9bc05e72dcb@142.132.152.46:14656,2f733fee182504c70f38be10f083263ead4a579e@14.238.7.58:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27016,805f69593aeb23e78ae19b4adca24d0ddd513e12@38.242.141.147:26656,5bf83be8dfe52fe2c204300f1e9b1449487ce5af@88.99.164.158:1176,28cdf59b342cb19fe488e99fab754ccc90c379e3@185.196.21.104:26656,12b146cd82c7142e9d8aeb4f246499927ecb1c0f@217.13.223.167:36656,8c385e6c57a0f3d010437fbf4d5fd6db84d73a8d@185.215.165.0:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nolus/config/config.toml
```
