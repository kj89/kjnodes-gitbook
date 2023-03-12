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

**live-peers** (17)
```bash
peers="b12591db8b67f7a78b2834b5c122299fdb6c8deb@65.108.201.154:2060,c62e0701155a690616fcd3a57fa2fda444840561@65.108.76.242:32095,9dc8a19299064e8d5a414a1fc25dd0d12d9871c8@138.201.16.240:30095,6cf8b25d99bacca213c1d762e8d9ea21636fea41@178.211.139.222:26656,66c551ebcb68fe343c7e2720593dc47426813a68@93.189.30.101:26656,d6f2eee997d108d4fde5683e31d678427376dfce@77.68.27.75:26656,f62a0842be95a33b191879c977eed2072e37926b@57.128.20.147:30256,fa57c7c253be46ad9f696ee2f2c1d72cbc6a1591@146.59.52.135:31095,a7e7864f241db457f38d8e5b5b3c3de989dea2fe@66.94.126.62:26656,b8e8c1738a49cd6143cf83287a5087c2618ebca0@141.95.47.82:30256,8df276d9873c0ab16a911c5f779caa6f121c845e@89.163.145.138:26656,3a7733d4b670a672db326bd6e5f8ae37e14a3dbd@138.201.226.227:26656,2544287899424decd29c659445578a579a500ab2@85.10.200.231:31095,129771a48f43b83c6144c7d282ad1da62434cc07@15.204.197.12:26656,253d2293272a29057a27797a5703f5171c267da1@192.99.15.159:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.169.213:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
