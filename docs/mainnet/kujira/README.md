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
* grpc: [https://kujira.grpc.kjnodes.com](https://kujira.grpc.kjnodes.com)

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

**live-peers** (18)
```bash
peers="b12591db8b67f7a78b2834b5c122299fdb6c8deb@65.108.201.154:2060,eb9742d81b436b95e324816794229a9efdaf8ea8@142.132.155.170:26656,3a7733d4b670a672db326bd6e5f8ae37e14a3dbd@138.201.226.227:26656,da2673cf09dc2c124947827f4cf5e7c17114d504@142.132.202.98:26656,66c551ebcb68fe343c7e2720593dc47426813a68@93.189.30.101:26656,b80cf7882c8cab4894d41ccd4f5a00406d8b5f7d@146.59.52.48:30095,15679999b404a9ee027dc9f5e795d6c4fddb6cee@51.91.152.102:20000,e751b31b5444ed4a7489a456be805c736756eeb8@195.3.223.19:26656,0c2e37714b7922b160bce8579eeb444e59802efa@65.108.198.118:11856,fa57c7c253be46ad9f696ee2f2c1d72cbc6a1591@146.59.52.135:31095,253d2293272a29057a27797a5703f5171c267da1@192.99.15.159:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656,9dc8a19299064e8d5a414a1fc25dd0d12d9871c8@138.201.16.240:30095,9c8826ceeb1254d16856092a50df4fd720910362@50.116.49.237:26656,d6f2eee997d108d4fde5683e31d678427376dfce@77.68.27.75:26656,c55d35ef908b74c2ddec2f47dbdb4032d7dfbcd4@23.88.69.22:27266,6cf8b25d99bacca213c1d762e8d9ea21636fea41@178.211.139.222:26656,4ae125f9c9b8e2f1ac83749c2209e26056b97851@65.108.238.103:11856"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
