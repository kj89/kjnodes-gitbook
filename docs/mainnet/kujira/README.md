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
peers="9ef0bd43e617127e3978c585437619008ccca263@65.108.229.102:22656,177872437b2a31ebb0fb740ba5bd32b0be99e280@5.79.74.229:31095,d3427d444b6909529d73025fe32a73dfea7b90d1@148.251.85.115:26656,780ee91b43bcdced2daebee61996742f6b01b579@138.201.197.119:2000,d6f2eee997d108d4fde5683e31d678427376dfce@77.68.27.75:26656,da2673cf09dc2c124947827f4cf5e7c17114d504@142.132.202.98:26656,89757803f40da51678451735445ad40d5b15e059@169.155.45.187:26656,213dbb8301ce1c0f5662a9b723bd613f15e1dd4e@75.119.157.167:30656,eb9742d81b436b95e324816794229a9efdaf8ea8@142.132.155.170:26656,3a7733d4b670a672db326bd6e5f8ae37e14a3dbd@138.201.226.227:26656,b80cf7882c8cab4894d41ccd4f5a00406d8b5f7d@146.59.52.48:30095,66c551ebcb68fe343c7e2720593dc47426813a68@93.189.30.101:26656,c55d35ef908b74c2ddec2f47dbdb4032d7dfbcd4@23.88.69.22:27266,0c2e37714b7922b160bce8579eeb444e59802efa@65.108.198.118:11856,9dc8a19299064e8d5a414a1fc25dd0d12d9871c8@138.201.16.240:30095,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.169.213:26656,3d150f6a71caca5607daff69c9049c04c37da64e@51.210.223.186:30095,8df276d9873c0ab16a911c5f779caa6f121c845e@89.163.145.138:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
