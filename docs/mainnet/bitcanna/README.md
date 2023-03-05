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
peers="9301659e822226a1eaefe6e6fa99da96c99d7db6@94.130.10.43:30656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:42656,bba10290da32f3cb41e15c3a192413666ce05cee@136.243.119.241:26656,66ed3885f2932912df2b04646d2c3d643467719b@212.227.115.165:26656,630a9c88188001a4427ef0718c3a8d4e55cee5bb@207.201.218.211:26656,320d0d38559140608b72a361db44b2a8f14bf0d1@107.181.229.154:16656,a7d96dc929824613315dcc1c90fee119f28cc51f@134.65.193.132:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.54:26656,ec4796daea06ecf0e51819b931fbcb3e1a99b137@144.91.101.49:26656,c124ce0b508e8b9ed1c5b6957f362225659b5343@144.76.177.185:26656,89757803f40da51678451735445ad40d5b15e059@169.155.168.66:26656,17065f4b6062471aa2e1e615d5061e200a1d44e0@62.171.190.198:26656,4e1c2471efb89239fb04a4b75f9f87177fd91d00@95.217.151.241:26656,df99de6cec9152c517990317b340b8b9a307493c@193.34.144.156:26656,a992c93343986c27af28a0c72c3e5b13397c9689@161.97.168.19:26656,935a9d809781aa4094dd806c2afed29a25ec8b8e@135.181.210.189:26656,02c8045236f844632ef1d4411ad356b3332d4f2f@65.108.226.44:34656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.bcna/config/config.toml
```
