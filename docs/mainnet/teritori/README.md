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
peers="106490318e51355bc6d72e7941a0080f8b8256b9@185.16.39.14:26656,9f769bedc6a17199804e323700d5eaa6685b8be9@161.97.79.100:26656,2afdb9300c47e43e555fa572d033b2d68ac28506@65.109.70.68:26686,06b8b9a4d201beee58fe66e1af4c4265543ace2b@135.181.153.228:46656,fe8765a154fc336ab284f28cdabc0bcb50a7afae@95.111.252.207:19656,51345b444fb291c03cf18084bdfc51123de7b5ac@51.178.74.75:36656,4b04b3d164dc6dd5bb555a7a106a8d314f30516f@65.21.136.170:53656,722b63e6c65628b929f22013dcbcde980210cb44@176.9.127.54:26656,010f61b6cb13193853be4f42c328df3a0680d4d6@65.108.101.50:60656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@144.76.163.233:19656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.teritorid/config/config.toml
```
