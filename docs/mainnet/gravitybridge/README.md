# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/gravitybridge.png" width="150" alt=""><figcaption></figcaption></figure>

An open, decentralized bridge that unlocks the power of  interoperability & liquidity between blockchain ecosystems.

**Chain ID**: gravity-bridge-3 | **Latest Version Tag**: v1.8.1 | **Wasm**: OFF

[Website](https://www.gravitybridge.net) | [Discord](https://discord.gg/ARV8dTSjAk) | [Twitter](https://twitter.com/gravity_bridge)

## Restake

[Restake with kjnodes](https://restake.app/gravitybridge/gravityvaloper1nw3uavthnjwsgrrjzav2wdg9m0pw7k4fc7hvlz) (every day at 08:00, 20:00)
## Chain explorer
[https://explorer.kjnodes.com/gravitybridge](https://explorer.kjnodes.com/gravitybridge)

## Public endpoints

* api: [https://gravitybridge.api.kjnodes.com](https://gravitybridge.api.kjnodes.com)
* rpc: [https://gravitybridge.rpc.kjnodes.com](https://gravitybridge.rpc.kjnodes.com)
* grpc: [https://gravitybridge.grpc.kjnodes.com](https://gravitybridge.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@gravitybridge.rpc.kjnodes.com:26656
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@gravitybridge.rpc.kjnodes.com:26659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/gravitybridge/addrbook.json > $HOME/.gravity/config/addrbook.json
```

**live-peers** (10)
```bash
peers="84fb0a9180b2b67b4901330a13f1dee4226ce3ac@65.108.9.169:26656,c9bfc18ab832296903fb7f3370add5f4c28e1434@34.88.123.18:26656,c93bd39c0b41fb1e76fb52598e88b0b069ef05bc@95.217.170.202:27014,b2608e51a520866a91637ca3b354903bc5b46bfa@137.184.214.71:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:26656,c57dcf8e3af80236059194c86a6f81c1735903d6@162.19.89.8:10256,4bebde6a1b2907bd3cc167d2802b909770cbfda1@137.184.197.230:26656,7ba85ad424e6bc299668617f9e1281a391955e34@94.130.111.155:26657,5ad3fe86b1214e1f5c897d23a2863fb46bdfc1f7@185.16.38.165:14256,3eae7c785e7038b3c1376dc2fc8e6cff9d0ad709@65.108.121.110:14656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gravity/config/config.toml
```
