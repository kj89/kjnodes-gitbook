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
peers="002aa595555a41de38f3816f10e5cced923757b3@34.223.93.26:26656,48e54221a2656616093469137ced63487f7bf456@146.56.50.55:26656,5eac126c1b13eb220f8deb1239d9bcf713338ea3@15.235.13.145:26656,7a05c69e10c76348e4fadeda5e0803ff4804e183@188.34.180.92:26656,77367b424f624c4f9f423267dd8d4d559b289b62@167.235.9.250:26656,776a1bbafe0835847a129ebdff40b00eaa5fc057@45.76.35.76:26656,6dbb1f051998d6972597941209e80dc84c308389@46.0.203.78:26656,ef05d5aca4398f4b217b9bbf08729a1338c67eeb@142.132.193.186:36656,8357279ecb5f1b80eda324762a1406868c89bb5a@172.105.103.88:26656,6eb2a2e7bcd82aad56b6652a328c72f148f84935@194.147.58.224:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gravity/config/config.toml
```
