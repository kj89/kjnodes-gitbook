# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/haqq.png" width="150" alt=""><figcaption></figcaption></figure>

Haqq is the blockchain network that issues Islamic Coin,  its native cryptocurrency. Haqq is fast, trusted and  compatible with thousands of applications around the world.

**Chain ID**: haqq_54211-3 | **Latest Version Tag**: v1.2.1 | **Wasm**: OFF

Website: [https://islamiccoin.net](https://islamiccoin.net)


## Public endpoints

* rpc: [https://haqq-testnet.rpc.kjnodes.com](https://haqq-testnet.rpc.kjnodes.com)
* api: [https://haqq-testnet.api.kjnodes.com](https://haqq-testnet.api.kjnodes.com)

## Peering

**state-sync**

```
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@haqq-testnet.rpc.kjnodes.com:35656
```

**seed-node**

```
3f472746f46493309650e5a033076689996c8881@haqq-testnet.rpc.kjnodes.com:35659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/haqq-testnet/addrbook.json > $HOME/.haqqd/config/addrbook.json
```

**live-peers** (10)
```
peers="35e1bf6fda8a37c9c4872527a30b1fe26b0a155f@45.13.59.201:26656,f57fae1bdea281392b563a58978a2d8c0a37725f@95.217.233.234:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:35656,0d5a3f0be2d61efe4151fe58c94d6e5299210e8d@65.109.12.191:26656,4d996674f678ebc035165d7d7c894010b32420a2@65.109.69.240:36656,2d13d679b64e1a574904a140f72815644ec71131@65.21.133.125:30656,7e45021be5e7754b62b6016305ba26f8bf40beda@142.132.199.27:20116,f909e50b6f27a964ae20d982d300f1137cb3bef2@144.76.90.130:30656,a3e587b8ac1ee3a1563b43388d2bd475c890a6c0@65.109.81.240:26656,562a589b82682f695344bc4a9d7a2fcb5a5a4d80@65.21.60.82:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.haqqd/config/config.toml
```
