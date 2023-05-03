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

**live-peers** (30)
```bash
peers="b12591db8b67f7a78b2834b5c122299fdb6c8deb@65.108.201.154:2060,a7d96dc929824613315dcc1c90fee119f28cc51f@134.65.193.158:26656,4db916788d45d5454cfe7a68ca02c56996ee6b96@194.163.151.124:26656,8362a432d50cc800618de6a76cc92d532baa8fa4@173.212.247.202:26656,1fb8ef552bf812a15d0d81ffbc8a3eb77b4319e6@65.21.231.176:26656,79ace78a1fb98876c7bcbf8ec54864b740aa76ff@65.108.128.201:11856,ccffabe81f2de8a81e171f93fe1209392bf9993f@65.108.234.59:26656,0babb41bab58bda22245976ee385deddf76a14b3@95.216.46.251:26656,ecafd5cadaf3526a588550a7bc343ce2670c988d@185.16.39.231:26656,a9ed3a9256cbabe889b2989ad99a3e7e173c3ffe@108.165.178.242:26655,3a15fa46fe0a27d4ee60497a470a8c91911a9e5e@15.235.66.89:11756,9dc8a19299064e8d5a414a1fc25dd0d12d9871c8@138.201.16.240:30095,c62e0701155a690616fcd3a57fa2fda444840561@65.108.76.242:32095,c8b74590ce04f0f7c32b1c668290e00ec7ec275e@148.113.8.63:11856,55d5419822feeab727b2be57e834534cbd91d6a4@65.108.69.91:26656,1cbc1bff7cdaeffd5a25583f9525f44fb55f7215@95.214.54.28:26156,fd0a34b84a53b7ed9bd399f6267e4a4f91207f37@20.41.24.115:26656,04b384fd77f70082a9a6e4d8fb3db827340f4e74@148.251.13.186:11856,cedf10f69de7d77b358964a1b802a15ad79a7c97@74.80.183.130:26655,d6f2eee997d108d4fde5683e31d678427376dfce@77.68.27.75:26656,8d59c2958dfb2f852b201cbaa60743c771ce338b@147.135.45.32:26656,ff7a1787ea93a49ece2ee92f601a4c52951278c4@185.119.118.112:2000,59d39d2da07414b350ec36f7a6f43a9aa46132a4@47.75.104.62:26656,3d150f6a71caca5607daff69c9049c04c37da64e@51.210.223.186:30095,d02fc7c5db5e502bb78ceeb81067ddab5b0cf51a@89.39.104.128:13656,9c8826ceeb1254d16856092a50df4fd720910362@50.116.49.237:26656,1d6fceb2a8182e9b91d105053dbe03bc9248bcd0@89.163.146.22:26656,fdde823fb8c9ef908d4b229f177c5f8b18e90274@54.235.174.123:26656,b29969a2384159db8f8052bc118066bd067157c4@85.215.105.19:15602,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
