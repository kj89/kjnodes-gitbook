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

**live-peers** (19)
```bash
peers="d27dc1222e9ab0d90e49490ee315797afa14a03f@65.108.99.254:27656,b5ce8fac0dd173d7154b3eb8d10136710e609d1e@95.216.21.37:29656,8e4e1f1e087c76c71c64e477e95495833da82aa2@135.181.173.137:26656,8fa7a04d55ca7d0ab70dc5cbc35d5cf26c5ecfb7@65.108.142.81:26682,a66bce0ddb49dcf60a5b83fd94a7bd4d0878f127@154.53.40.9:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:42656,dd4d3c0de38aa0575436c34c237b33bc0dda3ef2@142.132.158.93:13056,32b1cf90be5dc6a01dc2684f0bd97bf052690082@144.91.97.191:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.54:26656,5af4f132d1c63cbe9d828d58522fdbb4bd508880@136.244.29.116:31656,cb9741ce22ab5f615913ac11b211c3c7f58dee71@107.191.36.154:26656,d8a0facda705edbbdd2d79fb302e017df009e9da@207.244.231.189:26656,9428323a2f7d73dd45c72efdc147f1978e3aa449@45.143.196.110:13056,630a9c88188001a4427ef0718c3a8d4e55cee5bb@207.201.218.211:26656,b15c0fade5fc0a354b4ac3fd9cdd8a716cddd24a@136.144.182.191:26656,5bb0a042e8a4ee28bcda1e26148e57787e75a42e@23.88.69.22:28466,36a17684dc4809eb0c722aa4b5bd829b0429e8a1@207.246.84.132:26656,4dabde84771e8689403ce7c8b76d27e555ab2f00@65.21.136.170:50656,48970472844c638389ba56bffd32b73d7b186de6@50.18.24.204:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.bcna/config/config.toml
```
