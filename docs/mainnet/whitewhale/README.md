# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/whitewhale.png" width="150" alt=""><figcaption></figcaption></figure>

Whitewhale is a Tendermint-based Interchain Liquidity.

**Chain ID**: migaloo-1 | **Latest Version Tag**: v1.0.0 | **Wasm**: OFF

[Website](https://whitewhale.money) | [Discord](https://discord.gg/AyvcgD4jy3) | [Twitter](https://twitter.com/WhiteWhaleDefi)




## Chain explorer
[https://explorer.kjnodes.com/whitewhale](https://explorer.kjnodes.com/whitewhale)

## Public endpoints

* api: [https://whitewhale.api.kjnodes.com](https://whitewhale.api.kjnodes.com)
* rpc: [https://whitewhale.rpc.kjnodes.com](https://whitewhale.rpc.kjnodes.com)
* grpc: [https://whitewhale.grpc.kjnodes.com](https://whitewhale.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@whitewhale.rpc.kjnodes.com:49656
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@whitewhale.rpc.kjnodes.com:49659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/whitewhale/addrbook.json > $HOME/.migalood/config/addrbook.json
```

**live-peers** (0)
```bash
peers=""
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.migalood/config/config.toml
```
