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

**live-peers** (29)
```bash
peers="d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656,4d3ecadfa5002bdd407c56c04933999b8f96cfbd@34.173.154.254:26656,27227b6c380d806bc9c934bdbd8ca060fb61d7df@217.174.247.59:15602,d6d14f99ef25c8ffee6fa4afca40fece0c1ab9fe@107.181.229.154:20656,af9465035c6111c6cedddd7bdee60c78a8f9921c@54.235.174.123:26656,b690b0e6a904fc0172ef1eccc07bea9f48f4e454@141.94.73.39:53756,a9ed3a9256cbabe889b2989ad99a3e7e173c3ffe@108.165.178.242:26655,52739251216bd8e7d17ac69810f83bf58a7b1b10@47.144.5.20:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.169.213:26656,1d6fceb2a8182e9b91d105053dbe03bc9248bcd0@89.163.146.22:26656,09076c7908db88316498cf4cd4702a8d269e0da9@15.235.114.85:26656,da2673cf09dc2c124947827f4cf5e7c17114d504@142.132.202.98:26656,7f83a8f94bddb377ff195b3c9ee2abc91ddf0433@51.81.242.74:26656,861f4624276d80aa538ad446ce608910ca24940d@148.251.177.45:11656,79ace78a1fb98876c7bcbf8ec54864b740aa76ff@65.108.128.201:11856,698529d303400cc4dff026c6c47eb0dc6547b595@95.216.43.190:36346,ebc272824924ea1a27ea3183dd0b9ba713494f83@178.211.139.77:26796,9dc8a19299064e8d5a414a1fc25dd0d12d9871c8@138.201.16.240:30095,0cd7caa189ab5e3fb19b4d32516027b578ab7838@45.79.118.43:26656,ecafd5cadaf3526a588550a7bc343ce2670c988d@185.16.39.231:26656,01d708d4124f30700c05c97947ae10231d8755f7@95.217.197.100:26655,1d436f8d9a36e7d93d897012dd4e98871e8c4fbb@65.108.137.37:26656,6ae61aaf7973ae5e1b54804fc6b8f636ed474bcd@104.45.204.217:26656,e751b31b5444ed4a7489a456be805c736756eeb8@195.3.223.19:26656,58fc044463399f5c2d94a39e3474ea6196dab0bd@65.108.198.118:11856,b29969a2384159db8f8052bc118066bd067157c4@85.215.105.19:15602,b12591db8b67f7a78b2834b5c122299fdb6c8deb@65.108.201.154:2060,3d150f6a71caca5607daff69c9049c04c37da64e@51.210.223.186:30095,935c1065ad23338a5e6a75f08fb650f9f46dbd3e@65.108.201.167:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
