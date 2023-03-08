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
peers="4ae125f9c9b8e2f1ac83749c2209e26056b97851@65.108.238.103:11856,2544287899424decd29c659445578a579a500ab2@85.10.200.231:31095,3d150f6a71caca5607daff69c9049c04c37da64e@51.210.223.186:30095,cd11312654b4368dd2097afd468356d03a92cfe6@178.63.184.132:26656,b802fbfb83d6400639f17f2883f30a46ee6b05ad@51.210.223.185:32095,d6f2eee997d108d4fde5683e31d678427376dfce@77.68.27.75:26656,fa57c7c253be46ad9f696ee2f2c1d72cbc6a1591@146.59.52.135:31095,129771a48f43b83c6144c7d282ad1da62434cc07@15.204.197.12:26656,01cf570d3b08fdb5fe2f307cb485de7a35a3af23@135.148.55.229:11856,9dc8a19299064e8d5a414a1fc25dd0d12d9871c8@138.201.16.240:30095,3a7733d4b670a672db326bd6e5f8ae37e14a3dbd@138.201.226.227:26656,ffac364ae5a9a730b49f02ba95b11878f76b7043@135.125.189.131:31095,bd2821b2dc8b928946026caf3e9bd1e7a0013a61@145.239.10.46:13656,66c551ebcb68fe343c7e2720593dc47426813a68@93.189.30.101:26656,ccffabe81f2de8a81e171f93fe1209392bf9993f@65.108.234.59:26656,ecafd5cadaf3526a588550a7bc343ce2670c988d@185.16.39.231:26656,4db916788d45d5454cfe7a68ca02c56996ee6b96@194.163.151.124:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
