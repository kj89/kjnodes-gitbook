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
peers="89c643c1f8bee0eaa680a304eb067905df986643@95.217.122.233:26656,7b8ba795663a3d0ffa5333ab5bbbff3cac4e6dff@142.132.244.107:27002,07fc76b0a1dfcd25e3139a339728d50507bb5d96@67.209.54.35:26656,2e470eb2dfd65ffa34a9ae2d73646f82c6e594b7@65.108.10.36:26656,8dc4fd0007c74bdf4b7ee1e5a3ab68161cc8f845@142.132.208.213:26656,44594a57ce538a21f8558bcb1c9ce560ad879e3e@15.235.114.84:26656,a94dff85ed430f0475f41fe306c82b7eb7f6e858@51.91.153.78:31649,67685d93f2256caa7a2d53e3a104f9e437c3d247@95.216.114.244:26656,ead79014a1d4295011cbcfd079e775c40d532caa@65.108.79.216:26656,c1e437f73b8889b78ea34981e7c349157ad80284@107.135.15.66:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@144.76.163.233:34656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gaiad/config/config.toml
```
