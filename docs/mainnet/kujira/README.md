# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/kujira.png" width="150" alt=""><figcaption></figcaption></figure>

Kujira is a Layer 1 protocol built on Cosmos, which can be used for  hosting community-selected projects.

**Chain ID**: kaiyo-1 | **Latest Version Tag**: v0.7.1 | **Wasm**: ON

[Website](https://kujira.app) | [Discord](https://discord.gg/teamkujira) | [Twitter](https://twitter.com/TeamKujira)

[![Stake with kjnodes](https://i.ibb.co/cr44Q8j/button-stake-with-kjnodes.png)](https://restake.app/kujira/kujiravaloper1tnuqj73jfn3724lqz34c27tuv80nv336sadqym)

## Restake

[Restake with kjnodes](https://restake.app/kujira/kujiravaloper1tnuqj73jfn3724lqz34c27tuv80nv336sadqym) (every 5 minutes)
## Chain explorer
[https://explorer.kjnodes.com/kujira](https://explorer.kjnodes.com/kujira)

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

**live-peers** (19)
```bash
peers="3d150f6a71caca5607daff69c9049c04c37da64e@51.210.223.186:30095,b802fbfb83d6400639f17f2883f30a46ee6b05ad@51.210.223.185:32095,3a7733d4b670a672db326bd6e5f8ae37e14a3dbd@138.201.226.227:26656,fa57c7c253be46ad9f696ee2f2c1d72cbc6a1591@146.59.52.135:31095,66c551ebcb68fe343c7e2720593dc47426813a68@93.189.30.101:26656,15679999b404a9ee027dc9f5e795d6c4fddb6cee@51.91.152.102:20000,9dc8a19299064e8d5a414a1fc25dd0d12d9871c8@138.201.16.240:30095,9c8826ceeb1254d16856092a50df4fd720910362@50.116.49.237:26656,780ee91b43bcdced2daebee61996742f6b01b579@138.201.197.119:2000,d6f2eee997d108d4fde5683e31d678427376dfce@77.68.27.75:26656,a7d96dc929824613315dcc1c90fee119f28cc51f@134.65.193.158:26656,4018be5af4189573366762fa168826b4408418db@135.125.188.17:32095,a0927acbf1e931fc16e11e454b328c991e56d3fe@51.89.155.17:44656,b12591db8b67f7a78b2834b5c122299fdb6c8deb@65.108.201.154:2060,d3427d444b6909529d73025fe32a73dfea7b90d1@148.251.85.115:26656,0c2e37714b7922b160bce8579eeb444e59802efa@65.108.198.118:11856,a8f9cedd64e5fb2dc019061985afe8c34fd5efcb@141.94.251.25:26656,253d2293272a29057a27797a5703f5171c267da1@192.99.15.159:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
