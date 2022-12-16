# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/haqq.png" width="150" alt=""><figcaption></figcaption></figure>

Haqq is the blockchain network that issues Islamic Coin,  its native cryptocurrency. Haqq is fast, trusted and  compatible with thousands of applications around the world.

**Chain ID**: haqq_54211-3 | **Latest Version Tag**: v1.3.0 | **Wasm**: OFF

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
peers="62d44513c7fd5aafa65773e5c015ca032f8eea4a@213.239.213.179:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:35656,ce080696d69228597caf0e80920dfe1bae2dcd54@95.217.12.131:26656,f909e50b6f27a964ae20d982d300f1137cb3bef2@144.76.90.130:30656,88fb8b08f2184cf9390826eeb470b8b693a7e68b@185.202.223.85:36656,9eb507f9365313dbe7f426050fec9648298f58ee@109.205.183.51:26656,ec8a285e36888bd3134266b8ba668b48c327e6bf@142.132.202.50:36656,62bf004201a90ce00df6f69390378c3d90f6dd7e@34.90.129.213:26656,adce9d7f72360f6d66c4248b8db8de151b877130@167.235.132.152:26656,23a1176c9911eac442d6d1bf15f92eeabb3981d5@34.91.81.33:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.haqqd/config/config.toml
```
