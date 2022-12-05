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
peers="526d8c7c44f59be9a39d7463c576b68c0db23174@65.108.234.23:15956,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:19656,009e25e99e3f8fde86d283d4b8b0ce2f777cde53@138.201.8.248:53656,5a98d637a16b16bf425a4a785c9d11a7d1e5b8a0@65.21.131.215:26736,ff8f8c1b4cf70f38e1c370af05a40c1845022ae8@51.79.103.43:26656,26d6ee4138c7533c5541722c6e1ecc6d60d47a86@104.193.254.42:26656,2f93424bd346b857bd5164eaac0b2bfd5fd644c0@144.91.127.252:26656,106490318e51355bc6d72e7941a0080f8b8256b9@185.16.39.14:26656,b336b83d9bab0b8cf96a3833efcbc196fab63fdd@212.95.51.215:36656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.teritorid/config/config.toml
```
