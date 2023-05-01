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

**live-peers** (30)
```bash
peers="ff7a1787ea93a49ece2ee92f601a4c52951278c4@185.119.118.112:2000,4a87e847c8fc15812e4d8ce57c43581ab0e7a4dd@95.214.55.100:26256,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656,beb3329e969ae64d97c276f0ed0a1773ebdf61dc@146.19.24.142:26656,55d5419822feeab727b2be57e834534cbd91d6a4@65.108.69.91:26656,3d150f6a71caca5607daff69c9049c04c37da64e@51.210.223.186:30095,b12591db8b67f7a78b2834b5c122299fdb6c8deb@65.108.201.154:2060,9dc8a19299064e8d5a414a1fc25dd0d12d9871c8@138.201.16.240:30095,01d708d4124f30700c05c97947ae10231d8755f7@95.217.197.100:26655,4ae125f9c9b8e2f1ac83749c2209e26056b97851@65.108.238.103:11856,15679999b404a9ee027dc9f5e795d6c4fddb6cee@51.91.152.102:20000,8d59c2958dfb2f852b201cbaa60743c771ce338b@147.135.45.32:26656,79ace78a1fb98876c7bcbf8ec54864b740aa76ff@65.108.128.201:11856,58fc044463399f5c2d94a39e3474ea6196dab0bd@65.108.198.118:11856,c62e0701155a690616fcd3a57fa2fda444840561@65.108.76.242:32095,d6f2eee997d108d4fde5683e31d678427376dfce@77.68.27.75:26656,0babb41bab58bda22245976ee385deddf76a14b3@95.216.46.251:26656,e250c12df7aa910e9950e162df6b6e8ef210c8da@44.206.174.98:26656,cedf10f69de7d77b358964a1b802a15ad79a7c97@74.80.183.130:26655,a76e18bffe05fb1332dcd4340fc6e2b482ed38fb@195.3.222.246:26656,bd2821b2dc8b928946026caf3e9bd1e7a0013a61@145.239.10.46:13656,1cbc1bff7cdaeffd5a25583f9525f44fb55f7215@95.214.54.28:26156,52739251216bd8e7d17ac69810f83bf58a7b1b10@47.144.18.69:26656,d2247f7b919f0781c90ee61958d7044665a22d38@169.155.169.182:26656,de08e6178779ff3b19a8b6d22a05664392cb2b35@185.216.179.205:26656,5ae54af5483ff090e57a51f9f3568490373e2419@135.181.26.211:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.169.213:26656,338d79e24ce36a9580ce3e9fce8eeb84e0e6f17b@65.108.130.171:26656,b21f57d5054aaa4cf8e3599bbe13719a47cc02d4@141.94.193.12:14656,a9ed3a9256cbabe889b2989ad99a3e7e173c3ffe@108.165.178.242:26655"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
