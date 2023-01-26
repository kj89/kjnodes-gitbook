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

**live-peers** (9)
```bash
peers="8e4e1f1e087c76c71c64e477e95495833da82aa2@135.181.173.137:26656,07c829cf936db34be61143fabb09541d05aea899@65.108.98.124:64206,90ee680b1738344354c48c23ba1e1fd68e071d80@142.132.248.138:26696,0a658df9d9fab096983a12e6f878e87281a15ce6@194.163.172.37:27656,881b4ec9a1d37587c44476a22c0864b08b1c88fe@195.3.221.21:13056,a1ceb81a5498642753f8600a5c3b9ca056af3051@67.222.144.195:16656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:42656,c38a5912b4b0f827732862594671c65ad0059932@172.105.196.25:26656,17de6cb601246b429027545e420df0a60fe3591e@65.21.200.224:13056"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.bcna/config/config.toml
```
