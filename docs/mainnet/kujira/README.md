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
peers="c62e0701155a690616fcd3a57fa2fda444840561@65.108.76.242:32095,3d150f6a71caca5607daff69c9049c04c37da64e@51.210.223.186:30095,89757803f40da51678451735445ad40d5b15e059@169.155.45.187:26656,4018be5af4189573366762fa168826b4408418db@135.125.188.17:32095,3a7733d4b670a672db326bd6e5f8ae37e14a3dbd@138.201.226.227:26656,d6d14f99ef25c8ffee6fa4afca40fece0c1ab9fe@107.181.229.154:20656,79ace78a1fb98876c7bcbf8ec54864b740aa76ff@65.108.128.201:11856,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656,a9ed3a9256cbabe889b2989ad99a3e7e173c3ffe@108.165.178.242:26655,01d708d4124f30700c05c97947ae10231d8755f7@95.217.197.100:26655,da2673cf09dc2c124947827f4cf5e7c17114d504@142.132.202.98:26656,09076c7908db88316498cf4cd4702a8d269e0da9@15.235.114.85:26656,35af92154fdb2ac19f3f010c26cca9e5c175d054@65.108.238.61:27656,1d436f8d9a36e7d93d897012dd4e98871e8c4fbb@65.108.137.37:26656,d6f2eee997d108d4fde5683e31d678427376dfce@77.68.27.75:26656,58fc044463399f5c2d94a39e3474ea6196dab0bd@65.108.198.118:11856,7f83a8f94bddb377ff195b3c9ee2abc91ddf0433@51.81.242.74:26656,ecafd5cadaf3526a588550a7bc343ce2670c988d@185.16.39.231:26656,8362a432d50cc800618de6a76cc92d532baa8fa4@173.212.247.202:26656,05224d96ed4ffb9bab79ee6e37ca954c28864507@40.84.170.115:26656,beb3329e969ae64d97c276f0ed0a1773ebdf61dc@146.19.24.142:26656,e751b31b5444ed4a7489a456be805c736756eeb8@195.3.223.19:26656,52739251216bd8e7d17ac69810f83bf58a7b1b10@47.144.5.20:26656,4db916788d45d5454cfe7a68ca02c56996ee6b96@194.163.151.124:26656,861f4624276d80aa538ad446ce608910ca24940d@148.251.177.45:11656,935c1065ad23338a5e6a75f08fb650f9f46dbd3e@65.108.201.167:26656,42e9c232f830e39824747ce6a4e5ef1e765cad72@67.222.144.195:26656,e557abe0e49127c3e738eca6fc816c7cf0106dec@54.235.174.123:26656,27227b6c380d806bc9c934bdbd8ca060fb61d7df@217.174.247.59:15602"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
