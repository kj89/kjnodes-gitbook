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
peers="fd53be6145264c86f2db22659141c925e119794c@138.201.155.226:12656,9eb507f9365313dbe7f426050fec9648298f58ee@109.205.183.51:26656,2d13d679b64e1a574904a140f72815644ec71131@65.21.133.125:30656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:35656,d648d598c34e0e58ec759aa399fe4534021e8401@109.205.180.81:26656,88b8b733d8b96e9a518c1a8bea4dbc5bf896026e@5.161.156.183:26656,b70802dd7c7705f1c7d5535f2ad529c66bdbdee1@95.217.236.79:12656,7f4b4501af5f744210dcad95fb9b3915283fd0e9@185.244.182.203:26656,0760b7526738dac0af14b5e3d3b62e49c63dd490@185.154.14.142:26656,e0e50095bf450bb28150649be569331f97be9726@159.69.223.112:12656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.haqqd/config/config.toml
```
