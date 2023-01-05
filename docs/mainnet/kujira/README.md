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
peers="b12591db8b67f7a78b2834b5c122299fdb6c8deb@65.108.201.154:2060,ffac364ae5a9a730b49f02ba95b11878f76b7043@135.125.189.131:31095,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656,66778cba932969c95117cf720c1ad820fdc68ff5@65.108.235.34:26656,bed81e8d4243382da745f3e33c1a0d749bfe7ade@185.217.127.128:26656,b8e8c1738a49cd6143cf83287a5087c2618ebca0@141.95.47.82:30256,fa57c7c253be46ad9f696ee2f2c1d72cbc6a1591@146.59.52.135:31095,177872437b2a31ebb0fb740ba5bd32b0be99e280@5.79.74.229:31095,2edc8606a894033340ac8e647ff731e437ece150@139.59.8.48:26020,d87e960e5512e89af70721484617fe72e43dcb29@165.22.199.234:26020"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.kujira/config/config.toml
```
