# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/kujira.png" width="150" alt=""><figcaption></figcaption></figure>

Kujira is a Layer 1 protocol built on Cosmos, which can be used for  hosting community-selected projects.

**Chain ID**: kaiyo-1 | **Latest Version Tag**: v0.7.1 | **Wasm**: ON

Website: [https://kujira.app](https://kujira.app)

## Restake

[Restake with kjnodes](https://restake.app/kujira/kujiravaloper1tnuqj73jfn3724lqz34c27tuv80nv336sadqym) (every day at 08:00, 20:00)
## Public endpoints

* rpc: [https://kujira.rpc.kjnodes.com](https://kujira.rpc.kjnodes.com)
* api: [https://kujira.api.kjnodes.com](https://kujira.api.kjnodes.com)

## Peering

**state-sync**

```
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@kujira.rpc.kjnodes.com:13656
```

**seed-node**

```
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@kujira.rpc.kjnodes.com:13659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/kujira/addrbook.json > $HOME/.kujira/config/addrbook.json
```

**live-peers** (10)
```
peers="94469c0d109e00e65d62a307f7ab3dc109c01055@65.108.238.104:11856,4018be5af4189573366762fa168826b4408418db@135.125.188.17:32095,d3cbe679ef7e491d3b34f6557bde23077f28e21f@77.22.195.34:26656,7ce3988ad06172aa22856e1c3ec7940dd01c2592@95.217.144.25:15602,01cf570d3b08fdb5fe2f307cb485de7a35a3af23@135.148.55.229:11856,129771a48f43b83c6144c7d282ad1da62434cc07@15.204.197.12:26656,3a7733d4b670a672db326bd6e5f8ae37e14a3dbd@138.201.226.227:26656,de08e6178779ff3b19a8b6d22a05664392cb2b35@185.216.179.205:26656,da2673cf09dc2c124947827f4cf5e7c17114d504@142.132.202.98:26656,f35e499b047c1aa78fe04a16705b508610b7a896@135.181.57.223:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.kujira/config/config.toml
```
