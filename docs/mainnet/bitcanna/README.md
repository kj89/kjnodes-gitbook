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

**live-peers** (15)
```bash
peers="17065f4b6062471aa2e1e615d5061e200a1d44e0@62.171.190.198:26656,d16080503125692e49e7d43275c5de1e48bfff1f@5.9.50.59:26656,b587bf827b5f680c417601b536ffbd505c88bb07@193.70.45.106:13056,2af9f118d9be86892ef47193b6ab9e47046b9f44@74.207.231.41:26656,32b1cf90be5dc6a01dc2684f0bd97bf052690082@144.91.97.191:26656,c6658742ae4c889ecf8dee95ca2a8e4b45d46dfd@85.214.208.127:26656,ec4796daea06ecf0e51819b931fbcb3e1a99b137@144.91.101.49:26656,b204222a9b6ca4eee39a836b7406483a5ad4e719@144.91.114.250:26656,320d0d38559140608b72a361db44b2a8f14bf0d1@107.181.229.154:16656,c124ce0b508e8b9ed1c5b6957f362225659b5343@144.76.177.185:26656,8e4e1f1e087c76c71c64e477e95495833da82aa2@135.181.173.137:26656,2ff33d346b1b0f19cd59018ceb62d06a6406d472@88.99.164.158:21326,881b4ec9a1d37587c44476a22c0864b08b1c88fe@195.3.221.21:13056,a9f839c6e24221fb093f13ee41a0af842378fec5@94.130.12.22:26642,ad820cb2fa85e525538207bb24ee49a61a74eb45@93.115.25.15:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.bcna/config/config.toml
```
