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

**live-peers** (29)
```bash
peers="c62e0701155a690616fcd3a57fa2fda444840561@65.108.76.242:32095,4ae125f9c9b8e2f1ac83749c2209e26056b97851@65.108.238.103:11856,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656,55d5419822feeab727b2be57e834534cbd91d6a4@65.108.69.91:26656,8d59c2958dfb2f852b201cbaa60743c771ce338b@147.135.45.32:26656,c1a740841a6dc0b56730e975b1a4aa2d8c73b204@65.108.237.233:29656,3d150f6a71caca5607daff69c9049c04c37da64e@51.210.223.186:30095,1f0cacffa06af0633e1a4cb6710f57081147081d@109.236.88.56:21156,1fb8ef552bf812a15d0d81ffbc8a3eb77b4319e6@65.21.231.176:26656,0babb41bab58bda22245976ee385deddf76a14b3@95.216.46.251:26656,d6f2eee997d108d4fde5683e31d678427376dfce@77.68.27.75:26656,79ace78a1fb98876c7bcbf8ec54864b740aa76ff@65.108.128.201:11856,a9ed3a9256cbabe889b2989ad99a3e7e173c3ffe@108.165.178.242:26655,0c7da38c54e1a7d8ab7d48601b51847564ce019e@5.161.91.34:45656,bb755a830bb788e3f5bd58896db17044b1a0e9ec@138.197.178.136:26656,9dc8a19299064e8d5a414a1fc25dd0d12d9871c8@138.201.16.240:30095,ff7a1787ea93a49ece2ee92f601a4c52951278c4@185.119.118.112:2000,e92b3424ba53c10aefdf9b402f4c03888de96c2e@45.77.61.157:26656,52739251216bd8e7d17ac69810f83bf58a7b1b10@47.144.18.69:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.169.213:26656,1d6fceb2a8182e9b91d105053dbe03bc9248bcd0@89.163.146.22:26656,1cbc1bff7cdaeffd5a25583f9525f44fb55f7215@95.214.54.28:26156,b690b0e6a904fc0172ef1eccc07bea9f48f4e454@141.94.73.39:53756,9c328ada1ae5f9f397c409a950e9c9948bb812b8@40.84.170.19:26656,fb5b72024981de8ea392876c8409fe60a439d699@54.235.174.123:26656,d2247f7b919f0781c90ee61958d7044665a22d38@169.155.169.182:26656,553dfc2712cd890a423c70fce1f60781a20876ad@65.109.95.26:28656,89757803f40da51678451735445ad40d5b15e059@169.155.45.187:26656,4d3ecadfa5002bdd407c56c04933999b8f96cfbd@34.173.154.254:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
