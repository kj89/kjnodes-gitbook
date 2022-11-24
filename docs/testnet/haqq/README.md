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
peers="ee0328492fd21eee29ecbde19b52dfde6bd5da54@176.9.146.72:46656,0d5a3f0be2d61efe4151fe58c94d6e5299210e8d@65.109.12.191:26656,f4442b1ed7f64504f44ed85c89e38cfb2b19ef91@65.108.77.250:26641,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:35656,e754d614c1b96b5738b59bac601aae445cd15189@65.108.230.245:26656,f909e50b6f27a964ae20d982d300f1137cb3bef2@144.76.90.130:30656,ec8a285e36888bd3134266b8ba668b48c327e6bf@142.132.202.50:36656,2d13d679b64e1a574904a140f72815644ec71131@65.21.133.125:30656,7f4b4501af5f744210dcad95fb9b3915283fd0e9@185.244.182.203:26656,986cf051df64fc21a32b7596c7264e51b25ea3dc@65.109.50.189:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.haqqd/config/config.toml
```
