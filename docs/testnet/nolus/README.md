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

**live-peers** (32)
```
peers="df5523a9d35328716337343cbeea3063cd4fa9b3@65.108.206.118:61256,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:43656,5289137e6134895c5b3b82a9847869f2a889cdc0@65.108.97.58:2776,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27016,8b0b427b4567a7a66f05fab1146ee97b52ad7958@93.189.30.119:26656,71cb32264e19b25fc313d0ff8baf24fe948576a1@65.109.30.12:60656,7a1fc4d1cc0ffec7db6a2a15496136e62561b162@161.97.146.108:26656,fcb82df30d2056c3af024fb389e173d683fe8229@65.108.105.48:19756,c2e5fbe1a0acc345889ea778079f6ae8001f6f87@78.159.115.21:26656,fb7c2278380a7484ab2b06a9cc9f3f6f522d7b54@46.101.106.146:26656,43b2582d9f63b46df12879729e8d3d1daa899ef4@144.126.154.230:26656,93a2be8b44d56906ce3ff9d92494a69def225207@173.212.199.21:26656,9c2e998a64480dd06d36806a9cc85fa2692cd8f0@46.0.203.78:23636,4152f28255f59b366df88fd4ac08d8b4c15d0d30@46.151.24.237:26656,67be97f5ef69a4f149fbef7970ba888e5b2c2cff@65.108.231.124:16656,1bcd840dc4f8e73da6f13f6281ee3e7823a89721@65.108.227.112:46656,d694df8e90ddf6102be5c825e57fc58d55217629@143.198.205.193:26656,0a2dd0e7331154b40b0d0ddf9834bca9c93a2e53@194.190.152.23:26656,5f68a93ac48f0382d214ed4d0b9c5d4313e5dd52@173.212.223.233:26656,6d5921160c688c2e4e3b510fcfa48496e74cf2c6@80.92.204.247:37656,9d761ce1e1dc54ded3ab82ce0256c27631b5e82c@173.212.241.80:43656,59dbd8203d88a96006a7057db27438e7dc3eae3c@125.164.23.9:14656,de7b54f988a5d086656dcb588f079eb7367f6033@34.244.137.169:26656,1bf4f60cdf17be26b4b22266e589097e7a6c3a6b@38.242.198.110:37656,2c48f832db11915efd85c8de84f1d779eec565f0@185.245.182.58:43656,56f14005119e17ffb4ef3091886e6f7efd375bfd@34.241.107.0:26656,ac38d6ef4cc254c689bcd6bcaf2a359672e4405b@77.238.148.219:26656,12b146cd82c7142e9d8aeb4f246499927ecb1c0f@217.13.223.167:36656,7f4a1876560d807bb049b2e0d0aa4c60cc83aa0a@63.32.88.49:26656,66a81705eb9a8ec9c12726acbd82366ed0143724@79.137.248.243:26656,dd9e346624ad3cadc723a21c3003f70bf6f3e407@217.199.117.158:37656,fed075577012e8223973d2b678e09ae9e32dfab8@167.71.222.34:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.nolus/config/config.toml
```
