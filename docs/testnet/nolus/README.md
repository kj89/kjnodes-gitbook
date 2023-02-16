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
peers="d8088d91bdbf2ccdf59f0b3ee1c1b07e8cb60798@195.201.237.185:11656,e0ab3276d94a8fbdf04b0b9eb95df22f7037eb89@167.235.31.186:34656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:43656,387393e38531ac010f500d294505232a77c88766@45.33.32.8:26656,6cf1dbaf1cfee65f14421ba5ac5b165ebe7b0d0a@5.9.97.58:26656,7a1fc4d1cc0ffec7db6a2a15496136e62561b162@161.97.146.108:26656,8c385e6c57a0f3d010437fbf4d5fd6db84d73a8d@185.215.165.0:26656,e0aac09f3de68abf583b0e3994228ee8bd19d1eb@168.119.124.130:45659,6b14535ff005667f324f8439a55a21ee2f170d12@95.217.211.81:26656,28cdf59b342cb19fe488e99fab754ccc90c379e3@185.196.21.104:26656,038eef443b6bab9c28f9109599cd8733b3eb8dff@65.21.185.92:26656,df5523a9d35328716337343cbeea3063cd4fa9b3@65.108.206.118:61256,5289137e6134895c5b3b82a9847869f2a889cdc0@65.108.97.58:2776,e8473dede42e7f0d4668a24d909a5708c5a04a3e@65.108.78.116:11656,19c6579ebb9d869e61c4dd082dc414cac6f799f3@46.4.122.235:26656,d71f6a702561b08023810464a96668045dbabd9e@95.214.55.25:26656,c2c7344a10a39040592a8aa156ef9da17700d9a2@45.84.0.252:26656,9951244a6f7cc04d30e7a122dfbee14c8ca5b542@185.239.208.142:656,85c5ef9ff695574abdf1ab38fb1196bc6482aec5@89.252.21.37:26656,0130c7e5dbc56f4a933215b2ea25cd1ac80efd41@95.31.16.222:26656,1278e67b0f6523c20e665109dd092ef20d6fd70e@45.67.230.23:26656,2b728f3cc8cb5adb9d19f78895892905d895acf4@161.97.171.229:26656,5bf83be8dfe52fe2c204300f1e9b1449487ce5af@88.99.164.158:1176,0bc65a562eff399463fcf18f54716e32054e4cf4@188.166.88.185:26656,0005b1e2c88dbad64b71a706016b340f2afa982f@109.123.244.56:26686,5e2ac913af7420f19157b5f0258dcec5df3511e3@49.37.250.184:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27016,236a2626ad46bb671b200883b6105350310372ef@135.181.81.65:37656,8b0b427b4567a7a66f05fab1146ee97b52ad7958@93.189.30.119:26656,12b146cd82c7142e9d8aeb4f246499927ecb1c0f@217.13.223.167:36656,67be97f5ef69a4f149fbef7970ba888e5b2c2cff@65.108.231.124:16656,e711b6631c3e5bb2f6c389cbc5d422912b05316b@213.239.216.252:15256"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nolus/config/config.toml
```
