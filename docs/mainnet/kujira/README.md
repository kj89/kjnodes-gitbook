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
peers="da2673cf09dc2c124947827f4cf5e7c17114d504@142.132.202.98:26656,4af5ea231c2fe1ca8174fb627e65bc09564f313b@45.143.196.110:11856,27227b6c380d806bc9c934bdbd8ca060fb61d7df@217.174.247.59:15602,a7e7864f241db457f38d8e5b5b3c3de989dea2fe@66.94.126.62:26656,79ace78a1fb98876c7bcbf8ec54864b740aa76ff@65.108.128.201:11856,1fb8ef552bf812a15d0d81ffbc8a3eb77b4319e6@65.21.231.176:26656,ecafd5cadaf3526a588550a7bc343ce2670c988d@185.16.39.231:26656,7f83a8f94bddb377ff195b3c9ee2abc91ddf0433@51.81.242.74:26656,b80cf7882c8cab4894d41ccd4f5a00406d8b5f7d@146.59.52.48:30095,d02fc7c5db5e502bb78ceeb81067ddab5b0cf51a@89.39.104.128:13656,fb5b72024981de8ea392876c8409fe60a439d699@54.235.174.123:26656,1d436f8d9a36e7d93d897012dd4e98871e8c4fbb@65.108.137.37:26656,d6f2eee997d108d4fde5683e31d678427376dfce@77.68.27.75:26656,a7d96dc929824613315dcc1c90fee119f28cc51f@134.65.193.158:26656,f62a0842be95a33b191879c977eed2072e37926b@57.128.20.147:30256,2dee642e616c8ad3991e98791f23bbc59112fe76@20.42.13.26:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656,b29969a2384159db8f8052bc118066bd067157c4@85.215.105.19:15602,c62e0701155a690616fcd3a57fa2fda444840561@65.108.76.242:32095,01d708d4124f30700c05c97947ae10231d8755f7@95.217.197.100:26655,213dbb8301ce1c0f5662a9b723bd613f15e1dd4e@75.119.157.167:30656,030f65339defb01b0e3ddaeaa54cbeac00dd0c74@185.182.193.89:26656,b4cbe0e3f6436833dd50ee4ba5cb472605652953@35.213.142.220:26656,09076c7908db88316498cf4cd4702a8d269e0da9@15.235.114.85:26656,e250c12df7aa910e9950e162df6b6e8ef210c8da@44.206.174.98:26656,a430d40d7c4272a649b8309abed412f562057539@3.37.223.124:26656,1d6fceb2a8182e9b91d105053dbe03bc9248bcd0@89.163.146.22:26656,b8e8c1738a49cd6143cf83287a5087c2618ebca0@141.95.47.82:30256,a9ed3a9256cbabe889b2989ad99a3e7e173c3ffe@108.165.178.242:26655,8362a432d50cc800618de6a76cc92d532baa8fa4@173.212.247.202:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
