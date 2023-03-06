# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/bitcanna.png" width="150" alt=""><figcaption></figcaption></figure>

BitCanna is a proof-of-stake (POS) decentralized payment network designed exclusively to serve the cannabis industry. 

**Chain ID**: bitcanna-1 | **Latest Version Tag**: v1.6.0-fix | **Wasm**: OFF

[Website](https://www.bitcanna.io) | [Discord](https://discord.gg/9AVrzaVQvs) | [Twitter](https://twitter.com/BitCannaGlobal)

[![Stake with kjnodes](https://i.ibb.co/cr44Q8j/button-stake-with-kjnodes.png)](https://restake.app/bitcanna/bcnavaloper1aym6s8eza7kjvnxuwxufrzccz6vqvgnsc47cc7)

## Restake

[Restake with kjnodes](https://restake.app/bitcanna/bcnavaloper1aym6s8eza7kjvnxuwxufrzccz6vqvgnsc47cc7) (e, v, e, r, y,  , 5,  , m, i, n, u, t, e, s)
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
peers="89757803f40da51678451735445ad40d5b15e059@169.155.168.66:26656,02c8045236f844632ef1d4411ad356b3332d4f2f@65.108.226.44:34656,f68feb1847416930fa046a303242adde39ba92e6@154.12.232.8:26656,cb9741ce22ab5f615913ac11b211c3c7f58dee71@107.191.36.154:26656,4dabde84771e8689403ce7c8b76d27e555ab2f00@65.21.136.170:50656,a9f839c6e24221fb093f13ee41a0af842378fec5@94.130.12.22:26642,88c6b1fa1c7fef98b4449b769eb2705476586664@65.109.92.241:21326,97e4468ac589eac505a800411c635b14511a61bb@144.76.239.25:26656,8a210f1bcfc9015a7bc18dcc5add29c0dce3f2dc@135.181.173.65:26656,6be83de3e5ab1a912340ddad3e67d10c32d5b574@161.97.170.83:26656,66ed3885f2932912df2b04646d2c3d643467719b@212.227.115.165:26656,c124ce0b508e8b9ed1c5b6957f362225659b5343@144.76.177.185:26656,8e4e1f1e087c76c71c64e477e95495833da82aa2@135.181.173.137:26656,5bb0a042e8a4ee28bcda1e26148e57787e75a42e@23.88.69.22:28466"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.bcna/config/config.toml
```
