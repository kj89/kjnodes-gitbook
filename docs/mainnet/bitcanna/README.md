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
peers="4e1c2471efb89239fb04a4b75f9f87177fd91d00@95.217.151.241:26656,d5ed854872ad96f114737889ac9521ea3a29e3a3@185.220.205.209:26656,c124ce0b508e8b9ed1c5b6957f362225659b5343@144.76.177.185:26656,90ee680b1738344354c48c23ba1e1fd68e071d80@142.132.248.138:26696,16c65855784409bf2978feb121eeb805b4db9501@75.119.136.20:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:42656,a66bce0ddb49dcf60a5b83fd94a7bd4d0878f127@154.53.40.9:26656,be87c9abf1c54e1cc2f37e68d21fcd61679abb4c@65.21.196.90:46656,afb45e7806c2578f3bd8e13f845a8f9859af161d@138.201.8.248:50656,43f8f9eee8fe7de19e958edb4e95185ab40f8e39@65.108.238.104:13056"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.bcna/config/config.toml
```
