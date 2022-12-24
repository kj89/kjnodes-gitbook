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

**live-peers** (20)
```
peers="681ecb99467dd00a586d9499a1002f2829f1a02d@65.109.85.208:29656,9c2e998a64480dd06d36806a9cc85fa2692cd8f0@46.0.203.78:23636,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:43656,ebaae5968cd32c423c277a3dc8e0a09615078ec0@65.108.126.35:24656,8b0b427b4567a7a66f05fab1146ee97b52ad7958@93.189.30.119:26656,67be97f5ef69a4f149fbef7970ba888e5b2c2cff@65.108.231.124:16656,12b146cd82c7142e9d8aeb4f246499927ecb1c0f@217.13.223.167:36656,d06eccc10c08784a56836ddd1278614f2a50f82f@164.68.127.58:36656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27016,df5523a9d35328716337343cbeea3063cd4fa9b3@65.108.206.118:61256,8d636705234cc52f6cce11dc46fc826a47b622ff@65.109.84.215:36656,d694df8e90ddf6102be5c825e57fc58d55217629@143.198.205.193:26656,56f14005119e17ffb4ef3091886e6f7efd375bfd@34.241.107.0:26656,5c236704215735ea722a3ca742a5161c2e871ec6@65.109.85.209:29656,6cb8e63bf00d37399454ab24b6cf316062b90117@199.175.98.110:36656,7a1fc4d1cc0ffec7db6a2a15496136e62561b162@161.97.146.108:26656,7f26067679b4323496319fda007a279b52387d77@63.35.222.83:26656,56c262dbc7ccc509f1768768d87f8a53bf037f02@65.21.92.150:26656,5f68a93ac48f0382d214ed4d0b9c5d4313e5dd52@173.212.223.233:26656,16db477834a9bdafef61baf9f2c0f5bd4eadeedb@13.48.57.97:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.nolus/config/config.toml
```
