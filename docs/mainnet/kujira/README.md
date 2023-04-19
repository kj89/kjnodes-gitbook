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

**live-peers** (29)
```bash
peers="58fc044463399f5c2d94a39e3474ea6196dab0bd@65.108.198.118:11856,d3427d444b6909529d73025fe32a73dfea7b90d1@148.251.85.115:26656,27227b6c380d806bc9c934bdbd8ca060fb61d7df@217.174.247.59:15602,66c551ebcb68fe343c7e2720593dc47426813a68@93.189.30.101:26656,d6f2eee997d108d4fde5683e31d678427376dfce@77.68.27.75:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656,7f83a8f94bddb377ff195b3c9ee2abc91ddf0433@51.81.242.74:26656,b12591db8b67f7a78b2834b5c122299fdb6c8deb@65.108.201.154:2060,897c55fb33076c9cecc56f6c04e2a3cbed195e7c@185.248.24.20:26796,a7d96dc929824613315dcc1c90fee119f28cc51f@134.65.193.158:26656,7460c89399950966969c541331ec32e9e5d7c922@13.66.10.247:26656,4db916788d45d5454cfe7a68ca02c56996ee6b96@194.163.151.124:26656,79ace78a1fb98876c7bcbf8ec54864b740aa76ff@65.108.128.201:11856,253d2293272a29057a27797a5703f5171c267da1@192.99.15.159:26656,030f65339defb01b0e3ddaeaa54cbeac00dd0c74@185.182.193.89:26656,cedf10f69de7d77b358964a1b802a15ad79a7c97@74.80.183.130:26655,da2673cf09dc2c124947827f4cf5e7c17114d504@142.132.202.98:26656,ff7a1787ea93a49ece2ee92f601a4c52951278c4@185.119.118.112:2000,a76e18bffe05fb1332dcd4340fc6e2b482ed38fb@195.3.222.246:26656,a9ed3a9256cbabe889b2989ad99a3e7e173c3ffe@108.165.178.242:26655,09076c7908db88316498cf4cd4702a8d269e0da9@15.235.114.85:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.169.213:26656,ebc272824924ea1a27ea3183dd0b9ba713494f83@178.211.139.77:26796,4ae125f9c9b8e2f1ac83749c2209e26056b97851@65.108.238.103:11856,beb3329e969ae64d97c276f0ed0a1773ebdf61dc@146.19.24.142:26656,d21056f3e4fd703ca99f75de46a6cc5983339585@65.108.137.37:26656,c8b74590ce04f0f7c32b1c668290e00ec7ec275e@148.113.8.63:11856,8362a432d50cc800618de6a76cc92d532baa8fa4@173.212.247.202:26656,fdde823fb8c9ef908d4b229f177c5f8b18e90274@54.235.174.123:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
