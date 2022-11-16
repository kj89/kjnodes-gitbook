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
peers="67685d93f2256caa7a2d53e3a104f9e437c3d247@95.216.114.244:26656,58b31074c33d34e96c35e071dc97fc1a82410df3@161.97.142.147:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@144.76.163.233:34656,8dc4fd0007c74bdf4b7ee1e5a3ab68161cc8f845@142.132.208.213:26656,84cc83cd09a974a234a3fdb5bb4fd46fd856f8ec@142.132.135.239:26656,2122aa0409c6ccd7845e23eb6adb12f1d276665e@34.88.247.213:26656,f8ae898b130457bbbf05fd3d2e9ca4559bd528fd@37.120.245.157:26656,5780219cf20802dc8726cb58a93cc9180a75fcbc@80.190.129.50:56666,213857e741833d17275ea559bb2d0342398cec99@35.245.206.45:26656,34f0e424f747f62e04e8c34fde60013fb4dbc04b@65.108.0.165:14956"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gaiad/config/config.toml
```
