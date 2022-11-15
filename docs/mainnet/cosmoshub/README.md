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
peers="44594a57ce538a21f8558bcb1c9ce560ad879e3e@15.235.114.84:26656,a94dff85ed430f0475f41fe306c82b7eb7f6e858@51.91.153.78:31649,52a6b8f416ba3ed2aafa72e35df28ee4c3ee547b@5.9.108.156:36656,58b31074c33d34e96c35e071dc97fc1a82410df3@161.97.142.147:26656,c1e437f73b8889b78ea34981e7c349157ad80284@107.135.15.66:26656,a35cc47b1025162b82b2220fb7dd20a438866742@157.90.93.245:26656,a784d54afef0bb2000bb1bc116ad62de4488fc19@173.212.199.111:26656,88b03d0ae562ec55414bef4b3e0073bb16933938@18.138.176.63:26656,2e470eb2dfd65ffa34a9ae2d73646f82c6e594b7@65.108.10.36:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@144.76.163.233:34656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gaiad/config/config.toml
```
