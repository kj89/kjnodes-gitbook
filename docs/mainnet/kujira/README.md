# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/kujira.png" width="150" alt=""><figcaption></figcaption></figure>

Kujira is a Layer 1 protocol built on Cosmos, which can be used for  hosting community-selected projects.

**Chain ID**: kaiyo-1 | **Latest Version Tag**: v0.7.1 | **Wasm**: ON

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

**live-peers** (18)
```bash
peers="ccffabe81f2de8a81e171f93fe1209392bf9993f@65.108.234.59:26656,377510fb7c0ee3cacd1a46dbf13b45a4e1525fa6@51.91.153.78:32011,780ee91b43bcdced2daebee61996742f6b01b579@138.201.197.119:2000,8362a432d50cc800618de6a76cc92d532baa8fa4@173.212.247.202:26656,a7d96dc929824613315dcc1c90fee119f28cc51f@134.65.193.158:26656,a7e7864f241db457f38d8e5b5b3c3de989dea2fe@66.94.126.62:26656,b690b0e6a904fc0172ef1eccc07bea9f48f4e454@141.94.73.39:53756,8d59c2958dfb2f852b201cbaa60743c771ce338b@147.135.45.32:26656,ccdd8ee4d8fef171e8c2bfaaa2a535033d4af32b@65.108.135.82:29656,01cf570d3b08fdb5fe2f307cb485de7a35a3af23@135.148.55.229:11856,9c8826ceeb1254d16856092a50df4fd720910362@50.116.49.237:26656,177872437b2a31ebb0fb740ba5bd32b0be99e280@5.79.74.229:31095,b80cf7882c8cab4894d41ccd4f5a00406d8b5f7d@146.59.52.48:30095,9dc8a19299064e8d5a414a1fc25dd0d12d9871c8@138.201.16.240:30095,de08e6178779ff3b19a8b6d22a05664392cb2b35@185.216.179.205:26656,ffac364ae5a9a730b49f02ba95b11878f76b7043@135.125.189.131:31095,d6f2eee997d108d4fde5683e31d678427376dfce@77.68.27.75:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
