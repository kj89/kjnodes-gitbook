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

**live-peers** (9)
```
peers="77367b424f624c4f9f423267dd8d4d559b289b62@167.235.9.250:26656,930f874c17eff988acd8eb761fea8d4873ea6eb3@185.249.227.231:29656,373803026c47e18b718283921662b85cf0fbc695@47.52.111.198:25656,e5a11a1a8a36f0910755d0fc3546e8e3198283da@18.156.199.4:26656,4e1ea298ef66eec3ec320171f90336a1e4bb13ea@51.81.107.95:10256,b2608e51a520866a91637ca3b354903bc5b46bfa@137.184.214.71:26656,002aa595555a41de38f3816f10e5cced923757b3@34.223.93.26:26656,df80212f5356a2d2f047f546162baa9a3dfe6865@13.232.72.69:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gravity/config/config.toml
```
