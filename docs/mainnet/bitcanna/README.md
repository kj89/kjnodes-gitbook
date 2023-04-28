# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/bitcanna.png" alt=""><figcaption></figcaption></figure>

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
peers="7c00beb4956bc40cd33ced6e2c2ffe07d4fa32e7@95.216.242.82:36656,5bb0a042e8a4ee28bcda1e26148e57787e75a42e@23.88.69.22:28466,32b1cf90be5dc6a01dc2684f0bd97bf052690082@144.91.97.191:26656,df99de6cec9152c517990317b340b8b9a307493c@193.34.144.156:26656,cb9741ce22ab5f615913ac11b211c3c7f58dee71@107.191.36.154:26656,320d0d38559140608b72a361db44b2a8f14bf0d1@107.181.229.154:16656,65b12d58cc642eb8a1eb4e8344eaf26afce2e6d3@37.120.191.47:36656,66ed3885f2932912df2b04646d2c3d643467719b@212.227.115.165:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:42656,dd4d3c0de38aa0575436c34c237b33bc0dda3ef2@142.132.158.93:13056"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.bcna/config/config.toml
```
