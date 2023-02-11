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
peers="5b7092ce1624e8a23a5d90897c4c5231fb7b1238@185.245.183.172:16656,2e80da0046dd3f2205a207dd435b6c9b0f9bfc04@65.109.93.152:27656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:43656,7a1fc4d1cc0ffec7db6a2a15496136e62561b162@161.97.146.108:26656,387393e38531ac010f500d294505232a77c88766@45.33.32.8:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27016,03ec7af23216082eeccc690b7bdcbe497bf2dcf8@136.243.88.91:9000,fcb82df30d2056c3af024fb389e173d683fe8229@65.108.105.48:19756,0bc65a562eff399463fcf18f54716e32054e4cf4@188.166.88.185:26656,6b14535ff005667f324f8439a55a21ee2f170d12@95.217.211.81:26656,8c5de077ed97fea13f822e0afa9d5720b1ff7e1d@178.63.8.245:26656,3be781c50aac85518bb3cfb8620528cbc5dacd67@146.190.45.222:26656,681ecb99467dd00a586d9499a1002f2829f1a02d@65.109.85.208:29656,ab938d7b2af2ecad6af86df956fd61634ce439ff@65.108.234.11:16656,e0ab3276d94a8fbdf04b0b9eb95df22f7037eb89@167.235.31.186:34656,1278e67b0f6523c20e665109dd092ef20d6fd70e@45.67.230.23:26656,e0aac09f3de68abf583b0e3994228ee8bd19d1eb@168.119.124.130:45659,d8088d91bdbf2ccdf59f0b3ee1c1b07e8cb60798@195.201.237.185:11656,67be97f5ef69a4f149fbef7970ba888e5b2c2cff@65.108.231.124:16656,d53006a0db9a2eac79f853526719716cece550ad@144.76.92.112:26656,28cdf59b342cb19fe488e99fab754ccc90c379e3@185.196.21.104:26656,19c6579ebb9d869e61c4dd082dc414cac6f799f3@46.4.122.235:26656,654e76e7d4b27fdb3a931fe2d44c51184d8a5731@5.161.78.48:26656,56268f0d71ff5a6380ca82c2f741a240d6ec91da@45.151.122.213:26656,0130c7e5dbc56f4a933215b2ea25cd1ac80efd41@95.31.16.222:26656,6cf1dbaf1cfee65f14421ba5ac5b165ebe7b0d0a@5.9.97.58:26656,8b0b427b4567a7a66f05fab1146ee97b52ad7958@93.189.30.119:26656,9e54327630e4f9668fb6137c5631c0ed6905b6e7@89.252.21.37:26656,4b418e9dbc5e45c39ee8329b0d1bae42b7eface1@136.243.103.32:26656,5bf83be8dfe52fe2c204300f1e9b1449487ce5af@88.99.164.158:1176,f09a8ba06a00d1edc517995040313732f94c2b56@95.214.55.155:18656,93b90db2cb18bfa490c7dc4dddd0720ec9cfcfb5@212.24.101.2:26656,33f4b7f56b6708526f0638162f020394de0ce5e9@65.21.229.33:28656,0005b1e2c88dbad64b71a706016b340f2afa982f@109.123.244.56:26686,60c57c5b7215c84260249768cf66ae550142af9f@141.98.169.25:26656,8ca0bffdf45aa4aaa4624c6d4c3e258a8c595591@65.108.43.58:27659,fd2ff06cfc095873b823a8c619220773ad4ef080@20.228.131.71:26656,12b146cd82c7142e9d8aeb4f246499927ecb1c0f@217.13.223.167:36656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nolus/config/config.toml
```
