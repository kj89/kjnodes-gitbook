# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/bitcanna.png" width="150" alt=""><figcaption></figcaption></figure>

BitCanna is a proof-of-stake (POS) decentralized payment network designed exclusively to serve the cannabis industry. 

**Chain ID**: bitcanna-1 | **Latest Version Tag**: v1.6.3 | **Wasm**: OFF

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

**live-peers** (18)
```bash
peers="82588f011491c6100d922d133f52fc23460b9231@135.181.67.233:26656,d2247f7b919f0781c90ee61958d7044665a22d38@169.155.169.55:26656,471518432477e31ea348af246c0b54095d41352c@78.47.210.209:26656,751513c7cd42a2565c37ab482bbe66f4d92c2740@136.244.106.130:26656,5bb0a042e8a4ee28bcda1e26148e57787e75a42e@23.88.69.22:28466,104d7ec9d84c8da66b97d50669b8ba58f1b60470@62.171.180.31:26656,b204222a9b6ca4eee39a836b7406483a5ad4e719@144.91.114.250:26656,5cfb82bd566ad3c5330c8326f0da5c7f048aca25@81.0.218.135:24356,b15c0fade5fc0a354b4ac3fd9cdd8a716cddd24a@136.144.182.191:26656,630a9c88188001a4427ef0718c3a8d4e55cee5bb@207.201.218.211:26656,89757803f40da51678451735445ad40d5b15e059@169.155.168.66:26656,9532a13b05e5f68f2ca01f90b3d1ba9a762af817@65.108.131.190:21956,8fa7a04d55ca7d0ab70dc5cbc35d5cf26c5ecfb7@65.108.142.81:26682,9428323a2f7d73dd45c72efdc147f1978e3aa449@45.143.196.110:13056,88c6b1fa1c7fef98b4449b769eb2705476586664@65.109.92.241:21326,0393c19b176d1cf8bc560c5a8fa990301deb1a7e@95.217.126.185:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:42656,dd4d3c0de38aa0575436c34c237b33bc0dda3ef2@142.132.158.93:13056"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.bcna/config/config.toml
```
