# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/kujira.png" alt=""><figcaption></figcaption></figure>

Kujira is a Layer 1 protocol built on Cosmos, which can be used for  hosting community-selected projects.

**Chain ID**: kaiyo-1 | **Latest Version Tag**: v0.8.6 | **Wasm**: ON

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
* grpc: kujira.grpc.kjnodes.com:11390

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@kujira.rpc.kjnodes.com:11356
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@kujira.rpc.kjnodes.com:11359
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/kujira/addrbook.json > $HOME/.kujira/config/addrbook.json
```

**live-peers** (12)
```bash
peers="935c1065ad23338a5e6a75f08fb650f9f46dbd3e@65.108.201.167:26656,7878121e8fa201c836c8c0a95b6a9c7ac6e5b101@51.161.117.214:26656,8d59c2958dfb2f852b201cbaa60743c771ce338b@147.135.45.32:26656,56598f1d3153b4368a0d9ac083b379b09ae2b531@162.19.95.239:11856,b3c01f34ce7de9a0f74e1b45e8ebda4af293c5c7@31.17.205.204:26656,ff7a1787ea93a49ece2ee92f601a4c52951278c4@185.119.118.112:2000,a9ed3a9256cbabe889b2989ad99a3e7e173c3ffe@108.165.178.242:26655,a7e7864f241db457f38d8e5b5b3c3de989dea2fe@66.94.126.62:26656,d02fc7c5db5e502bb78ceeb81067ddab5b0cf51a@89.39.104.128:13656,08dae6e7a7b2da2697ed3dd982b57fab2c3cf64b@5.75.178.169:26635,01d708d4124f30700c05c97947ae10231d8755f7@95.217.197.100:26655,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:11356"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
