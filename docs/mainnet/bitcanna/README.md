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
peers="4dabde84771e8689403ce7c8b76d27e555ab2f00@65.21.136.170:50656,0393c19b176d1cf8bc560c5a8fa990301deb1a7e@95.217.126.185:26656,88c6b1fa1c7fef98b4449b769eb2705476586664@65.109.92.241:21326,d2247f7b919f0781c90ee61958d7044665a22d38@169.155.169.55:26656,5bb0a042e8a4ee28bcda1e26148e57787e75a42e@23.88.69.22:28466,8a3d8b8a6608f19fbdb34d330c9c9dd44a756a38@88.198.52.150:26666,bba10290da32f3cb41e15c3a192413666ce05cee@136.243.119.241:26656,2c46e946a2375111b345f5bd2a8617c0e5438767@94.130.200.168:46656,104d7ec9d84c8da66b97d50669b8ba58f1b60470@62.171.180.31:26656,9428323a2f7d73dd45c72efdc147f1978e3aa449@45.143.196.110:13056,f68feb1847416930fa046a303242adde39ba92e6@154.12.232.8:26656,845dc78ccd4e3509d0f00dd6151bcebc8dde0324@66.94.99.253:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:42656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.54:26656,dd4d3c0de38aa0575436c34c237b33bc0dda3ef2@142.132.158.93:13056,5cfb82bd566ad3c5330c8326f0da5c7f048aca25@81.0.218.135:24356,97e4468ac589eac505a800411c635b14511a61bb@144.76.239.25:26656,5af4f132d1c63cbe9d828d58522fdbb4bd508880@136.244.29.116:31656,66ed3885f2932912df2b04646d2c3d643467719b@212.227.115.165:26656,630a9c88188001a4427ef0718c3a8d4e55cee5bb@207.201.218.211:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.bcna/config/config.toml
```
