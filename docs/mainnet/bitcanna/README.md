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

**live-peers** (9)
```
peers="b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.54:26656,cb9741ce22ab5f615913ac11b211c3c7f58dee71@107.191.36.154:26656,d3796f3f2a179afab1485a672ace3d909cd0eeed@185.137.122.214:26656,881b4ec9a1d37587c44476a22c0864b08b1c88fe@195.3.221.21:13056,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:42656,90ee680b1738344354c48c23ba1e1fd68e071d80@142.132.248.138:26696,c38a5912b4b0f827732862594671c65ad0059932@172.105.196.25:26656,751513c7cd42a2565c37ab482bbe66f4d92c2740@136.244.106.130:26656,7eba6089dd06147b7993979f901d212e722c21c3@24.158.14.212:36656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.bcna/config/config.toml
```
