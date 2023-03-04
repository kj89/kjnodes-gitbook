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

**live-peers** (17)
```bash
peers="b15c0fade5fc0a354b4ac3fd9cdd8a716cddd24a@136.144.182.191:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:42656,d27dc1222e9ab0d90e49490ee315797afa14a03f@65.108.99.254:27656,6be83de3e5ab1a912340ddad3e67d10c32d5b574@161.97.170.83:26656,7c00beb4956bc40cd33ced6e2c2ffe07d4fa32e7@95.216.242.82:36656,d2247f7b919f0781c90ee61958d7044665a22d38@169.155.169.55:26656,4e1c2471efb89239fb04a4b75f9f87177fd91d00@95.217.151.241:26656,d4cef8cf26d1d6b7167ac6c15601965081176df7@144.91.118.216:26656,846fca7d90fdc1ddbcf1892a0b6338a44e93b76d@65.108.0.93:36656,c124ce0b508e8b9ed1c5b6957f362225659b5343@144.76.177.185:26656,935a9d809781aa4094dd806c2afed29a25ec8b8e@135.181.210.189:26656,82588f011491c6100d922d133f52fc23460b9231@135.181.67.233:26656,a992c93343986c27af28a0c72c3e5b13397c9689@161.97.168.19:26656,a9f839c6e24221fb093f13ee41a0af842378fec5@94.130.12.22:26642,02c8045236f844632ef1d4411ad356b3332d4f2f@65.108.226.44:34656,630a9c88188001a4427ef0718c3a8d4e55cee5bb@207.201.218.211:26656,d7322625044ad733bce4178dc397b2b9b5f68b41@43.153.27.130:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.bcna/config/config.toml
```
