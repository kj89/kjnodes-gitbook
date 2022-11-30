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
peers="ef05d5aca4398f4b217b9bbf08729a1338c67eeb@142.132.193.186:36656,961dc8a5e131e058c87c25f1d5c3b9395076e46a@65.108.106.131:26656,afde09a999e9c28dbd97fea259d15bd229b9f92f@88.198.10.250:26656,77367b424f624c4f9f423267dd8d4d559b289b62@167.235.9.250:26656,7a05c69e10c76348e4fadeda5e0803ff4804e183@188.34.180.92:26656,1f43c723cb26092e20263905cbd71609d87a9c00@172.104.202.149:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:26656,0a8487549154b7dd96fd0af1843ecfa62246f816@18.144.134.123:26656,d20fb90c25dcd447fc574d20c3511a05b19aa9a5@35.215.12.41:26656,da83aa34f4e8ca895c445637073c15592ba04b8a@161.97.101.202:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gravity/config/config.toml
```
