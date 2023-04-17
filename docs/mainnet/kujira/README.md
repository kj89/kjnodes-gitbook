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

**live-peers** (30)
```bash
peers="b12591db8b67f7a78b2834b5c122299fdb6c8deb@65.108.201.154:2060,79ace78a1fb98876c7bcbf8ec54864b740aa76ff@65.108.128.201:11856,4018be5af4189573366762fa168826b4408418db@135.125.188.17:32095,1d6fceb2a8182e9b91d105053dbe03bc9248bcd0@89.163.146.22:26656,471518432477e31ea348af246c0b54095d41352c@88.198.131.126:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656,ff7a1787ea93a49ece2ee92f601a4c52951278c4@185.119.118.112:2000,b29969a2384159db8f8052bc118066bd067157c4@85.215.105.19:15602,8362a432d50cc800618de6a76cc92d532baa8fa4@173.212.247.202:26656,ebc272824924ea1a27ea3183dd0b9ba713494f83@178.211.139.77:26796,da2673cf09dc2c124947827f4cf5e7c17114d504@142.132.202.98:26656,a9ed3a9256cbabe889b2989ad99a3e7e173c3ffe@108.165.178.242:26655,ef5f630a1f3fd5a8623791a91ea3cd54b1a56685@44.206.174.98:26656,09076c7908db88316498cf4cd4702a8d269e0da9@15.235.114.85:26656,01d708d4124f30700c05c97947ae10231d8755f7@95.217.197.100:26655,e751b31b5444ed4a7489a456be805c736756eeb8@195.3.223.19:26656,030f65339defb01b0e3ddaeaa54cbeac00dd0c74@185.182.193.89:26656,7f83a8f94bddb377ff195b3c9ee2abc91ddf0433@51.81.242.74:26656,a7400009548180ad2b229b2acfb27b8359984346@90.68.89.146:26656,58fc044463399f5c2d94a39e3474ea6196dab0bd@65.108.198.118:11856,6cab44dad82daa85fed9ea99d5ab398293006984@65.21.136.170:26656,fdde823fb8c9ef908d4b229f177c5f8b18e90274@54.235.174.123:26656,beb3329e969ae64d97c276f0ed0a1773ebdf61dc@146.19.24.142:26656,d21056f3e4fd703ca99f75de46a6cc5983339585@65.108.137.37:26656,a7d96dc929824613315dcc1c90fee119f28cc51f@134.65.193.158:26656,c6eaf84ee15c3f311236b19f5de2c231d96e5ac4@95.217.209.187:26656,0a51eaa669fa7ad9ad6a8d19942f324725596f23@65.109.80.92:26656,1965ceb15d8a26edd931680698acbffd6b863f7b@13.87.244.192:26656,cedf10f69de7d77b358964a1b802a15ad79a7c97@74.80.183.130:26655,c55d35ef908b74c2ddec2f47dbdb4032d7dfbcd4@23.88.69.22:27266"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
