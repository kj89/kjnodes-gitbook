# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/bitcanna.png" width="150" alt=""><figcaption></figcaption></figure>

BitCanna is a proof-of-stake (POS) decentralized payment network designed exclusively to serve the cannabis industry. 

**Chain ID**: bitcanna-1 | **Latest Version Tag**: v1.6.0-fix | **Wasm**: OFF

[Website](https://www.bitcanna.io) | [Discord](https://discord.gg/9AVrzaVQvs) | [Twitter](https://twitter.com/BitCannaGlobal)




## Chain explorer
[https://explorer.kjnodes.com/bitcanna](https://explorer.kjnodes.com/bitcanna)

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

**live-peers** (15)
```bash
peers="630a9c88188001a4427ef0718c3a8d4e55cee5bb@207.201.218.211:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:42656,88c6b1fa1c7fef98b4449b769eb2705476586664@65.109.92.241:21326,66ed3885f2932912df2b04646d2c3d643467719b@212.227.115.165:26656,b204222a9b6ca4eee39a836b7406483a5ad4e719@144.91.114.250:26656,89757803f40da51678451735445ad40d5b15e059@169.155.168.66:26656,6cceba286b498d4a1931f85e35ea0fa433373057@78.47.208.97:26656,6be83de3e5ab1a912340ddad3e67d10c32d5b574@161.97.170.83:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.54:26656,8a210f1bcfc9015a7bc18dcc5add29c0dce3f2dc@135.181.173.65:26656,a66bce0ddb49dcf60a5b83fd94a7bd4d0878f127@154.53.40.9:26656,751513c7cd42a2565c37ab482bbe66f4d92c2740@136.244.106.130:26656,935a9d809781aa4094dd806c2afed29a25ec8b8e@135.181.210.189:26656,02c8045236f844632ef1d4411ad356b3332d4f2f@65.108.226.44:34656,57a3e858a5c860e6355683c88add28d52df6c24a@38.242.232.202:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.bcna/config/config.toml
```
