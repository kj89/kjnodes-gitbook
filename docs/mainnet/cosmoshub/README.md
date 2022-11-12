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
peers="7b8ba795663a3d0ffa5333ab5bbbff3cac4e6dff@142.132.244.107:27002,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@144.76.163.233:34656,a09ed43e09f773e39855dc5d8b6a220eff4cb947@204.16.241.207:26656,3504eb147082bb848e70c7f7e54d869d86788046@135.181.139.29:46656,af91ecf985f01119866d1e34b57a52bb3b3447de@3.65.228.19:26656,3da88430414ec9084c8983fe4d462cce655ff1f3@51.222.245.114:26656,53b3651680ec3482d736808cbb3035940107f8ab@185.146.148.119:26656,4ed63a4748d04d1e0adfcdd240ab8ff43fbf41d3@89.149.218.202:26656,da48fde15b0290a8eee6c6f0dc9bca658f73d361@65.108.200.49:26656,a35cc47b1025162b82b2220fb7dd20a438866742@157.90.93.245:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gaiad/config/config.toml
```
