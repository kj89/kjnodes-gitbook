# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/bitcanna.png" width="150" alt=""><figcaption></figcaption></figure>

BitCanna is a proof-of-stake (POS) decentralized payment network designed exclusively to serve the cannabis industry. 

**Chain ID**: bitcanna-1 | **Latest Version Tag**: v1.6.1 | **Wasm**: OFF

[Website](https://www.bitcanna.io) | [Discord](https://discord.gg/9AVrzaVQvs) | [Twitter](https://twitter.com/BitCannaGlobal)

[![Stake with kjnodes](https://i.ibb.co/cr44Q8j/button-stake-with-kjnodes.png)](https://restake.app/bitcanna/bcnavaloper1aym6s8eza7kjvnxuwxufrzccz6vqvgnsc47cc7)

## Restake

[Restake with kjnodes](https://restake.app/bitcanna/bcnavaloper1aym6s8eza7kjvnxuwxufrzccz6vqvgnsc47cc7) (every 5 minutes)
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

**live-peers** (20)
```bash
peers="8e4e1f1e087c76c71c64e477e95495833da82aa2@135.181.173.137:26656,88c6b1fa1c7fef98b4449b769eb2705476586664@65.109.92.241:21326,a7d96dc929824613315dcc1c90fee119f28cc51f@134.65.193.132:26656,66ed3885f2932912df2b04646d2c3d643467719b@212.227.115.165:26656,bba10290da32f3cb41e15c3a192413666ce05cee@136.243.119.241:26656,da04ee3f8bd93421a3264e3a061a09c139aaa937@161.97.150.65:26656,6cceba286b498d4a1931f85e35ea0fa433373057@78.47.208.97:26656,b587bf827b5f680c417601b536ffbd505c88bb07@193.70.45.106:13056,b7295f18b7150cc128d47c0546e2225179fc5427@202.61.194.254:60856,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.54:26656,b204222a9b6ca4eee39a836b7406483a5ad4e719@144.91.114.250:26656,17065f4b6062471aa2e1e615d5061e200a1d44e0@62.171.190.198:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:42656,751513c7cd42a2565c37ab482bbe66f4d92c2740@136.244.106.130:26656,5af4f132d1c63cbe9d828d58522fdbb4bd508880@136.244.29.116:31656,1cb3c50f74b83d29868e11b7e3ead261426a009e@173.249.59.70:35656,312237a27c62e21e3ec5e2a075cba0035db3fb66@95.217.42.107:26656,cb0848b84987c37ba0fa465585c6b9d6cec6deab@65.108.77.98:26696,df99de6cec9152c517990317b340b8b9a307493c@193.34.144.156:26656,320d0d38559140608b72a361db44b2a8f14bf0d1@107.181.229.154:16656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.bcna/config/config.toml
```
