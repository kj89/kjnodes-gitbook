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

**live-peers** (19)
```bash
peers="4dabde84771e8689403ce7c8b76d27e555ab2f00@65.21.136.170:50656,88c6b1fa1c7fef98b4449b769eb2705476586664@65.109.92.241:21326,803fc66e3bd7b724921ef9c40636067f36e880c6@65.108.199.222:26356,b5ce8fac0dd173d7154b3eb8d10136710e609d1e@95.216.21.37:29656,17065f4b6062471aa2e1e615d5061e200a1d44e0@62.171.190.198:26656,32b1cf90be5dc6a01dc2684f0bd97bf052690082@144.91.97.191:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:42656,35b0d76e165e5b6852665a5f234eb416b8e045a0@65.21.204.46:31656,2c46e946a2375111b345f5bd2a8617c0e5438767@94.130.200.168:46656,471518432477e31ea348af246c0b54095d41352c@78.47.210.209:26656,8e4e1f1e087c76c71c64e477e95495833da82aa2@135.181.173.137:26656,1cb3c50f74b83d29868e11b7e3ead261426a009e@173.249.59.70:35656,b587bf827b5f680c417601b536ffbd505c88bb07@193.70.45.106:13056,881b4ec9a1d37587c44476a22c0864b08b1c88fe@195.3.221.21:13056,df99de6cec9152c517990317b340b8b9a307493c@193.34.144.156:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.54:26656,36b45a10fb3afd1687c6e93a07b626709cccb524@148.251.19.197:26706,b7295f18b7150cc128d47c0546e2225179fc5427@202.61.194.254:60856,320d0d38559140608b72a361db44b2a8f14bf0d1@107.181.229.154:16656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.bcna/config/config.toml
```
