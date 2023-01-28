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

**live-peers** (38)
```bash
peers="e0ab3276d94a8fbdf04b0b9eb95df22f7037eb89@167.235.31.186:34656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27016,7a1fc4d1cc0ffec7db6a2a15496136e62561b162@161.97.146.108:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:43656,387393e38531ac010f500d294505232a77c88766@45.33.32.8:26656,301dcb25951a0ebd6a36e09e612c85dc3aea3767@95.70.160.37:26656,df5523a9d35328716337343cbeea3063cd4fa9b3@65.108.206.118:61256,db05aaa5ee2d67f3418cd77df4307f2bb412ee40@65.108.199.62:19656,e0aac09f3de68abf583b0e3994228ee8bd19d1eb@168.119.124.130:45659,98907b8c92c003aa2d003bb5d47e5ae6e34b0732@77.51.200.79:46656,9e54327630e4f9668fb6137c5631c0ed6905b6e7@89.252.21.37:26656,e4b7228ccadf3180e6e323aa4c0c97946ac054dc@65.109.112.20:11134,89aaf76a23b16bd57a1982e7b304fd998a49942a@65.109.85.226:9000,b6c8dc38a5dba19a3f10d23b3572065db9265fa3@65.109.85.225:9000,5bf83be8dfe52fe2c204300f1e9b1449487ce5af@88.99.164.158:1176,58d7fc67e12548f3f1ddda3bbe6000ae3d9d638c@85.10.198.169:13656,8c5de077ed97fea13f822e0afa9d5720b1ff7e1d@178.63.8.245:26656,681ecb99467dd00a586d9499a1002f2829f1a02d@65.109.85.208:29656,e2c89ba2a9e998ff69b955d5bb317e7438816b7b@95.217.4.157:43656,6cb8e63bf00d37399454ab24b6cf316062b90117@199.175.98.110:36656,5118f29924e801e965e48d129fb29561aaa93966@193.203.15.174:26656,f94390d9e922e8430ad9fd5062244ddf7d4babd4@45.130.104.121:26656,723d799586cb2659f797a336bcbafaf6b0903586@92.53.65.56:16656,1cb8223111a5fb8a631d73aa3bcd7abd2ef41ba7@45.87.104.84:1184,5289137e6134895c5b3b82a9847869f2a889cdc0@65.108.97.58:2776,04a0036ff421f2dd8f46cca1fae9a893624bd868@95.216.14.72:29656,8b0b427b4567a7a66f05fab1146ee97b52ad7958@93.189.30.119:26656,8cfc45157cbe7314c29402fe560999e2e7043744@95.217.232.152:26656,1dc853554645753a372791d127f2623c5adfadd2@151.106.34.127:26656,29815a33ec3ac811901545fd632d16deb89dc641@194.163.172.188:37656,bcdaea50a4b47aca51e586bca2abfa68b8cc23fd@185.252.235.247:26656,e4d5f8e6c8c55305488daf55d9160f544fdc15fb@1.54.112.59:26656,2f733fee182504c70f38be10f083263ead4a579e@14.238.7.58:26656,805f69593aeb23e78ae19b4adca24d0ddd513e12@38.242.141.147:26656,67be97f5ef69a4f149fbef7970ba888e5b2c2cff@65.108.231.124:16656,a95975f3a58e20ba1c518f3cbb1c23ef7569e4d4@14.241.82.87:26656,12b146cd82c7142e9d8aeb4f246499927ecb1c0f@217.13.223.167:36656,8539e9777b36e6d8cfd3d68d44dd369cb8f8514f@188.232.23.24:37656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nolus/config/config.toml
```
