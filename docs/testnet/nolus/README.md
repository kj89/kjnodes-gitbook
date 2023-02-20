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

**live-peers** (26)
```bash
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:43656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27016,387393e38531ac010f500d294505232a77c88766@45.33.32.8:26656,80adbc33862b62282016de27380e6e709308346a@45.14.194.209:26656,8c5de077ed97fea13f822e0afa9d5720b1ff7e1d@178.63.8.245:26656,8b0b427b4567a7a66f05fab1146ee97b52ad7958@93.189.30.119:26656,236a2626ad46bb671b200883b6105350310372ef@135.181.81.65:37656,6b14535ff005667f324f8439a55a21ee2f170d12@95.217.211.81:26656,1278e67b0f6523c20e665109dd092ef20d6fd70e@45.67.230.23:26656,fcb82df30d2056c3af024fb389e173d683fe8229@65.108.105.48:19756,5289137e6134895c5b3b82a9847869f2a889cdc0@65.108.97.58:2776,e0aac09f3de68abf583b0e3994228ee8bd19d1eb@168.119.124.130:45659,5365635387f1effc39473e19dace5a0ea2c3a4de@14.173.140.22:26656,5bf83be8dfe52fe2c204300f1e9b1449487ce5af@88.99.164.158:1176,03ec7af23216082eeccc690b7bdcbe497bf2dcf8@136.243.88.91:9000,28cdf59b342cb19fe488e99fab754ccc90c379e3@185.196.21.104:26656,1cb8223111a5fb8a631d73aa3bcd7abd2ef41ba7@45.87.104.84:1184,4b418e9dbc5e45c39ee8329b0d1bae42b7eface1@136.243.103.32:26656,0130c7e5dbc56f4a933215b2ea25cd1ac80efd41@95.31.16.222:26656,9951244a6f7cc04d30e7a122dfbee14c8ca5b542@185.239.208.142:656,769552416bbe807f319e2fa6125a40969b254182@65.108.108.52:18656,cb1d1e10c38fe276e3901efbbaa787f34b3f1a08@38.242.226.233:26656,ab938d7b2af2ecad6af86df956fd61634ce439ff@65.108.234.11:16656,6cb8e63bf00d37399454ab24b6cf316062b90117@199.175.98.110:36656,12b146cd82c7142e9d8aeb4f246499927ecb1c0f@217.13.223.167:36656,2d500ae8bddfa548ee0fb0ed969709d78a4015af@144.168.47.230:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nolus/config/config.toml
```
