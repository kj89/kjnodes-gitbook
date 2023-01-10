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
peers="d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:42656,1b01a388eaba8f15634c1e5cd5bb7c55810250d2@135.181.219.115:27656,c38376851f76a488bcc464ce9e248d6cf2956ba8@176.9.188.21:50656,d8a0facda705edbbdd2d79fb302e017df009e9da@207.244.231.189:26656,846fca7d90fdc1ddbcf1892a0b6338a44e93b76d@65.108.0.93:36656,c38a5912b4b0f827732862594671c65ad0059932@172.105.196.25:26656,d3796f3f2a179afab1485a672ace3d909cd0eeed@185.137.122.214:26656,8e4e1f1e087c76c71c64e477e95495833da82aa2@135.181.173.137:26656,312237a27c62e21e3ec5e2a075cba0035db3fb66@95.217.42.107:26656,0a658df9d9fab096983a12e6f878e87281a15ce6@194.163.172.37:27656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.bcna/config/config.toml
```
