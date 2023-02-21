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
peers="ac762c8dd9224bfe3021c10e3300a78f58d64a85@194.163.183.211:37656,8b0b427b4567a7a66f05fab1146ee97b52ad7958@93.189.30.119:26656,98907b8c92c003aa2d003bb5d47e5ae6e34b0732@77.51.200.79:46656,c4a974e2a4d548163e6506f2d2f2d4aeb1c89f18@194.163.190.167:36656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27016,387393e38531ac010f500d294505232a77c88766@45.33.32.8:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:43656,e0aac09f3de68abf583b0e3994228ee8bd19d1eb@168.119.124.130:45659,8c5de077ed97fea13f822e0afa9d5720b1ff7e1d@178.63.8.245:26656,52ba17ca5b0d25f60fa1a2f93685380089a8b2ec@65.108.201.15:6656,236a2626ad46bb671b200883b6105350310372ef@135.181.81.65:37656,fcb82df30d2056c3af024fb389e173d683fe8229@65.108.105.48:19756,ab938d7b2af2ecad6af86df956fd61634ce439ff@65.108.234.11:16656,367fb20ca2380ebbb73eb19b772564383b0f37ee@65.21.123.172:26656,28cdf59b342cb19fe488e99fab754ccc90c379e3@185.196.21.104:26656,654e76e7d4b27fdb3a931fe2d44c51184d8a5731@5.161.78.48:26656,e4b7228ccadf3180e6e323aa4c0c97946ac054dc@65.109.112.20:11134,cb1d1e10c38fe276e3901efbbaa787f34b3f1a08@38.242.226.233:26656,0130c7e5dbc56f4a933215b2ea25cd1ac80efd41@95.31.16.222:26656,67be97f5ef69a4f149fbef7970ba888e5b2c2cff@65.108.231.124:16656,769552416bbe807f319e2fa6125a40969b254182@65.108.108.52:18656,2d500ae8bddfa548ee0fb0ed969709d78a4015af@144.168.47.230:26656,cb989bd3f416226bfd71631c0348ea38a1df3ec0@65.109.106.91:23656,03ec7af23216082eeccc690b7bdcbe497bf2dcf8@136.243.88.91:9000,d71f6a702561b08023810464a96668045dbabd9e@95.214.55.25:26656,dd22261eb9101fb33110a715056bc949066b4113@79.137.33.26:16656,e6e48680fa62c03bed242c52eb21d3cbe44a6752@46.8.210.144:26856,5289137e6134895c5b3b82a9847869f2a889cdc0@65.108.97.58:2776,2b728f3cc8cb5adb9d19f78895892905d895acf4@161.97.171.229:26656,fafd77c56097164a004e22851cc75fed5d983f8f@80.65.211.56:37656,12b146cd82c7142e9d8aeb4f246499927ecb1c0f@217.13.223.167:36656,5365635387f1effc39473e19dace5a0ea2c3a4de@14.173.140.22:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nolus/config/config.toml
```
