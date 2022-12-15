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
peers="35aa2649d5986e9ae3aac47b5b629004c8be1748@95.217.225.212:26656,b2608e51a520866a91637ca3b354903bc5b46bfa@137.184.214.71:26656,e940c7788dfbf02030d0838fb3dc9cdb21cf5832@66.94.112.81:26656,5ad3fe86b1214e1f5c897d23a2863fb46bdfc1f7@185.16.38.165:14256,4bebde6a1b2907bd3cc167d2802b909770cbfda1@137.184.197.230:26656,ca4270ebed73b4d0982450aac16fe08860410fac@142.132.248.138:26626,77367b424f624c4f9f423267dd8d4d559b289b62@167.235.9.250:26656,74efecf52ba78626d4ba796fb6073fa9cb26b19e@65.108.11.250:26656,c93bd39c0b41fb1e76fb52598e88b0b069ef05bc@95.217.170.202:27014,ef05d5aca4398f4b217b9bbf08729a1338c67eeb@142.132.193.186:36656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gravity/config/config.toml
```
