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
peers="751513c7cd42a2565c37ab482bbe66f4d92c2740@136.244.106.130:26656,afb45e7806c2578f3bd8e13f845a8f9859af161d@138.201.8.248:50656,88c6b1fa1c7fef98b4449b769eb2705476586664@65.109.92.241:21326,630a9c88188001a4427ef0718c3a8d4e55cee5bb@207.201.218.211:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:42656,d4cef8cf26d1d6b7167ac6c15601965081176df7@144.91.118.216:26656,c38a5912b4b0f827732862594671c65ad0059932@172.105.196.25:26656,3b6d207fb9771473771abb4a93385cd642fa7b12@151.80.78.132:26656,7eba6089dd06147b7993979f901d212e722c21c3@24.158.14.212:36656,881b4ec9a1d37587c44476a22c0864b08b1c88fe@195.3.221.21:13056"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.bcna/config/config.toml
```
