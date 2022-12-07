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
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:35656,d648d598c34e0e58ec759aa399fe4534021e8401@109.205.180.81:26656,24da98830276fb0b4fc209cfcaf0cc3a287e1bdd@135.181.222.179:26656,88f134e7caad68e01554f4d648069c443a21fd4c@135.181.35.46:36656,51e4544568cf880451bfffc292de88adc472f0e0@34.147.126.38:26656,62bf004201a90ce00df6f69390378c3d90f6dd7e@34.90.129.213:26656,2d13d679b64e1a574904a140f72815644ec71131@65.21.133.125:30656,59af99085c961a6a5c8dc4bc8b3abffda16ddccb@135.181.38.62:26656,7f2828e3910a4b165a65e5bfb2465c1e809bad3b@65.108.48.182:26656,fed6ab9973f224f3b2334fd48fa835512d6311da@185.244.183.200:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.haqqd/config/config.toml
```
