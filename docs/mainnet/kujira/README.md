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
peers="d2247f7b919f0781c90ee61958d7044665a22d38@169.155.169.182:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656,fa925ef53799d2cf30b317ac52759871909b151c@44.206.174.98:26656,c1a740841a6dc0b56730e975b1a4aa2d8c73b204@65.108.237.233:29656,4c54a10004045c74ae65e57de7ed7126d8481549@95.216.46.251:26656,ecafd5cadaf3526a588550a7bc343ce2670c988d@185.16.39.231:26656,b29969a2384159db8f8052bc118066bd067157c4@85.215.105.19:15602,55d5419822feeab727b2be57e834534cbd91d6a4@65.108.69.91:26656,ffac364ae5a9a730b49f02ba95b11878f76b7043@135.125.189.131:31095,b12591db8b67f7a78b2834b5c122299fdb6c8deb@65.108.201.154:2060,213dbb8301ce1c0f5662a9b723bd613f15e1dd4e@75.119.157.167:30656,c8b74590ce04f0f7c32b1c668290e00ec7ec275e@148.113.8.63:11856,9dc8a19299064e8d5a414a1fc25dd0d12d9871c8@138.201.16.240:30095,177872437b2a31ebb0fb740ba5bd32b0be99e280@5.79.74.229:31095,d6f2eee997d108d4fde5683e31d678427376dfce@77.68.27.75:26656,ff7a1787ea93a49ece2ee92f601a4c52951278c4@185.119.118.112:2000,79ace78a1fb98876c7bcbf8ec54864b740aa76ff@65.108.128.201:11856,0a03f5dfb5b995647808c4d100e7b98d0526302f@85.214.18.167:26656,0cd7caa189ab5e3fb19b4d32516027b578ab7838@45.79.118.43:26656,a9ed3a9256cbabe889b2989ad99a3e7e173c3ffe@108.165.178.242:26655,52739251216bd8e7d17ac69810f83bf58a7b1b10@104.34.161.115:26656,a7d96dc929824613315dcc1c90fee119f28cc51f@134.65.193.158:26656,cedf10f69de7d77b358964a1b802a15ad79a7c97@74.80.183.130:26655,27227b6c380d806bc9c934bdbd8ca060fb61d7df@217.174.247.59:15602,ccffabe81f2de8a81e171f93fe1209392bf9993f@65.108.234.59:26656,e557abe0e49127c3e738eca6fc816c7cf0106dec@54.235.174.123:26656,1d6fceb2a8182e9b91d105053dbe03bc9248bcd0@89.163.146.22:26656,1cbc1bff7cdaeffd5a25583f9525f44fb55f7215@95.214.54.28:26156,3a15fa46fe0a27d4ee60497a470a8c91911a9e5e@15.235.66.89:11756,8362a432d50cc800618de6a76cc92d532baa8fa4@173.212.247.202:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
