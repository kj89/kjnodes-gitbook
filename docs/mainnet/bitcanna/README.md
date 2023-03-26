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
peers="9532a13b05e5f68f2ca01f90b3d1ba9a762af817@65.108.131.190:21956,4dabde84771e8689403ce7c8b76d27e555ab2f00@65.21.136.170:50656,d2247f7b919f0781c90ee61958d7044665a22d38@169.155.169.55:26656,89757803f40da51678451735445ad40d5b15e059@169.155.168.66:26656,a9f839c6e24221fb093f13ee41a0af842378fec5@94.130.12.22:26642,17065f4b6062471aa2e1e615d5061e200a1d44e0@62.171.190.198:26656,b15c0fade5fc0a354b4ac3fd9cdd8a716cddd24a@136.144.182.191:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:42656,23671067d0fd40aec523290585c7d8e91034a771@65.108.43.170:26656,df99de6cec9152c517990317b340b8b9a307493c@193.34.144.156:26656,b7295f18b7150cc128d47c0546e2225179fc5427@202.61.194.254:60856,66ed3885f2932912df2b04646d2c3d643467719b@212.227.115.165:26656,d7322625044ad733bce4178dc397b2b9b5f68b41@43.153.27.130:26656,88c6b1fa1c7fef98b4449b769eb2705476586664@65.109.92.241:21326,5af4f132d1c63cbe9d828d58522fdbb4bd508880@136.244.29.116:31656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.54:26656,6cceba286b498d4a1931f85e35ea0fa433373057@78.47.208.97:26656,a7d96dc929824613315dcc1c90fee119f28cc51f@134.65.193.132:26656,320d0d38559140608b72a361db44b2a8f14bf0d1@107.181.229.154:16656,c124ce0b508e8b9ed1c5b6957f362225659b5343@144.76.177.185:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.bcna/config/config.toml
```
