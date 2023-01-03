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
peers="312237a27c62e21e3ec5e2a075cba0035db3fb66@95.217.42.107:26656,935a9d809781aa4094dd806c2afed29a25ec8b8e@135.181.210.189:26656,d2247f7b919f0781c90ee61958d7044665a22d38@169.155.169.55:26656,afb45e7806c2578f3bd8e13f845a8f9859af161d@138.201.8.248:50656,104d7ec9d84c8da66b97d50669b8ba58f1b60470@62.171.180.31:26656,c6658742ae4c889ecf8dee95ca2a8e4b45d46dfd@85.214.208.127:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:42656,d7322625044ad733bce4178dc397b2b9b5f68b41@43.153.27.130:26656,d5ed854872ad96f114737889ac9521ea3a29e3a3@185.220.205.209:26656,c38a5912b4b0f827732862594671c65ad0059932@172.105.196.25:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.bcna/config/config.toml
```
