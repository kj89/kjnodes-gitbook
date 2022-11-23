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
peers="453ed8a41a059519310219fab9b8d9f2ff89eab0@65.108.42.105:26656,6ce864d853904ebef9400528f129d8fefa6f1827@91.211.251.232:36656,c932600aa633bb17e07dcb53ae982c834ba1b734@185.225.232.148:26656,562a589b82682f695344bc4a9d7a2fcb5a5a4d80@65.21.60.82:26656,d648d598c34e0e58ec759aa399fe4534021e8401@109.205.180.81:26656,001eb7a3a03dc11539541737262c4ddc84dec283@91.195.101.98:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:35656,ec8a285e36888bd3134266b8ba668b48c327e6bf@142.132.202.50:36656,51e4544568cf880451bfffc292de88adc472f0e0@34.147.126.38:26656,dae56b465293b5f122d795f742f87c6b16539acc@23.88.44.170:12656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.haqqd/config/config.toml
```
