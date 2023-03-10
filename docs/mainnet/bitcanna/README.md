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

**live-peers** (14)
```bash
peers="f68feb1847416930fa046a303242adde39ba92e6@154.12.232.8:26656,4dabde84771e8689403ce7c8b76d27e555ab2f00@65.21.136.170:50656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.54:26656,d4cef8cf26d1d6b7167ac6c15601965081176df7@144.91.118.216:26656,320d0d38559140608b72a361db44b2a8f14bf0d1@107.181.229.154:16656,a1ceb81a5498642753f8600a5c3b9ca056af3051@67.222.144.195:16656,df99de6cec9152c517990317b340b8b9a307493c@193.34.144.156:26656,8e4e1f1e087c76c71c64e477e95495833da82aa2@135.181.173.137:26656,c124ce0b508e8b9ed1c5b6957f362225659b5343@144.76.177.185:26656,32b1cf90be5dc6a01dc2684f0bd97bf052690082@144.91.97.191:26656,d2247f7b919f0781c90ee61958d7044665a22d38@169.155.169.55:26656,2ff33d346b1b0f19cd59018ceb62d06a6406d472@88.99.164.158:21326,97e4468ac589eac505a800411c635b14511a61bb@144.76.239.25:26656,7546889cad5cb44012a9b190bee9c5a8d92d47cd@73.40.151.121:31656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.bcna/config/config.toml
```
