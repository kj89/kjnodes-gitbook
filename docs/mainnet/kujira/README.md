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
peers="ccffabe81f2de8a81e171f93fe1209392bf9993f@65.108.234.59:26656,a7d96dc929824613315dcc1c90fee119f28cc51f@134.65.193.158:26656,d2247f7b919f0781c90ee61958d7044665a22d38@169.155.169.182:26656,3a7733d4b670a672db326bd6e5f8ae37e14a3dbd@138.201.226.227:26656,3d150f6a71caca5607daff69c9049c04c37da64e@51.210.223.186:30095,7f83a8f94bddb377ff195b3c9ee2abc91ddf0433@51.81.242.74:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656,ff7a1787ea93a49ece2ee92f601a4c52951278c4@185.119.118.112:2000,58fc044463399f5c2d94a39e3474ea6196dab0bd@65.108.198.118:11856,8362a432d50cc800618de6a76cc92d532baa8fa4@173.212.247.202:26656,94da43cae2bc6e9d16decfe3d78c64603f5ad9e2@192.118.76.122:26616,ebc272824924ea1a27ea3183dd0b9ba713494f83@178.211.139.77:26796,a9ed3a9256cbabe889b2989ad99a3e7e173c3ffe@108.165.178.242:26655,09076c7908db88316498cf4cd4702a8d269e0da9@15.235.114.85:26656,ecafd5cadaf3526a588550a7bc343ce2670c988d@185.16.39.231:26656,da2673cf09dc2c124947827f4cf5e7c17114d504@142.132.202.98:26656,79ace78a1fb98876c7bcbf8ec54864b740aa76ff@65.108.128.201:11856,897c55fb33076c9cecc56f6c04e2a3cbed195e7c@185.248.24.20:26796,a7e7864f241db457f38d8e5b5b3c3de989dea2fe@66.94.126.62:26656,1d436f8d9a36e7d93d897012dd4e98871e8c4fbb@65.108.137.37:26656,fa925ef53799d2cf30b317ac52759871909b151c@44.206.174.98:26656,52739251216bd8e7d17ac69810f83bf58a7b1b10@47.144.5.20:26656,d6f2eee997d108d4fde5683e31d678427376dfce@77.68.27.75:26656,4db916788d45d5454cfe7a68ca02c56996ee6b96@194.163.151.124:26656,01d708d4124f30700c05c97947ae10231d8755f7@95.217.197.100:26655,e751b31b5444ed4a7489a456be805c736756eeb8@195.3.223.19:26656,1d6fceb2a8182e9b91d105053dbe03bc9248bcd0@89.163.146.22:26656,030f65339defb01b0e3ddaeaa54cbeac00dd0c74@185.182.193.89:26656,4d3ecadfa5002bdd407c56c04933999b8f96cfbd@34.173.154.254:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
