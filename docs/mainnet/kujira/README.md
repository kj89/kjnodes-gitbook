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
peers="177872437b2a31ebb0fb740ba5bd32b0be99e280@5.79.74.229:31095,4db916788d45d5454cfe7a68ca02c56996ee6b96@194.163.151.124:26656,42e9c232f830e39824747ce6a4e5ef1e765cad72@67.222.144.195:26656,d6f2eee997d108d4fde5683e31d678427376dfce@77.68.27.75:26656,1d6fceb2a8182e9b91d105053dbe03bc9248bcd0@89.163.146.22:26656,213dbb8301ce1c0f5662a9b723bd613f15e1dd4e@75.119.157.167:30656,ff7a1787ea93a49ece2ee92f601a4c52951278c4@185.119.118.112:2000,ecafd5cadaf3526a588550a7bc343ce2670c988d@185.16.39.231:26656,4ae125f9c9b8e2f1ac83749c2209e26056b97851@65.108.238.103:11856,f46cdadb43b2078fba2a8b261e0109c18967fdaf@95.214.55.140:21156,897c55fb33076c9cecc56f6c04e2a3cbed195e7c@185.248.24.20:26796,a9ed3a9256cbabe889b2989ad99a3e7e173c3ffe@108.165.178.242:26655,af9465035c6111c6cedddd7bdee60c78a8f9921c@54.235.174.123:26656,7f83a8f94bddb377ff195b3c9ee2abc91ddf0433@51.81.242.74:26656,33029bd94bc0251ca686f4e69cf24a1c6fdcb68e@176.191.97.120:28656,6212f700687500f96ef56af3488e99fc4b009e19@212.68.34.95:26656,d2247f7b919f0781c90ee61958d7044665a22d38@169.155.169.182:26656,beb3329e969ae64d97c276f0ed0a1773ebdf61dc@146.19.24.142:26656,da2673cf09dc2c124947827f4cf5e7c17114d504@142.132.202.98:26656,bb755a830bb788e3f5bd58896db17044b1a0e9ec@138.197.178.136:26656,38e36150df914ec2c9fbaf378ab0e73ada4a3987@95.216.6.111:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656,030f65339defb01b0e3ddaeaa54cbeac00dd0c74@185.182.193.89:26656,d21056f3e4fd703ca99f75de46a6cc5983339585@65.108.137.37:26656,cedf10f69de7d77b358964a1b802a15ad79a7c97@74.80.183.130:26655,fa925ef53799d2cf30b317ac52759871909b151c@44.206.174.98:26656,c8b74590ce04f0f7c32b1c668290e00ec7ec275e@148.113.8.63:11856,e751b31b5444ed4a7489a456be805c736756eeb8@195.3.223.19:26656,52739251216bd8e7d17ac69810f83bf58a7b1b10@47.144.5.20:26656,8362a432d50cc800618de6a76cc92d532baa8fa4@173.212.247.202:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
