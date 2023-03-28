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
peers="a5253fd5dcf432cfc1eb29fa5631edaa1b913061@135.181.22.238:36654,177872437b2a31ebb0fb740ba5bd32b0be99e280@5.79.74.229:31095,7c26c34148779b1d0979eb069dbe354752a3644f@5.9.84.213:25656,780ee91b43bcdced2daebee61996742f6b01b579@138.201.197.119:2000,beb3329e969ae64d97c276f0ed0a1773ebdf61dc@146.19.24.142:26656,d6f2eee997d108d4fde5683e31d678427376dfce@77.68.27.75:26656,a7e7864f241db457f38d8e5b5b3c3de989dea2fe@66.94.126.62:26656,8a210f1bcfc9015a7bc18dcc5add29c0dce3f2dc@95.217.70.62:26656,fa57c7c253be46ad9f696ee2f2c1d72cbc6a1591@146.59.52.135:31095,4018be5af4189573366762fa168826b4408418db@135.125.188.17:32095,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656,3d150f6a71caca5607daff69c9049c04c37da64e@51.210.223.186:30095,b8e8c1738a49cd6143cf83287a5087c2618ebca0@141.95.47.82:30256,9c8826ceeb1254d16856092a50df4fd720910362@50.116.49.237:26656,01d708d4124f30700c05c97947ae10231d8755f7@95.217.197.100:26655,471518432477e31ea348af246c0b54095d41352c@88.198.131.126:26656,bba10290da32f3cb41e15c3a192413666ce05cee@5.9.208.14:26656,79ace78a1fb98876c7bcbf8ec54864b740aa76ff@65.108.128.201:11856,d2247f7b919f0781c90ee61958d7044665a22d38@169.155.169.182:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
