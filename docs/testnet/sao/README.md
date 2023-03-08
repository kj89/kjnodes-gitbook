# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/sao.png" width="150" alt=""><figcaption></figcaption></figure>

SAO Network is a secure and decentralized Web3 storage infrastructure  based on Cosmos SDK and IPFS protocol. It aims to facilitate the adoption  of Web3 storage, support the growing demand for Web3 applications and  allow for a more decentralized way of storing and accessing data.

**Chain ID**: sao-testnet0 | **Latest Version Tag**: v0.0.9 | **Wasm**: OFF

[Website](https://www.sao.network) | [Discord](https://discord.gg/f4xzfvPhhA) | [Twitter](https://twitter.com/SAONetwork)




## Chain explorer
[https://explorer.kjnodes.com/sao-testnet](https://explorer.kjnodes.com/sao-testnet)

## Public endpoints

* api: [https://sao-testnet.api.kjnodes.com](https://sao-testnet.api.kjnodes.com)
* rpc: [https://sao-testnet.rpc.kjnodes.com](https://sao-testnet.rpc.kjnodes.com)
* grpc: [https://sao-testnet.grpc.kjnodes.com](https://sao-testnet.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@sao-testnet.rpc.kjnodes.com:49656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@sao-testnet.rpc.kjnodes.com:49659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/sao-testnet/addrbook.json > $HOME/.sao/config/addrbook.json
```

**live-peers** (28)
```bash
peers="b5230bd84d4d7576690d90a39398f197e629fe9d@116.202.227.117:49656,7075469d8ed68a423e065b67bcde29b6ca4266fd@142.132.248.253:65528,61e9e3927c1d25d91e8fefbdc880791e7974bfb5@159.223.19.154:27656,70502c3cbd5aabc12245f44bebf767d83fe76434@134.209.255.7:20656,658f473c2399f87c5e5ff4d329c8c53ae9f399e0@46.101.232.154:26656,266d8a31a1cecf8d2f673e4cb65ea736173428e9@165.22.76.250:20656,244c464e3d500ee3f242fa3a10ae50d4cd02fc26@164.90.221.101:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:49656,8c6201e793348d8f89dedcae6df3cd36198477fd@94.46.187.220:26656,72a2bbeb32621600de4b2a6ed42b11bf3be1105c@146.190.40.115:20656,a4a02db4e2753ebb13a77eb53531d87e566cae7b@27.71.128.102:26656,8167fbcc27bbf431f36b9a980c7ec57803502f2e@206.189.81.5:20656,0c77942550c78ae8939b691b725a9dd7ffa4d864@185.219.142.182:27656,47971c889b727897dfc753ca93a15d8e1ce9cd5a@3.140.188.3:26656,ada0a0b4b5b3d290cae51b946b33a1079d00df72@185.197.250.35:27656,8e3091665e048465393d93bb9a6c25cb760b4f64@65.109.24.223:24556,cec1fdc272372d8254aaa33dcf12016c6ad1dbf6@65.109.24.121:26656,91b67dd0d2904d95748e1ec5311e39033cfeaabc@65.109.92.240:1076,6a23f4da326ceeab0a6e112c25ff39715439b8ce@167.86.75.138:49656,746c2645f49602887cc6e38bb58c79860de93c1a@157.245.152.0:24556,0d9a4d351e9e88362f39bc50d7e12900d534dc47@134.209.104.239:27656,aa269fc09dc0b73e45f1c6b514aea634fa0193c7@45.88.223.247:27656,a22a3ad8f847ab87bd64d0b9365b870750bde4e5@143.198.204.248:20656,ec7e0b075202f836feac71f017a90e0d83674cb8@65.108.9.164:24556,0a661ed79b169c7c2b0f289c436e35900bb0de90@157.97.108.38:24556,7226702dd45f4bee9f35b6a20b5b4e51f963fae8@188.166.187.23:27656,39320c6f494f7e091ce9b40e7ed49b1abb6b6c5d@95.217.57.232:46656,e711b6631c3e5bb2f6c389cbc5d422912b05316b@213.239.216.252:41256"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.sao/config/config.toml
```
