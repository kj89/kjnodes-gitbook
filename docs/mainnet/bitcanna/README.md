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
peers="d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:42656,a1ceb81a5498642753f8600a5c3b9ca056af3051@67.222.144.195:16656,82588f011491c6100d922d133f52fc23460b9231@135.181.67.233:26656,d3796f3f2a179afab1485a672ace3d909cd0eeed@185.137.122.214:26656,104d7ec9d84c8da66b97d50669b8ba58f1b60470@62.171.180.31:26656,751513c7cd42a2565c37ab482bbe66f4d92c2740@136.244.106.130:26656,32b1cf90be5dc6a01dc2684f0bd97bf052690082@144.91.97.191:26656,b587bf827b5f680c417601b536ffbd505c88bb07@193.70.45.106:13056,a66bce0ddb49dcf60a5b83fd94a7bd4d0878f127@154.53.40.9:26656,c124ce0b508e8b9ed1c5b6957f362225659b5343@144.76.177.185:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.bcna/config/config.toml
```
