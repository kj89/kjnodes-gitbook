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
peers="66778cba932969c95117cf720c1ad820fdc68ff5@65.108.235.34:26656,a7d96dc929824613315dcc1c90fee119f28cc51f@134.65.193.158:26656,c4737bc4c7705c4bd94ab23d0089bdb1136573ce@159.89.101.239:26020,b29969a2384159db8f8052bc118066bd067157c4@85.215.105.19:15602,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656,15679999b404a9ee027dc9f5e795d6c4fddb6cee@51.91.152.102:20000,0179a6055fc1e36053facef08766d06186f3cd33@65.21.200.224:11856,bed81e8d4243382da745f3e33c1a0d749bfe7ade@185.217.127.128:26656,253d2293272a29057a27797a5703f5171c267da1@192.99.15.159:26656,b802fbfb83d6400639f17f2883f30a46ee6b05ad@51.210.223.185:32095"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
