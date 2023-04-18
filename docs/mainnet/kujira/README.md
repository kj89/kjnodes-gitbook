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
peers="c62e0701155a690616fcd3a57fa2fda444840561@65.108.76.242:32095,d6f2eee997d108d4fde5683e31d678427376dfce@77.68.27.75:26656,ff7a1787ea93a49ece2ee92f601a4c52951278c4@185.119.118.112:2000,3a7733d4b670a672db326bd6e5f8ae37e14a3dbd@138.201.226.227:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656,da2673cf09dc2c124947827f4cf5e7c17114d504@142.132.202.98:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.169.213:26656,42b5d12955b4211a500db05c0a97c6907dea1c78@13.84.8.144:26656,79ace78a1fb98876c7bcbf8ec54864b740aa76ff@65.108.128.201:11856,ebc272824924ea1a27ea3183dd0b9ba713494f83@178.211.139.77:26796,beb3329e969ae64d97c276f0ed0a1773ebdf61dc@146.19.24.142:26656,3a15fa46fe0a27d4ee60497a470a8c91911a9e5e@15.235.66.89:11756,ffc433d20c23eea2b905e1239b5dc79c69ef4167@84.80.24.31:26156,b29969a2384159db8f8052bc118066bd067157c4@85.215.105.19:15602,7f83a8f94bddb377ff195b3c9ee2abc91ddf0433@51.81.242.74:26656,09076c7908db88316498cf4cd4702a8d269e0da9@15.235.114.85:26656,a9ed3a9256cbabe889b2989ad99a3e7e173c3ffe@108.165.178.242:26655,e92b3424ba53c10aefdf9b402f4c03888de96c2e@45.77.61.157:26656,27227b6c380d806bc9c934bdbd8ca060fb61d7df@217.174.247.59:15602,af9465035c6111c6cedddd7bdee60c78a8f9921c@54.235.174.123:26656,935c1065ad23338a5e6a75f08fb650f9f46dbd3e@65.108.201.167:26656,cedf10f69de7d77b358964a1b802a15ad79a7c97@74.80.183.130:26655,1d6fceb2a8182e9b91d105053dbe03bc9248bcd0@89.163.146.22:26656,b12591db8b67f7a78b2834b5c122299fdb6c8deb@65.108.201.154:2060,a8f9cedd64e5fb2dc019061985afe8c34fd5efcb@141.94.251.25:26656,bd2821b2dc8b928946026caf3e9bd1e7a0013a61@145.239.10.46:13656,1fb8ef552bf812a15d0d81ffbc8a3eb77b4319e6@65.21.231.176:26656,4db916788d45d5454cfe7a68ca02c56996ee6b96@194.163.151.124:26656,66c551ebcb68fe343c7e2720593dc47426813a68@93.189.30.101:26656,4d3ecadfa5002bdd407c56c04933999b8f96cfbd@34.173.154.254:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
