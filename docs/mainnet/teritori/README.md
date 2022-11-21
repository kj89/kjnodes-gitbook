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
peers="39fc4816c6cf92a7813a277d918b3c2d5de54b02@95.217.88.61:28656,5a98d637a16b16bf425a4a785c9d11a7d1e5b8a0@65.21.131.215:26736,3950af34da35ce3ff8c50ff3c47a43f5dfc93947@195.3.220.154:19656,bbc594f0a8424368b869fef47a18d6e35965db2e@176.9.188.21:53656,9c5393bb5611f8c3aaa0abde1ce753284c1428d0@141.95.34.175:27656,82ebb17ddac20928fb8107201dad9f5aea7f9132@198.244.200.3:26656,d856120f262134ebf13e1d2632d778b69e704208@65.108.4.188:15956,2afdb9300c47e43e555fa572d033b2d68ac28506@65.109.70.68:26686,2c094a61df0c0bb0e94c74680d08f9ab36f45df3@144.76.17.48:10756,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@144.76.163.233:19656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.teritorid/config/config.toml
```
