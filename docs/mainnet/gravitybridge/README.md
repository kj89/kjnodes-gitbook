# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/gravitybridge.png" width="150" alt=""><figcaption></figcaption></figure>

An open, decentralized bridge that unlocks the power of  interoperability & liquidity between blockchain ecosystems.

**Chain ID**: gravity-bridge-3 | **Latest Binary Version**: v1.7.2 | **Wasm**: OFF

[Website](https://www.gravitybridge.net) | [Discord](https://discord.gg/ARV8dTSjAk) | [Twitter](https://twitter.com/gravity_bridge)

## Restake

[Restake with kjnodes](https://restake.app/gravitybridge/gravityvaloper1nw3uavthnjwsgrrjzav2wdg9m0pw7k4fc7hvlz) (every day at 08:00, 20:00)
## Public endpoints

* rpc: [https://gravitybridge.rpc.kjnodes.com](https://gravitybridge.rpc.kjnodes.com)
* api: [https://gravitybridge.api.kjnodes.com](https://gravitybridge.api.kjnodes.com)

## Peering

**state-sync**

```
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@gravitybridge.rpc.kjnodes.com:26656
```

**seed-node**

```
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@gravitybridge.rpc.kjnodes.com:26659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/gravitybridge/addrbook.json > $HOME/.gravity/config/addrbook.json
```

**live-peers** (10)
```
peers="0087e4801051e620f18493e9927eb9c63171aec3@95.217.121.178:26656,d1f6c66610b6b03e86b13675c842cc1a5fbb593b@95.216.67.178:26656,e5a11a1a8a36f0910755d0fc3546e8e3198283da@18.156.199.4:26656,ef05d5aca4398f4b217b9bbf08729a1338c67eeb@142.132.193.186:36656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:26656,774406f9e2c9c65e084effc8d823c470b82de6d0@146.19.24.186:26656,94a09a149acbaf7435d8d4082fd6100598e1fee0@157.90.5.119:26656,f09419b93a9070a74ba7e9eb3803e49673a2fcd0@85.190.254.58:26656,bfd8af9f3af0d9d48d5eb53eacb6862e6eca932b@195.201.202.39:26656,3eae7c785e7038b3c1376dc2fc8e6cff9d0ad709@65.108.121.110:14656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gravity/config/config.toml
```
