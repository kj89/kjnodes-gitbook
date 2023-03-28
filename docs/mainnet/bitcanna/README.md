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
peers="88c6b1fa1c7fef98b4449b769eb2705476586664@65.109.92.241:21326,104d7ec9d84c8da66b97d50669b8ba58f1b60470@62.171.180.31:26656,f68feb1847416930fa046a303242adde39ba92e6@154.12.232.8:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:42656,9428323a2f7d73dd45c72efdc147f1978e3aa449@45.143.196.110:13056,c124ce0b508e8b9ed1c5b6957f362225659b5343@144.76.177.185:26656,b7295f18b7150cc128d47c0546e2225179fc5427@202.61.194.254:60856,df99de6cec9152c517990317b340b8b9a307493c@193.34.144.156:26656,845dc78ccd4e3509d0f00dd6151bcebc8dde0324@66.94.99.253:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.54:26656,23671067d0fd40aec523290585c7d8e91034a771@65.108.43.170:26656,7c00beb4956bc40cd33ced6e2c2ffe07d4fa32e7@95.216.242.82:36656,8e4e1f1e087c76c71c64e477e95495833da82aa2@135.181.173.137:26656,cb9741ce22ab5f615913ac11b211c3c7f58dee71@107.191.36.154:26656,4dabde84771e8689403ce7c8b76d27e555ab2f00@65.21.136.170:50656,d8a0facda705edbbdd2d79fb302e017df009e9da@207.244.231.189:26656,0393c19b176d1cf8bc560c5a8fa990301deb1a7e@95.217.126.185:26656,b15c0fade5fc0a354b4ac3fd9cdd8a716cddd24a@136.144.182.191:26656,d7322625044ad733bce4178dc397b2b9b5f68b41@43.153.27.130:26656,dd4d3c0de38aa0575436c34c237b33bc0dda3ef2@142.132.158.93:13056"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.bcna/config/config.toml
```
