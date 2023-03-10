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

**live-peers** (18)
```bash
peers="4db916788d45d5454cfe7a68ca02c56996ee6b96@194.163.151.124:26656,9dc8a19299064e8d5a414a1fc25dd0d12d9871c8@138.201.16.240:30095,66c551ebcb68fe343c7e2720593dc47426813a68@93.189.30.101:26656,ecafd5cadaf3526a588550a7bc343ce2670c988d@185.16.39.231:26656,a8f9cedd64e5fb2dc019061985afe8c34fd5efcb@141.94.251.25:26656,9c8826ceeb1254d16856092a50df4fd720910362@50.116.49.237:26656,26d19e5b3f3a5ebafe827dabca4ef008d9c5e6fd@168.119.15.94:26656,da2673cf09dc2c124947827f4cf5e7c17114d504@142.132.202.98:26656,fa57c7c253be46ad9f696ee2f2c1d72cbc6a1591@146.59.52.135:31095,780ee91b43bcdced2daebee61996742f6b01b579@138.201.197.119:2000,d6f2eee997d108d4fde5683e31d678427376dfce@77.68.27.75:26656,d3427d444b6909529d73025fe32a73dfea7b90d1@148.251.85.115:26656,4018be5af4189573366762fa168826b4408418db@135.125.188.17:32095,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.169.213:26656,b8e8c1738a49cd6143cf83287a5087c2618ebca0@141.95.47.82:30256,eb9742d81b436b95e324816794229a9efdaf8ea8@142.132.155.170:26656,3a7733d4b670a672db326bd6e5f8ae37e14a3dbd@138.201.226.227:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
