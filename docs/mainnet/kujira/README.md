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

**live-peers** (19)
```bash
peers="4ae125f9c9b8e2f1ac83749c2209e26056b97851@65.108.238.103:11856,b12591db8b67f7a78b2834b5c122299fdb6c8deb@65.108.201.154:2060,ffac364ae5a9a730b49f02ba95b11878f76b7043@135.125.189.131:31095,eb9742d81b436b95e324816794229a9efdaf8ea8@142.132.155.170:26656,9dc8a19299064e8d5a414a1fc25dd0d12d9871c8@138.201.16.240:30095,04b384fd77f70082a9a6e4d8fb3db827340f4e74@148.251.13.186:11856,26d19e5b3f3a5ebafe827dabca4ef008d9c5e6fd@168.119.15.94:26656,b8d3a5e5d43d8e18c4ecfd56a8ca46dc3b91bc32@107.181.231.178:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656,b29969a2384159db8f8052bc118066bd067157c4@85.215.105.19:15602,3a7733d4b670a672db326bd6e5f8ae37e14a3dbd@138.201.226.227:26656,fa57c7c253be46ad9f696ee2f2c1d72cbc6a1591@146.59.52.135:31095,d2247f7b919f0781c90ee61958d7044665a22d38@169.155.169.182:26656,01cf570d3b08fdb5fe2f307cb485de7a35a3af23@135.148.55.229:11856,253d2293272a29057a27797a5703f5171c267da1@192.99.15.159:26656,c55d35ef908b74c2ddec2f47dbdb4032d7dfbcd4@23.88.69.22:27266,6212f700687500f96ef56af3488e99fc4b009e19@212.68.34.95:26656,da2673cf09dc2c124947827f4cf5e7c17114d504@142.132.202.98:26656,ed71d6328a0228cd2eac7d71451509813c660b5d@116.202.164.206:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
