# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/haqq.png" width="150" alt=""><figcaption></figcaption></figure>

Haqq is the blockchain network that issues Islamic Coin,  its native cryptocurrency. Haqq is fast, trusted and  compatible with thousands of applications around the world.

**Chain ID**: haqq_54211-3 | **Latest Version Tag**: v1.3.0 | **Wasm**: OFF

[Website](https://islamiccoin.net) | [Discord](https://discord.gg/hU9MHG5kZq) | [Twitter](https://twitter.com/Islamic_Coin)


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

**live-peers** (9)
```
peers="7f2828e3910a4b165a65e5bfb2465c1e809bad3b@65.108.48.182:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:35656,2d13d679b64e1a574904a140f72815644ec71131@65.21.133.125:30656,de231cd155362b2687dca190a744bf839ce4ce63@23.88.112.123:26656,62bf004201a90ce00df6f69390378c3d90f6dd7e@34.90.129.213:26656,59af99085c961a6a5c8dc4bc8b3abffda16ddccb@135.181.38.62:26656,f57fae1bdea281392b563a58978a2d8c0a37725f@95.217.233.234:26656,ed145a35b436878c1f1c10634bd18600f3696e17@95.217.181.142:26656,1fefb6b75431482502e125a290deba1e7e539d4e@135.181.148.11:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.haqqd/config/config.toml
```
