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
peers="4ae125f9c9b8e2f1ac83749c2209e26056b97851@65.108.238.103:11856,213dbb8301ce1c0f5662a9b723bd613f15e1dd4e@75.119.157.167:30656,ecafd5cadaf3526a588550a7bc343ce2670c988d@185.16.39.231:26656,4a87e847c8fc15812e4d8ce57c43581ab0e7a4dd@95.214.55.100:26256,177872437b2a31ebb0fb740ba5bd32b0be99e280@5.79.74.229:31095,030f65339defb01b0e3ddaeaa54cbeac00dd0c74@185.182.193.89:26656,e557abe0e49127c3e738eca6fc816c7cf0106dec@54.235.174.123:26656,1cbc1bff7cdaeffd5a25583f9525f44fb55f7215@95.214.54.28:26156,e92b3424ba53c10aefdf9b402f4c03888de96c2e@45.77.61.157:26656,1fb8ef552bf812a15d0d81ffbc8a3eb77b4319e6@65.21.231.176:26656,55d5419822feeab727b2be57e834534cbd91d6a4@65.108.69.91:26656,3d150f6a71caca5607daff69c9049c04c37da64e@51.210.223.186:30095,c8b74590ce04f0f7c32b1c668290e00ec7ec275e@148.113.8.63:11856,04b384fd77f70082a9a6e4d8fb3db827340f4e74@148.251.13.186:11856,c62e0701155a690616fcd3a57fa2fda444840561@65.108.76.242:32095,8362a432d50cc800618de6a76cc92d532baa8fa4@173.212.247.202:26656,ffac364ae5a9a730b49f02ba95b11878f76b7043@135.125.189.131:31095,fa925ef53799d2cf30b317ac52759871909b151c@44.206.174.98:26656,d6f2eee997d108d4fde5683e31d678427376dfce@77.68.27.75:26656,a7e7864f241db457f38d8e5b5b3c3de989dea2fe@66.94.126.62:26656,6f3129d01218b939511cccf7e0318bfe872d97c4@65.109.33.181:26656,79ace78a1fb98876c7bcbf8ec54864b740aa76ff@65.108.128.201:11856,44cdb43183527cad8a3a9b032532e1b4422e53e7@24.158.14.210:26656,42e9c232f830e39824747ce6a4e5ef1e765cad72@67.222.144.195:26656,52739251216bd8e7d17ac69810f83bf58a7b1b10@47.144.5.20:26656,7f83a8f94bddb377ff195b3c9ee2abc91ddf0433@51.81.242.74:26656,9c753f4e99433b79b0b7dce69fffa0a892491f95@65.108.234.154:26656,a2fe17951700482c92c67b0af403eafdf1d26961@52.150.24.72:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656,0c7da38c54e1a7d8ab7d48601b51847564ce019e@5.161.91.34:45656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
