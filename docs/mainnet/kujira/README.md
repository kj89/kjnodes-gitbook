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

**live-peers** (19)
```bash
peers="8a210f1bcfc9015a7bc18dcc5add29c0dce3f2dc@95.217.70.62:26656,780ee91b43bcdced2daebee61996742f6b01b579@138.201.197.119:2000,97e4468ac589eac505a800411c635b14511a61bb@5.9.239.238:26656,7c26c34148779b1d0979eb069dbe354752a3644f@5.9.84.213:25656,b29969a2384159db8f8052bc118066bd067157c4@85.215.105.19:15602,d6f2eee997d108d4fde5683e31d678427376dfce@77.68.27.75:26656,a7d96dc929824613315dcc1c90fee119f28cc51f@134.65.193.158:26656,8e4e1f1e087c76c71c64e477e95495833da82aa2@95.217.65.54:26656,d2247f7b919f0781c90ee61958d7044665a22d38@169.155.169.182:26656,d3427d444b6909529d73025fe32a73dfea7b90d1@148.251.85.115:26656,82588f011491c6100d922d133f52fc23460b9231@95.217.91.238:26656,c55d35ef908b74c2ddec2f47dbdb4032d7dfbcd4@23.88.69.22:27266,177872437b2a31ebb0fb740ba5bd32b0be99e280@5.79.74.229:31095,66c551ebcb68fe343c7e2720593dc47426813a68@93.189.30.101:26656,fa57c7c253be46ad9f696ee2f2c1d72cbc6a1591@146.59.52.135:31095,0393c19b176d1cf8bc560c5a8fa990301deb1a7e@95.216.235.54:26656,a7e7864f241db457f38d8e5b5b3c3de989dea2fe@66.94.126.62:26656,4e1c2471efb89239fb04a4b75f9f87177fd91d00@95.217.82.78:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
