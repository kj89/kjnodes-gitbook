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
peers="d9dbd30f7e9ae99dc05645f48f4637c2f4a14645@34.107.9.71:26656,1997e68bf205bedeed0c4723786bf03464987dc1@77.87.108.21:26656,d5cdd27a0aae56776f6fba0b7ba0ee66aeba534a@88.198.11.139:26656,44594a57ce538a21f8558bcb1c9ce560ad879e3e@15.235.114.84:26656,e0ab6c5cc86959853f499236b8297344802ac5f4@5.161.139.201:26656,cf10a45ead9e76d45b06dee97ef779e65103c78e@3.128.185.235:26656,915a5d104236764e33d5f7fd8d6c946e66766723@34.74.124.82:26656,67685d93f2256caa7a2d53e3a104f9e437c3d247@95.216.114.244:26656,5be5d5a7f68d573310692c9073190aaede216906@45.63.82.80:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@144.76.163.233:34656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gaiad/config/config.toml
```
