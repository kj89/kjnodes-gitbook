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
peers="b587bf827b5f680c417601b536ffbd505c88bb07@193.70.45.106:13056,88c6b1fa1c7fef98b4449b769eb2705476586664@65.109.92.241:21326,d27dc1222e9ab0d90e49490ee315797afa14a03f@65.108.99.254:27656,23671067d0fd40aec523290585c7d8e91034a771@65.108.43.170:26656,8fa7a04d55ca7d0ab70dc5cbc35d5cf26c5ecfb7@65.108.142.81:26682,a7d96dc929824613315dcc1c90fee119f28cc51f@134.65.193.132:26656,66ed3885f2932912df2b04646d2c3d643467719b@212.227.115.165:26656,471518432477e31ea348af246c0b54095d41352c@78.47.210.209:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:42656,881b4ec9a1d37587c44476a22c0864b08b1c88fe@195.3.221.21:13056,7c00beb4956bc40cd33ced6e2c2ffe07d4fa32e7@95.216.242.82:36656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.54:26656,9428323a2f7d73dd45c72efdc147f1978e3aa449@45.143.196.110:13056,d5ed854872ad96f114737889ac9521ea3a29e3a3@185.220.205.209:26656,5cfb82bd566ad3c5330c8326f0da5c7f048aca25@81.0.218.135:24356,0393c19b176d1cf8bc560c5a8fa990301deb1a7e@95.217.126.185:26656,35b0d76e165e5b6852665a5f234eb416b8e045a0@65.21.204.46:31656,4e1c2471efb89239fb04a4b75f9f87177fd91d00@95.217.151.241:26656,df99de6cec9152c517990317b340b8b9a307493c@193.34.144.156:26656,d7322625044ad733bce4178dc397b2b9b5f68b41@43.153.27.130:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.bcna/config/config.toml
```
