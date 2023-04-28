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
peers="1fb8ef552bf812a15d0d81ffbc8a3eb77b4319e6@65.21.231.176:26656,b12591db8b67f7a78b2834b5c122299fdb6c8deb@65.108.201.154:2060,4018be5af4189573366762fa168826b4408418db@135.125.188.17:32095,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656,d2247f7b919f0781c90ee61958d7044665a22d38@169.155.169.182:26656,ccffabe81f2de8a81e171f93fe1209392bf9993f@65.108.234.59:26656,c62e0701155a690616fcd3a57fa2fda444840561@65.108.76.242:32095,ff7a1787ea93a49ece2ee92f601a4c52951278c4@185.119.118.112:2000,cedf10f69de7d77b358964a1b802a15ad79a7c97@74.80.183.130:26655,f3f9b8c36eaca48ca753bffcd49cd257080d3a67@40.84.170.74:26656,ecafd5cadaf3526a588550a7bc343ce2670c988d@185.16.39.231:26656,d6f2eee997d108d4fde5683e31d678427376dfce@77.68.27.75:26656,79ace78a1fb98876c7bcbf8ec54864b740aa76ff@65.108.128.201:11856,9dc8a19299064e8d5a414a1fc25dd0d12d9871c8@138.201.16.240:30095,04b384fd77f70082a9a6e4d8fb3db827340f4e74@148.251.13.186:11856,4d3ecadfa5002bdd407c56c04933999b8f96cfbd@34.173.154.254:26656,c8b74590ce04f0f7c32b1c668290e00ec7ec275e@148.113.8.63:11856,3d150f6a71caca5607daff69c9049c04c37da64e@51.210.223.186:30095,da2673cf09dc2c124947827f4cf5e7c17114d504@142.132.202.98:26656,8d59c2958dfb2f852b201cbaa60743c771ce338b@147.135.45.32:26656,55d5419822feeab727b2be57e834534cbd91d6a4@65.108.69.91:26656,a9ed3a9256cbabe889b2989ad99a3e7e173c3ffe@108.165.178.242:26655,b29969a2384159db8f8052bc118066bd067157c4@85.215.105.19:15602,3a15fa46fe0a27d4ee60497a470a8c91911a9e5e@15.235.66.89:11756,beb3329e969ae64d97c276f0ed0a1773ebdf61dc@146.19.24.142:26656,338d79e24ce36a9580ce3e9fce8eeb84e0e6f17b@65.108.130.171:26656,1cbc1bff7cdaeffd5a25583f9525f44fb55f7215@95.214.54.28:26156,a7d96dc929824613315dcc1c90fee119f28cc51f@134.65.193.158:26656,ffac364ae5a9a730b49f02ba95b11878f76b7043@135.125.189.131:31095,89757803f40da51678451735445ad40d5b15e059@169.155.45.187:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
