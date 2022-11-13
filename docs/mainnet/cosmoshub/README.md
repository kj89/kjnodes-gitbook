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

**live-peers** (9)
```
peers="53b3651680ec3482d736808cbb3035940107f8ab@185.146.148.119:26656,a35cc47b1025162b82b2220fb7dd20a438866742@157.90.93.245:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@144.76.163.233:34656,ba3bacc714817218562f743178228f23678b2873@34.141.15.99:26656,a94dff85ed430f0475f41fe306c82b7eb7f6e858@51.91.153.78:31649,67685d93f2256caa7a2d53e3a104f9e437c3d247@95.216.114.244:26656,da48fde15b0290a8eee6c6f0dc9bca658f73d361@65.108.200.49:26656,6d9b1e1dda527cac3bf50602c29c1a8d501e6c5a@65.108.229.102:25656,1da54d20c7339713f1d6d28dd2117087dd33d0ca@154.53.32.78:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gaiad/config/config.toml
```
