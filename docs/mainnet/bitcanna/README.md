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
peers="4e1c2471efb89239fb04a4b75f9f87177fd91d00@95.217.151.241:26656,dd4d3c0de38aa0575436c34c237b33bc0dda3ef2@142.132.158.93:13056,5bb0a042e8a4ee28bcda1e26148e57787e75a42e@23.88.69.22:28466,471518432477e31ea348af246c0b54095d41352c@78.47.210.209:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:42656,6cceba286b498d4a1931f85e35ea0fa433373057@78.47.208.97:26656,845dc78ccd4e3509d0f00dd6151bcebc8dde0324@66.94.99.253:26656,0393c19b176d1cf8bc560c5a8fa990301deb1a7e@95.217.126.185:26656,d8a0facda705edbbdd2d79fb302e017df009e9da@207.244.231.189:26656,b587bf827b5f680c417601b536ffbd505c88bb07@193.70.45.106:13056,17065f4b6062471aa2e1e615d5061e200a1d44e0@62.171.190.198:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.54:26656,89757803f40da51678451735445ad40d5b15e059@169.155.168.66:26656,b7295f18b7150cc128d47c0546e2225179fc5427@202.61.194.254:60856,8e4e1f1e087c76c71c64e477e95495833da82aa2@135.181.173.137:26656,35b0d76e165e5b6852665a5f234eb416b8e045a0@65.21.204.46:31656,f68feb1847416930fa046a303242adde39ba92e6@154.12.232.8:26656,9428323a2f7d73dd45c72efdc147f1978e3aa449@45.143.196.110:13056,c6658742ae4c889ecf8dee95ca2a8e4b45d46dfd@85.214.208.127:26656,a66bce0ddb49dcf60a5b83fd94a7bd4d0878f127@154.53.40.9:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.bcna/config/config.toml
```
