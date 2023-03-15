# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/kujira.png" width="150" alt=""><figcaption></figcaption></figure>

Kujira is a Layer 1 protocol built on Cosmos, which can be used for  hosting community-selected projects.

**Chain ID**: kaiyo-1 | **Latest Version Tag**: v0.7.1 | **Wasm**: ON

[Website](https://kujira.app) | [Discord](https://discord.gg/teamkujira) | [Twitter](https://twitter.com/TeamKujira)

[![Stake with kjnodes](https://i.ibb.co/cr44Q8j/button-stake-with-kjnodes.png)](https://restake.app/kujira/kujiravaloper1tnuqj73jfn3724lqz34c27tuv80nv336sadqym)

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
peers="c62e0701155a690616fcd3a57fa2fda444840561@65.108.76.242:32095,471518432477e31ea348af246c0b54095d41352c@88.198.131.126:26656,4db916788d45d5454cfe7a68ca02c56996ee6b96@194.163.151.124:26656,780ee91b43bcdced2daebee61996742f6b01b579@138.201.197.119:2000,e751b31b5444ed4a7489a456be805c736756eeb8@195.3.223.19:26656,fa57c7c253be46ad9f696ee2f2c1d72cbc6a1591@146.59.52.135:31095,01d708d4124f30700c05c97947ae10231d8755f7@95.217.197.100:26655,9dc8a19299064e8d5a414a1fc25dd0d12d9871c8@138.201.16.240:30095,213dbb8301ce1c0f5662a9b723bd613f15e1dd4e@75.119.157.167:30656,253d2293272a29057a27797a5703f5171c267da1@192.99.15.159:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.169.213:26656,ffac364ae5a9a730b49f02ba95b11878f76b7043@135.125.189.131:31095,d6f2eee997d108d4fde5683e31d678427376dfce@77.68.27.75:26656,0743497e30049ac8d59fee5b2ab3a49c3824b95c@198.244.200.196:26656,0c2e37714b7922b160bce8579eeb444e59802efa@65.108.198.118:11856,a7e7864f241db457f38d8e5b5b3c3de989dea2fe@66.94.126.62:26656,bd2821b2dc8b928946026caf3e9bd1e7a0013a61@145.239.10.46:13656,a9ed3a9256cbabe889b2989ad99a3e7e173c3ffe@108.165.178.242:26655,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
