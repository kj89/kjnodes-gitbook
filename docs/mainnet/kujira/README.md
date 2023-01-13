# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/kujira.png" width="150" alt=""><figcaption></figcaption></figure>

Kujira is a Layer 1 protocol built on Cosmos, which can be used for  hosting community-selected projects.

**Chain ID**: kaiyo-1 | **Latest Version Tag**: v0.7.1 | **Wasm**: ON

[Website](https://kujira.app) | [Discord](https://discord.gg/teamkujira) | [Twitter](https://twitter.com/TeamKujira)

## Restake

[Restake with kjnodes](https://restake.app/kujira/kujiravaloper1tnuqj73jfn3724lqz34c27tuv80nv336sadqym) (every day at 08:00, 20:00)
## Public endpoints

* rpc: [https://kujira.rpc.kjnodes.com](https://kujira.rpc.kjnodes.com)
* api: [https://kujira.api.kjnodes.com](https://kujira.api.kjnodes.com)

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@kujira.rpc.kjnodes.com:13656
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@kujira.rpc.kjnodes.com:13659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/kujira/addrbook.json > $HOME/.kujira/config/addrbook.json
```

**live-peers** (10)
```bash
peers="04b384fd77f70082a9a6e4d8fb3db827340f4e74@148.251.13.186:11856,935c1065ad23338a5e6a75f08fb650f9f46dbd3e@65.108.201.167:26656,66c551ebcb68fe343c7e2720593dc47426813a68@93.189.30.101:26656,01d708d4124f30700c05c97947ae10231d8755f7@95.217.197.100:26655,4018be5af4189573366762fa168826b4408418db@135.125.188.17:32095,b12591db8b67f7a78b2834b5c122299fdb6c8deb@65.108.201.154:2060,4ae125f9c9b8e2f1ac83749c2209e26056b97851@65.108.238.103:11856,129771a48f43b83c6144c7d282ad1da62434cc07@15.204.197.12:26656,ecafd5cadaf3526a588550a7bc343ce2670c988d@185.16.39.231:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
