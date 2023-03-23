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

**live-peers** (18)
```bash
peers="0393c19b176d1cf8bc560c5a8fa990301deb1a7e@95.217.126.185:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.54:26656,89757803f40da51678451735445ad40d5b15e059@169.155.168.66:26656,36b45a10fb3afd1687c6e93a07b626709cccb524@148.251.19.197:26706,471518432477e31ea348af246c0b54095d41352c@78.47.210.209:26656,b587bf827b5f680c417601b536ffbd505c88bb07@193.70.45.106:13056,a7d96dc929824613315dcc1c90fee119f28cc51f@134.65.193.132:26656,88c6b1fa1c7fef98b4449b769eb2705476586664@65.109.92.241:21326,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:42656,d2247f7b919f0781c90ee61958d7044665a22d38@169.155.169.55:26656,35b0d76e165e5b6852665a5f234eb416b8e045a0@65.21.204.46:31656,dd4d3c0de38aa0575436c34c237b33bc0dda3ef2@142.132.158.93:13056,1cb3c50f74b83d29868e11b7e3ead261426a009e@173.249.59.70:35656,23671067d0fd40aec523290585c7d8e91034a771@65.108.43.170:26656,cb9741ce22ab5f615913ac11b211c3c7f58dee71@107.191.36.154:26656,b204222a9b6ca4eee39a836b7406483a5ad4e719@144.91.114.250:26656,d8a0facda705edbbdd2d79fb302e017df009e9da@207.244.231.189:26656,5bb0a042e8a4ee28bcda1e26148e57787e75a42e@23.88.69.22:28466"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.bcna/config/config.toml
```
