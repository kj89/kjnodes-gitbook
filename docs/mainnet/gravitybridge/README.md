# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/gravitybridge.png" width="150" alt=""><figcaption></figcaption></figure>

An open, decentralized bridge that unlocks the power of  interoperability & liquidity between blockchain ecosystems.

**Chain ID**: gravity-bridge-3 | **Latest Version Tag**: v1.8.1 | **Wasm**: OFF

[Website](https://www.gravitybridge.net) | [Discord](https://discord.gg/ARV8dTSjAk) | [Twitter](https://twitter.com/gravity_bridge)

[![Stake with kjnodes](https://i.ibb.co/cr44Q8j/button-stake-with-kjnodes.png)](https://restake.app/gravitybridge/gravityvaloper1nw3uavthnjwsgrrjzav2wdg9m0pw7k4fc7hvlz)

## Restake

[Restake with kjnodes](https://restake.app/gravitybridge/gravityvaloper1nw3uavthnjwsgrrjzav2wdg9m0pw7k4fc7hvlz) (every 5 minutes)
## Chain explorer
[https://explorer.kjnodes.com/gravitybridge](https://explorer.kjnodes.com/gravitybridge)

## Public endpoints

* api: [https://gravitybridge.api.kjnodes.com](https://gravitybridge.api.kjnodes.com)
* rpc: [https://gravitybridge.rpc.kjnodes.com](https://gravitybridge.rpc.kjnodes.com)
* grpc: [https://gravitybridge.grpc.kjnodes.com](https://gravitybridge.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@gravitybridge.rpc.kjnodes.com:26656
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@gravitybridge.rpc.kjnodes.com:26659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/gravitybridge/addrbook.json > $HOME/.gravity/config/addrbook.json
```

**live-peers** (13)
```bash
peers="e38de921f46e22de0be8e4eba0b0338cbd065fc9@51.81.159.162:26656,b2608e51a520866a91637ca3b354903bc5b46bfa@137.184.214.71:26656,373803026c47e18b718283921662b85cf0fbc695@47.52.111.198:25656,ca9d9d0605f178fbba3bdf92e13719ab9dce0fc7@23.88.59.82:26656,1cab2a9034532b5a83a6469537da9c296c2ea09d@65.108.73.25:46656,56a8349703e8f5c97c452c7e45f5bcaac966ccbf@207.180.204.110:26656,bcd4d083788130ccbd6d3fafd2d1083c8547506f@138.197.153.126:26656,c57dcf8e3af80236059194c86a6f81c1735903d6@162.19.89.8:10256,e5362a93c6e7f686d72c8d6d98be2c7bceeb5cc3@49.12.23.149:27010,df80212f5356a2d2f047f546162baa9a3dfe6865@13.232.72.69:26656,7a05c69e10c76348e4fadeda5e0803ff4804e183@188.34.180.92:26656,4d94ca2877c879e016620681fde7c22bc23bbc6d@185.119.118.113:3000,67f95dbac6fe6bed8dfb24a5f92d9beb6b7b4ac6@97.113.90.102:27656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gravity/config/config.toml
```
