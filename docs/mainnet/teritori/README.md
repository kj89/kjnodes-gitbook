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
peers="24b28cf013e6d7b5b88b6dba2701c5ddd2dd5ee1@65.109.58.225:28656,ad95a806c87682a553725a76329646425607d79f@65.108.105.25:10856,26d6ee4138c7533c5541722c6e1ecc6d60d47a86@104.193.254.42:26656,2afdb9300c47e43e555fa572d033b2d68ac28506@65.109.70.68:26686,46b7ae20e3cc4264076a91c3601f3894a021a80d@65.108.6.45:36656,9c5393bb5611f8c3aaa0abde1ce753284c1428d0@141.95.34.175:27656,4d6c820a7d426ad934a5e51f2e020836f0378919@116.202.143.91:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:19656,2b4f46e601fb4ede2a0c98976337e3afdaa50dac@65.108.238.102:15956,43da931d00da102c002e0a227de7258b8fb1871a@144.126.135.53:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.teritorid/config/config.toml
```
