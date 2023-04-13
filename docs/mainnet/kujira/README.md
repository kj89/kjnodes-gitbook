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
peers="58fc044463399f5c2d94a39e3474ea6196dab0bd@65.108.198.118:11856,9dc8a19299064e8d5a414a1fc25dd0d12d9871c8@138.201.16.240:30095,b12591db8b67f7a78b2834b5c122299fdb6c8deb@65.108.201.154:2060,4af5ea231c2fe1ca8174fb627e65bc09564f313b@45.143.196.110:11856,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656,ecafd5cadaf3526a588550a7bc343ce2670c988d@185.16.39.231:26656,a9ed3a9256cbabe889b2989ad99a3e7e173c3ffe@108.165.178.242:26655,27227b6c380d806bc9c934bdbd8ca060fb61d7df@217.174.247.59:15602,4db916788d45d5454cfe7a68ca02c56996ee6b96@194.163.151.124:26656,79ace78a1fb98876c7bcbf8ec54864b740aa76ff@65.108.128.201:11856,7f83a8f94bddb377ff195b3c9ee2abc91ddf0433@51.81.242.74:26656,da2673cf09dc2c124947827f4cf5e7c17114d504@142.132.202.98:26656,6cceba286b498d4a1931f85e35ea0fa433373057@88.198.128.174:26656,177872437b2a31ebb0fb740ba5bd32b0be99e280@5.79.74.229:31095,d6f2eee997d108d4fde5683e31d678427376dfce@77.68.27.75:26656,52739251216bd8e7d17ac69810f83bf58a7b1b10@47.144.5.20:26656,3d150f6a71caca5607daff69c9049c04c37da64e@51.210.223.186:30095,09076c7908db88316498cf4cd4702a8d269e0da9@15.235.114.85:26656,afc247bceddc0eeeb6cf62db6fb4f985b03dd3b0@95.214.53.191:26656,1d436f8d9a36e7d93d897012dd4e98871e8c4fbb@65.108.137.37:26656,3533d12b4dcacec1ab74183fad9cc65cb9e71ac7@198.244.167.22:5060,fb5b72024981de8ea392876c8409fe60a439d699@54.235.174.123:26656,35af92154fdb2ac19f3f010c26cca9e5c175d054@65.108.238.61:27656,01d708d4124f30700c05c97947ae10231d8755f7@95.217.197.100:26655,030f65339defb01b0e3ddaeaa54cbeac00dd0c74@185.182.193.89:26656,f2fe529a8d41ce4beffccb2e00342e74df9ebeca@78.31.71.246:26656,8362a432d50cc800618de6a76cc92d532baa8fa4@173.212.247.202:26656,0cd7caa189ab5e3fb19b4d32516027b578ab7838@45.79.118.43:26656,1d6fceb2a8182e9b91d105053dbe03bc9248bcd0@89.163.146.22:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
