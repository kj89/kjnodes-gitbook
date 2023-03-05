# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/kujira.png" width="150" alt=""><figcaption></figcaption></figure>

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

**live-peers** (17)
```bash
peers="da2673cf09dc2c124947827f4cf5e7c17114d504@142.132.202.98:26656,0c7da38c54e1a7d8ab7d48601b51847564ce019e@5.161.91.34:45656,d6f2eee997d108d4fde5683e31d678427376dfce@77.68.27.75:26656,213dbb8301ce1c0f5662a9b723bd613f15e1dd4e@75.119.157.167:30656,2544287899424decd29c659445578a579a500ab2@85.10.200.231:31095,9dc8a19299064e8d5a414a1fc25dd0d12d9871c8@138.201.16.240:30095,66c551ebcb68fe343c7e2720593dc47426813a68@93.189.30.101:26656,0c2e37714b7922b160bce8579eeb444e59802efa@65.108.198.118:11856,b12591db8b67f7a78b2834b5c122299fdb6c8deb@65.108.201.154:2060,ffac364ae5a9a730b49f02ba95b11878f76b7043@135.125.189.131:31095,3d150f6a71caca5607daff69c9049c04c37da64e@51.210.223.186:30095,4ae125f9c9b8e2f1ac83749c2209e26056b97851@65.108.238.103:11856,d2247f7b919f0781c90ee61958d7044665a22d38@169.155.169.182:26656,15679999b404a9ee027dc9f5e795d6c4fddb6cee@51.91.152.102:20000,cedf10f69de7d77b358964a1b802a15ad79a7c97@74.80.183.130:26655,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656,01d708d4124f30700c05c97947ae10231d8755f7@95.217.197.100:26655"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
