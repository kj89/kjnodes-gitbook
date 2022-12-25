# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/nolus.png" width="150" alt=""><figcaption></figcaption></figure>

Nolus aims to be the leading DeFi Lease platform. The protocol  intends to become a tool for empowering people, simple to use, and highly efficient.

**Chain ID**: nolus-rila | **Latest Version Tag**: v0.1.39 | **Wasm**: ON

[Website](https://www.nolus.io) | [Discord](https://discord.gg/nolus-protocol) | [Twitter](https://twitter.com/NolusProtocol)


## Public endpoints

* rpc: [https://nolus-testnet.rpc.kjnodes.com](https://nolus-testnet.rpc.kjnodes.com)
* api: [https://nolus-testnet.api.kjnodes.com](https://nolus-testnet.api.kjnodes.com)

## Peering

**state-sync**

```
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@nolus-testnet.rpc.kjnodes.com:43656
```

**seed-node**

```
3f472746f46493309650e5a033076689996c8881@nolus-testnet.rpc.kjnodes.com:43659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/nolus-testnet/addrbook.json > $HOME/.nolus/config/addrbook.json
```

**live-peers** (34)
```
peers="a7a48a15db2140201f22047ee9abbc0b259c1f92@194.163.129.102:26656,681ecb99467dd00a586d9499a1002f2829f1a02d@65.109.85.208:29656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:43656,8b0b427b4567a7a66f05fab1146ee97b52ad7958@93.189.30.119:26656,d694df8e90ddf6102be5c825e57fc58d55217629@143.198.205.193:26656,1b8bd4b240836a80920dde13b19f6089851af3ca@65.108.238.217:11234,7a1fc4d1cc0ffec7db6a2a15496136e62561b162@161.97.146.108:26656,55fd96d4b7ccbc99c9b3be44d9071dc15d8341fe@185.241.151.41:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27016,4152f28255f59b366df88fd4ac08d8b4c15d0d30@46.151.24.237:26656,5289137e6134895c5b3b82a9847869f2a889cdc0@65.108.97.58:2776,cb989bd3f416226bfd71631c0348ea38a1df3ec0@65.109.106.91:23656,b6c8dc38a5dba19a3f10d23b3572065db9265fa3@65.109.85.225:9000,fcb82df30d2056c3af024fb389e173d683fe8229@65.108.105.48:19756,67be97f5ef69a4f149fbef7970ba888e5b2c2cff@65.108.231.124:16656,66a81705eb9a8ec9c12726acbd82366ed0143724@79.137.248.243:26656,d788696b4ea9ddd295f86f0cb10a6be86a94764c@161.97.136.72:26656,e17967a4b9a8183d12659fab318a4f81673f6a51@185.245.183.172:37656,560ca78a1e7b5c1f3ba6fe50c3b43ef5476c9bff@116.102.89.243:26656,e0aac09f3de68abf583b0e3994228ee8bd19d1eb@168.119.124.130:45656,1c50df97e155afa50189f48daf41be046c7fe682@85.10.202.135:32656,616f417473062edb5e534f403fccbf6f50232882@176.126.87.161:26656,654e76e7d4b27fdb3a931fe2d44c51184d8a5731@5.161.78.48:26656,ac38d6ef4cc254c689bcd6bcaf2a359672e4405b@77.238.148.219:26656,bbf62211cf012f816c1ab9ffb8aba790e9b7a4a9@149.102.137.76:43656,6d5921160c688c2e4e3b510fcfa48496e74cf2c6@80.92.204.247:37656,fcc3160a91d360e68b2b7459ec57f2c550a45dce@167.71.222.34:26656,55acbb36f6e18ce9d5034c1e0f615bf13ee1ae27@195.2.80.63:43656,c836a0a1ba952a83308fff0a6dd418e0d0d94481@37.252.74.190:37656,f940d6da3187d4b9a20f4302166fa905bf83e10b@94.103.83.30:26656,12b146cd82c7142e9d8aeb4f246499927ecb1c0f@217.13.223.167:36656,ea777d59ec44f1739c6a4908942db43966a1f475@45.55.59.70:26656,19022cad75ccd8a3fb7f84d4adc37a48fdd201e2@77.91.123.62:37656,e711b6631c3e5bb2f6c389cbc5d422912b05316b@213.239.216.252:15256"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.nolus/config/config.toml
```
