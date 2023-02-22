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

**live-peers** (14)
```bash
peers="d6df4d2bc05d11b5beb09658f1382ba094961c9e@84.46.252.45:60656,fcb82df30d2056c3af024fb389e173d683fe8229@65.108.105.48:19756,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:43656,7a1fc4d1cc0ffec7db6a2a15496136e62561b162@161.97.146.108:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27016,387393e38531ac010f500d294505232a77c88766@45.33.32.8:26656,621c459c333de1a03250bb846647fc858b9c8638@38.242.142.83:26656,5b7092ce1624e8a23a5d90897c4c5231fb7b1238@185.245.183.172:16656,e0aac09f3de68abf583b0e3994228ee8bd19d1eb@168.119.124.130:45659,8b0b427b4567a7a66f05fab1146ee97b52ad7958@93.189.30.119:26656,33f4b7f56b6708526f0638162f020394de0ce5e9@65.21.229.33:28656,4b418e9dbc5e45c39ee8329b0d1bae42b7eface1@136.243.103.32:26656,9951244a6f7cc04d30e7a122dfbee14c8ca5b542@185.239.208.142:656,8c385e6c57a0f3d010437fbf4d5fd6db84d73a8d@185.215.165.0:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nolus/config/config.toml
```
