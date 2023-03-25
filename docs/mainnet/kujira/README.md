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

**live-peers** (19)
```bash
peers="ccffabe81f2de8a81e171f93fe1209392bf9993f@65.108.234.59:26656,8e4e1f1e087c76c71c64e477e95495833da82aa2@95.217.65.54:26656,79ace78a1fb98876c7bcbf8ec54864b740aa76ff@65.108.128.201:11856,177872437b2a31ebb0fb740ba5bd32b0be99e280@5.79.74.229:31095,15679999b404a9ee027dc9f5e795d6c4fddb6cee@51.91.152.102:20000,fa57c7c253be46ad9f696ee2f2c1d72cbc6a1591@146.59.52.135:31095,ecafd5cadaf3526a588550a7bc343ce2670c988d@185.16.39.231:26656,a7e7864f241db457f38d8e5b5b3c3de989dea2fe@66.94.126.62:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656,a7d96dc929824613315dcc1c90fee119f28cc51f@134.65.193.158:26656,b80cf7882c8cab4894d41ccd4f5a00406d8b5f7d@146.59.52.48:30095,d3427d444b6909529d73025fe32a73dfea7b90d1@148.251.85.115:26656,935c1065ad23338a5e6a75f08fb650f9f46dbd3e@65.108.201.167:26656,b802fbfb83d6400639f17f2883f30a46ee6b05ad@51.210.223.185:32095,da2673cf09dc2c124947827f4cf5e7c17114d504@142.132.202.98:26656,c124ce0b508e8b9ed1c5b6957f362225659b5343@136.243.248.190:26656,0393c19b176d1cf8bc560c5a8fa990301deb1a7e@95.216.235.54:26656,6cceba286b498d4a1931f85e35ea0fa433373057@88.198.128.174:26656,3d150f6a71caca5607daff69c9049c04c37da64e@51.210.223.186:30095"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
