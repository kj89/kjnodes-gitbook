# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/bitcanna.png" width="150" alt=""><figcaption></figcaption></figure>

BitCanna is a proof-of-stake (POS) decentralized payment network designed exclusively to serve the cannabis industry. 

**Chain ID**: bitcanna-1 | **Latest Version Tag**: v1.5.3 | **Wasm**: OFF

[Website](https://www.bitcanna.io) | [Discord](https://discord.gg/9AVrzaVQvs) | [Twitter](https://twitter.com/BitCannaGlobal)


## Public endpoints

* rpc: [https://bitcanna.rpc.kjnodes.com](https://bitcanna.rpc.kjnodes.com)
* api: [https://bitcanna.api.kjnodes.com](https://bitcanna.api.kjnodes.com)

## Peering

**state-sync**

```
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@bitcanna.rpc.kjnodes.com:42656
```

**seed-node**

```
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@bitcanna.rpc.kjnodes.com:42659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/bitcanna/addrbook.json > $HOME/.bcna/config/addrbook.json
```

**live-peers** (10)
```
peers="43f8f9eee8fe7de19e958edb4e95185ab40f8e39@65.108.238.104:13056,17de6cb601246b429027545e420df0a60fe3591e@65.21.200.224:13056,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.54:26656,881b4ec9a1d37587c44476a22c0864b08b1c88fe@195.3.221.21:13056,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:42656,1b01a388eaba8f15634c1e5cd5bb7c55810250d2@135.181.219.115:27656,471518432477e31ea348af246c0b54095d41352c@78.47.210.209:26656,a9f839c6e24221fb093f13ee41a0af842378fec5@94.130.12.22:26642,d2247f7b919f0781c90ee61958d7044665a22d38@169.155.169.55:26656,935a9d809781aa4094dd806c2afed29a25ec8b8e@135.181.210.189:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.bcna/config/config.toml
```
