# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/kujira.png" alt=""><figcaption></figcaption></figure>

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
* grpc: kujira.grpc.kjnodes.com:11390

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@kujira.rpc.kjnodes.com:11356
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@kujira.rpc.kjnodes.com:11359
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/kujira/addrbook.json > $HOME/.kujira/config/addrbook.json
```

**live-peers** (10)
```bash
peers="79ace78a1fb98876c7bcbf8ec54864b740aa76ff@65.108.128.201:11856,e751b31b5444ed4a7489a456be805c736756eeb8@195.3.223.19:26656,3a15fa46fe0a27d4ee60497a470a8c91911a9e5e@15.235.66.89:11756,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:11356,6f3129d01218b939511cccf7e0318bfe872d97c4@65.109.33.181:26656,3d150f6a71caca5607daff69c9049c04c37da64e@51.210.223.186:30095,b80cf7882c8cab4894d41ccd4f5a00406d8b5f7d@146.59.52.48:30095,c8b74590ce04f0f7c32b1c668290e00ec7ec275e@148.113.8.63:11856,ff7a1787ea93a49ece2ee92f601a4c52951278c4@185.119.118.112:2000,f46cdadb43b2078fba2a8b261e0109c18967fdaf@95.214.55.140:21156"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
