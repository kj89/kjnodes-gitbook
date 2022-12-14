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
peers="ccffabe81f2de8a81e171f93fe1209392bf9993f@65.108.234.59:26656,01d708d4124f30700c05c97947ae10231d8755f7@95.217.197.100:26655,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656,3a7733d4b670a672db326bd6e5f8ae37e14a3dbd@138.201.226.227:26656,35629bef4cc1a0be69ebd053ff4e16de82970add@5.79.79.80:30095,177872437b2a31ebb0fb740ba5bd32b0be99e280@5.79.74.229:31095,ecafd5cadaf3526a588550a7bc343ce2670c988d@185.16.39.231:26656,129771a48f43b83c6144c7d282ad1da62434cc07@15.204.197.12:26656,15679999b404a9ee027dc9f5e795d6c4fddb6cee@51.91.152.102:20000,b29969a2384159db8f8052bc118066bd067157c4@85.215.105.19:15602"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.kujira/config/config.toml
```
