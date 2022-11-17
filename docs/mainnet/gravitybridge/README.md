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
peers="872d4a6598e03c578004b3e7b1ac9a5c28cf910c@51.154.19.13:26656,e5a11a1a8a36f0910755d0fc3546e8e3198283da@18.156.199.4:26656,5ad3fe86b1214e1f5c897d23a2863fb46bdfc1f7@185.16.38.165:14256,b2608e51a520866a91637ca3b354903bc5b46bfa@137.184.214.71:26656,bcd4d083788130ccbd6d3fafd2d1083c8547506f@138.197.153.126:26656,0b0f045fb385118c3a8f32138748922ac6358103@66.172.36.133:12656,94a09a149acbaf7435d8d4082fd6100598e1fee0@157.90.5.119:26656,2397921d048339698933a6cb204fe502e018dad2@135.181.179.123:26656,d1f6c66610b6b03e86b13675c842cc1a5fbb593b@95.216.67.178:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@144.76.163.233:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gravity/config/config.toml
```
