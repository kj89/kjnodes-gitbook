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
peers="01d708d4124f30700c05c97947ae10231d8755f7@95.217.197.100:26655,04b384fd77f70082a9a6e4d8fb3db827340f4e74@148.251.13.186:11856,213dbb8301ce1c0f5662a9b723bd613f15e1dd4e@75.119.157.167:30656,4018be5af4189573366762fa168826b4408418db@135.125.188.17:32095,bed81e8d4243382da745f3e33c1a0d749bfe7ade@185.217.127.128:26656,2840e88816e487a096cca323bc779ad98187e3e4@5.9.72.212:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656,6f3129d01218b939511cccf7e0318bfe872d97c4@65.109.33.181:26656,177872437b2a31ebb0fb740ba5bd32b0be99e280@5.79.74.229:31095,1d85c9f16727584753db78b5b54eedf0ce8de3ed@51.159.16.49:5060"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.kujira/config/config.toml
```
