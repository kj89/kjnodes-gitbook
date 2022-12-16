# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/bitcanna.png" width="150" alt=""><figcaption></figcaption></figure>

BitCanna is a proof-of-stake (POS) decentralized payment network designed exclusively to serve the cannabis industry. 

**Chain ID**: bitcanna-1 | **Latest Version Tag**: v1.5.3 | **Wasm**: OFF

Website: [https://www.bitcanna.io](https://www.bitcanna.io)


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
peers="d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:42656,0393c19b176d1cf8bc560c5a8fa990301deb1a7e@95.217.126.185:26656,d5ed854872ad96f114737889ac9521ea3a29e3a3@185.220.205.209:26656,c73f11f731e4a78df73123747d38bc3a9d4d036b@23.88.66.239:36656,bba10290da32f3cb41e15c3a192413666ce05cee@136.243.119.241:26656,881b4ec9a1d37587c44476a22c0864b08b1c88fe@195.3.221.21:13056,d16080503125692e49e7d43275c5de1e48bfff1f@5.9.50.59:26656,88c6b1fa1c7fef98b4449b769eb2705476586664@65.109.92.241:21326,d3796f3f2a179afab1485a672ace3d909cd0eeed@185.137.122.214:26656,a1ceb81a5498642753f8600a5c3b9ca056af3051@67.222.144.195:16656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.bcna/config/config.toml
```
