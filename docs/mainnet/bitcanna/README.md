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

**live-peers** (18)
```bash
peers="88c6b1fa1c7fef98b4449b769eb2705476586664@65.109.92.241:21326,23671067d0fd40aec523290585c7d8e91034a771@65.108.43.170:26656,4dabde84771e8689403ce7c8b76d27e555ab2f00@65.21.136.170:50656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:42656,c124ce0b508e8b9ed1c5b6957f362225659b5343@144.76.177.185:26656,66ed3885f2932912df2b04646d2c3d643467719b@212.227.115.165:26656,6cceba286b498d4a1931f85e35ea0fa433373057@78.47.208.97:26656,32b1cf90be5dc6a01dc2684f0bd97bf052690082@144.91.97.191:26656,a9f839c6e24221fb093f13ee41a0af842378fec5@94.130.12.22:26642,b204222a9b6ca4eee39a836b7406483a5ad4e719@144.91.114.250:26656,f68feb1847416930fa046a303242adde39ba92e6@154.12.232.8:26656,cb9741ce22ab5f615913ac11b211c3c7f58dee71@107.191.36.154:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.54:26656,da04ee3f8bd93421a3264e3a061a09c139aaa937@161.97.150.65:26656,b5ce8fac0dd173d7154b3eb8d10136710e609d1e@95.216.21.37:29656,c6658742ae4c889ecf8dee95ca2a8e4b45d46dfd@85.214.208.127:26656,0393c19b176d1cf8bc560c5a8fa990301deb1a7e@95.217.126.185:26656,bba10290da32f3cb41e15c3a192413666ce05cee@136.243.119.241:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.bcna/config/config.toml
```
