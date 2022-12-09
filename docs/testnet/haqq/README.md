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
peers="1c5a4624a7f1a71e240ae2df82e97d5e9f46ff5c@88.99.214.188:60956,849d98423e3f757233bef91d7b80937329d7684f@162.19.131.173:26656,562a589b82682f695344bc4a9d7a2fcb5a5a4d80@65.21.60.82:26656,ee4db669ed2ff87cb2a47f848fa061517eb47737@161.97.151.46:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:35656,0d5a3f0be2d61efe4151fe58c94d6e5299210e8d@65.109.12.191:26656,de231cd155362b2687dca190a744bf839ce4ce63@23.88.112.123:26656,9eb507f9365313dbe7f426050fec9648298f58ee@109.205.183.51:26656,88b8b733d8b96e9a518c1a8bea4dbc5bf896026e@5.161.156.183:26656,62bf004201a90ce00df6f69390378c3d90f6dd7e@34.90.129.213:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.haqqd/config/config.toml
```
