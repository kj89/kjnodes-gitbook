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
peers="7c00beb4956bc40cd33ced6e2c2ffe07d4fa32e7@95.216.242.82:36656,9532a13b05e5f68f2ca01f90b3d1ba9a762af817@65.108.131.190:21956,4dabde84771e8689403ce7c8b76d27e555ab2f00@65.21.136.170:50656,b5ce8fac0dd173d7154b3eb8d10136710e609d1e@95.216.21.37:29656,d2247f7b919f0781c90ee61958d7044665a22d38@169.155.169.55:26656,89757803f40da51678451735445ad40d5b15e059@169.155.168.66:26656,2c46e946a2375111b345f5bd2a8617c0e5438767@94.130.200.168:46656,32b1cf90be5dc6a01dc2684f0bd97bf052690082@144.91.97.191:26656,8a210f1bcfc9015a7bc18dcc5add29c0dce3f2dc@135.181.173.65:26656,f68feb1847416930fa046a303242adde39ba92e6@154.12.232.8:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:42656,df99de6cec9152c517990317b340b8b9a307493c@193.34.144.156:26656,6be83de3e5ab1a912340ddad3e67d10c32d5b574@161.97.170.83:26656,35b0d76e165e5b6852665a5f234eb416b8e045a0@65.21.204.46:31656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.54:26656,5bb0a042e8a4ee28bcda1e26148e57787e75a42e@23.88.69.22:28466,88c6b1fa1c7fef98b4449b769eb2705476586664@65.109.92.241:21326,8fa7a04d55ca7d0ab70dc5cbc35d5cf26c5ecfb7@65.108.142.81:26682,b587bf827b5f680c417601b536ffbd505c88bb07@193.70.45.106:13056,b7295f18b7150cc128d47c0546e2225179fc5427@202.61.194.254:60856"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.bcna/config/config.toml
```
