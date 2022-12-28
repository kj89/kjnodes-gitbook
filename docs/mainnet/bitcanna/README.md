# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/bitcanna.png" width="150" alt=""><figcaption></figcaption></figure>

BitCanna is a proof-of-stake (POS) decentralized payment network designed exclusively to serve the cannabis industry. 

**Chain ID**: bitcanna-1 | **Latest Version Tag**: v1.5.3 | **Wasm**: OFF

[Website](https://www.bitcanna.io) | [Discord](https://discord.gg/9AVrzaVQvs) | [Twitter](https://twitter.com/BitCannaGlobal)


## Public endpoints

* rpc: [https://bitcanna.rpc.kjnodes.com](https://bitcanna.rpc.kjnodes.com)
* api: [https://bitcanna.api.kjnodes.com](https://bitcanna.api.kjnodes.com)

## Peering

**state-sync**

```
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@bitcanna.rpc.kjnodes.com:42656
```

**seed-node**

```
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@bitcanna.rpc.kjnodes.com:42659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/bitcanna/addrbook.json > $HOME/.bcna/config/addrbook.json
```

**live-peers** (10)
```
peers="9532a13b05e5f68f2ca01f90b3d1ba9a762af817@65.108.131.190:21956,d2247f7b919f0781c90ee61958d7044665a22d38@169.155.169.55:26656,b2010fecba7153f5ad3aa4e7aad08fd94ed826c9@52.9.185.28:26656,2235f1e518c5ea4a412f9dece386348eda356916@66.42.50.244:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:42656,3635058fcdbe97e72d191faedfe4c6acab835877@107.181.235.66:16656,c38a5912b4b0f827732862594671c65ad0059932@172.105.196.25:26656,881b4ec9a1d37587c44476a22c0864b08b1c88fe@195.3.221.21:13056,8a210f1bcfc9015a7bc18dcc5add29c0dce3f2dc@135.181.173.65:26656,cb9741ce22ab5f615913ac11b211c3c7f58dee71@107.191.36.154:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.bcna/config/config.toml
```
