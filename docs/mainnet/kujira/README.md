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
peers="177872437b2a31ebb0fb740ba5bd32b0be99e280@5.79.74.229:31095,27227b6c380d806bc9c934bdbd8ca060fb61d7df@217.174.247.59:15602,e751b31b5444ed4a7489a456be805c736756eeb8@195.3.223.19:26656,4018be5af4189573366762fa168826b4408418db@135.125.188.17:32095,d6f2eee997d108d4fde5683e31d678427376dfce@77.68.27.75:26656,ff7a1787ea93a49ece2ee92f601a4c52951278c4@185.119.118.112:2000,ecafd5cadaf3526a588550a7bc343ce2670c988d@185.16.39.231:26656,7f83a8f94bddb377ff195b3c9ee2abc91ddf0433@51.81.242.74:26656,780ee91b43bcdced2daebee61996742f6b01b579@138.201.197.119:2000,66c551ebcb68fe343c7e2720593dc47426813a68@93.189.30.101:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656,030f65339defb01b0e3ddaeaa54cbeac00dd0c74@185.182.193.89:26656,a9ed3a9256cbabe889b2989ad99a3e7e173c3ffe@108.165.178.242:26655,ebc272824924ea1a27ea3183dd0b9ba713494f83@178.211.139.77:26796,c55d35ef908b74c2ddec2f47dbdb4032d7dfbcd4@23.88.69.22:27266,b29969a2384159db8f8052bc118066bd067157c4@85.215.105.19:15602,cedf10f69de7d77b358964a1b802a15ad79a7c97@74.80.183.130:26655,8f610c29d253f448be4543d38bf772e79c70c195@172.176.217.66:26656,09076c7908db88316498cf4cd4702a8d269e0da9@15.235.114.85:26656,44cdb43183527cad8a3a9b032532e1b4422e53e7@24.158.14.210:26656,da2673cf09dc2c124947827f4cf5e7c17114d504@142.132.202.98:26656,fdde823fb8c9ef908d4b229f177c5f8b18e90274@54.235.174.123:26656,01d708d4124f30700c05c97947ae10231d8755f7@95.217.197.100:26655,b12591db8b67f7a78b2834b5c122299fdb6c8deb@65.108.201.154:2060,1d6fceb2a8182e9b91d105053dbe03bc9248bcd0@89.163.146.22:26656,b8d3a5e5d43d8e18c4ecfd56a8ca46dc3b91bc32@107.181.231.178:26656,79ace78a1fb98876c7bcbf8ec54864b740aa76ff@65.108.128.201:11856,a7400009548180ad2b229b2acfb27b8359984346@90.68.89.146:26656,8362a432d50cc800618de6a76cc92d532baa8fa4@173.212.247.202:26656,4db916788d45d5454cfe7a68ca02c56996ee6b96@194.163.151.124:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
