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

**live-peers** (20)
```bash
peers="9c8826ceeb1254d16856092a50df4fd720910362@50.116.49.237:26656,da2673cf09dc2c124947827f4cf5e7c17114d504@142.132.202.98:26656,4db916788d45d5454cfe7a68ca02c56996ee6b96@194.163.151.124:26656,2544287899424decd29c659445578a579a500ab2@85.10.200.231:31095,b80cf7882c8cab4894d41ccd4f5a00406d8b5f7d@146.59.52.48:30095,471518432477e31ea348af246c0b54095d41352c@88.198.131.126:26656,15679999b404a9ee027dc9f5e795d6c4fddb6cee@51.91.152.102:20000,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.169.213:26656,cedf10f69de7d77b358964a1b802a15ad79a7c97@74.80.183.130:26655,ffac364ae5a9a730b49f02ba95b11878f76b7043@135.125.189.131:31095,38e36150df914ec2c9fbaf378ab0e73ada4a3987@95.216.6.111:26656,a9ed3a9256cbabe889b2989ad99a3e7e173c3ffe@108.165.178.242:26655,d6f2eee997d108d4fde5683e31d678427376dfce@77.68.27.75:26656,3a7733d4b670a672db326bd6e5f8ae37e14a3dbd@138.201.226.227:26656,780ee91b43bcdced2daebee61996742f6b01b579@138.201.197.119:2000,66c551ebcb68fe343c7e2720593dc47426813a68@93.189.30.101:26656,eb9742d81b436b95e324816794229a9efdaf8ea8@142.132.155.170:26656,a7e7864f241db457f38d8e5b5b3c3de989dea2fe@66.94.126.62:26656,c62e0701155a690616fcd3a57fa2fda444840561@65.108.76.242:32095,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
