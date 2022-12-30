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
peers="ca9d9d0605f178fbba3bdf92e13719ab9dce0fc7@23.88.59.82:26656,661e4a8fbd8bba46237a1c41c35668a26cfa8783@79.143.177.97:26656,a23523a46e1c6beefde15210f419407c59c5f6f2@31.7.207.16:26656,0a8487549154b7dd96fd0af1843ecfa62246f816@18.144.134.123:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:26656,ca4270ebed73b4d0982450aac16fe08860410fac@142.132.248.138:26626,114180a593e480b0443ca61bb1325289a7029bc6@78.47.198.121:26656,f09419b93a9070a74ba7e9eb3803e49673a2fcd0@85.190.254.58:26656,da401c011881747aa47b7348349edfc855794ba2@74.208.108.68:26656,002aa595555a41de38f3816f10e5cced923757b3@34.223.93.26:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gravity/config/config.toml
```
