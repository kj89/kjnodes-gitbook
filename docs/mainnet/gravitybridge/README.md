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

**live-peers** (10)
```
peers="9f13103f7eb8e82c6ba18eb53ba18ed88dac6950@65.109.69.59:14256,5ad3fe86b1214e1f5c897d23a2863fb46bdfc1f7@185.16.38.165:14256,7cd0057e01f8aa985b650e94cf724375f6dff5f5@95.214.53.225:26676,5568cb9d7585c9b9d8b1685510c3ce6d2a465e8c@15.235.44.50:26656,572d417e11368f588d110efdeb7102a6a3c0752d@161.35.224.108:26656,7ba85ad424e6bc299668617f9e1281a391955e34@94.130.111.155:26657,782d0262283415af141497ac5f23c7262cac7b8f@46.4.79.183:26646,ef05d5aca4398f4b217b9bbf08729a1338c67eeb@142.132.193.186:36656,9c3beda36b4e6d0a14fcb4e1a7823bb5495bcb10@159.69.58.176:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@144.76.163.233:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gravity/config/config.toml
```
