# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/kujira.png" width="150" alt=""><figcaption></figcaption></figure>

Kujira is a Layer 1 protocol built on Cosmos, which can be used for  hosting community-selected projects.

**Chain ID**: kaiyo-1 | **Latest Version Tag**: v0.8.4-mainnet | **Wasm**: ON

[Website](https://kujira.app) | [Discord](https://discord.gg/teamkujira) | [Twitter](https://twitter.com/TeamKujira)

[![Stake with kjnodes](https://i.ibb.co/cr44Q8j/button-stake-with-kjnodes.png)](https://restake.app/kujira/kujiravaloper1tnuqj73jfn3724lqz34c27tuv80nv336sadqym)

Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals

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
peers="79ace78a1fb98876c7bcbf8ec54864b740aa76ff@65.108.128.201:11856,89757803f40da51678451735445ad40d5b15e059@169.155.45.187:26656,f62a0842be95a33b191879c977eed2072e37926b@57.128.20.147:30256,c124ce0b508e8b9ed1c5b6957f362225659b5343@136.243.248.190:26656,6cceba286b498d4a1931f85e35ea0fa433373057@88.198.128.174:26656,a7e7864f241db457f38d8e5b5b3c3de989dea2fe@66.94.126.62:26656,413bd0410b649de5070b2fe8356cad356459dc37@65.108.235.165:26656,a7d96dc929824613315dcc1c90fee119f28cc51f@134.65.193.158:26656,b8e8c1738a49cd6143cf83287a5087c2618ebca0@141.95.47.82:30256,3a15fa46fe0a27d4ee60497a470a8c91911a9e5e@15.235.66.89:11756,7c26c34148779b1d0979eb069dbe354752a3644f@5.9.84.213:25656,58fc044463399f5c2d94a39e3474ea6196dab0bd@65.108.198.118:11856,4db916788d45d5454cfe7a68ca02c56996ee6b96@194.163.151.124:26656,9dc8a19299064e8d5a414a1fc25dd0d12d9871c8@138.201.16.240:30095,213dbb8301ce1c0f5662a9b723bd613f15e1dd4e@75.119.157.167:30656,eb9742d81b436b95e324816794229a9efdaf8ea8@142.132.155.170:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656,ecafd5cadaf3526a588550a7bc343ce2670c988d@185.16.39.231:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
