# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/gitopia.png" width="150" alt=""><figcaption></figcaption></figure>

Gitopia is the next-generation Code Collaboration Platform fuelled by  a decentralized network and interactive token economy. It is designed  to optimize the open-source software development process through  collaboration, transparency, and incentivization.

**Chain ID**: gitopia-janus-testnet-2 | **Latest Version Tag**: v1.2.0 | **Wasm**: OFF

[Website](https://gitopia.com/) | [Discord](https://discord.gg/hFTXCGNYDZ) | [Twitter](https://twitter.com/gitopiaDAO)




## Chain explorer
[https://explorer.kjnodes.com/gitopia-testnet](https://explorer.kjnodes.com/gitopia-testnet)

## Public endpoints

* api: [https://gitopia-testnet.api.kjnodes.com](https://gitopia-testnet.api.kjnodes.com)
* rpc: [https://gitopia-testnet.rpc.kjnodes.com](https://gitopia-testnet.rpc.kjnodes.com)
* grpc: [https://gitopia-testnet.grpc.kjnodes.com](https://gitopia-testnet.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@gitopia-testnet.rpc.kjnodes.com:41656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@gitopia-testnet.rpc.kjnodes.com:41659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/gitopia-testnet/addrbook.json > $HOME/.gitopia/config/addrbook.json
```

**live-peers** (21)
```bash
peers="f9b892ea2e8ed8aa83f7b98e7e47371c23b01924@213.239.207.175:36656,798cf016b5150592badc8257402312fc50b7361d@65.108.45.200:26878,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:41656,399d4e19186577b04c23296c4f7ecc53e61080cb@34.143.189.236:26656,9bb344d83fc1fafc4bce6b8e4a95b82f37ac4f31@82.208.20.136:26656,63381c5528ed8ca93f9ba31008a9630d21b29a97@142.132.152.46:46656,619a23818cddd40d0b9f57e9754b719da13609bc@65.108.108.52:24656,099052dd7c948a76afdc952b32cd733933c5a9ba@65.21.192.90:10656,f0b8227e40f25eaec0e25b9e91ca199d2d9a1ecb@167.86.94.177:656,03073657e8bc5bcf71e7fd8df281ab8dcbc8821a@45.151.122.130:656,e17763e03ef6819b6f549b97abe9da7a1a7eeac8@164.68.121.241:656,4cd60a4dd4211d38d948a86a614f1fd8d3d274eb@75.119.153.139:656,d238167163e6d34ff8a500afe23386160805d387@193.46.243.144:36656,59a99a10a28baeda8535598acef9abb706ec5dbc@45.85.249.132:656,007d2419fea80aee707d009af0153f5105c53379@38.242.139.164:656,417311f0ceeff950dd9bf0f389e5a9c5ed8d22cd@146.190.88.155:41656,7d819fa869f7c5b42c2c7a9538e1a9e7a52cfdee@65.108.226.26:24656,df5c15eeaeecb2116ab947e10c065353d762f5ad@185.163.124.151:41656,ba614c2b5beae6df39a4310043294ffde60e8e8d@45.85.250.147:26656,4e0e57bcac8aa2bc3188d5b7845eeee61a61f3f0@194.163.170.165:26656,0c31077af45cb4f0424e58c91b0a917c36a90fd9@65.108.195.235:16656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gitopia/config/config.toml
```
