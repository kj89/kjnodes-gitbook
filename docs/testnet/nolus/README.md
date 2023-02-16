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
peers="d8088d91bdbf2ccdf59f0b3ee1c1b07e8cb60798@195.201.237.185:11656,8b0b427b4567a7a66f05fab1146ee97b52ad7958@93.189.30.119:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:43656,0005b1e2c88dbad64b71a706016b340f2afa982f@109.123.244.56:26686,7a1fc4d1cc0ffec7db6a2a15496136e62561b162@161.97.146.108:26656,387393e38531ac010f500d294505232a77c88766@45.33.32.8:26656,9951244a6f7cc04d30e7a122dfbee14c8ca5b542@185.239.208.142:656,e8473dede42e7f0d4668a24d909a5708c5a04a3e@65.108.78.116:11656,85c5ef9ff695574abdf1ab38fb1196bc6482aec5@89.252.21.37:26656,e0ab3276d94a8fbdf04b0b9eb95df22f7037eb89@167.235.31.186:34656,e0aac09f3de68abf583b0e3994228ee8bd19d1eb@168.119.124.130:45659,5b7092ce1624e8a23a5d90897c4c5231fb7b1238@185.245.183.172:16656,2d2e38e8958c54e2ccd8bed0f5651567da4db99b@137.184.133.198:26656,6cf1dbaf1cfee65f14421ba5ac5b165ebe7b0d0a@5.9.97.58:26656,0bc65a562eff399463fcf18f54716e32054e4cf4@188.166.88.185:26656,7c2ea36064077da73d0ad5b60d8ef215acbee50b@161.97.79.100:36656,60c57c5b7215c84260249768cf66ae550142af9f@141.98.169.25:26656,6b14535ff005667f324f8439a55a21ee2f170d12@95.217.211.81:26656,89d4b6b28f4399f49c82f9b0e891463f07f26cfe@95.216.65.177:29656,28cdf59b342cb19fe488e99fab754ccc90c379e3@185.196.21.104:26656,43294ababb32039af22c5bac16451d7a2b056f33@77.94.99.52:26656,5bf83be8dfe52fe2c204300f1e9b1449487ce5af@88.99.164.158:1176,df5523a9d35328716337343cbeea3063cd4fa9b3@65.108.206.118:61256,00ce364657c9b520febb563beb7c4a1c9fc2d352@195.2.70.100:26656,1278e67b0f6523c20e665109dd092ef20d6fd70e@45.67.230.23:26656,b6c8dc38a5dba19a3f10d23b3572065db9265fa3@65.109.85.225:9000,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27016,769552416bbe807f319e2fa6125a40969b254182@65.108.108.52:18656,538e2a3d6e96cd7bc0635eaa3f8f3695f26503a7@65.108.104.167:21656,67be97f5ef69a4f149fbef7970ba888e5b2c2cff@65.108.231.124:16656,048df3fd3100c57b1a661aef3336a7c681657928@185.193.17.226:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nolus/config/config.toml
```
