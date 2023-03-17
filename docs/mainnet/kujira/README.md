# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/kujira.png" width="150" alt=""><figcaption></figcaption></figure>

Kujira is a Layer 1 protocol built on Cosmos, which can be used for  hosting community-selected projects.

**Chain ID**: kaiyo-1 | **Latest Version Tag**: v0.7.1 | **Wasm**: ON

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

**live-peers** (19)
```bash
peers="c62e0701155a690616fcd3a57fa2fda444840561@65.108.76.242:32095,d6f2eee997d108d4fde5683e31d678427376dfce@77.68.27.75:26656,780ee91b43bcdced2daebee61996742f6b01b579@138.201.197.119:2000,ecafd5cadaf3526a588550a7bc343ce2670c988d@185.16.39.231:26656,e751b31b5444ed4a7489a456be805c736756eeb8@195.3.223.19:26656,b690b0e6a904fc0172ef1eccc07bea9f48f4e454@141.94.73.39:53756,fa57c7c253be46ad9f696ee2f2c1d72cbc6a1591@146.59.52.135:31095,9c8826ceeb1254d16856092a50df4fd720910362@50.116.49.237:26656,da2673cf09dc2c124947827f4cf5e7c17114d504@142.132.202.98:26656,4db916788d45d5454cfe7a68ca02c56996ee6b96@194.163.151.124:26656,c124ce0b508e8b9ed1c5b6957f362225659b5343@136.243.248.190:26656,b802fbfb83d6400639f17f2883f30a46ee6b05ad@51.210.223.185:32095,a7e7864f241db457f38d8e5b5b3c3de989dea2fe@66.94.126.62:26656,8d59c2958dfb2f852b201cbaa60743c771ce338b@147.135.45.32:26656,d3427d444b6909529d73025fe32a73dfea7b90d1@148.251.85.115:26656,3d150f6a71caca5607daff69c9049c04c37da64e@51.210.223.186:30095,3a7733d4b670a672db326bd6e5f8ae37e14a3dbd@138.201.226.227:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656,4af5ea231c2fe1ca8174fb627e65bc09564f313b@45.143.196.110:11856"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
