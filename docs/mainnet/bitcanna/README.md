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
peers="9532a13b05e5f68f2ca01f90b3d1ba9a762af817@65.108.131.190:21956,3635058fcdbe97e72d191faedfe4c6acab835877@107.181.235.66:16656,751513c7cd42a2565c37ab482bbe66f4d92c2740@136.244.106.130:26656,6cceba286b498d4a1931f85e35ea0fa433373057@78.47.208.97:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:42656,07c829cf936db34be61143fabb09541d05aea899@65.108.98.124:64206,935a9d809781aa4094dd806c2afed29a25ec8b8e@135.181.210.189:26656,d2247f7b919f0781c90ee61958d7044665a22d38@169.155.169.55:26656,c38a5912b4b0f827732862594671c65ad0059932@172.105.196.25:26656,d3796f3f2a179afab1485a672ace3d909cd0eeed@185.137.122.214:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.bcna/config/config.toml
```
