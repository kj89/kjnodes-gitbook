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

**live-peers** (14)
```bash
peers="0a8487549154b7dd96fd0af1843ecfa62246f816@18.144.134.123:26656,c9bfc18ab832296903fb7f3370add5f4c28e1434@34.88.123.18:26656,d1f6c66610b6b03e86b13675c842cc1a5fbb593b@95.216.67.178:26656,e38de921f46e22de0be8e4eba0b0338cbd065fc9@51.81.159.162:26656,c57dcf8e3af80236059194c86a6f81c1735903d6@162.19.89.8:10256,ddf8f9ff250f760228c667d256d16ed4f1880c27@65.109.43.75:27010,d20fb90c25dcd447fc574d20c3511a05b19aa9a5@35.215.12.41:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:26656,162e8994c0738fb5895e77b888718ea51d4c40d3@167.86.106.22:26656,56a8349703e8f5c97c452c7e45f5bcaac966ccbf@207.180.204.110:26656,6eb2a2e7bcd82aad56b6652a328c72f148f84935@194.147.58.224:26656,84fb0a9180b2b67b4901330a13f1dee4226ce3ac@65.108.9.169:26656,e5a11a1a8a36f0910755d0fc3546e8e3198283da@18.156.199.4:26656,4bebde6a1b2907bd3cc167d2802b909770cbfda1@137.184.197.230:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gravity/config/config.toml
```
