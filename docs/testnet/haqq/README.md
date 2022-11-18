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
peers="7e45021be5e7754b62b6016305ba26f8bf40beda@142.132.199.27:20116,adce9d7f72360f6d66c4248b8db8de151b877130@167.235.132.152:26656,7f2828e3910a4b165a65e5bfb2465c1e809bad3b@65.108.48.182:26656,6ce864d853904ebef9400528f129d8fefa6f1827@91.211.251.232:36656,562a589b82682f695344bc4a9d7a2fcb5a5a4d80@65.21.60.82:26656,ed145a35b436878c1f1c10634bd18600f3696e17@95.217.181.142:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:35656,5f0492553fc69a7db26e8f2b9ffe6cfd21b715f3@95.216.72.28:26656,ee0328492fd21eee29ecbde19b52dfde6bd5da54@176.9.146.72:46656,6771e65c1b30cc514faf5943320fdda480fe9124@95.216.39.183:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.haqqd/config/config.toml
```
