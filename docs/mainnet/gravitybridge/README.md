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
peers="b2608e51a520866a91637ca3b354903bc5b46bfa@137.184.214.71:26656,811817c6ddc112ed37f7cd71c6bbae186f1e8239@135.125.188.17:34095,0a8487549154b7dd96fd0af1843ecfa62246f816@18.144.134.123:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:26656,32ec6bad2b67212d2cde5e01554cd2d22940ce03@142.132.154.176:26656,9a8c4af7574a5d1fcd5e89f755348c7b6df3b4be@142.132.158.93:14256,58dcaae5a8186fcbce6b6a4e9bdcd9f2b4c9cc80@38.242.252.64:26656,9f13103f7eb8e82c6ba18eb53ba18ed88dac6950@65.109.69.59:14256,572d417e11368f588d110efdeb7102a6a3c0752d@161.35.224.108:26656,e940c7788dfbf02030d0838fb3dc9cdb21cf5832@66.94.112.81:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gravity/config/config.toml
```
