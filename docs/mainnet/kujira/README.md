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
peers="94469c0d109e00e65d62a307f7ab3dc109c01055@65.108.238.104:11856,213dbb8301ce1c0f5662a9b723bd613f15e1dd4e@75.119.157.167:30656,3d150f6a71caca5607daff69c9049c04c37da64e@51.210.223.186:30095,610b8e096b4d8f923b1f41f7bdf92d5b63e033dc@162.55.243.82:4060,4018be5af4189573366762fa168826b4408418db@135.125.188.17:32095,da2673cf09dc2c124947827f4cf5e7c17114d504@142.132.202.98:26656,ccffabe81f2de8a81e171f93fe1209392bf9993f@65.108.234.59:26656,450e62f04093c283cc7dcf1257a9b2e4893ad545@148.251.85.115:26656,d7c5f6099886bc3b770cdc4cdc16e69d17dc9442@185.249.227.231:28656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@144.76.163.233:13656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.kujira/config/config.toml
```
