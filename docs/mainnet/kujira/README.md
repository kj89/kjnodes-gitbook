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
peers="98a6a264d2f2f5093d317f09e71036e62aa73906@107.181.235.66:20656,ecafd5cadaf3526a588550a7bc343ce2670c988d@185.16.39.231:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@144.76.163.233:13656,94469c0d109e00e65d62a307f7ab3dc109c01055@65.108.238.104:11856,a429a1fa5cc1e8757b6bbc3975ecc13e0ab2bf2f@95.217.228.124:11856,471518432477e31ea348af246c0b54095d41352c@88.198.131.126:26656,da2673cf09dc2c124947827f4cf5e7c17114d504@142.132.202.98:26656,08d426315d8b1b8996f5dd969777c143d27a5f06@142.132.199.211:26655,c124ce0b508e8b9ed1c5b6957f362225659b5343@136.243.248.190:26656,3a7733d4b670a672db326bd6e5f8ae37e14a3dbd@138.201.226.227:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.kujira/config/config.toml
```
