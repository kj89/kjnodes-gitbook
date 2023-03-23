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
peers="8fa7a04d55ca7d0ab70dc5cbc35d5cf26c5ecfb7@65.108.142.81:26682,4dabde84771e8689403ce7c8b76d27e555ab2f00@65.21.136.170:50656,c124ce0b508e8b9ed1c5b6957f362225659b5343@144.76.177.185:26656,b7295f18b7150cc128d47c0546e2225179fc5427@202.61.194.254:60856,df99de6cec9152c517990317b340b8b9a307493c@193.34.144.156:26656,9428323a2f7d73dd45c72efdc147f1978e3aa449@45.143.196.110:13056,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:42656,35b0d76e165e5b6852665a5f234eb416b8e045a0@65.21.204.46:31656,23671067d0fd40aec523290585c7d8e91034a771@65.108.43.170:26656,0393c19b176d1cf8bc560c5a8fa990301deb1a7e@95.217.126.185:26656,88c6b1fa1c7fef98b4449b769eb2705476586664@65.109.92.241:21326,d8a0facda705edbbdd2d79fb302e017df009e9da@207.244.231.189:26656,bba10290da32f3cb41e15c3a192413666ce05cee@136.243.119.241:26656,36b45a10fb3afd1687c6e93a07b626709cccb524@148.251.19.197:26706,a7d96dc929824613315dcc1c90fee119f28cc51f@134.65.193.132:26656,89757803f40da51678451735445ad40d5b15e059@169.155.168.66:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.54:26656,66ed3885f2932912df2b04646d2c3d643467719b@212.227.115.165:26656,5bb0a042e8a4ee28bcda1e26148e57787e75a42e@23.88.69.22:28466,5af4f132d1c63cbe9d828d58522fdbb4bd508880@136.244.29.116:31656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.bcna/config/config.toml
```
