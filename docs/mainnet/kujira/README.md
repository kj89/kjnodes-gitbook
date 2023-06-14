# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/kujira.png" alt=""><figcaption></figcaption></figure>

Kujira is a Layer 1 protocol built on Cosmos, which can be used for  hosting community-selected projects.

**Chain ID**: kaiyo-1 | **Latest Version Tag**: v0.8.7 | **Wasm**: ON

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

**live-peers** (13)
```bash
peers="c62e0701155a690616fcd3a57fa2fda444840561@65.108.76.242:32095,c030a6692eb4f39b00b1dbb68e47698230bc2de9@142.132.248.34:11856,56598f1d3153b4368a0d9ac083b379b09ae2b531@162.19.95.239:11856,e751b31b5444ed4a7489a456be805c736756eeb8@195.3.223.19:26656,7878121e8fa201c836c8c0a95b6a9c7ac6e5b101@51.161.117.214:26656,e8f53eab61a5cb9f2c3460c739080ee86f2b80cc@13.40.82.236:26656,d6f2eee997d108d4fde5683e31d678427376dfce@77.68.27.75:26656,d2247f7b919f0781c90ee61958d7044665a22d38@169.155.169.182:26656,79ace78a1fb98876c7bcbf8ec54864b740aa76ff@65.108.128.201:11856,b3c01f34ce7de9a0f74e1b45e8ebda4af293c5c7@31.17.205.204:26656,08dae6e7a7b2da2697ed3dd982b57fab2c3cf64b@5.75.178.169:26635,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:11356,3a52966037a81007a9a73499bd68cf5e38db1e67@178.211.139.222:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
