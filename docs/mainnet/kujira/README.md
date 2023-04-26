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
peers="9dc8a19299064e8d5a414a1fc25dd0d12d9871c8@138.201.16.240:30095,da2673cf09dc2c124947827f4cf5e7c17114d504@142.132.202.98:26656,129771a48f43b83c6144c7d282ad1da62434cc07@15.204.197.12:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656,1a781f294b8c30ab0b4e54494359263e9b389ebb@141.94.219.133:11756,4c54a10004045c74ae65e57de7ed7126d8481549@95.216.46.251:26656,a7d96dc929824613315dcc1c90fee119f28cc51f@134.65.193.158:26656,177872437b2a31ebb0fb740ba5bd32b0be99e280@5.79.74.229:31095,b8d3a5e5d43d8e18c4ecfd56a8ca46dc3b91bc32@107.181.231.178:26656,ff7a1787ea93a49ece2ee92f601a4c52951278c4@185.119.118.112:2000,ffac364ae5a9a730b49f02ba95b11878f76b7043@135.125.189.131:31095,c8b74590ce04f0f7c32b1c668290e00ec7ec275e@148.113.8.63:11856,1cbc1bff7cdaeffd5a25583f9525f44fb55f7215@95.214.54.28:26156,55d5419822feeab727b2be57e834534cbd91d6a4@65.108.69.91:26656,b29969a2384159db8f8052bc118066bd067157c4@85.215.105.19:15602,1d6fceb2a8182e9b91d105053dbe03bc9248bcd0@89.163.146.22:26656,fb5b72024981de8ea392876c8409fe60a439d699@54.235.174.123:26656,79ace78a1fb98876c7bcbf8ec54864b740aa76ff@65.108.128.201:11856,0743497e30049ac8d59fee5b2ab3a49c3824b95c@198.244.200.196:26656,cedf10f69de7d77b358964a1b802a15ad79a7c97@74.80.183.130:26655,4d3ecadfa5002bdd407c56c04933999b8f96cfbd@34.173.154.254:26656,a9ed3a9256cbabe889b2989ad99a3e7e173c3ffe@108.165.178.242:26655,ffc433d20c23eea2b905e1239b5dc79c69ef4167@84.80.24.31:26156,fa925ef53799d2cf30b317ac52759871909b151c@44.206.174.98:26656,ecafd5cadaf3526a588550a7bc343ce2670c988d@185.16.39.231:26656,ccffabe81f2de8a81e171f93fe1209392bf9993f@65.108.234.59:26656,d6f2eee997d108d4fde5683e31d678427376dfce@77.68.27.75:26656,437f25b8219e6d5e4520906ca60607c8b73516b5@20.49.37.21:26656,0cd7caa189ab5e3fb19b4d32516027b578ab7838@45.79.118.43:26656,4a87e847c8fc15812e4d8ce57c43581ab0e7a4dd@95.214.55.100:26256"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
