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
peers="94a09a149acbaf7435d8d4082fd6100598e1fee0@157.90.5.119:26656,e5a11a1a8a36f0910755d0fc3546e8e3198283da@18.156.199.4:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:26656,32ec6bad2b67212d2cde5e01554cd2d22940ce03@142.132.154.176:26656,77367b424f624c4f9f423267dd8d4d559b289b62@167.235.9.250:26656,7a05c69e10c76348e4fadeda5e0803ff4804e183@188.34.180.92:26656,572d417e11368f588d110efdeb7102a6a3c0752d@161.35.224.108:26656,8bc91ffabd860b6b54766ac3788d7c284e45b964@174.138.30.240:26656,c93bd39c0b41fb1e76fb52598e88b0b069ef05bc@95.217.170.202:27014,ef05d5aca4398f4b217b9bbf08729a1338c67eeb@142.132.193.186:36656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gravity/config/config.toml
```
