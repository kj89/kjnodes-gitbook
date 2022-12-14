# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/gravitybridge.png" width="150" alt=""><figcaption></figcaption></figure>

An open, decentralized bridge that unlocks the power of  interoperability & liquidity between blockchain ecosystems.

**Chain ID**: gravity-bridge-3 | **Latest Binary Version**: v1.7.2 | **Wasm**: OFF

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

**live-peers** (10)
```
peers="35aa2649d5986e9ae3aac47b5b629004c8be1748@95.217.225.212:26656,ef05d5aca4398f4b217b9bbf08729a1338c67eeb@142.132.193.186:36656,ca4270ebed73b4d0982450aac16fe08860410fac@142.132.248.138:26626,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:26656,f750840e55b48690e6078fca417dace5433a2e8b@65.108.135.212:23656,782d0262283415af141497ac5f23c7262cac7b8f@46.4.79.183:26646,da401c011881747aa47b7348349edfc855794ba2@74.208.108.68:26656,774406f9e2c9c65e084effc8d823c470b82de6d0@146.19.24.186:26656,4cd92ed2cfb0637e326a9f270e476586ef86b0c3@65.108.46.123:26656,9c3beda36b4e6d0a14fcb4e1a7823bb5495bcb10@159.69.58.176:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gravity/config/config.toml
```
