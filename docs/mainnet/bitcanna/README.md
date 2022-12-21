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
peers="88c6b1fa1c7fef98b4449b769eb2705476586664@65.109.92.241:21326,6cceba286b498d4a1931f85e35ea0fa433373057@78.47.208.97:26656,c124ce0b508e8b9ed1c5b6957f362225659b5343@144.76.177.185:26656,90ee680b1738344354c48c23ba1e1fd68e071d80@142.132.248.138:26696,a66bce0ddb49dcf60a5b83fd94a7bd4d0878f127@154.53.40.9:26656,a1ceb81a5498642753f8600a5c3b9ca056af3051@67.222.144.195:16656,b2010fecba7153f5ad3aa4e7aad08fd94ed826c9@52.9.185.28:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:42656,afb45e7806c2578f3bd8e13f845a8f9859af161d@138.201.8.248:50656,a7a358efdbe72da953e73a628924e6336e4364c4@24.158.14.212:36656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.bcna/config/config.toml
```
