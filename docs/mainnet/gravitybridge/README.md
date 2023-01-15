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
* grpc: https://gravitybridge.grpc.kjnodes.com:443

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
peers="03fabb7a15f8209c8eb8f5770c25bbee78a1d82c@94.130.8.219:26656,4bebde6a1b2907bd3cc167d2802b909770cbfda1@137.184.197.230:26656,2b2548493c4653d9c4388e9cd24b670a3cfbd564@185.16.39.3:18656,0a8487549154b7dd96fd0af1843ecfa62246f816@18.144.134.123:26656,e940c7788dfbf02030d0838fb3dc9cdb21cf5832@66.94.112.81:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:26656,32ec6bad2b67212d2cde5e01554cd2d22940ce03@142.132.154.176:26656,774406f9e2c9c65e084effc8d823c470b82de6d0@146.19.24.186:26656,b2608e51a520866a91637ca3b354903bc5b46bfa@137.184.214.71:26656,811817c6ddc112ed37f7cd71c6bbae186f1e8239@135.125.188.17:34095"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gravity/config/config.toml
```
