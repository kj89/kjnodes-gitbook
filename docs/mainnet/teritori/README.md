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
peers="8ac41af54dfd91c41de71cde222a55670f2f405d@141.95.65.73:15956,317d9a102d4a04337c65571c18df0e98269dce87@141.94.193.12:13656,412afea7f33f6f91c85f8d149eff81acb6624bb3@195.201.63.87:42656,6085c32b26fb1baa4b16b426f5d56f2fff81cfc7@135.181.165.246:26656,7f9773971291b77b2d65364a8928cb31c40aa70f@65.108.73.124:13656,bbc594f0a8424368b869fef47a18d6e35965db2e@176.9.188.21:53656,06b8b9a4d201beee58fe66e1af4c4265543ace2b@135.181.153.228:46656,26d6ee4138c7533c5541722c6e1ecc6d60d47a86@104.193.254.42:26656,6fd88e2143e6d4ba02a7f745565120df18e84699@109.236.80.46:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.teritorid/config/config.toml
```
