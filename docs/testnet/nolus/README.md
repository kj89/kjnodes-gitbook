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
peers="8b0b427b4567a7a66f05fab1146ee97b52ad7958@93.189.30.119:26656,387393e38531ac010f500d294505232a77c88766@45.33.32.8:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:43656,c2c7344a10a39040592a8aa156ef9da17700d9a2@45.84.0.252:26656,7a1fc4d1cc0ffec7db6a2a15496136e62561b162@161.97.146.108:26656,28cdf59b342cb19fe488e99fab754ccc90c379e3@185.196.21.104:26656,048df3fd3100c57b1a661aef3336a7c681657928@185.193.17.226:26656,e0ab3276d94a8fbdf04b0b9eb95df22f7037eb89@167.235.31.186:34656,66a81705eb9a8ec9c12726acbd82366ed0143724@79.137.248.243:26656,5289137e6134895c5b3b82a9847869f2a889cdc0@65.108.97.58:2776,236a2626ad46bb671b200883b6105350310372ef@135.181.81.65:37656,dd22261eb9101fb33110a715056bc949066b4113@79.137.33.26:16656,e0aac09f3de68abf583b0e3994228ee8bd19d1eb@168.119.124.130:45659,33f4b7f56b6708526f0638162f020394de0ce5e9@65.21.229.33:28656,5b7092ce1624e8a23a5d90897c4c5231fb7b1238@185.245.183.172:16656,98907b8c92c003aa2d003bb5d47e5ae6e34b0732@77.51.200.79:46656,367fb20ca2380ebbb73eb19b772564383b0f37ee@65.21.123.172:26656,4f2f4bc6a3ac511cacbcf8faf04683684a44313b@38.242.221.91:26656,03ec7af23216082eeccc690b7bdcbe497bf2dcf8@136.243.88.91:9000,6cf1dbaf1cfee65f14421ba5ac5b165ebe7b0d0a@5.9.97.58:26656,6b14535ff005667f324f8439a55a21ee2f170d12@95.217.211.81:26656,0130c7e5dbc56f4a933215b2ea25cd1ac80efd41@95.31.16.222:26656,d6f7b2380e994c6b8f6fcb05b4a326ae2d1f202a@37.123.114.30:26656,fcb82df30d2056c3af024fb389e173d683fe8229@65.108.105.48:19756,0bc65a562eff399463fcf18f54716e32054e4cf4@188.166.88.185:26656,5bf83be8dfe52fe2c204300f1e9b1449487ce5af@88.99.164.158:1176,df5523a9d35328716337343cbeea3063cd4fa9b3@65.108.206.118:61256,e6e48680fa62c03bed242c52eb21d3cbe44a6752@46.8.210.144:26856,d8088d91bdbf2ccdf59f0b3ee1c1b07e8cb60798@195.201.237.185:11656,647c0cefcd470b6d92b03b3511a0a4defe2a30dd@135.181.208.169:31656,bab1600bf84b25635483483cd69fa19717eb5852@203.238.191.195:26656,a9cce28334e6111c74934140ef915abb20968d2f@89.252.21.37:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27016,43e6a1f6f6d0d8d1fd7e7f8e13ca92ca3969433e@65.21.207.188:26656,67be97f5ef69a4f149fbef7970ba888e5b2c2cff@65.108.231.124:16656,d0ad1c1b427f5924a74f64acd18155684d8b3089@109.123.251.34:26656,a12f0c225332ab006fbc46d58706669bf44f52e0@123.31.73.177:26656,12b146cd82c7142e9d8aeb4f246499927ecb1c0f@217.13.223.167:36656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nolus/config/config.toml
```
