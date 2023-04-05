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
peers="b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.169.213:26656,4018be5af4189573366762fa168826b4408418db@135.125.188.17:32095,79ace78a1fb98876c7bcbf8ec54864b740aa76ff@65.108.128.201:11856,d6f2eee997d108d4fde5683e31d678427376dfce@77.68.27.75:26656,b8d3a5e5d43d8e18c4ecfd56a8ca46dc3b91bc32@107.181.231.178:26656,da2673cf09dc2c124947827f4cf5e7c17114d504@142.132.202.98:26656,94da43cae2bc6e9d16decfe3d78c64603f5ad9e2@192.118.76.122:26616,beb3329e969ae64d97c276f0ed0a1773ebdf61dc@146.19.24.142:26656,0c7da38c54e1a7d8ab7d48601b51847564ce019e@5.161.91.34:45656,7f83a8f94bddb377ff195b3c9ee2abc91ddf0433@51.81.242.74:26656,b29969a2384159db8f8052bc118066bd067157c4@85.215.105.19:15602,97e4468ac589eac505a800411c635b14511a61bb@5.9.239.238:26656,4db916788d45d5454cfe7a68ca02c56996ee6b96@194.163.151.124:26656,fb5b72024981de8ea392876c8409fe60a439d699@54.235.174.123:26656,a9ed3a9256cbabe889b2989ad99a3e7e173c3ffe@108.165.178.242:26655,01d708d4124f30700c05c97947ae10231d8755f7@95.217.197.100:26655,1d6fceb2a8182e9b91d105053dbe03bc9248bcd0@89.163.146.22:26656,1d436f8d9a36e7d93d897012dd4e98871e8c4fbb@65.108.137.37:26656,ecafd5cadaf3526a588550a7bc343ce2670c988d@185.16.39.231:26656,1d7c2841744c496990b5240668393e785302d102@172.177.154.107:26656,e81c56107cc4506c1d6645cbe64f115beaccef26@34.173.154.254:26656,e250c12df7aa910e9950e162df6b6e8ef210c8da@44.206.174.98:26656,42e9c232f830e39824747ce6a4e5ef1e765cad72@67.222.144.195:26656,935c1065ad23338a5e6a75f08fb650f9f46dbd3e@65.108.201.167:26656,897c55fb33076c9cecc56f6c04e2a3cbed195e7c@185.248.24.20:26796,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656,a8f9cedd64e5fb2dc019061985afe8c34fd5efcb@141.94.251.25:26656,afc247bceddc0eeeb6cf62db6fb4f985b03dd3b0@95.214.53.191:26656,a430d40d7c4272a649b8309abed412f562057539@3.37.223.124:26656,8362a432d50cc800618de6a76cc92d532baa8fa4@173.212.247.202:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
