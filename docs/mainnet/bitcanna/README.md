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
peers="82588f011491c6100d922d133f52fc23460b9231@135.181.67.233:26656,8e4e1f1e087c76c71c64e477e95495833da82aa2@135.181.173.137:26656,be87c9abf1c54e1cc2f37e68d21fcd61679abb4c@65.21.196.90:46656,32b1cf90be5dc6a01dc2684f0bd97bf052690082@144.91.97.191:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:42656,935a9d809781aa4094dd806c2afed29a25ec8b8e@135.181.210.189:26656,312237a27c62e21e3ec5e2a075cba0035db3fb66@95.217.42.107:26656,c38a5912b4b0f827732862594671c65ad0059932@172.105.196.25:26656,4dabde84771e8689403ce7c8b76d27e555ab2f00@65.21.136.170:50656,66ed3885f2932912df2b04646d2c3d643467719b@212.227.115.165:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.bcna/config/config.toml
```
