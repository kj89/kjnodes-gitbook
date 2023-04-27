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
peers="213dbb8301ce1c0f5662a9b723bd613f15e1dd4e@75.119.157.167:30656,1cbc1bff7cdaeffd5a25583f9525f44fb55f7215@95.214.54.28:26156,7f83a8f94bddb377ff195b3c9ee2abc91ddf0433@51.81.242.74:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656,ccffabe81f2de8a81e171f93fe1209392bf9993f@65.108.234.59:26656,58fc044463399f5c2d94a39e3474ea6196dab0bd@65.108.198.118:11856,da2673cf09dc2c124947827f4cf5e7c17114d504@142.132.202.98:26656,3a15fa46fe0a27d4ee60497a470a8c91911a9e5e@15.235.66.89:11756,c62e0701155a690616fcd3a57fa2fda444840561@65.108.76.242:32095,0cd7caa189ab5e3fb19b4d32516027b578ab7838@45.79.118.43:26656,55d5419822feeab727b2be57e834534cbd91d6a4@65.108.69.91:26656,b802fbfb83d6400639f17f2883f30a46ee6b05ad@51.210.223.185:32095,8d59c2958dfb2f852b201cbaa60743c771ce338b@147.135.45.32:26656,79ace78a1fb98876c7bcbf8ec54864b740aa76ff@65.108.128.201:11856,9dc8a19299064e8d5a414a1fc25dd0d12d9871c8@138.201.16.240:30095,177872437b2a31ebb0fb740ba5bd32b0be99e280@5.79.74.229:31095,ff7a1787ea93a49ece2ee92f601a4c52951278c4@185.119.118.112:2000,d6f2eee997d108d4fde5683e31d678427376dfce@77.68.27.75:26656,4a87e847c8fc15812e4d8ce57c43581ab0e7a4dd@95.214.55.100:26256,ebc272824924ea1a27ea3183dd0b9ba713494f83@178.211.139.77:26796,1a781f294b8c30ab0b4e54494359263e9b389ebb@141.94.219.133:11756,fa925ef53799d2cf30b317ac52759871909b151c@44.206.174.98:26656,0a03f5dfb5b995647808c4d100e7b98d0526302f@85.214.18.167:26656,a185a830eda85adcd822a92efe330519fbb0d102@13.88.99.213:26656,cedf10f69de7d77b358964a1b802a15ad79a7c97@74.80.183.130:26655,a9ed3a9256cbabe889b2989ad99a3e7e173c3ffe@108.165.178.242:26655,b29969a2384159db8f8052bc118066bd067157c4@85.215.105.19:15602,8362a432d50cc800618de6a76cc92d532baa8fa4@173.212.247.202:26656,af9465035c6111c6cedddd7bdee60c78a8f9921c@54.235.174.123:26656,4d3ecadfa5002bdd407c56c04933999b8f96cfbd@34.173.154.254:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
