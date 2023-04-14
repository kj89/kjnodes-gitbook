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
peers="177872437b2a31ebb0fb740ba5bd32b0be99e280@5.79.74.229:31095,89757803f40da51678451735445ad40d5b15e059@169.155.45.187:26656,de08e6178779ff3b19a8b6d22a05664392cb2b35@185.216.179.205:26656,1cbc1bff7cdaeffd5a25583f9525f44fb55f7215@95.214.54.28:26156,1d6fceb2a8182e9b91d105053dbe03bc9248bcd0@89.163.146.22:26656,b29969a2384159db8f8052bc118066bd067157c4@85.215.105.19:15602,7f83a8f94bddb377ff195b3c9ee2abc91ddf0433@51.81.242.74:26656,213dbb8301ce1c0f5662a9b723bd613f15e1dd4e@75.119.157.167:30656,ecafd5cadaf3526a588550a7bc343ce2670c988d@185.16.39.231:26656,a7e7864f241db457f38d8e5b5b3c3de989dea2fe@66.94.126.62:26656,fa925ef53799d2cf30b317ac52759871909b151c@44.206.174.98:26656,030f65339defb01b0e3ddaeaa54cbeac00dd0c74@185.182.193.89:26656,861f4624276d80aa538ad446ce608910ca24940d@148.251.177.45:11656,79ace78a1fb98876c7bcbf8ec54864b740aa76ff@65.108.128.201:11856,fdde823fb8c9ef908d4b229f177c5f8b18e90274@54.235.174.123:26656,09076c7908db88316498cf4cd4702a8d269e0da9@15.235.114.85:26656,c55d35ef908b74c2ddec2f47dbdb4032d7dfbcd4@23.88.69.22:27266,6cceba286b498d4a1931f85e35ea0fa433373057@88.198.128.174:26656,0cd7caa189ab5e3fb19b4d32516027b578ab7838@45.79.118.43:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656,52739251216bd8e7d17ac69810f83bf58a7b1b10@47.144.5.20:26656,e751b31b5444ed4a7489a456be805c736756eeb8@195.3.223.19:26656,a430d40d7c4272a649b8309abed412f562057539@3.37.223.124:26656,da2673cf09dc2c124947827f4cf5e7c17114d504@142.132.202.98:26656,66f1214484eaf4c28b8bbd1cad49a2eeba86a19d@40.84.170.51:26656,01d708d4124f30700c05c97947ae10231d8755f7@95.217.197.100:26655,248ce6171230cddb4b6a5f14591e2de345e14bbd@54.151.138.189:26656,1d436f8d9a36e7d93d897012dd4e98871e8c4fbb@65.108.137.37:26656,ebc272824924ea1a27ea3183dd0b9ba713494f83@178.211.139.77:26796"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
