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

**live-peers** (18)
```bash
peers="0393c19b176d1cf8bc560c5a8fa990301deb1a7e@95.217.126.185:26656,b5ce8fac0dd173d7154b3eb8d10136710e609d1e@95.216.21.37:29656,a7d96dc929824613315dcc1c90fee119f28cc51f@134.65.193.132:26656,2c46e946a2375111b345f5bd2a8617c0e5438767@94.130.200.168:46656,36b45a10fb3afd1687c6e93a07b626709cccb524@148.251.19.197:26706,ec4796daea06ecf0e51819b931fbcb3e1a99b137@144.91.101.49:26656,d2247f7b919f0781c90ee61958d7044665a22d38@169.155.169.55:26656,471518432477e31ea348af246c0b54095d41352c@78.47.210.209:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:42656,b587bf827b5f680c417601b536ffbd505c88bb07@193.70.45.106:13056,320d0d38559140608b72a361db44b2a8f14bf0d1@107.181.229.154:16656,23671067d0fd40aec523290585c7d8e91034a771@65.108.43.170:26656,803fc66e3bd7b724921ef9c40636067f36e880c6@65.108.199.222:26356,4dabde84771e8689403ce7c8b76d27e555ab2f00@65.21.136.170:50656,89757803f40da51678451735445ad40d5b15e059@169.155.168.66:26656,4e1c2471efb89239fb04a4b75f9f87177fd91d00@95.217.151.241:26656,ad820cb2fa85e525538207bb24ee49a61a74eb45@93.115.25.15:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.54:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.bcna/config/config.toml
```
