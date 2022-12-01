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
peers="5ad3fe86b1214e1f5c897d23a2863fb46bdfc1f7@185.16.38.165:14256,b2608e51a520866a91637ca3b354903bc5b46bfa@137.184.214.71:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:26656,3ea8c2f299c5031bc76a5ed056154c3f3b6db379@135.181.142.216:26656,d0af949fc3940dcab036ba0948aa21fc7ac020a1@65.21.237.170:10156,002aa595555a41de38f3816f10e5cced923757b3@34.223.93.26:26656,bcd4d083788130ccbd6d3fafd2d1083c8547506f@138.197.153.126:26656,6edddf41ca6bad0362c069afced6a9f0c67bd2a4@195.201.195.108:26656,4bebde6a1b2907bd3cc167d2802b909770cbfda1@137.184.197.230:26656,6eb2a2e7bcd82aad56b6652a328c72f148f84935@194.147.58.224:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gravity/config/config.toml
```
