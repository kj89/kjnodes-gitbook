# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/cosmoshub.png" width="150" alt=""><figcaption></figcaption></figure>

The Cosmos Hub is the blockchain protocol underlying an  increasingly large number of blockchains built on the  Cosmos Network, allowing them to communicate with each other.

**Chain ID**: cosmoshub-4 | **Latest Version Tag**: v7.1.0 | **Wasm**: OFF

Website: [https://hub.cosmos.network](https://hub.cosmos.network)


## Public endpoints

* rpc: [https://cosmoshub.rpc.kjnodes.com](https://cosmoshub.rpc.kjnodes.com)
* api: [https://cosmoshub.api.kjnodes.com](https://cosmoshub.api.kjnodes.com)

## Peering

**state-sync**

```
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@cosmoshub.rpc.kjnodes.com:34656
```

**seed-node**

```
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@cosmoshub.rpc.kjnodes.com:34659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/cosmoshub/addrbook.json > $HOME/.gaiad/config/addrbook.json
```

**live-peers** (10)
```
peers="d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@144.76.163.233:34656,4ed63a4748d04d1e0adfcdd240ab8ff43fbf41d3@89.149.218.202:26656,25d3ec5a00235fe95d7a87bab54f03b6ac1962ba@34.78.95.235:26656,37dfe1ec33e9f88f378a61a32462d57d2baa5e74@65.108.99.140:26656,a35cc47b1025162b82b2220fb7dd20a438866742@157.90.93.245:26656,aea820ece7c45c0a8b5dababc9ea813f7eb62638@93.186.201.125:26656,53b3651680ec3482d736808cbb3035940107f8ab@185.146.148.119:26656,a09ed43e09f773e39855dc5d8b6a220eff4cb947@204.16.241.207:26656,97e4468ac589eac505a800411c635b14511a61bb@23.88.18.49:26656,ed53d253068e44a1233798a08d82f7ac4897c5f3@54.251.217.58:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gaiad/config/config.toml
```
