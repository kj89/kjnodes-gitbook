# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/bitcanna.png" width="150" alt=""><figcaption></figcaption></figure>

BitCanna is a proof-of-stake (POS) decentralized payment network designed exclusively to serve the cannabis industry. 

**Chain ID**: bitcanna-1 | **Latest Version Tag**: v1.6.3 | **Wasm**: OFF

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

**live-peers** (10)
```bash
peers="da04ee3f8bd93421a3264e3a061a09c139aaa937@161.97.150.65:26656,b15c0fade5fc0a354b4ac3fd9cdd8a716cddd24a@136.144.182.191:26656,9428323a2f7d73dd45c72efdc147f1978e3aa449@45.143.196.110:13056,23671067d0fd40aec523290585c7d8e91034a771@65.108.43.170:26656,320d0d38559140608b72a361db44b2a8f14bf0d1@107.181.229.154:16656,751513c7cd42a2565c37ab482bbe66f4d92c2740@136.244.106.130:26656,c124ce0b508e8b9ed1c5b6957f362225659b5343@144.76.177.185:26656,88c6b1fa1c7fef98b4449b769eb2705476586664@65.109.92.241:21326,d2247f7b919f0781c90ee61958d7044665a22d38@169.155.169.55:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:42656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.bcna/config/config.toml
```
