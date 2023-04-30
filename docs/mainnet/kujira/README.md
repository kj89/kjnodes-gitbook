# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/kujira.png" alt=""><figcaption></figcaption></figure>

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
peers="b12591db8b67f7a78b2834b5c122299fdb6c8deb@65.108.201.154:2060,1fb8ef552bf812a15d0d81ffbc8a3eb77b4319e6@65.21.231.176:26656,4018be5af4189573366762fa168826b4408418db@135.125.188.17:32095,8d59c2958dfb2f852b201cbaa60743c771ce338b@147.135.45.32:26656,a9ed3a9256cbabe889b2989ad99a3e7e173c3ffe@108.165.178.242:26655,55d5419822feeab727b2be57e834534cbd91d6a4@65.108.69.91:26656,213dbb8301ce1c0f5662a9b723bd613f15e1dd4e@75.119.157.167:30656,c8b74590ce04f0f7c32b1c668290e00ec7ec275e@148.113.8.63:11856,79ace78a1fb98876c7bcbf8ec54864b740aa76ff@65.108.128.201:11856,2447ee9b31fa85fc6dc35644636364fccb16d976@95.216.46.251:26656,c62e0701155a690616fcd3a57fa2fda444840561@65.108.76.242:32095,fdde823fb8c9ef908d4b229f177c5f8b18e90274@54.235.174.123:26656,3d150f6a71caca5607daff69c9049c04c37da64e@51.210.223.186:30095,ffac364ae5a9a730b49f02ba95b11878f76b7043@135.125.189.131:31095,ff7a1787ea93a49ece2ee92f601a4c52951278c4@185.119.118.112:2000,780ee91b43bcdced2daebee61996742f6b01b579@138.201.197.119:2000,3a15fa46fe0a27d4ee60497a470a8c91911a9e5e@15.235.66.89:11756,b802fbfb83d6400639f17f2883f30a46ee6b05ad@51.210.223.185:32095,1d6fceb2a8182e9b91d105053dbe03bc9248bcd0@89.163.146.22:26656,9dc8a19299064e8d5a414a1fc25dd0d12d9871c8@138.201.16.240:30095,fa57c7c253be46ad9f696ee2f2c1d72cbc6a1591@146.59.52.135:31095,459229e89fd0722f7f758b7de782d0eb94aa9639@146.59.85.223:11856,e250c12df7aa910e9950e162df6b6e8ef210c8da@44.206.174.98:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656,177872437b2a31ebb0fb740ba5bd32b0be99e280@5.79.74.229:31095,66e141c0327dc94e45232a0742e57777f452c89d@13.88.61.209:26656,d6f2eee997d108d4fde5683e31d678427376dfce@77.68.27.75:26656,ecafd5cadaf3526a588550a7bc343ce2670c988d@185.16.39.231:26656,52739251216bd8e7d17ac69810f83bf58a7b1b10@47.144.18.69:26656,4d3ecadfa5002bdd407c56c04933999b8f96cfbd@34.173.154.254:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
