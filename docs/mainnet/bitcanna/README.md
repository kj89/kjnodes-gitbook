# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/bitcanna.png" width="150" alt=""><figcaption></figcaption></figure>

BitCanna is a proof-of-stake (POS) decentralized payment network designed exclusively to serve the cannabis industry. 

**Chain ID**: bitcanna-1 | **Latest Version Tag**: v1.5.3 | **Wasm**: OFF

[Website](https://www.bitcanna.io) | [Discord](https://discord.gg/9AVrzaVQvs) | [Twitter](https://twitter.com/BitCannaGlobal)


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
peers="8a210f1bcfc9015a7bc18dcc5add29c0dce3f2dc@135.181.173.65:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.54:26656,5bb0a042e8a4ee28bcda1e26148e57787e75a42e@23.88.69.22:28466,bba10290da32f3cb41e15c3a192413666ce05cee@136.243.119.241:26656,afb45e7806c2578f3bd8e13f845a8f9859af161d@138.201.8.248:50656,c6658742ae4c889ecf8dee95ca2a8e4b45d46dfd@85.214.208.127:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:42656,d7322625044ad733bce4178dc397b2b9b5f68b41@43.153.27.130:26656,be87c9abf1c54e1cc2f37e68d21fcd61679abb4c@65.21.196.90:46656,a1ceb81a5498642753f8600a5c3b9ca056af3051@67.222.144.195:16656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.bcna/config/config.toml
```
