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
peers="32ec6bad2b67212d2cde5e01554cd2d22940ce03@142.132.154.176:26656,cdb12d97706e295640e067c9424e8f24e01c131b@45.32.216.243:26656,e940c7788dfbf02030d0838fb3dc9cdb21cf5832@66.94.112.81:26656,0a8487549154b7dd96fd0af1843ecfa62246f816@18.144.134.123:26656,5ad3fe86b1214e1f5c897d23a2863fb46bdfc1f7@185.16.38.165:14256,5eac126c1b13eb220f8deb1239d9bcf713338ea3@15.235.13.145:26656,3eae7c785e7038b3c1376dc2fc8e6cff9d0ad709@65.108.121.110:14656,ca9d9d0605f178fbba3bdf92e13719ab9dce0fc7@23.88.59.82:26656,cc01880390b84a5ad31c9fa471748eb5a7565ee4@35.243.229.224:26656,ef05d5aca4398f4b217b9bbf08729a1338c67eeb@142.132.193.186:36656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gravity/config/config.toml
```
