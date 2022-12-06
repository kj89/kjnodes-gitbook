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
peers="9f769bedc6a17199804e323700d5eaa6685b8be9@161.97.79.100:26656,406fc7fe86ba396cb7fc8616c546f21a1d3c51cd@89.58.57.158:26656,358f13bd95d91517053a58f4d30205842672837f@104.37.187.214:60656,fefd8ffb33a5d6ae194f082a39c4bb713da3a06b@167.86.86.197:36656,51345b444fb291c03cf18084bdfc51123de7b5ac@51.178.74.75:36656,7fb5a1a53f481f037487920ed08b0495158e2041@148.251.53.202:26796,82ebb17ddac20928fb8107201dad9f5aea7f9132@198.244.200.3:26656,88a407d4749e1ccbb630f98ca44f304744d97864@38.242.141.168:26656,48980875839186e08e12ebf0d9a2803b45206833@65.109.92.241:38026,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:19656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.teritorid/config/config.toml
```
