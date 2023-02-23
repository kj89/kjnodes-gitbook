# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/bitcanna.png" width="150" alt=""><figcaption></figcaption></figure>

BitCanna is a proof-of-stake (POS) decentralized payment network designed exclusively to serve the cannabis industry. 

**Chain ID**: bitcanna-1 | **Latest Version Tag**: v1.5.3 | **Wasm**: OFF

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

**live-peers** (10)
```bash
peers="d4cef8cf26d1d6b7167ac6c15601965081176df7@144.91.118.216:26656,d2247f7b919f0781c90ee61958d7044665a22d38@169.155.169.55:26656,32b1cf90be5dc6a01dc2684f0bd97bf052690082@144.91.97.191:26656,8e4e1f1e087c76c71c64e477e95495833da82aa2@135.181.173.137:26656,3635058fcdbe97e72d191faedfe4c6acab835877@107.181.235.66:16656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:42656,c6658742ae4c889ecf8dee95ca2a8e4b45d46dfd@85.214.208.127:26656,a7d96dc929824613315dcc1c90fee119f28cc51f@134.65.193.132:26656,82588f011491c6100d922d133f52fc23460b9231@135.181.67.233:26656,4e1c2471efb89239fb04a4b75f9f87177fd91d00@95.217.151.241:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.bcna/config/config.toml
```
