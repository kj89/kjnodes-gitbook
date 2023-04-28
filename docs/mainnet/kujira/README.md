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

**live-peers** (29)
```bash
peers="b12591db8b67f7a78b2834b5c122299fdb6c8deb@65.108.201.154:2060,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.169.213:26656,b80cf7882c8cab4894d41ccd4f5a00406d8b5f7d@146.59.52.48:30095,ff7a1787ea93a49ece2ee92f601a4c52951278c4@185.119.118.112:2000,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656,1a781f294b8c30ab0b4e54494359263e9b389ebb@141.94.219.133:11756,897c55fb33076c9cecc56f6c04e2a3cbed195e7c@185.248.24.20:26796,79ace78a1fb98876c7bcbf8ec54864b740aa76ff@65.108.128.201:11856,9dc8a19299064e8d5a414a1fc25dd0d12d9871c8@138.201.16.240:30095,4a87e847c8fc15812e4d8ce57c43581ab0e7a4dd@95.214.55.100:26256,3d150f6a71caca5607daff69c9049c04c37da64e@51.210.223.186:30095,da2673cf09dc2c124947827f4cf5e7c17114d504@142.132.202.98:26656,fa925ef53799d2cf30b317ac52759871909b151c@44.206.174.98:26656,a9ed3a9256cbabe889b2989ad99a3e7e173c3ffe@108.165.178.242:26655,d6f2eee997d108d4fde5683e31d678427376dfce@77.68.27.75:26656,b29969a2384159db8f8052bc118066bd067157c4@85.215.105.19:15602,a7e7864f241db457f38d8e5b5b3c3de989dea2fe@66.94.126.62:26656,4c54a10004045c74ae65e57de7ed7126d8481549@95.216.46.251:26656,4018be5af4189573366762fa168826b4408418db@135.125.188.17:32095,5e198508b28dce7dd2375cb26911e1e2bb635e28@172.177.255.3:26656,ffac364ae5a9a730b49f02ba95b11878f76b7043@135.125.189.131:31095,8d59c2958dfb2f852b201cbaa60743c771ce338b@147.135.45.32:26656,fa57c7c253be46ad9f696ee2f2c1d72cbc6a1591@146.59.52.135:31095,04b384fd77f70082a9a6e4d8fb3db827340f4e74@148.251.13.186:11856,213dbb8301ce1c0f5662a9b723bd613f15e1dd4e@75.119.157.167:30656,55d5419822feeab727b2be57e834534cbd91d6a4@65.108.69.91:26656,52739251216bd8e7d17ac69810f83bf58a7b1b10@47.144.18.69:26656,b802fbfb83d6400639f17f2883f30a46ee6b05ad@51.210.223.185:32095,861f4624276d80aa538ad446ce608910ca24940d@148.251.177.45:11656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
