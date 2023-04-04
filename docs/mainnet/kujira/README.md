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
peers="1fb8ef552bf812a15d0d81ffbc8a3eb77b4319e6@65.21.231.176:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.169.213:26656,1d6fceb2a8182e9b91d105053dbe03bc9248bcd0@89.163.146.22:26656,e250c12df7aa910e9950e162df6b6e8ef210c8da@44.206.174.98:26656,ecafd5cadaf3526a588550a7bc343ce2670c988d@185.16.39.231:26656,da2673cf09dc2c124947827f4cf5e7c17114d504@142.132.202.98:26656,79ace78a1fb98876c7bcbf8ec54864b740aa76ff@65.108.128.201:11856,8362a432d50cc800618de6a76cc92d532baa8fa4@173.212.247.202:26656,213dbb8301ce1c0f5662a9b723bd613f15e1dd4e@75.119.157.167:30656,177872437b2a31ebb0fb740ba5bd32b0be99e280@5.79.74.229:31095,1d436f8d9a36e7d93d897012dd4e98871e8c4fbb@65.108.137.37:26656,e81c56107cc4506c1d6645cbe64f115beaccef26@34.173.154.254:26656,6cceba286b498d4a1931f85e35ea0fa433373057@88.198.128.174:26656,d6f2eee997d108d4fde5683e31d678427376dfce@77.68.27.75:26656,2300d8048f91762a1f8f93667e4c09b56b7d192f@20.171.51.39:26656,eb9742d81b436b95e324816794229a9efdaf8ea8@142.132.155.170:26656,fb5b72024981de8ea392876c8409fe60a439d699@54.235.174.123:26656,3a15fa46fe0a27d4ee60497a470a8c91911a9e5e@15.235.66.89:11756,4db916788d45d5454cfe7a68ca02c56996ee6b96@194.163.151.124:26656,57719ff9d3ceac462735fc2eeb1fd1a80c7a3f82@52.171.141.233:26656,a430d40d7c4272a649b8309abed412f562057539@3.37.223.124:26656,75cd9d2f96a352eb429e166e69b45cb1dfb99d06@65.108.200.49:9556,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656,8e4fe99c78d3f01087e8856b95817f24ba4238b1@31.156.88.34:26656,e751b31b5444ed4a7489a456be805c736756eeb8@195.3.223.19:26656,de08e6178779ff3b19a8b6d22a05664392cb2b35@185.216.179.205:26656,2076be2d3d4d1e4da9ba33b1a365bfcc14eb46c3@216.158.230.242:26786,a9ed3a9256cbabe889b2989ad99a3e7e173c3ffe@108.165.178.242:26655,c6eaf84ee15c3f311236b19f5de2c231d96e5ac4@95.217.209.187:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
