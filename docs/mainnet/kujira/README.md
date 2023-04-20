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
peers="26d19e5b3f3a5ebafe827dabca4ef008d9c5e6fd@168.119.15.94:26656,ff7a1787ea93a49ece2ee92f601a4c52951278c4@185.119.118.112:2000,fdde823fb8c9ef908d4b229f177c5f8b18e90274@54.235.174.123:26656,d21056f3e4fd703ca99f75de46a6cc5983339585@65.108.137.37:26656,c62e0701155a690616fcd3a57fa2fda444840561@65.108.76.242:32095,7f83a8f94bddb377ff195b3c9ee2abc91ddf0433@51.81.242.74:26656,030f65339defb01b0e3ddaeaa54cbeac00dd0c74@185.182.193.89:26656,a9ed3a9256cbabe889b2989ad99a3e7e173c3ffe@108.165.178.242:26655,3a15fa46fe0a27d4ee60497a470a8c91911a9e5e@15.235.66.89:11756,d3427d444b6909529d73025fe32a73dfea7b90d1@148.251.85.115:26656,b802fbfb83d6400639f17f2883f30a46ee6b05ad@51.210.223.185:32095,42e9c232f830e39824747ce6a4e5ef1e765cad72@67.222.144.195:26656,cedf10f69de7d77b358964a1b802a15ad79a7c97@74.80.183.130:26655,58fc044463399f5c2d94a39e3474ea6196dab0bd@65.108.198.118:11856,b12591db8b67f7a78b2834b5c122299fdb6c8deb@65.108.201.154:2060,1d6fceb2a8182e9b91d105053dbe03bc9248bcd0@89.163.146.22:26656,897c55fb33076c9cecc56f6c04e2a3cbed195e7c@185.248.24.20:26796,da2673cf09dc2c124947827f4cf5e7c17114d504@142.132.202.98:26656,3a7733d4b670a672db326bd6e5f8ae37e14a3dbd@138.201.226.227:26656,3d150f6a71caca5607daff69c9049c04c37da64e@51.210.223.186:30095,4ae125f9c9b8e2f1ac83749c2209e26056b97851@65.108.238.103:11856,09076c7908db88316498cf4cd4702a8d269e0da9@15.235.114.85:26656,79ace78a1fb98876c7bcbf8ec54864b740aa76ff@65.108.128.201:11856,ffac364ae5a9a730b49f02ba95b11878f76b7043@135.125.189.131:31095,c8b74590ce04f0f7c32b1c668290e00ec7ec275e@148.113.8.63:11856,b8d3a5e5d43d8e18c4ecfd56a8ca46dc3b91bc32@107.181.231.178:26656,0a03f5dfb5b995647808c4d100e7b98d0526302f@85.214.18.167:26656,e751b31b5444ed4a7489a456be805c736756eeb8@195.3.223.19:26656,b29969a2384159db8f8052bc118066bd067157c4@85.215.105.19:15602,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
