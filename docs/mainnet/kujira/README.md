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
peers="b29969a2384159db8f8052bc118066bd067157c4@85.215.105.19:15602,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656,66778cba932969c95117cf720c1ad820fdc68ff5@65.108.235.34:26656,177872437b2a31ebb0fb740ba5bd32b0be99e280@5.79.74.229:31095,d2247f7b919f0781c90ee61958d7044665a22d38@169.155.169.182:26656,d6f2eee997d108d4fde5683e31d678427376dfce@77.68.27.75:26656,129771a48f43b83c6144c7d282ad1da62434cc07@15.204.197.12:26656,04b384fd77f70082a9a6e4d8fb3db827340f4e74@148.251.13.186:11856,450e62f04093c283cc7dcf1257a9b2e4893ad545@148.251.85.115:26656,35629bef4cc1a0be69ebd053ff4e16de82970add@5.79.79.80:30095"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.kujira/config/config.toml
```
