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

**live-peers** (19)
```bash
peers="d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:42656,0393c19b176d1cf8bc560c5a8fa990301deb1a7e@95.217.126.185:26656,89757803f40da51678451735445ad40d5b15e059@169.155.168.66:26656,66ed3885f2932912df2b04646d2c3d643467719b@212.227.115.165:26656,6cceba286b498d4a1931f85e35ea0fa433373057@78.47.208.97:26656,d4cef8cf26d1d6b7167ac6c15601965081176df7@144.91.118.216:26656,5bb0a042e8a4ee28bcda1e26148e57787e75a42e@23.88.69.22:28466,471518432477e31ea348af246c0b54095d41352c@78.47.210.209:26656,f68feb1847416930fa046a303242adde39ba92e6@154.12.232.8:26656,a66bce0ddb49dcf60a5b83fd94a7bd4d0878f127@154.53.40.9:26656,d2247f7b919f0781c90ee61958d7044665a22d38@169.155.169.55:26656,4dabde84771e8689403ce7c8b76d27e555ab2f00@65.21.136.170:50656,4e1c2471efb89239fb04a4b75f9f87177fd91d00@95.217.151.241:26656,35b0d76e165e5b6852665a5f234eb416b8e045a0@65.21.204.46:31656,b204222a9b6ca4eee39a836b7406483a5ad4e719@144.91.114.250:26656,df99de6cec9152c517990317b340b8b9a307493c@193.34.144.156:26656,9428323a2f7d73dd45c72efdc147f1978e3aa449@45.143.196.110:13056,88c6b1fa1c7fef98b4449b769eb2705476586664@65.109.92.241:21326,7c00beb4956bc40cd33ced6e2c2ffe07d4fa32e7@95.216.242.82:36656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.bcna/config/config.toml
```
