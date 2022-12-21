# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/haqq.png" width="150" alt=""><figcaption></figcaption></figure>

Haqq is the blockchain network that issues Islamic Coin,  its native cryptocurrency. Haqq is fast, trusted and  compatible with thousands of applications around the world.

**Chain ID**: haqq_54211-3 | **Latest Version Tag**: v1.3.0 | **Wasm**: OFF

Website: [https://islamiccoin.net](https://islamiccoin.net) | [Discord](https://discord.gg/hU9MHG5kZq) | [Twitter](https://twitter.com/Islamic_Coin)


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
peers="23a1176c9911eac442d6d1bf15f92eeabb3981d5@34.91.81.33:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:35656,064fe9fe19fe5552b2d4922d659466e583f42b22@95.216.2.219:26658,927a323649e7dd8d4c75da6e5edaee439652b46f@65.109.92.241:20116,de231cd155362b2687dca190a744bf839ce4ce63@23.88.112.123:26656,ce080696d69228597caf0e80920dfe1bae2dcd54@95.217.12.131:26656,6ce864d853904ebef9400528f129d8fefa6f1827@91.211.251.232:36656,62bf004201a90ce00df6f69390378c3d90f6dd7e@34.90.129.213:26656,0760b7526738dac0af14b5e3d3b62e49c63dd490@185.154.14.142:26656,f57fae1bdea281392b563a58978a2d8c0a37725f@95.217.233.234:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.haqqd/config/config.toml
```
