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
peers="d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:26656,d1f6c66610b6b03e86b13675c842cc1a5fbb593b@95.216.67.178:26656,ca9d9d0605f178fbba3bdf92e13719ab9dce0fc7@23.88.59.82:26656,1f43c723cb26092e20263905cbd71609d87a9c00@172.104.202.149:26656,dc840076d50cf601da3ca708bc3665c7d480ff98@65.108.13.74:26656,2699fcd4a4128ddf1fe573011977a343b06bbef6@107.135.15.67:26646,6eb2a2e7bcd82aad56b6652a328c72f148f84935@194.147.58.224:26656,4bebde6a1b2907bd3cc167d2802b909770cbfda1@137.184.197.230:26656,0a8487549154b7dd96fd0af1843ecfa62246f816@18.144.134.123:26656,5ad3fe86b1214e1f5c897d23a2863fb46bdfc1f7@185.16.38.165:14256"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gravity/config/config.toml
```
