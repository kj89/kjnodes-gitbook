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

**live-peers** (28)
```bash
peers="12b146cd82c7142e9d8aeb4f246499927ecb1c0f@217.13.223.167:36656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:43656,387393e38531ac010f500d294505232a77c88766@45.33.32.8:26656,236a2626ad46bb671b200883b6105350310372ef@135.181.81.65:37656,7a1fc4d1cc0ffec7db6a2a15496136e62561b162@161.97.146.108:26656,5b7092ce1624e8a23a5d90897c4c5231fb7b1238@185.245.183.172:16656,d71f6a702561b08023810464a96668045dbabd9e@95.214.55.25:26656,67be97f5ef69a4f149fbef7970ba888e5b2c2cff@65.108.231.124:16656,e0aac09f3de68abf583b0e3994228ee8bd19d1eb@168.119.124.130:45659,038eef443b6bab9c28f9109599cd8733b3eb8dff@65.21.185.92:26656,33f4b7f56b6708526f0638162f020394de0ce5e9@65.21.229.33:28656,d8088d91bdbf2ccdf59f0b3ee1c1b07e8cb60798@195.201.237.185:11656,aeb7d7ae104bff006d9ef09e780ca2bb5ce5ee9e@95.84.213.151:26656,c6e7b095d965209c8d15086c2a173627fb9b29e1@161.97.169.22:26656,6cf1dbaf1cfee65f14421ba5ac5b165ebe7b0d0a@5.9.97.58:26656,9951244a6f7cc04d30e7a122dfbee14c8ca5b542@185.239.208.142:656,00ce364657c9b520febb563beb7c4a1c9fc2d352@195.2.70.100:26656,85c5ef9ff695574abdf1ab38fb1196bc6482aec5@89.252.21.37:26656,8b0b427b4567a7a66f05fab1146ee97b52ad7958@93.189.30.119:26656,df5523a9d35328716337343cbeea3063cd4fa9b3@65.108.206.118:61256,1278e67b0f6523c20e665109dd092ef20d6fd70e@45.67.230.23:26656,28cdf59b342cb19fe488e99fab754ccc90c379e3@185.196.21.104:26656,367fb20ca2380ebbb73eb19b772564383b0f37ee@65.21.123.172:26656,7c2ea36064077da73d0ad5b60d8ef215acbee50b@161.97.79.100:36656,55acbb36f6e18ce9d5034c1e0f615bf13ee1ae27@195.2.80.63:43656,5289137e6134895c5b3b82a9847869f2a889cdc0@65.108.97.58:2776,5bf83be8dfe52fe2c204300f1e9b1449487ce5af@88.99.164.158:1176,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27016"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nolus/config/config.toml
```
