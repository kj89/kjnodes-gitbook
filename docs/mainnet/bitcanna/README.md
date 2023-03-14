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

**live-peers** (19)
```bash
peers="b5ce8fac0dd173d7154b3eb8d10136710e609d1e@95.216.21.37:29656,a7d96dc929824613315dcc1c90fee119f28cc51f@134.65.193.132:26656,89757803f40da51678451735445ad40d5b15e059@169.155.168.66:26656,d2247f7b919f0781c90ee61958d7044665a22d38@169.155.169.55:26656,b587bf827b5f680c417601b536ffbd505c88bb07@193.70.45.106:13056,97e4468ac589eac505a800411c635b14511a61bb@144.76.239.25:26656,104d7ec9d84c8da66b97d50669b8ba58f1b60470@62.171.180.31:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:42656,881b4ec9a1d37587c44476a22c0864b08b1c88fe@195.3.221.21:13056,471518432477e31ea348af246c0b54095d41352c@78.47.210.209:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.54:26656,dd4d3c0de38aa0575436c34c237b33bc0dda3ef2@142.132.158.93:13056,320d0d38559140608b72a361db44b2a8f14bf0d1@107.181.229.154:16656,b7295f18b7150cc128d47c0546e2225179fc5427@202.61.194.254:60856,cb0848b84987c37ba0fa465585c6b9d6cec6deab@65.108.77.98:26696,35b0d76e165e5b6852665a5f234eb416b8e045a0@65.21.204.46:31656,88c6b1fa1c7fef98b4449b769eb2705476586664@65.109.92.241:21326,f68feb1847416930fa046a303242adde39ba92e6@154.12.232.8:26656,17065f4b6062471aa2e1e615d5061e200a1d44e0@62.171.190.198:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.bcna/config/config.toml
```
