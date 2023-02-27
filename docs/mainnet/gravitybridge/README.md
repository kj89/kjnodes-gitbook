# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/gravitybridge.png" width="150" alt=""><figcaption></figcaption></figure>

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

**live-peers** (9)
```bash
peers="46374f308b7cbf6a8d8242bad8666760b433cb9d@62.171.164.145:26656,9f13103f7eb8e82c6ba18eb53ba18ed88dac6950@65.109.69.59:14256,9c3beda36b4e6d0a14fcb4e1a7823bb5495bcb10@159.69.58.176:26656,4d94ca2877c879e016620681fde7c22bc23bbc6d@185.119.118.113:3000,5ad3fe86b1214e1f5c897d23a2863fb46bdfc1f7@185.16.38.165:14256,bfd8af9f3af0d9d48d5eb53eacb6862e6eca932b@195.201.202.39:26656,c57dcf8e3af80236059194c86a6f81c1735903d6@162.19.89.8:10256,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:26656,91e4523f2fcf6c7a8314b583d2f9f92cf93f10d7@51.250.18.132:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gravity/config/config.toml
```
