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
peers="d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:42656,66ed3885f2932912df2b04646d2c3d643467719b@212.227.115.165:26656,bba10290da32f3cb41e15c3a192413666ce05cee@136.243.119.241:26656,c124ce0b508e8b9ed1c5b6957f362225659b5343@144.76.177.185:26656,b15c0fade5fc0a354b4ac3fd9cdd8a716cddd24a@136.144.182.191:26656,320d0d38559140608b72a361db44b2a8f14bf0d1@107.181.229.154:16656,da04ee3f8bd93421a3264e3a061a09c139aaa937@161.97.150.65:26656,d16080503125692e49e7d43275c5de1e48bfff1f@5.9.50.59:26656,16c65855784409bf2978feb121eeb805b4db9501@75.119.136.20:26656,c38376851f76a488bcc464ce9e248d6cf2956ba8@176.9.188.21:50656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.bcna/config/config.toml
```
