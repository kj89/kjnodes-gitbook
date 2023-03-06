# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/bitcanna.png" width="150" alt=""><figcaption></figcaption></figure>

BitCanna is a proof-of-stake (POS) decentralized payment network designed exclusively to serve the cannabis industry. 

**Chain ID**: bitcanna-1 | **Latest Version Tag**: v1.6.0-fix | **Wasm**: OFF

[Website](https://www.bitcanna.io) | [Discord](https://discord.gg/9AVrzaVQvs) | [Twitter](https://twitter.com/BitCannaGlobal)

[![Stake with kjnodes](https://i.ibb.co/cr44Q8j/button-stake-with-kjnodes.png)](https://restake.app/bitcanna/bcnavaloper1aym6s8eza7kjvnxuwxufrzccz6vqvgnsc47cc7)

## Restake

[Restake with kjnodes](https://restake.app/bitcanna/bcnavaloper1aym6s8eza7kjvnxuwxufrzccz6vqvgnsc47cc7) (e, v, e, r, y,  , 5,  , m, i, n, u, t, e, s)
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

**live-peers** (12)
```bash
peers="02c8045236f844632ef1d4411ad356b3332d4f2f@65.108.226.44:34656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:42656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.54:26656,320d0d38559140608b72a361db44b2a8f14bf0d1@107.181.229.154:16656,d7322625044ad733bce4178dc397b2b9b5f68b41@43.153.27.130:26656,0393c19b176d1cf8bc560c5a8fa990301deb1a7e@95.217.126.185:26656,97e4468ac589eac505a800411c635b14511a61bb@144.76.239.25:26656,2af9f118d9be86892ef47193b6ab9e47046b9f44@74.207.231.41:26656,89757803f40da51678451735445ad40d5b15e059@169.155.168.66:26656,c124ce0b508e8b9ed1c5b6957f362225659b5343@144.76.177.185:26656,a1ceb81a5498642753f8600a5c3b9ca056af3051@67.222.144.195:16656,935a9d809781aa4094dd806c2afed29a25ec8b8e@135.181.210.189:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.bcna/config/config.toml
```
