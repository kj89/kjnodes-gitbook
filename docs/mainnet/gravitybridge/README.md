# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/gravitybridge.png" width="150" alt=""><figcaption></figcaption></figure>

An open, decentralized bridge that unlocks the power of  interoperability & liquidity between blockchain ecosystems.

**Chain ID**: gravity-bridge-3 | **Latest Version Tag**: v1.8.1 | **Wasm**: OFF

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
peers="74efecf52ba78626d4ba796fb6073fa9cb26b19e@65.108.11.250:26656,ef05d5aca4398f4b217b9bbf08729a1338c67eeb@142.132.193.186:36656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:26656,03fabb7a15f8209c8eb8f5770c25bbee78a1d82c@94.130.8.219:26656,5568cb9d7585c9b9d8b1685510c3ce6d2a465e8c@15.235.44.50:26656,811817c6ddc112ed37f7cd71c6bbae186f1e8239@135.125.188.17:34095,35aa2649d5986e9ae3aac47b5b629004c8be1748@95.217.225.212:26656,4bebde6a1b2907bd3cc167d2802b909770cbfda1@137.184.197.230:26656,381c0aabfa183467858bd4e1f2071b1b0a77e94c@142.132.154.39:26656,c57dcf8e3af80236059194c86a6f81c1735903d6@162.19.89.8:10256"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gravity/config/config.toml
```
