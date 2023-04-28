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
peers="a7e7864f241db457f38d8e5b5b3c3de989dea2fe@66.94.126.62:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656,c62e0701155a690616fcd3a57fa2fda444840561@65.108.76.242:32095,3d150f6a71caca5607daff69c9049c04c37da64e@51.210.223.186:30095,ff7a1787ea93a49ece2ee92f601a4c52951278c4@185.119.118.112:2000,da2673cf09dc2c124947827f4cf5e7c17114d504@142.132.202.98:26656,897c55fb33076c9cecc56f6c04e2a3cbed195e7c@185.248.24.20:26796,d6f2eee997d108d4fde5683e31d678427376dfce@77.68.27.75:26656,698529d303400cc4dff026c6c47eb0dc6547b595@95.216.43.190:36346,3a15fa46fe0a27d4ee60497a470a8c91911a9e5e@15.235.66.89:11756,cedf10f69de7d77b358964a1b802a15ad79a7c97@74.80.183.130:26655,ffac364ae5a9a730b49f02ba95b11878f76b7043@135.125.189.131:31095,79ace78a1fb98876c7bcbf8ec54864b740aa76ff@65.108.128.201:11856,e557abe0e49127c3e738eca6fc816c7cf0106dec@54.235.174.123:26656,4018be5af4189573366762fa168826b4408418db@135.125.188.17:32095,fa925ef53799d2cf30b317ac52759871909b151c@44.206.174.98:26656,b29969a2384159db8f8052bc118066bd067157c4@85.215.105.19:15602,55d5419822feeab727b2be57e834534cbd91d6a4@65.108.69.91:26656,4c54a10004045c74ae65e57de7ed7126d8481549@95.216.46.251:26656,7b83569fca7c6ea461853fbeba269a4a7344ad4d@13.64.10.202:26656,8d59c2958dfb2f852b201cbaa60743c771ce338b@147.135.45.32:26656,ccffabe81f2de8a81e171f93fe1209392bf9993f@65.108.234.59:26656,fa57c7c253be46ad9f696ee2f2c1d72cbc6a1591@146.59.52.135:31095,9dc8a19299064e8d5a414a1fc25dd0d12d9871c8@138.201.16.240:30095,a9ed3a9256cbabe889b2989ad99a3e7e173c3ffe@108.165.178.242:26655,7878121e8fa201c836c8c0a95b6a9c7ac6e5b101@51.161.117.214:26656,52739251216bd8e7d17ac69810f83bf58a7b1b10@47.144.18.69:26656,2e3c72b0b6f3007a109e78864e22661dd7071c06@38.242.130.118:26656,1cbc1bff7cdaeffd5a25583f9525f44fb55f7215@95.214.54.28:26156,8362a432d50cc800618de6a76cc92d532baa8fa4@173.212.247.202:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
