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

**live-peers** (40)
```bash
peers="8b0b427b4567a7a66f05fab1146ee97b52ad7958@93.189.30.119:26656,5b7092ce1624e8a23a5d90897c4c5231fb7b1238@185.245.183.172:16656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:43656,7a1fc4d1cc0ffec7db6a2a15496136e62561b162@161.97.146.108:26656,28cdf59b342cb19fe488e99fab754ccc90c379e3@185.196.21.104:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27016,d8088d91bdbf2ccdf59f0b3ee1c1b07e8cb60798@195.201.237.185:11656,3be781c50aac85518bb3cfb8620528cbc5dacd67@146.190.45.222:26656,e0aac09f3de68abf583b0e3994228ee8bd19d1eb@168.119.124.130:45659,33f4b7f56b6708526f0638162f020394de0ce5e9@65.21.229.33:28656,03ec7af23216082eeccc690b7bdcbe497bf2dcf8@136.243.88.91:9000,f09a8ba06a00d1edc517995040313732f94c2b56@95.214.55.155:18656,e0ab3276d94a8fbdf04b0b9eb95df22f7037eb89@167.235.31.186:34656,8d636705234cc52f6cce11dc46fc826a47b622ff@65.109.84.215:36656,048df3fd3100c57b1a661aef3336a7c681657928@185.193.17.226:26656,0bc65a562eff399463fcf18f54716e32054e4cf4@188.166.88.185:26656,6b14535ff005667f324f8439a55a21ee2f170d12@95.217.211.81:26656,51abbd224cbeaeb6d1a962d07894b356d174e948@38.242.248.112:26656,654e76e7d4b27fdb3a931fe2d44c51184d8a5731@5.161.78.48:26656,0130c7e5dbc56f4a933215b2ea25cd1ac80efd41@95.31.16.222:26656,769552416bbe807f319e2fa6125a40969b254182@65.108.108.52:18656,387393e38531ac010f500d294505232a77c88766@45.33.32.8:26656,00ce364657c9b520febb563beb7c4a1c9fc2d352@195.2.70.100:26656,55acbb36f6e18ce9d5034c1e0f615bf13ee1ae27@195.2.80.63:43656,f77c45399c1dea69fcc48ff15995e8387169249a@80.85.242.54:26656,e62dd608a302ba4f815a7cd3cf3d7facafa0e171@135.181.123.154:16656,982e4b1fae74b220b3650cf2caa04ada8cf65a52@89.117.55.120:26656,d6f7b2380e994c6b8f6fcb05b4a326ae2d1f202a@37.123.114.30:26656,0005b1e2c88dbad64b71a706016b340f2afa982f@109.123.244.56:26686,fcb82df30d2056c3af024fb389e173d683fe8229@65.108.105.48:19756,2d500ae8bddfa548ee0fb0ed969709d78a4015af@144.168.47.230:26656,cb989bd3f416226bfd71631c0348ea38a1df3ec0@65.109.106.91:23656,5bf83be8dfe52fe2c204300f1e9b1449487ce5af@88.99.164.158:1176,19c6579ebb9d869e61c4dd082dc414cac6f799f3@46.4.122.235:26656,c6dfc10a46da7ba0677f294c156a4e686c96629f@207.154.242.36:26656,55b85dda16f276027c2318e172e487dbf95f6723@185.244.182.79:37656,4b418e9dbc5e45c39ee8329b0d1bae42b7eface1@136.243.103.32:26656,67be97f5ef69a4f149fbef7970ba888e5b2c2cff@65.108.231.124:16656,12b146cd82c7142e9d8aeb4f246499927ecb1c0f@217.13.223.167:36656,b58f28536e9170b919a24242387e7c41b97371f1@113.161.144.108:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nolus/config/config.toml
```
