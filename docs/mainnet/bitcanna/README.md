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
peers="c6658742ae4c889ecf8dee95ca2a8e4b45d46dfd@85.214.208.127:26656,cb9741ce22ab5f615913ac11b211c3c7f58dee71@107.191.36.154:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:42656,82588f011491c6100d922d133f52fc23460b9231@135.181.67.233:26656,2235f1e518c5ea4a412f9dece386348eda356916@66.42.50.244:26656,881b4ec9a1d37587c44476a22c0864b08b1c88fe@195.3.221.21:13056,c38a5912b4b0f827732862594671c65ad0059932@172.105.196.25:26656,3635058fcdbe97e72d191faedfe4c6acab835877@107.181.235.66:16656,07c829cf936db34be61143fabb09541d05aea899@65.108.98.124:64206,afb45e7806c2578f3bd8e13f845a8f9859af161d@138.201.8.248:50656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.bcna/config/config.toml
```
