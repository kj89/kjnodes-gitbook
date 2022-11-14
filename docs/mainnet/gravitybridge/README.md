# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/gravitybridge.png" width="150" alt=""><figcaption></figcaption></figure>

An open, decentralized bridge that unlocks the power of  interoperability & liquidity between blockchain ecosystems.

**Chain ID**: gravity-bridge-3 | **Latest Version Tag**: pleiades | **Wasm**: OFF

Website: [https://www.gravitybridge.net](https://www.gravitybridge.net)

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

**live-peers** (9)
```
peers="6770e29a9224810bcde6655b742d52b8a49d51e8@65.19.136.133:26656,82bf13b3c0af8cd0ea69c64ff43e61a5b7dbae7f@176.126.87.56:26656,bfd8af9f3af0d9d48d5eb53eacb6862e6eca932b@195.201.202.39:26656,5eac126c1b13eb220f8deb1239d9bcf713338ea3@15.235.13.145:26656,5568cb9d7585c9b9d8b1685510c3ce6d2a465e8c@15.235.44.50:26656,002aa595555a41de38f3816f10e5cced923757b3@34.223.93.26:26656,776a1bbafe0835847a129ebdff40b00eaa5fc057@45.76.35.76:26656,04ceb585f79410b709bee926ce209013bb3174ac@167.235.107.42:27013,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@144.76.163.233:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gravity/config/config.toml
```
