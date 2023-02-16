# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/bitcanna.png" width="150" alt=""><figcaption></figcaption></figure>

BitCanna is a proof-of-stake (POS) decentralized payment network designed exclusively to serve the cannabis industry. 

**Chain ID**: bitcanna-1 | **Latest Version Tag**: v1.5.3 | **Wasm**: OFF

[Website](https://www.bitcanna.io) | [Discord](https://discord.gg/9AVrzaVQvs) | [Twitter](https://twitter.com/BitCannaGlobal)




## Chain explorer
[https://explorer.kjnodes.com/bitcanna](https://explorer.kjnodes.com/bitcanna)

## Public endpoints

* api: [https://bitcanna.api.kjnodes.com](https://bitcanna.api.kjnodes.com)
* rpc: [https://bitcanna.rpc.kjnodes.com](https://bitcanna.rpc.kjnodes.com)
* grpc: [https://bitcanna.grpc.kjnodes.com](https://bitcanna.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@bitcanna.rpc.kjnodes.com:42656
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@bitcanna.rpc.kjnodes.com:42659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/bitcanna/addrbook.json > $HOME/.bcna/config/addrbook.json
```

**live-peers** (10)
```bash
peers="8a210f1bcfc9015a7bc18dcc5add29c0dce3f2dc@135.181.173.65:26656,c73f11f731e4a78df73123747d38bc3a9d4d036b@23.88.66.239:36656,d4cef8cf26d1d6b7167ac6c15601965081176df7@144.91.118.216:26656,630a9c88188001a4427ef0718c3a8d4e55cee5bb@207.201.218.211:26656,3635058fcdbe97e72d191faedfe4c6acab835877@107.181.235.66:16656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:42656,320d0d38559140608b72a361db44b2a8f14bf0d1@107.181.229.154:16656,c38a5912b4b0f827732862594671c65ad0059932@172.105.196.25:26656,5cfb82bd566ad3c5330c8326f0da5c7f048aca25@81.0.218.135:24356,5bb0a042e8a4ee28bcda1e26148e57787e75a42e@23.88.69.22:28466"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.bcna/config/config.toml
```
