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
peers="58fc044463399f5c2d94a39e3474ea6196dab0bd@65.108.198.118:11856,4db916788d45d5454cfe7a68ca02c56996ee6b96@194.163.151.124:26656,e81c56107cc4506c1d6645cbe64f115beaccef26@34.173.154.254:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.169.213:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656,c1a740841a6dc0b56730e975b1a4aa2d8c73b204@65.108.237.233:29656,7f83a8f94bddb377ff195b3c9ee2abc91ddf0433@51.81.242.74:26656,79ace78a1fb98876c7bcbf8ec54864b740aa76ff@65.108.128.201:11856,d0eac3080ce36476503b0a8ea6c63a6f1c42642f@138.91.87.19:26656,7b29fc249e80d4275c2afa7ea1b76513ec792169@20.51.128.131:26656,52739251216bd8e7d17ac69810f83bf58a7b1b10@47.144.5.20:26656,a8f9cedd64e5fb2dc019061985afe8c34fd5efcb@141.94.251.25:26656,6cceba286b498d4a1931f85e35ea0fa433373057@88.198.128.174:26656,01d708d4124f30700c05c97947ae10231d8755f7@95.217.197.100:26655,ecafd5cadaf3526a588550a7bc343ce2670c988d@185.16.39.231:26656,1d436f8d9a36e7d93d897012dd4e98871e8c4fbb@65.108.137.37:26656,e557abe0e49127c3e738eca6fc816c7cf0106dec@54.235.174.123:26656,de08e6178779ff3b19a8b6d22a05664392cb2b35@185.216.179.205:26656,09076c7908db88316498cf4cd4702a8d269e0da9@15.235.114.85:26656,f46cdadb43b2078fba2a8b261e0109c18967fdaf@95.214.55.140:21156,d6f2eee997d108d4fde5683e31d678427376dfce@77.68.27.75:26656,a9ed3a9256cbabe889b2989ad99a3e7e173c3ffe@108.165.178.242:26655,780ee91b43bcdced2daebee61996742f6b01b579@138.201.197.119:2000,d3cbe679ef7e491d3b34f6557bde23077f28e21f@31.17.205.204:26656,e751b31b5444ed4a7489a456be805c736756eeb8@195.3.223.19:26656,f2fe529a8d41ce4beffccb2e00342e74df9ebeca@78.31.71.246:26656,b21f57d5054aaa4cf8e3599bbe13719a47cc02d4@141.94.193.12:14656,afc247bceddc0eeeb6cf62db6fb4f985b03dd3b0@95.214.53.191:26656,8362a432d50cc800618de6a76cc92d532baa8fa4@173.212.247.202:26656,1fb8ef552bf812a15d0d81ffbc8a3eb77b4319e6@65.21.231.176:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
