# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/bitcanna.png" width="150" alt=""><figcaption></figcaption></figure>

BitCanna is a proof-of-stake (POS) decentralized payment network designed exclusively to serve the cannabis industry. 

**Chain ID**: bitcanna-1 | **Latest Version Tag**: v1.6.0-fix | **Wasm**: OFF

[Website](https://www.bitcanna.io) | [Discord](https://discord.gg/9AVrzaVQvs) | [Twitter](https://twitter.com/BitCannaGlobal)




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
peers="8a210f1bcfc9015a7bc18dcc5add29c0dce3f2dc@135.181.173.65:26656,4dabde84771e8689403ce7c8b76d27e555ab2f00@65.21.136.170:50656,66ed3885f2932912df2b04646d2c3d643467719b@212.227.115.165:26656,d2247f7b919f0781c90ee61958d7044665a22d38@169.155.169.55:26656,dd4d3c0de38aa0575436c34c237b33bc0dda3ef2@142.132.158.93:13056,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:42656,d27dc1222e9ab0d90e49490ee315797afa14a03f@65.108.99.254:27656,cb9741ce22ab5f615913ac11b211c3c7f58dee71@107.191.36.154:26656,320d0d38559140608b72a361db44b2a8f14bf0d1@107.181.229.154:16656,5bb0a042e8a4ee28bcda1e26148e57787e75a42e@23.88.69.22:28466,b7295f18b7150cc128d47c0546e2225179fc5427@202.61.194.254:60856,4e1c2471efb89239fb04a4b75f9f87177fd91d00@95.217.151.241:26656,da04ee3f8bd93421a3264e3a061a09c139aaa937@161.97.150.65:26656,a1ceb81a5498642753f8600a5c3b9ca056af3051@67.222.144.195:16656,104d7ec9d84c8da66b97d50669b8ba58f1b60470@62.171.180.31:26656,d3796f3f2a179afab1485a672ace3d909cd0eeed@185.137.122.214:26656,3635058fcdbe97e72d191faedfe4c6acab835877@107.181.235.66:16656,36a17684dc4809eb0c722aa4b5bd829b0429e8a1@207.246.84.132:26656,881b4ec9a1d37587c44476a22c0864b08b1c88fe@195.3.221.21:13056,c6658742ae4c889ecf8dee95ca2a8e4b45d46dfd@85.214.208.127:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.bcna/config/config.toml
```
