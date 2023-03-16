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
* grpc: kujira.grpc.kjnodes.com:13090

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
peers="b12591db8b67f7a78b2834b5c122299fdb6c8deb@65.108.201.154:2060,6cf8b25d99bacca213c1d762e8d9ea21636fea41@178.211.139.222:26656,01d708d4124f30700c05c97947ae10231d8755f7@95.217.197.100:26655,89757803f40da51678451735445ad40d5b15e059@169.155.45.187:26656,66c551ebcb68fe343c7e2720593dc47426813a68@93.189.30.101:26656,e751b31b5444ed4a7489a456be805c736756eeb8@195.3.223.19:26656,9c753f4e99433b79b0b7dce69fffa0a892491f95@65.108.234.154:26656,780ee91b43bcdced2daebee61996742f6b01b579@138.201.197.119:2000,213dbb8301ce1c0f5662a9b723bd613f15e1dd4e@75.119.157.167:30656,471518432477e31ea348af246c0b54095d41352c@88.198.131.126:26656,a9ed3a9256cbabe889b2989ad99a3e7e173c3ffe@108.165.178.242:26655,8d59c2958dfb2f852b201cbaa60743c771ce338b@147.135.45.32:26656,9dc8a19299064e8d5a414a1fc25dd0d12d9871c8@138.201.16.240:30095,97e4468ac589eac505a800411c635b14511a61bb@5.9.239.238:26656,4db916788d45d5454cfe7a68ca02c56996ee6b96@194.163.151.124:26656,ecafd5cadaf3526a588550a7bc343ce2670c988d@185.16.39.231:26656,4018be5af4189573366762fa168826b4408418db@135.125.188.17:32095,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
