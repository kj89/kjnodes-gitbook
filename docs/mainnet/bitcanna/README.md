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
peers="703714c82c94fc1c74b6ee0d1fc3417b932be5f3@164.152.161.98:26656,90ee680b1738344354c48c23ba1e1fd68e071d80@142.132.248.138:26696,b204222a9b6ca4eee39a836b7406483a5ad4e719@144.91.114.250:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:42656,a9f839c6e24221fb093f13ee41a0af842378fec5@94.130.12.22:26642,57a3e858a5c860e6355683c88add28d52df6c24a@38.242.232.202:26656,a1ceb81a5498642753f8600a5c3b9ca056af3051@67.222.144.195:16656,d3796f3f2a179afab1485a672ace3d909cd0eeed@185.137.122.214:26656,89757803f40da51678451735445ad40d5b15e059@169.155.168.66:26656,88c6b1fa1c7fef98b4449b769eb2705476586664@65.109.92.241:21326"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.bcna/config/config.toml
```
