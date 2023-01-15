# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/kujira.png" width="150" alt=""><figcaption></figcaption></figure>

Kujira is a Layer 1 protocol built on Cosmos, which can be used for  hosting community-selected projects.

**Chain ID**: kaiyo-1 | **Latest Version Tag**: v0.7.1 | **Wasm**: ON

[Website](https://kujira.app) | [Discord](https://discord.gg/teamkujira) | [Twitter](https://twitter.com/TeamKujira)

## Restake

[Restake with kjnodes](https://restake.app/kujira/kujiravaloper1tnuqj73jfn3724lqz34c27tuv80nv336sadqym) (every day at 08:00, 20:00)
## Public endpoints

* api: [https://kujira.api.kjnodes.com](https://kujira.api.kjnodes.com)
* rpc: [https://kujira.rpc.kjnodes.com](https://kujira.rpc.kjnodes.com)
* grpc: [https://kujira.grpc.kjnodes.com](https://kujira.grpc.kjnodes.com)

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
peers="15679999b404a9ee027dc9f5e795d6c4fddb6cee@51.91.152.102:20000,b802fbfb83d6400639f17f2883f30a46ee6b05ad@51.210.223.185:32095,213dbb8301ce1c0f5662a9b723bd613f15e1dd4e@75.119.157.167:30656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656,d87e960e5512e89af70721484617fe72e43dcb29@165.22.199.234:26020,129771a48f43b83c6144c7d282ad1da62434cc07@15.204.197.12:26656,c4737bc4c7705c4bd94ab23d0089bdb1136573ce@159.89.101.239:26020,d6f2eee997d108d4fde5683e31d678427376dfce@77.68.27.75:26656,4ae125f9c9b8e2f1ac83749c2209e26056b97851@65.108.238.103:11856,3d150f6a71caca5607daff69c9049c04c37da64e@51.210.223.186:30095"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
