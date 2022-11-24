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
peers="930f874c17eff988acd8eb761fea8d4873ea6eb3@185.249.227.231:29656,ef05d5aca4398f4b217b9bbf08729a1338c67eeb@142.132.193.186:36656,5568cb9d7585c9b9d8b1685510c3ce6d2a465e8c@15.235.44.50:26656,da401c011881747aa47b7348349edfc855794ba2@74.208.108.68:26656,e5a11a1a8a36f0910755d0fc3546e8e3198283da@18.156.199.4:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@144.76.163.233:26656,b2608e51a520866a91637ca3b354903bc5b46bfa@137.184.214.71:26656,32ec6bad2b67212d2cde5e01554cd2d22940ce03@142.132.154.176:26656,c9bfc18ab832296903fb7f3370add5f4c28e1434@34.88.123.18:26656,f09419b93a9070a74ba7e9eb3803e49673a2fcd0@85.190.254.58:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gravity/config/config.toml
```
