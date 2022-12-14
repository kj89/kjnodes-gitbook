# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/bitcanna.png" width="150" alt=""><figcaption></figcaption></figure>

BitCanna is a proof-of-stake (POS) decentralized payment network designed exclusively to serve the cannabis industry. 

**Chain ID**: bitcanna-1 | **Latest Version Tag**: v1.5.3 | **Wasm**: OFF

Website: [https://www.bitcanna.io](https://www.bitcanna.io)


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
peers="d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:42656,a1ceb81a5498642753f8600a5c3b9ca056af3051@67.222.144.195:16656,b2010fecba7153f5ad3aa4e7aad08fd94ed826c9@52.9.185.28:26656,63f85155ebe9759334dfae4e336b2f402853b5e4@138.94.49.22:26656,17065f4b6062471aa2e1e615d5061e200a1d44e0@62.171.190.198:26656,4e1c2471efb89239fb04a4b75f9f87177fd91d00@95.217.151.241:26656,881b4ec9a1d37587c44476a22c0864b08b1c88fe@195.3.221.21:13056,b204222a9b6ca4eee39a836b7406483a5ad4e719@144.91.114.250:26656,2235f1e518c5ea4a412f9dece386348eda356916@66.42.50.244:26656,4dabde84771e8689403ce7c8b76d27e555ab2f00@65.21.136.170:50656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.bcna/config/config.toml
```
