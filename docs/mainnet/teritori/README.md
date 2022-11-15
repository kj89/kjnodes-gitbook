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

**live-peers** (11)
```
peers="26d6ee4138c7533c5541722c6e1ecc6d60d47a86@104.193.254.42:26656,2afdb9300c47e43e555fa572d033b2d68ac28506@65.109.70.68:26686,9c5393bb5611f8c3aaa0abde1ce753284c1428d0@141.95.34.175:27656,bbc594f0a8424368b869fef47a18d6e35965db2e@176.9.188.21:53656,3950af34da35ce3ff8c50ff3c47a43f5dfc93947@195.3.220.154:19656,317d9a102d4a04337c65571c18df0e98269dce87@141.94.193.12:13656,106490318e51355bc6d72e7941a0080f8b8256b9@185.16.39.14:26656,b98db7bf9182a12b6ff7b8efc9f80350ccc67045@23.88.69.167:26878,6fd88e2143e6d4ba02a7f745565120df18e84699@109.236.80.46:26656,16f90d350de14a596ebdc683ce5e703c14e40bb3@75.119.146.181:19656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@144.76.163.233:19656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.teritorid/config/config.toml
```
