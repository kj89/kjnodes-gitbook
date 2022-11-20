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

**live-peers** (11)
```
peers="07fc76b0a1dfcd25e3139a339728d50507bb5d96@67.209.54.35:26656,67685d93f2256caa7a2d53e3a104f9e437c3d247@95.216.114.244:26656,89c643c1f8bee0eaa680a304eb067905df986643@95.217.122.233:26656,cf10a45ead9e76d45b06dee97ef779e65103c78e@3.128.185.235:26656,701036e718d0746d1d7055fb0fd1245cf361e0b8@168.119.79.106:26656,915a5d104236764e33d5f7fd8d6c946e66766723@34.74.124.82:26656,44594a57ce538a21f8558bcb1c9ce560ad879e3e@15.235.114.84:26656,1da54d20c7339713f1d6d28dd2117087dd33d0ca@154.53.32.78:26656,34f0e424f747f62e04e8c34fde60013fb4dbc04b@65.108.0.165:14956,0e71a3cbdddfe77ebff79378bf6ac07915e747dc@167.235.107.42:27002,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@144.76.163.233:34656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gaiad/config/config.toml
```
