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
peers="b12591db8b67f7a78b2834b5c122299fdb6c8deb@65.108.201.154:2060,897c55fb33076c9cecc56f6c04e2a3cbed195e7c@185.248.24.20:26796,177872437b2a31ebb0fb740ba5bd32b0be99e280@5.79.74.229:31095,ffac364ae5a9a730b49f02ba95b11878f76b7043@135.125.189.131:31095,89757803f40da51678451735445ad40d5b15e059@169.155.45.187:26656,213dbb8301ce1c0f5662a9b723bd613f15e1dd4e@75.119.157.167:30656,a9ed3a9256cbabe889b2989ad99a3e7e173c3ffe@108.165.178.242:26655,ecafd5cadaf3526a588550a7bc343ce2670c988d@185.16.39.231:26656,fdde823fb8c9ef908d4b229f177c5f8b18e90274@54.235.174.123:26656,b29969a2384159db8f8052bc118066bd067157c4@85.215.105.19:15602,d2247f7b919f0781c90ee61958d7044665a22d38@169.155.169.182:26656,3d150f6a71caca5607daff69c9049c04c37da64e@51.210.223.186:30095,cedf10f69de7d77b358964a1b802a15ad79a7c97@74.80.183.130:26655,030f65339defb01b0e3ddaeaa54cbeac00dd0c74@185.182.193.89:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656,9dc8a19299064e8d5a414a1fc25dd0d12d9871c8@138.201.16.240:30095,1d6fceb2a8182e9b91d105053dbe03bc9248bcd0@89.163.146.22:26656,7f83a8f94bddb377ff195b3c9ee2abc91ddf0433@51.81.242.74:26656,c8b74590ce04f0f7c32b1c668290e00ec7ec275e@148.113.8.63:11856,459229e89fd0722f7f758b7de782d0eb94aa9639@146.59.85.223:11856,ff7a1787ea93a49ece2ee92f601a4c52951278c4@185.119.118.112:2000,52739251216bd8e7d17ac69810f83bf58a7b1b10@47.144.5.20:26656,42e9c232f830e39824747ce6a4e5ef1e765cad72@67.222.144.195:26656,26d19e5b3f3a5ebafe827dabca4ef008d9c5e6fd@168.119.15.94:26656,79ace78a1fb98876c7bcbf8ec54864b740aa76ff@65.108.128.201:11856,70bb20d6078ff90294ebd7c9803de25b73d48955@148.251.77.27:26656,e92b3424ba53c10aefdf9b402f4c03888de96c2e@45.77.61.157:26656,8362a432d50cc800618de6a76cc92d532baa8fa4@173.212.247.202:26656,c6eaf84ee15c3f311236b19f5de2c231d96e5ac4@95.217.209.187:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
