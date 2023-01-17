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
peers="9a8c4af7574a5d1fcd5e89f755348c7b6df3b4be@142.132.158.93:14256,5eac126c1b13eb220f8deb1239d9bcf713338ea3@15.235.13.145:26656,48e54221a2656616093469137ced63487f7bf456@146.56.50.55:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:26656,5ad3fe86b1214e1f5c897d23a2863fb46bdfc1f7@185.16.38.165:14256,7ba85ad424e6bc299668617f9e1281a391955e34@94.130.111.155:26657,572d417e11368f588d110efdeb7102a6a3c0752d@161.35.224.108:26656,8bc91ffabd860b6b54766ac3788d7c284e45b964@174.138.30.240:26656,ef05d5aca4398f4b217b9bbf08729a1338c67eeb@142.132.193.186:36656,c57dcf8e3af80236059194c86a6f81c1735903d6@162.19.89.8:10256"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gravity/config/config.toml
```
