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

**live-peers** (10)
```
peers="23a1176c9911eac442d6d1bf15f92eeabb3981d5@34.91.81.33:26656,2d13d679b64e1a574904a140f72815644ec71131@65.21.133.125:30656,927a323649e7dd8d4c75da6e5edaee439652b46f@65.109.92.241:20116,de231cd155362b2687dca190a744bf839ce4ce63@23.88.112.123:26656,064fe9fe19fe5552b2d4922d659466e583f42b22@95.216.2.219:26658,62bf004201a90ce00df6f69390378c3d90f6dd7e@34.90.129.213:26656,54e81994c61bbb6c414f8ab0a606a7edda138a3b@95.216.154.100:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:35656,7f2828e3910a4b165a65e5bfb2465c1e809bad3b@65.108.48.182:26656,32a8eec046b95e8646ff0810b4596dc7083a0beb@65.108.145.131:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.haqqd/config/config.toml
```
