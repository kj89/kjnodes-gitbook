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
peers="ee0328492fd21eee29ecbde19b52dfde6bd5da54@176.9.146.72:46656,62bf004201a90ce00df6f69390378c3d90f6dd7e@34.90.129.213:26656,2d13d679b64e1a574904a140f72815644ec71131@65.21.133.125:30656,fed6ab9973f224f3b2334fd48fa835512d6311da@185.244.183.200:26656,5f0492553fc69a7db26e8f2b9ffe6cfd21b715f3@95.216.72.28:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:35656,ba56c564a5430632e59e2b08fc348735bc56b32f@154.12.232.140:26656,d648d598c34e0e58ec759aa399fe4534021e8401@109.205.180.81:26656,adce9d7f72360f6d66c4248b8db8de151b877130@167.235.132.152:26656,35e1bf6fda8a37c9c4872527a30b1fe26b0a155f@45.13.59.201:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.haqqd/config/config.toml
```
