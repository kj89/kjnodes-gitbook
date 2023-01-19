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
peers="8a210f1bcfc9015a7bc18dcc5add29c0dce3f2dc@135.181.173.65:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.54:26656,19555f24510894a112b2398ff55cd1f1225972cc@23.88.69.167:27100,a9f839c6e24221fb093f13ee41a0af842378fec5@94.130.12.22:26642,c38a5912b4b0f827732862594671c65ad0059932@172.105.196.25:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:42656,07c829cf936db34be61143fabb09541d05aea899@65.108.98.124:64206,6cceba286b498d4a1931f85e35ea0fa433373057@78.47.208.97:26656,9532a13b05e5f68f2ca01f90b3d1ba9a762af817@65.108.131.190:21956,9301659e822226a1eaefe6e6fa99da96c99d7db6@94.130.10.43:30656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.bcna/config/config.toml
```
