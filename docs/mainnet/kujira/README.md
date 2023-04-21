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
peers="7f83a8f94bddb377ff195b3c9ee2abc91ddf0433@51.81.242.74:26656,79ace78a1fb98876c7bcbf8ec54864b740aa76ff@65.108.128.201:11856,af9465035c6111c6cedddd7bdee60c78a8f9921c@54.235.174.123:26656,030f65339defb01b0e3ddaeaa54cbeac00dd0c74@185.182.193.89:26656,a9ed3a9256cbabe889b2989ad99a3e7e173c3ffe@108.165.178.242:26655,fa925ef53799d2cf30b317ac52759871909b151c@44.206.174.98:26656,c62e0701155a690616fcd3a57fa2fda444840561@65.108.76.242:32095,58fc044463399f5c2d94a39e3474ea6196dab0bd@65.108.198.118:11856,d6f2eee997d108d4fde5683e31d678427376dfce@77.68.27.75:26656,c8b74590ce04f0f7c32b1c668290e00ec7ec275e@148.113.8.63:11856,1d6fceb2a8182e9b91d105053dbe03bc9248bcd0@89.163.146.22:26656,b29969a2384159db8f8052bc118066bd067157c4@85.215.105.19:15602,897c55fb33076c9cecc56f6c04e2a3cbed195e7c@185.248.24.20:26796,177872437b2a31ebb0fb740ba5bd32b0be99e280@5.79.74.229:31095,9dc8a19299064e8d5a414a1fc25dd0d12d9871c8@138.201.16.240:30095,780ee91b43bcdced2daebee61996742f6b01b579@138.201.197.119:2000,b12591db8b67f7a78b2834b5c122299fdb6c8deb@65.108.201.154:2060,a7d96dc929824613315dcc1c90fee119f28cc51f@134.65.193.158:26656,fa57c7c253be46ad9f696ee2f2c1d72cbc6a1591@146.59.52.135:31095,15679999b404a9ee027dc9f5e795d6c4fddb6cee@51.91.152.102:20000,ffac364ae5a9a730b49f02ba95b11878f76b7043@135.125.189.131:31095,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.169.213:26656,1a781f294b8c30ab0b4e54494359263e9b389ebb@141.94.219.133:11756,de08e6178779ff3b19a8b6d22a05664392cb2b35@185.216.179.205:26656,da2673cf09dc2c124947827f4cf5e7c17114d504@142.132.202.98:26656,42e9c232f830e39824747ce6a4e5ef1e765cad72@67.222.144.195:26656,8362a432d50cc800618de6a76cc92d532baa8fa4@173.212.247.202:26656,1cbc1bff7cdaeffd5a25583f9525f44fb55f7215@95.214.54.28:26156,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
