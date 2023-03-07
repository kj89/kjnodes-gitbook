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

**live-peers** (15)
```bash
peers="5bb0a042e8a4ee28bcda1e26148e57787e75a42e@23.88.69.22:28466,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:42656,88c6b1fa1c7fef98b4449b769eb2705476586664@65.109.92.241:21326,935a9d809781aa4094dd806c2afed29a25ec8b8e@135.181.210.189:26656,d7322625044ad733bce4178dc397b2b9b5f68b41@43.153.27.130:26656,4e1c2471efb89239fb04a4b75f9f87177fd91d00@95.217.151.241:26656,48970472844c638389ba56bffd32b73d7b186de6@50.18.24.204:26656,17065f4b6062471aa2e1e615d5061e200a1d44e0@62.171.190.198:26656,a66bce0ddb49dcf60a5b83fd94a7bd4d0878f127@154.53.40.9:26656,471518432477e31ea348af246c0b54095d41352c@78.47.210.209:26656,7c00beb4956bc40cd33ced6e2c2ffe07d4fa32e7@95.216.242.82:36656,b5ce8fac0dd173d7154b3eb8d10136710e609d1e@95.216.21.37:29656,c6658742ae4c889ecf8dee95ca2a8e4b45d46dfd@85.214.208.127:26656,66ed3885f2932912df2b04646d2c3d643467719b@212.227.115.165:26656,881b4ec9a1d37587c44476a22c0864b08b1c88fe@195.3.221.21:13056"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.bcna/config/config.toml
```
