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
peers="4e1c2471efb89239fb04a4b75f9f87177fd91d00@95.217.151.241:26656,88c6b1fa1c7fef98b4449b769eb2705476586664@65.109.92.241:21326,4dabde84771e8689403ce7c8b76d27e555ab2f00@65.21.136.170:50656,6cceba286b498d4a1931f85e35ea0fa433373057@78.47.208.97:26656,63f85155ebe9759334dfae4e336b2f402853b5e4@138.94.49.22:26656,2235f1e518c5ea4a412f9dece386348eda356916@66.42.50.244:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:42656,320d0d38559140608b72a361db44b2a8f14bf0d1@107.181.229.154:16656,b15c0fade5fc0a354b4ac3fd9cdd8a716cddd24a@136.144.182.191:26656,d16080503125692e49e7d43275c5de1e48bfff1f@5.9.50.59:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.bcna/config/config.toml
```
