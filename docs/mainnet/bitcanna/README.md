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
peers="88c6b1fa1c7fef98b4449b769eb2705476586664@65.109.92.241:21326,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.54:26656,36b45a10fb3afd1687c6e93a07b626709cccb524@148.251.19.197:26706,66ed3885f2932912df2b04646d2c3d643467719b@212.227.115.165:26656,9428323a2f7d73dd45c72efdc147f1978e3aa449@45.143.196.110:13056,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:42656,471518432477e31ea348af246c0b54095d41352c@78.47.210.209:26656,4e1c2471efb89239fb04a4b75f9f87177fd91d00@95.217.151.241:26656,89757803f40da51678451735445ad40d5b15e059@169.155.168.66:26656,0393c19b176d1cf8bc560c5a8fa990301deb1a7e@95.217.126.185:26656,d2247f7b919f0781c90ee61958d7044665a22d38@169.155.169.55:26656,35b0d76e165e5b6852665a5f234eb416b8e045a0@65.21.204.46:31656,751513c7cd42a2565c37ab482bbe66f4d92c2740@136.244.106.130:26656,881b4ec9a1d37587c44476a22c0864b08b1c88fe@195.3.221.21:13056,8a210f1bcfc9015a7bc18dcc5add29c0dce3f2dc@135.181.173.65:26656,cb9741ce22ab5f615913ac11b211c3c7f58dee71@107.191.36.154:26656,5fde69fa32c6d509f920bedf1248c0c5f0369c14@15.165.223.141:26656,104d7ec9d84c8da66b97d50669b8ba58f1b60470@62.171.180.31:26656,5bb0a042e8a4ee28bcda1e26148e57787e75a42e@23.88.69.22:28466,2ff33d346b1b0f19cd59018ceb62d06a6406d472@88.99.164.158:21326"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.bcna/config/config.toml
```
