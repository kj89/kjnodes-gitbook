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

**live-peers** (14)
```bash
peers="320d0d38559140608b72a361db44b2a8f14bf0d1@107.181.229.154:16656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:42656,8e4e1f1e087c76c71c64e477e95495833da82aa2@135.181.173.137:26656,d16080503125692e49e7d43275c5de1e48bfff1f@5.9.50.59:26656,ad820cb2fa85e525538207bb24ee49a61a74eb45@93.115.25.15:26656,b204222a9b6ca4eee39a836b7406483a5ad4e719@144.91.114.250:26656,7c00beb4956bc40cd33ced6e2c2ffe07d4fa32e7@95.216.242.82:36656,a66bce0ddb49dcf60a5b83fd94a7bd4d0878f127@154.53.40.9:26656,97e4468ac589eac505a800411c635b14511a61bb@144.76.239.25:26656,4dabde84771e8689403ce7c8b76d27e555ab2f00@65.21.136.170:50656,c124ce0b508e8b9ed1c5b6957f362225659b5343@144.76.177.185:26656,5bb0a042e8a4ee28bcda1e26148e57787e75a42e@23.88.69.22:28466,6cceba286b498d4a1931f85e35ea0fa433373057@78.47.208.97:26656,ec4796daea06ecf0e51819b931fbcb3e1a99b137@144.91.101.49:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.bcna/config/config.toml
```
