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
* grpc: kujira.grpc.kjnodes.com:113090

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@kujira.rpc.kjnodes.com:113656
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@kujira.rpc.kjnodes.com:113659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/kujira/addrbook.json > $HOME/.kujira/config/addrbook.json
```

**live-peers** (24)
```bash
peers="c1a740841a6dc0b56730e975b1a4aa2d8c73b204@65.108.237.233:29656,c62e0701155a690616fcd3a57fa2fda444840561@65.108.76.242:32095,3d150f6a71caca5607daff69c9049c04c37da64e@51.210.223.186:30095,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656,9dc8a19299064e8d5a414a1fc25dd0d12d9871c8@138.201.16.240:30095,e250c12df7aa910e9950e162df6b6e8ef210c8da@44.206.174.98:26656,d6f2eee997d108d4fde5683e31d678427376dfce@77.68.27.75:26656,4018be5af4189573366762fa168826b4408418db@135.125.188.17:32095,ff7a1787ea93a49ece2ee92f601a4c52951278c4@185.119.118.112:2000,8d59c2958dfb2f852b201cbaa60743c771ce338b@147.135.45.32:26656,55d5419822feeab727b2be57e834534cbd91d6a4@65.108.69.91:26656,b29969a2384159db8f8052bc118066bd067157c4@85.215.105.19:15602,1cbc1bff7cdaeffd5a25583f9525f44fb55f7215@95.214.54.28:26156,4a87e847c8fc15812e4d8ce57c43581ab0e7a4dd@95.214.55.100:26256,8362a432d50cc800618de6a76cc92d532baa8fa4@173.212.247.202:26656,c55d35ef908b74c2ddec2f47dbdb4032d7dfbcd4@23.88.69.22:27266,c8b74590ce04f0f7c32b1c668290e00ec7ec275e@148.113.8.63:11856,1d85c9f16727584753db78b5b54eedf0ce8de3ed@51.159.16.49:5060,79ace78a1fb98876c7bcbf8ec54864b740aa76ff@65.108.128.201:11856,e244225f4ac1c401a913a8e48f8a715a8c61fe17@168.119.161.36:26635,e557abe0e49127c3e738eca6fc816c7cf0106dec@54.235.174.123:26656,01d708d4124f30700c05c97947ae10231d8755f7@95.217.197.100:26655,1d6fceb2a8182e9b91d105053dbe03bc9248bcd0@89.163.146.22:26656,4d3ecadfa5002bdd407c56c04933999b8f96cfbd@34.173.154.254:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
