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
peers="0c0e74c0550f5c394537f81617a6fd8480381654@94.130.142.27:36656,62bf004201a90ce00df6f69390378c3d90f6dd7e@34.90.129.213:26656,562a589b82682f695344bc4a9d7a2fcb5a5a4d80@65.21.60.82:26656,f57fae1bdea281392b563a58978a2d8c0a37725f@95.217.233.234:26656,89d067dc2a046f7b7c1c787740fff18962bf199f@95.165.149.94:29656,26a5bd6fb59f4dcd25f20bbc53b88860b2598f7d@65.21.91.50:35656,b70802dd7c7705f1c7d5535f2ad529c66bdbdee1@95.217.236.79:12656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:35656,022360b6d3bbae324b0cca90f80f6322576e2b42@135.181.109.140:12656,b9d04ade732a3bb91b91e279c36c6f2c12d522d3@109.107.187.78:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.haqqd/config/config.toml
```
