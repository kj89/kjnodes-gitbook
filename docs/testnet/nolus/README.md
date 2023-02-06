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
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:43656,387393e38531ac010f500d294505232a77c88766@45.33.32.8:26656,7a1fc4d1cc0ffec7db6a2a15496136e62561b162@161.97.146.108:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27016,5289137e6134895c5b3b82a9847869f2a889cdc0@65.108.97.58:2776,e0aac09f3de68abf583b0e3994228ee8bd19d1eb@168.119.124.130:45659,fc3fcb124a23e0fc56601d643ca56dfed586dcf0@84.46.241.63:26656,fa0a2fe57c2ab28aee6cc0be4eddbc68d6587a75@95.217.165.189:26656,33f4b7f56b6708526f0638162f020394de0ce5e9@65.21.229.33:28656,28cdf59b342cb19fe488e99fab754ccc90c379e3@185.196.21.104:26656,e4471d299c128572d1a26459f3d998f4a5fdebf4@27.72.126.82:26656,681ecb99467dd00a586d9499a1002f2829f1a02d@65.109.85.208:29656,1278e67b0f6523c20e665109dd092ef20d6fd70e@45.67.230.23:26656,04a0036ff421f2dd8f46cca1fae9a893624bd868@95.216.14.72:29656,98907b8c92c003aa2d003bb5d47e5ae6e34b0732@77.51.200.79:46656,9d761ce1e1dc54ded3ab82ce0256c27631b5e82c@173.212.241.80:43656,b18f05bafd90cde6391d41880fc2d2461034a5de@20.189.72.168:26656,48283100d4cf8068dc16ef1b10aacf092303ec2f@65.109.85.170:47656,e4b7228ccadf3180e6e323aa4c0c97946ac054dc@65.109.112.20:11134,c2c7344a10a39040592a8aa156ef9da17700d9a2@45.84.0.252:26656,87014496b4dd9d7b8336abac56119d34f93ef240@84.46.241.39:26656,654e76e7d4b27fdb3a931fe2d44c51184d8a5731@5.161.78.48:26656,6cf1dbaf1cfee65f14421ba5ac5b165ebe7b0d0a@5.9.97.58:26656,fcb82df30d2056c3af024fb389e173d683fe8229@65.108.105.48:19756,0005b1e2c88dbad64b71a706016b340f2afa982f@109.123.244.56:26686,5bf83be8dfe52fe2c204300f1e9b1449487ce5af@88.99.164.158:1176,8b0b427b4567a7a66f05fab1146ee97b52ad7958@93.189.30.119:26656,7c2ea36064077da73d0ad5b60d8ef215acbee50b@161.97.79.100:36656,eb2bc8a892148829a35b15674434bb6740131ffe@206.189.37.168:35656,37933575674b670c91a6aa336b1dd910057465a9@157.90.208.222:60556,d0d604e5c22d5be38adaea41fc9694a26dc143ac@217.79.255.69:26656,67be97f5ef69a4f149fbef7970ba888e5b2c2cff@65.108.231.124:16656,8638d61b59d2861f23d2be150b9706fad7cf5039@176.124.220.206:26656,275f61d9504fa59b9696f04f32c84e810546a4d9@84.46.240.255:26656,c8458dfd9d19f75e51ffec68019e8783c6c062a3@113.187.125.157:26656,12b146cd82c7142e9d8aeb4f246499927ecb1c0f@217.13.223.167:36656,7dcfb78dc49d46bb9dd1ff4030817da1f71eb0b7@84.46.240.248:26656,a502800f1e99446243d17db93778f9c8eaa3eee0@84.46.241.37:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nolus/config/config.toml
```
