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
peers="82588f011491c6100d922d133f52fc23460b9231@95.217.91.238:26656,8a210f1bcfc9015a7bc18dcc5add29c0dce3f2dc@95.217.70.62:26656,79ace78a1fb98876c7bcbf8ec54864b740aa76ff@65.108.128.201:11856,6f3129d01218b939511cccf7e0318bfe872d97c4@65.109.33.181:26656,1a781f294b8c30ab0b4e54494359263e9b389ebb@141.94.219.133:11756,e751b31b5444ed4a7489a456be805c736756eeb8@195.3.223.19:26656,d3427d444b6909529d73025fe32a73dfea7b90d1@148.251.85.115:26656,3a7733d4b670a672db326bd6e5f8ae37e14a3dbd@138.201.226.227:26656,4db916788d45d5454cfe7a68ca02c56996ee6b96@194.163.151.124:26656,c124ce0b508e8b9ed1c5b6957f362225659b5343@136.243.248.190:26656,3a15fa46fe0a27d4ee60497a470a8c91911a9e5e@15.235.66.89:11756,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656,ecafd5cadaf3526a588550a7bc343ce2670c988d@185.16.39.231:26656,a7e7864f241db457f38d8e5b5b3c3de989dea2fe@66.94.126.62:26656,f2fe529a8d41ce4beffccb2e00342e74df9ebeca@78.31.71.246:26656,7c26c34148779b1d0979eb069dbe354752a3644f@5.9.84.213:25656,9dc8a19299064e8d5a414a1fc25dd0d12d9871c8@138.201.16.240:30095,97e4468ac589eac505a800411c635b14511a61bb@5.9.239.238:26656,bba10290da32f3cb41e15c3a192413666ce05cee@5.9.208.14:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
