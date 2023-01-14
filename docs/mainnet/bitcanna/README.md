# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/bitcanna.png" width="150" alt=""><figcaption></figcaption></figure>

BitCanna is a proof-of-stake (POS) decentralized payment network designed exclusively to serve the cannabis industry. 

**Chain ID**: bitcanna-1 | **Latest Version Tag**: v1.5.3 | **Wasm**: OFF

[Website](https://www.bitcanna.io) | [Discord](https://discord.gg/9AVrzaVQvs) | [Twitter](https://twitter.com/BitCannaGlobal)


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
peers="846fca7d90fdc1ddbcf1892a0b6338a44e93b76d@65.108.0.93:36656,4dabde84771e8689403ce7c8b76d27e555ab2f00@65.21.136.170:50656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:42656,320d0d38559140608b72a361db44b2a8f14bf0d1@107.181.229.154:16656,cb9741ce22ab5f615913ac11b211c3c7f58dee71@107.191.36.154:26656,d8a0facda705edbbdd2d79fb302e017df009e9da@207.244.231.189:26656,07c829cf936db34be61143fabb09541d05aea899@65.108.98.124:64206,751513c7cd42a2565c37ab482bbe66f4d92c2740@136.244.106.130:26656,a1ceb81a5498642753f8600a5c3b9ca056af3051@67.222.144.195:16656,8a210f1bcfc9015a7bc18dcc5add29c0dce3f2dc@135.181.173.65:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.bcna/config/config.toml
```
