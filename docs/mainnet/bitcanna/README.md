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

**live-peers** (20)
```bash
peers="88c6b1fa1c7fef98b4449b769eb2705476586664@65.109.92.241:21326,89757803f40da51678451735445ad40d5b15e059@169.155.168.66:26656,a7d96dc929824613315dcc1c90fee119f28cc51f@134.65.193.132:26656,dd4d3c0de38aa0575436c34c237b33bc0dda3ef2@142.132.158.93:13056,5bb0a042e8a4ee28bcda1e26148e57787e75a42e@23.88.69.22:28466,d2247f7b919f0781c90ee61958d7044665a22d38@169.155.169.55:26656,104d7ec9d84c8da66b97d50669b8ba58f1b60470@62.171.180.31:26656,b15c0fade5fc0a354b4ac3fd9cdd8a716cddd24a@136.144.182.191:26656,f68feb1847416930fa046a303242adde39ba92e6@154.12.232.8:26656,4dabde84771e8689403ce7c8b76d27e555ab2f00@65.21.136.170:50656,23671067d0fd40aec523290585c7d8e91034a771@65.108.43.170:26656,d27dc1222e9ab0d90e49490ee315797afa14a03f@65.108.99.254:27656,c6658742ae4c889ecf8dee95ca2a8e4b45d46dfd@85.214.208.127:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.54:26656,9428323a2f7d73dd45c72efdc147f1978e3aa449@45.143.196.110:13056,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:42656,48970472844c638389ba56bffd32b73d7b186de6@50.18.24.204:26656,b7295f18b7150cc128d47c0546e2225179fc5427@202.61.194.254:60856,0393c19b176d1cf8bc560c5a8fa990301deb1a7e@95.217.126.185:26656,d7322625044ad733bce4178dc397b2b9b5f68b41@43.153.27.130:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.bcna/config/config.toml
```
