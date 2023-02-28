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

**live-peers** (20)
```bash
peers="7c26c34148779b1d0979eb069dbe354752a3644f@5.9.84.213:25656,ed71d6328a0228cd2eac7d71451509813c660b5d@116.202.164.206:26656,129771a48f43b83c6144c7d282ad1da62434cc07@15.204.197.12:26656,4db916788d45d5454cfe7a68ca02c56996ee6b96@194.163.151.124:26656,01cf570d3b08fdb5fe2f307cb485de7a35a3af23@135.148.55.229:11856,4ae125f9c9b8e2f1ac83749c2209e26056b97851@65.108.238.103:11856,9dc8a19299064e8d5a414a1fc25dd0d12d9871c8@138.201.16.240:30095,15679999b404a9ee027dc9f5e795d6c4fddb6cee@51.91.152.102:20000,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.169.213:26656,bba10290da32f3cb41e15c3a192413666ce05cee@5.9.208.14:26656,eb9742d81b436b95e324816794229a9efdaf8ea8@142.132.155.170:26656,a7d96dc929824613315dcc1c90fee119f28cc51f@134.65.193.158:26656,fa57c7c253be46ad9f696ee2f2c1d72cbc6a1591@146.59.52.135:31095,d6f2eee997d108d4fde5683e31d678427376dfce@77.68.27.75:26656,b8e8c1738a49cd6143cf83287a5087c2618ebca0@141.95.47.82:30256,0a51eaa669fa7ad9ad6a8d19942f324725596f23@65.109.80.92:26656,9ef0bd43e617127e3978c585437619008ccca263@65.108.229.102:22656,5ae54af5483ff090e57a51f9f3568490373e2419@135.181.26.211:26656,d6d14f99ef25c8ffee6fa4afca40fece0c1ab9fe@107.181.229.154:20656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
