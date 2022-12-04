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
peers="5a98d637a16b16bf425a4a785c9d11a7d1e5b8a0@65.21.131.215:26736,3178ac8fffd269325500c95679d58d5e8ec61746@198.244.213.94:22956,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:19656,ec4126b26336cd61b335345df4ff2a3fbb79338a@65.109.92.240:20026,24b28cf013e6d7b5b88b6dba2701c5ddd2dd5ee1@65.109.58.225:28656,2b4f46e601fb4ede2a0c98976337e3afdaa50dac@65.108.238.102:15956,8ac41af54dfd91c41de71cde222a55670f2f405d@141.95.65.73:15956,ff8f8c1b4cf70f38e1c370af05a40c1845022ae8@51.79.103.43:26656,106490318e51355bc6d72e7941a0080f8b8256b9@185.16.39.14:26656,fefd8ffb33a5d6ae194f082a39c4bb713da3a06b@167.86.86.197:36656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.teritorid/config/config.toml
```
