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
peers="cf09eb9922d57c8013b4de5cff03fbfb978e6d29@65.108.10.37:26656,be87c9abf1c54e1cc2f37e68d21fcd61679abb4c@65.21.196.90:46656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:42656,90ee680b1738344354c48c23ba1e1fd68e071d80@142.132.248.138:26696,afb45e7806c2578f3bd8e13f845a8f9859af161d@138.201.8.248:50656,d8a0facda705edbbdd2d79fb302e017df009e9da@207.244.231.189:26656,ad820cb2fa85e525538207bb24ee49a61a74eb45@93.115.25.15:26656,88c6b1fa1c7fef98b4449b769eb2705476586664@65.109.92.241:21326,8a210f1bcfc9015a7bc18dcc5add29c0dce3f2dc@135.181.173.65:26656,d7322625044ad733bce4178dc397b2b9b5f68b41@43.153.27.130:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.bcna/config/config.toml
```
