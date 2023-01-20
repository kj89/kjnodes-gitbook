# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/gravitybridge.png" width="150" alt=""><figcaption></figcaption></figure>

An open, decentralized bridge that unlocks the power of  interoperability & liquidity between blockchain ecosystems.

**Chain ID**: gravity-bridge-3 | **Latest Version Tag**: v1.8.1 | **Wasm**: OFF

[Website](https://www.gravitybridge.net) | [Discord](https://discord.gg/ARV8dTSjAk) | [Twitter](https://twitter.com/gravity_bridge)

## Restake

[Restake with kjnodes](https://restake.app/gravitybridge/gravityvaloper1nw3uavthnjwsgrrjzav2wdg9m0pw7k4fc7hvlz) (every day at 08:00, 20:00)
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
peers="d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:26656,c9bfc18ab832296903fb7f3370add5f4c28e1434@34.88.123.18:26656,0b0f045fb385118c3a8f32138748922ac6358103@66.172.36.133:12656,5be48b960e6fc61c0879e86854b9f05d3ddc3522@46.4.91.49:27656,58dcaae5a8186fcbce6b6a4e9bdcd9f2b4c9cc80@38.242.252.64:26656,7ba85ad424e6bc299668617f9e1281a391955e34@94.130.111.155:26657,572d417e11368f588d110efdeb7102a6a3c0752d@161.35.224.108:26656,e940c7788dfbf02030d0838fb3dc9cdb21cf5832@66.94.112.81:26656,4bebde6a1b2907bd3cc167d2802b909770cbfda1@137.184.197.230:26656,bcd4d083788130ccbd6d3fafd2d1083c8547506f@138.197.153.126:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gravity/config/config.toml
```
