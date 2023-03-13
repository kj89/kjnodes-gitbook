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

**live-peers** (12)
```bash
peers="c4385ec685f08dfd635df6d21be9dfbdfdb52896@161.97.182.71:26656,5be48b960e6fc61c0879e86854b9f05d3ddc3522@46.4.91.49:27656,3eae7c785e7038b3c1376dc2fc8e6cff9d0ad709@65.108.121.110:14656,d1f6c66610b6b03e86b13675c842cc1a5fbb593b@95.216.67.178:26656,a9e9c67632880147aad2517c9ee19cac6d9d052e@193.17.92.212:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:26656,91e4523f2fcf6c7a8314b583d2f9f92cf93f10d7@51.250.18.132:26656,4d94ca2877c879e016620681fde7c22bc23bbc6d@185.119.118.113:3000,774406f9e2c9c65e084effc8d823c470b82de6d0@146.19.24.186:26656,1f43c723cb26092e20263905cbd71609d87a9c00@172.104.202.149:26656,2acf8add94531707982f17b91192866ad02de504@154.12.227.186:26656,cdb12d97706e295640e067c9424e8f24e01c131b@45.32.216.243:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gravity/config/config.toml
```
