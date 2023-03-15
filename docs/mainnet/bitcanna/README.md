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
peers="d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:42656,9532a13b05e5f68f2ca01f90b3d1ba9a762af817@65.108.131.190:21956,89757803f40da51678451735445ad40d5b15e059@169.155.168.66:26656,66ed3885f2932912df2b04646d2c3d643467719b@212.227.115.165:26656,b204222a9b6ca4eee39a836b7406483a5ad4e719@144.91.114.250:26656,17065f4b6062471aa2e1e615d5061e200a1d44e0@62.171.190.198:26656,36b45a10fb3afd1687c6e93a07b626709cccb524@148.251.19.197:26706,1cb3c50f74b83d29868e11b7e3ead261426a009e@173.249.59.70:35656,320d0d38559140608b72a361db44b2a8f14bf0d1@107.181.229.154:16656,d7322625044ad733bce4178dc397b2b9b5f68b41@43.153.27.130:26656,4e1c2471efb89239fb04a4b75f9f87177fd91d00@95.217.151.241:26656,a7d96dc929824613315dcc1c90fee119f28cc51f@134.65.193.132:26656,c124ce0b508e8b9ed1c5b6957f362225659b5343@144.76.177.185:26656,df99de6cec9152c517990317b340b8b9a307493c@193.34.144.156:26656,b5ce8fac0dd173d7154b3eb8d10136710e609d1e@95.216.21.37:29656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.54:26656,471518432477e31ea348af246c0b54095d41352c@78.47.210.209:26656,88c6b1fa1c7fef98b4449b769eb2705476586664@65.109.92.241:21326,6be83de3e5ab1a912340ddad3e67d10c32d5b574@161.97.170.83:26656,a1ceb81a5498642753f8600a5c3b9ca056af3051@67.222.144.195:16656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.bcna/config/config.toml
```
