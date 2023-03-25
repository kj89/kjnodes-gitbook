# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/bitcanna.png" width="150" alt=""><figcaption></figcaption></figure>

BitCanna is a proof-of-stake (POS) decentralized payment network designed exclusively to serve the cannabis industry. 

**Chain ID**: bitcanna-1 | **Latest Version Tag**: v1.6.2 | **Wasm**: OFF

[Website](https://www.bitcanna.io) | [Discord](https://discord.gg/9AVrzaVQvs) | [Twitter](https://twitter.com/BitCannaGlobal)

[![Stake with kjnodes](https://i.ibb.co/cr44Q8j/button-stake-with-kjnodes.png)](https://restake.app/bitcanna/bcnavaloper1aym6s8eza7kjvnxuwxufrzccz6vqvgnsc47cc7)

Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals

## Restake

[Restake with kjnodes](https://restake.app/bitcanna/bcnavaloper1aym6s8eza7kjvnxuwxufrzccz6vqvgnsc47cc7) (every 5 minutes)
## Chain explorer
[https://explorer.kjnodes.com/bitcanna](https://explorer.kjnodes.com/bitcanna)

## Public endpoints

* api: [https://bitcanna.api.kjnodes.com](https://bitcanna.api.kjnodes.com)
* rpc: [https://bitcanna.rpc.kjnodes.com](https://bitcanna.rpc.kjnodes.com)
* grpc: bitcanna.grpc.kjnodes.com:42090

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
peers="b5ce8fac0dd173d7154b3eb8d10136710e609d1e@95.216.21.37:29656,88c6b1fa1c7fef98b4449b769eb2705476586664@65.109.92.241:21326,d27dc1222e9ab0d90e49490ee315797afa14a03f@65.108.99.254:27656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.54:26656,bba10290da32f3cb41e15c3a192413666ce05cee@136.243.119.241:26656,a9f839c6e24221fb093f13ee41a0af842378fec5@94.130.12.22:26642,b204222a9b6ca4eee39a836b7406483a5ad4e719@144.91.114.250:26656,6be83de3e5ab1a912340ddad3e67d10c32d5b574@161.97.170.83:26656,320d0d38559140608b72a361db44b2a8f14bf0d1@107.181.229.154:16656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:42656,f68feb1847416930fa046a303242adde39ba92e6@154.12.232.8:26656,17065f4b6062471aa2e1e615d5061e200a1d44e0@62.171.190.198:26656,5af4f132d1c63cbe9d828d58522fdbb4bd508880@136.244.29.116:31656,d8a0facda705edbbdd2d79fb302e017df009e9da@207.244.231.189:26656,23671067d0fd40aec523290585c7d8e91034a771@65.108.43.170:26656,5bb0a042e8a4ee28bcda1e26148e57787e75a42e@23.88.69.22:28466,9428323a2f7d73dd45c72efdc147f1978e3aa449@45.143.196.110:13056,8a210f1bcfc9015a7bc18dcc5add29c0dce3f2dc@135.181.173.65:26656,c124ce0b508e8b9ed1c5b6957f362225659b5343@144.76.177.185:26656,b7295f18b7150cc128d47c0546e2225179fc5427@202.61.194.254:60856"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.bcna/config/config.toml
```
