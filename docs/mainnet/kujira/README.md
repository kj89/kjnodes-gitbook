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
peers="698529d303400cc4dff026c6c47eb0dc6547b595@95.216.43.190:36346,ccffabe81f2de8a81e171f93fe1209392bf9993f@65.108.234.59:26656,01d708d4124f30700c05c97947ae10231d8755f7@95.217.197.100:26655,0cb9d54761ca14006daad4442378f2a1335de6ad@65.21.121.118:26656,6f3129d01218b939511cccf7e0318bfe872d97c4@65.109.33.181:26656,4018be5af4189573366762fa168826b4408418db@135.125.188.17:32095,b80cf7882c8cab4894d41ccd4f5a00406d8b5f7d@146.59.52.48:30095,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656,fc593f5f9fcf7f88790bd8274ebc791f612d3efe@65.21.89.54:26655,da2673cf09dc2c124947827f4cf5e7c17114d504@142.132.202.98:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.kujira/config/config.toml
```
