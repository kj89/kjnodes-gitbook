# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/teritori.png" width="150" alt=""><figcaption></figcaption></figure>

Teritori is a multi-chain hub designed to allow IBC and non IBC communities  to connect, trade services & NFTs, launch new projects & build further existing ones.

**Chain ID**: teritori-1 | **Latest Version Tag**: v1.3.0 | **Wasm**: ON

Website: [https://teritori.com](https://teritori.com)

## Restake

[Restake with kjnodes](https://restake.app/teritori/torivaloper184ln03hkpt75uhrrr26f66kvcqvf4yn4nc2xjm) (every day at 08:00, 20:00)
## Public endpoints

* rpc: [https://teritori.rpc.kjnodes.com](https://teritori.rpc.kjnodes.com)
* api: [https://teritori.api.kjnodes.com](https://teritori.api.kjnodes.com)

## Peering

**state-sync**

```
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@teritori.rpc.kjnodes.com:19656
```

**seed-node**

```
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@teritori.rpc.kjnodes.com:19659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/teritori/addrbook.json > $HOME/.teritorid/config/addrbook.json
```

**live-peers** (10)
```
peers="4b04b3d164dc6dd5bb555a7a106a8d314f30516f@65.21.136.170:53656,406fc7fe86ba396cb7fc8616c546f21a1d3c51cd@89.58.57.158:26656,53337d5ec1634ed29b6b9030a59349cfa9120277@142.132.199.27:38026,009e25e99e3f8fde86d283d4b8b0ce2f777cde53@138.201.8.248:53656,b336b83d9bab0b8cf96a3833efcbc196fab63fdd@212.95.51.215:36656,fe8765a154fc336ab284f28cdabc0bcb50a7afae@95.111.252.207:19656,8ac41af54dfd91c41de71cde222a55670f2f405d@141.95.65.73:15956,3178ac8fffd269325500c95679d58d5e8ec61746@198.244.213.94:22956,808437b010f4663bf007b33433262d1495b0fbfe@35.90.134.158:28656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@144.76.163.233:19656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.teritorid/config/config.toml
```
