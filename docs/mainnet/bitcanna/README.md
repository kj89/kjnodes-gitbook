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
peers="7c00beb4956bc40cd33ced6e2c2ffe07d4fa32e7@95.216.242.82:36656,4e1c2471efb89239fb04a4b75f9f87177fd91d00@95.217.151.241:26656,8a210f1bcfc9015a7bc18dcc5add29c0dce3f2dc@135.181.173.65:26656,dd4d3c0de38aa0575436c34c237b33bc0dda3ef2@142.132.158.93:13056,97e4468ac589eac505a800411c635b14511a61bb@144.76.239.25:26656,471518432477e31ea348af246c0b54095d41352c@78.47.210.209:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.54:26656,104d7ec9d84c8da66b97d50669b8ba58f1b60470@62.171.180.31:26656,b204222a9b6ca4eee39a836b7406483a5ad4e719@144.91.114.250:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:42656,a66bce0ddb49dcf60a5b83fd94a7bd4d0878f127@154.53.40.9:26656,17065f4b6062471aa2e1e615d5061e200a1d44e0@62.171.190.198:26656,a9f839c6e24221fb093f13ee41a0af842378fec5@94.130.12.22:26642,f68feb1847416930fa046a303242adde39ba92e6@154.12.232.8:26656,881b4ec9a1d37587c44476a22c0864b08b1c88fe@195.3.221.21:13056,a7d96dc929824613315dcc1c90fee119f28cc51f@134.65.193.132:26656,320d0d38559140608b72a361db44b2a8f14bf0d1@107.181.229.154:16656,751513c7cd42a2565c37ab482bbe66f4d92c2740@136.244.106.130:26656,a1ceb81a5498642753f8600a5c3b9ca056af3051@67.222.144.195:16656,88c6b1fa1c7fef98b4449b769eb2705476586664@65.109.92.241:21326"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.bcna/config/config.toml
```
