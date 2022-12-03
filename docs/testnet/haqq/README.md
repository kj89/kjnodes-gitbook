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
peers="9e894879ff46d8a9344cfd478abad423f568968a@159.69.69.183:26656,62d44513c7fd5aafa65773e5c015ca032f8eea4a@213.239.213.179:26656,88f134e7caad68e01554f4d648069c443a21fd4c@135.181.35.46:36656,88b8b733d8b96e9a518c1a8bea4dbc5bf896026e@5.161.156.183:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:35656,54e81994c61bbb6c414f8ab0a606a7edda138a3b@95.216.154.100:26656,b6554c65e24f46e2834b018ac1790f9c1bcd2c74@195.201.165.123:20116,2d13d679b64e1a574904a140f72815644ec71131@65.21.133.125:30656,a90a13b70727ae37267c3cd2bc0b287f8ab25fa8@195.54.41.122:22656,562a589b82682f695344bc4a9d7a2fcb5a5a4d80@65.21.60.82:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.haqqd/config/config.toml
```
