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

**live-peers** (32)
```bash
peers="8c5de077ed97fea13f822e0afa9d5720b1ff7e1d@178.63.8.245:26656,5b7092ce1624e8a23a5d90897c4c5231fb7b1238@185.245.183.172:16656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:43656,387393e38531ac010f500d294505232a77c88766@45.33.32.8:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27016,5365635387f1effc39473e19dace5a0ea2c3a4de@14.173.140.22:26656,ac762c8dd9224bfe3021c10e3300a78f58d64a85@194.163.183.211:37656,5bf83be8dfe52fe2c204300f1e9b1449487ce5af@88.99.164.158:1176,03ec7af23216082eeccc690b7bdcbe497bf2dcf8@136.243.88.91:9000,9951244a6f7cc04d30e7a122dfbee14c8ca5b542@185.239.208.142:656,1278e67b0f6523c20e665109dd092ef20d6fd70e@45.67.230.23:26656,654e76e7d4b27fdb3a931fe2d44c51184d8a5731@5.161.78.48:26656,e0aac09f3de68abf583b0e3994228ee8bd19d1eb@168.119.124.130:45659,8b0b427b4567a7a66f05fab1146ee97b52ad7958@93.189.30.119:26656,d6df4d2bc05d11b5beb09658f1382ba094961c9e@84.46.252.45:60656,28cdf59b342cb19fe488e99fab754ccc90c379e3@185.196.21.104:26656,50d786a2d242839fe2bdb69bee694d7ffa455824@5.161.60.42:18656,2d500ae8bddfa548ee0fb0ed969709d78a4015af@144.168.47.230:26656,367fb20ca2380ebbb73eb19b772564383b0f37ee@65.21.123.172:26656,cb1d1e10c38fe276e3901efbbaa787f34b3f1a08@38.242.226.233:26656,0130c7e5dbc56f4a933215b2ea25cd1ac80efd41@95.31.16.222:26656,fcb82df30d2056c3af024fb389e173d683fe8229@65.108.105.48:19756,52ba17ca5b0d25f60fa1a2f93685380089a8b2ec@65.108.201.15:6656,81ff6924175ccca5d1f09cb5d999f0e64852ccea@188.163.121.216:26656,80adbc33862b62282016de27380e6e709308346a@45.14.194.209:26656,71ad2a400e31641413083e46d7522f9b00fa1083@194.163.176.222:26656,8b8bb15cc131fbe09a8070351195022911fe6e8e@89.117.62.159:26656,d71f6a702561b08023810464a96668045dbabd9e@95.214.55.25:26656,a1eafc52084bc7affa8ed2339003433a09c944fb@128.199.1.92:26656,12b146cd82c7142e9d8aeb4f246499927ecb1c0f@217.13.223.167:36656,67be97f5ef69a4f149fbef7970ba888e5b2c2cff@65.108.231.124:16656,df5523a9d35328716337343cbeea3063cd4fa9b3@65.108.206.118:61256"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nolus/config/config.toml
```
