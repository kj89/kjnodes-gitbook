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

**live-peers** (9)
```
peers="526d8c7c44f59be9a39d7463c576b68c0db23174@65.108.234.23:15956,9adc9e74995610fa8b24c3d1a45939469e6e4c56@65.109.33.113:26656,39fc4816c6cf92a7813a277d918b3c2d5de54b02@95.217.88.61:28656,4d6c820a7d426ad934a5e51f2e020836f0378919@116.202.143.91:26656,f813a00f52de54a49aea3211b89a65ae6133eac2@88.99.167.148:26686,009e25e99e3f8fde86d283d4b8b0ce2f777cde53@138.201.8.248:53656,3594b73f909a9c4b87cfe6a361ef8b2b51124dd5@65.109.69.59:15956,e3b906fefa58783395fcf72086c698707908a558@141.95.65.26:27736,808437b010f4663bf007b33433262d1495b0fbfe@35.90.134.158:28656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.teritorid/config/config.toml
```
