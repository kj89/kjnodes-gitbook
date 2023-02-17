# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/bitcanna.png" width="150" alt=""><figcaption></figcaption></figure>

BitCanna is a proof-of-stake (POS) decentralized payment network designed exclusively to serve the cannabis industry. 

**Chain ID**: bitcanna-1 | **Latest Version Tag**: v1.5.3 | **Wasm**: OFF

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

**live-peers** (10)
```bash
peers="8a210f1bcfc9015a7bc18dcc5add29c0dce3f2dc@135.181.173.65:26656,82588f011491c6100d922d133f52fc23460b9231@135.181.67.233:26656,d2247f7b919f0781c90ee61958d7044665a22d38@169.155.169.55:26656,d3796f3f2a179afab1485a672ace3d909cd0eeed@185.137.122.214:26656,9065a2ebd940ad44e2955361fe27809b9f6e2765@159.148.31.234:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:42656,a1ceb81a5498642753f8600a5c3b9ca056af3051@67.222.144.195:16656,d7322625044ad733bce4178dc397b2b9b5f68b41@43.153.27.130:26656,881b4ec9a1d37587c44476a22c0864b08b1c88fe@195.3.221.21:13056,f68feb1847416930fa046a303242adde39ba92e6@154.12.232.8:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.bcna/config/config.toml
```
