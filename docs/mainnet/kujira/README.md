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

**live-peers** (30)
```bash
peers="ecafd5cadaf3526a588550a7bc343ce2670c988d@185.16.39.231:26656,3a7733d4b670a672db326bd6e5f8ae37e14a3dbd@138.201.226.227:26656,459229e89fd0722f7f758b7de782d0eb94aa9639@146.59.85.223:11856,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656,213dbb8301ce1c0f5662a9b723bd613f15e1dd4e@75.119.157.167:30656,b29969a2384159db8f8052bc118066bd067157c4@85.215.105.19:15602,030f65339defb01b0e3ddaeaa54cbeac00dd0c74@185.182.193.89:26656,3a15fa46fe0a27d4ee60497a470a8c91911a9e5e@15.235.66.89:11756,c62e0701155a690616fcd3a57fa2fda444840561@65.108.76.242:32095,ccb4fffc9caa2f0d8da833f3cad906b833320bab@51.222.254.98:26656,0a03f5dfb5b995647808c4d100e7b98d0526302f@85.214.18.167:26656,55d5419822feeab727b2be57e834534cbd91d6a4@65.108.69.91:26656,698529d303400cc4dff026c6c47eb0dc6547b595@95.216.43.190:36346,58fc044463399f5c2d94a39e3474ea6196dab0bd@65.108.198.118:11856,177872437b2a31ebb0fb740ba5bd32b0be99e280@5.79.74.229:31095,b12591db8b67f7a78b2834b5c122299fdb6c8deb@65.108.201.154:2060,3d150f6a71caca5607daff69c9049c04c37da64e@51.210.223.186:30095,9dc8a19299064e8d5a414a1fc25dd0d12d9871c8@138.201.16.240:30095,ff7a1787ea93a49ece2ee92f601a4c52951278c4@185.119.118.112:2000,ffac364ae5a9a730b49f02ba95b11878f76b7043@135.125.189.131:31095,a7d96dc929824613315dcc1c90fee119f28cc51f@134.65.193.158:26656,cedf10f69de7d77b358964a1b802a15ad79a7c97@74.80.183.130:26655,79ace78a1fb98876c7bcbf8ec54864b740aa76ff@65.108.128.201:11856,7f83a8f94bddb377ff195b3c9ee2abc91ddf0433@51.81.242.74:26656,fb5b72024981de8ea392876c8409fe60a439d699@54.235.174.123:26656,95904a998eec98aca444db406b0b6ce11de67e47@52.190.14.162:26656,1cbc1bff7cdaeffd5a25583f9525f44fb55f7215@95.214.54.28:26156,d21056f3e4fd703ca99f75de46a6cc5983339585@65.108.137.37:26656,52739251216bd8e7d17ac69810f83bf58a7b1b10@47.144.5.20:26656,4018be5af4189573366762fa168826b4408418db@135.125.188.17:32095"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
