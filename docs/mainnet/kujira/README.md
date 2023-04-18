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
peers="c62e0701155a690616fcd3a57fa2fda444840561@65.108.76.242:32095,1fb8ef552bf812a15d0d81ffbc8a3eb77b4319e6@65.21.231.176:26656,e751b31b5444ed4a7489a456be805c736756eeb8@195.3.223.19:26656,27227b6c380d806bc9c934bdbd8ca060fb61d7df@217.174.247.59:15602,ff7a1787ea93a49ece2ee92f601a4c52951278c4@185.119.118.112:2000,f46cdadb43b2078fba2a8b261e0109c18967fdaf@95.214.55.140:21156,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656,7f83a8f94bddb377ff195b3c9ee2abc91ddf0433@51.81.242.74:26656,d21056f3e4fd703ca99f75de46a6cc5983339585@65.108.137.37:26656,a8f9cedd64e5fb2dc019061985afe8c34fd5efcb@141.94.251.25:26656,ffac364ae5a9a730b49f02ba95b11878f76b7043@135.125.189.131:31095,da2673cf09dc2c124947827f4cf5e7c17114d504@142.132.202.98:26656,a9ed3a9256cbabe889b2989ad99a3e7e173c3ffe@108.165.178.242:26655,cedf10f69de7d77b358964a1b802a15ad79a7c97@74.80.183.130:26655,1d6fceb2a8182e9b91d105053dbe03bc9248bcd0@89.163.146.22:26656,79ace78a1fb98876c7bcbf8ec54864b740aa76ff@65.108.128.201:11856,09076c7908db88316498cf4cd4702a8d269e0da9@15.235.114.85:26656,b12591db8b67f7a78b2834b5c122299fdb6c8deb@65.108.201.154:2060,a7400009548180ad2b229b2acfb27b8359984346@90.68.89.146:26656,213dbb8301ce1c0f5662a9b723bd613f15e1dd4e@75.119.157.167:30656,e92b3424ba53c10aefdf9b402f4c03888de96c2e@45.77.61.157:26656,030f65339defb01b0e3ddaeaa54cbeac00dd0c74@185.182.193.89:26656,1cbc1bff7cdaeffd5a25583f9525f44fb55f7215@95.214.54.28:26156,d2247f7b919f0781c90ee61958d7044665a22d38@169.155.169.182:26656,c1a2642423a21ef0c306e73e5b89b592f9909828@70.37.167.38:26656,58fc044463399f5c2d94a39e3474ea6196dab0bd@65.108.198.118:11856,af9465035c6111c6cedddd7bdee60c78a8f9921c@54.235.174.123:26656,4db916788d45d5454cfe7a68ca02c56996ee6b96@194.163.151.124:26656,ebc272824924ea1a27ea3183dd0b9ba713494f83@178.211.139.77:26796"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
