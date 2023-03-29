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
peers="ccffabe81f2de8a81e171f93fe1209392bf9993f@65.108.234.59:26656,79ace78a1fb98876c7bcbf8ec54864b740aa76ff@65.108.128.201:11856,3a15fa46fe0a27d4ee60497a470a8c91911a9e5e@15.235.66.89:11756,fa57c7c253be46ad9f696ee2f2c1d72cbc6a1591@146.59.52.135:31095,97e4468ac589eac505a800411c635b14511a61bb@5.9.239.238:26656,d6f2eee997d108d4fde5683e31d678427376dfce@77.68.27.75:26656,ecafd5cadaf3526a588550a7bc343ce2670c988d@185.16.39.231:26656,9dc8a19299064e8d5a414a1fc25dd0d12d9871c8@138.201.16.240:30095,780ee91b43bcdced2daebee61996742f6b01b579@138.201.197.119:2000,a7e7864f241db457f38d8e5b5b3c3de989dea2fe@66.94.126.62:26656,9ef0bd43e617127e3978c585437619008ccca263@65.108.229.102:22656,471518432477e31ea348af246c0b54095d41352c@88.198.131.126:26656,6cceba286b498d4a1931f85e35ea0fa433373057@88.198.128.174:26656,b802fbfb83d6400639f17f2883f30a46ee6b05ad@51.210.223.185:32095,4af5ea231c2fe1ca8174fb627e65bc09564f313b@45.143.196.110:11856,9c753f4e99433b79b0b7dce69fffa0a892491f95@65.108.234.154:26656,ff7a1787ea93a49ece2ee92f601a4c52951278c4@185.119.118.112:2000,c62e0701155a690616fcd3a57fa2fda444840561@65.108.76.242:32095,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
