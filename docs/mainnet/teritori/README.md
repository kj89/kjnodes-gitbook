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
peers="4cef2b81f82420434c6ce0dc43ca04ad18ef773f@65.108.75.107:15656,40caa979c29a9930ea2b8a6249037924d308ae84@162.55.234.70:54256,5a98d637a16b16bf425a4a785c9d11a7d1e5b8a0@65.21.131.215:26736,412afea7f33f6f91c85f8d149eff81acb6624bb3@195.201.63.87:42656,16f90d350de14a596ebdc683ce5e703c14e40bb3@75.119.146.181:19656,9f769bedc6a17199804e323700d5eaa6685b8be9@161.97.79.100:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:19656,406fc7fe86ba396cb7fc8616c546f21a1d3c51cd@89.58.57.158:26656,358f13bd95d91517053a58f4d30205842672837f@104.37.187.214:60656,67a266c2819ef727e51232365d98db017e82b1c3@65.109.63.165:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.teritorid/config/config.toml
```
