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
peers="d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:42656,88c6b1fa1c7fef98b4449b769eb2705476586664@65.109.92.241:21326,82588f011491c6100d922d133f52fc23460b9231@135.181.67.233:26656,6be83de3e5ab1a912340ddad3e67d10c32d5b574@161.97.170.83:26656,36b45a10fb3afd1687c6e93a07b626709cccb524@148.251.19.197:26706,6cceba286b498d4a1931f85e35ea0fa433373057@78.47.208.97:26656,36a17684dc4809eb0c722aa4b5bd829b0429e8a1@207.246.84.132:26656,320d0d38559140608b72a361db44b2a8f14bf0d1@107.181.229.154:16656,846fca7d90fdc1ddbcf1892a0b6338a44e93b76d@65.108.0.93:36656,89757803f40da51678451735445ad40d5b15e059@169.155.168.66:26656,f68feb1847416930fa046a303242adde39ba92e6@154.12.232.8:26656,c124ce0b508e8b9ed1c5b6957f362225659b5343@144.76.177.185:26656,bba10290da32f3cb41e15c3a192413666ce05cee@136.243.119.241:26656,35b0d76e165e5b6852665a5f234eb416b8e045a0@65.21.204.46:31656,d2247f7b919f0781c90ee61958d7044665a22d38@169.155.169.55:26656,7c00beb4956bc40cd33ced6e2c2ffe07d4fa32e7@95.216.242.82:36656,b7295f18b7150cc128d47c0546e2225179fc5427@202.61.194.254:60856,df99de6cec9152c517990317b340b8b9a307493c@193.34.144.156:26656,dd4d3c0de38aa0575436c34c237b33bc0dda3ef2@142.132.158.93:13056,0393c19b176d1cf8bc560c5a8fa990301deb1a7e@95.217.126.185:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.bcna/config/config.toml
```
