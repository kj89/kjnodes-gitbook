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
peers="66778cba932969c95117cf720c1ad820fdc68ff5@65.108.235.34:26656,0cb9d54761ca14006daad4442378f2a1335de6ad@65.21.121.118:26656,6f3129d01218b939511cccf7e0318bfe872d97c4@65.109.33.181:26656,c4737bc4c7705c4bd94ab23d0089bdb1136573ce@159.89.101.239:26020,d7c5f6099886bc3b770cdc4cdc16e69d17dc9442@185.249.227.231:28656,ed71d6328a0228cd2eac7d71451509813c660b5d@116.202.164.206:26656,413bd0410b649de5070b2fe8356cad356459dc37@65.108.235.165:26656,bd1ec9985e9f3a1fbfbd7be5fa4c926a61cbd403@34.70.228.207:26656,bed81e8d4243382da745f3e33c1a0d749bfe7ade@185.217.127.128:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.kujira/config/config.toml
```
