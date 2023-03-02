# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/bitcanna.png" width="150" alt=""><figcaption></figcaption></figure>

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

**live-peers** (19)
```bash
peers="7c00beb4956bc40cd33ced6e2c2ffe07d4fa32e7@95.216.242.82:36656,2af9f118d9be86892ef47193b6ab9e47046b9f44@74.207.231.41:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:42656,881b4ec9a1d37587c44476a22c0864b08b1c88fe@195.3.221.21:13056,6be83de3e5ab1a912340ddad3e67d10c32d5b574@161.97.170.83:26656,d8a0facda705edbbdd2d79fb302e017df009e9da@207.244.231.189:26656,0393c19b176d1cf8bc560c5a8fa990301deb1a7e@95.217.126.185:26656,a7d96dc929824613315dcc1c90fee119f28cc51f@134.65.193.132:26656,36a17684dc4809eb0c722aa4b5bd829b0429e8a1@207.246.84.132:26656,8fa7a04d55ca7d0ab70dc5cbc35d5cf26c5ecfb7@65.108.142.81:26682,6cceba286b498d4a1931f85e35ea0fa433373057@78.47.208.97:26656,a1ceb81a5498642753f8600a5c3b9ca056af3051@67.222.144.195:16656,da04ee3f8bd93421a3264e3a061a09c139aaa937@161.97.150.65:26656,ad820cb2fa85e525538207bb24ee49a61a74eb45@93.115.25.15:26656,b5ce8fac0dd173d7154b3eb8d10136710e609d1e@95.216.21.37:29656,8a210f1bcfc9015a7bc18dcc5add29c0dce3f2dc@135.181.173.65:26656,4e1c2471efb89239fb04a4b75f9f87177fd91d00@95.217.151.241:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.54:26656,b204222a9b6ca4eee39a836b7406483a5ad4e719@144.91.114.250:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.bcna/config/config.toml
```
