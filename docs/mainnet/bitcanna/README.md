# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/bitcanna.png" width="150" alt=""><figcaption></figcaption></figure>

BitCanna is a proof-of-stake (POS) decentralized payment network designed exclusively to serve the cannabis industry. 

**Chain ID**: bitcanna-1 | **Latest Version Tag**: v1.6.1 | **Wasm**: OFF

[Website](https://www.bitcanna.io) | [Discord](https://discord.gg/9AVrzaVQvs) | [Twitter](https://twitter.com/BitCannaGlobal)

[![Stake with kjnodes](https://i.ibb.co/cr44Q8j/button-stake-with-kjnodes.png)](https://restake.app/bitcanna/bcnavaloper1aym6s8eza7kjvnxuwxufrzccz6vqvgnsc47cc7)

## Restake

[Restake with kjnodes](https://restake.app/bitcanna/bcnavaloper1aym6s8eza7kjvnxuwxufrzccz6vqvgnsc47cc7) (every 5 minutes)
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

**live-peers** (20)
```bash
peers="d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:42656,17065f4b6062471aa2e1e615d5061e200a1d44e0@62.171.190.198:26656,f68feb1847416930fa046a303242adde39ba92e6@154.12.232.8:26656,df99de6cec9152c517990317b340b8b9a307493c@193.34.144.156:26656,82588f011491c6100d922d133f52fc23460b9231@135.181.67.233:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.54:26656,88c6b1fa1c7fef98b4449b769eb2705476586664@65.109.92.241:21326,b7295f18b7150cc128d47c0546e2225179fc5427@202.61.194.254:60856,c6658742ae4c889ecf8dee95ca2a8e4b45d46dfd@85.214.208.127:26656,a7d96dc929824613315dcc1c90fee119f28cc51f@134.65.193.132:26656,bba10290da32f3cb41e15c3a192413666ce05cee@136.243.119.241:26656,48970472844c638389ba56bffd32b73d7b186de6@50.18.24.204:26656,89757803f40da51678451735445ad40d5b15e059@169.155.168.66:26656,c124ce0b508e8b9ed1c5b6957f362225659b5343@144.76.177.185:26656,8a210f1bcfc9015a7bc18dcc5add29c0dce3f2dc@135.181.173.65:26656,97e4468ac589eac505a800411c635b14511a61bb@144.76.239.25:26656,d2247f7b919f0781c90ee61958d7044665a22d38@169.155.169.55:26656,320d0d38559140608b72a361db44b2a8f14bf0d1@107.181.229.154:16656,471518432477e31ea348af246c0b54095d41352c@78.47.210.209:26656,2ff33d346b1b0f19cd59018ceb62d06a6406d472@88.99.164.158:21326"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.bcna/config/config.toml
```
