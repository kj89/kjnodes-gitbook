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
peers="fac4b8923599efb4de35e7970d0cd4d7a2012e9f@65.109.28.224:12656,be87c9abf1c54e1cc2f37e68d21fcd61679abb4c@65.21.196.90:46656,0a658df9d9fab096983a12e6f878e87281a15ce6@194.163.172.37:27656,b7295f18b7150cc128d47c0546e2225179fc5427@202.61.194.254:60856,c38a5912b4b0f827732862594671c65ad0059932@172.105.196.25:26656,881b4ec9a1d37587c44476a22c0864b08b1c88fe@195.3.221.21:13056,a1ceb81a5498642753f8600a5c3b9ca056af3051@67.222.144.195:16656,4dabde84771e8689403ce7c8b76d27e555ab2f00@65.21.136.170:50656,48970472844c638389ba56bffd32b73d7b186de6@50.18.24.204:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:42656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.bcna/config/config.toml
```
