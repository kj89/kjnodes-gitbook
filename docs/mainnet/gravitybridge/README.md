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

**live-peers** (11)
```
peers="2acf8add94531707982f17b91192866ad02de504@154.12.227.186:26656,b19d431eeaf02ffb3d0a633ae936894c4c0353c7@173.249.41.78:26656,f750840e55b48690e6078fca417dace5433a2e8b@65.108.135.212:23656,4bebde6a1b2907bd3cc167d2802b909770cbfda1@137.184.197.230:26656,b2608e51a520866a91637ca3b354903bc5b46bfa@137.184.214.71:26656,bcd4d083788130ccbd6d3fafd2d1083c8547506f@138.197.153.126:26656,c93bd39c0b41fb1e76fb52598e88b0b069ef05bc@95.217.170.202:27014,df80212f5356a2d2f047f546162baa9a3dfe6865@13.232.72.69:26656,002aa595555a41de38f3816f10e5cced923757b3@34.223.93.26:26656,7e5b7671f0ec3729124102f23c50d8cdd0faa583@192.26.37.56:36656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gravity/config/config.toml
```
