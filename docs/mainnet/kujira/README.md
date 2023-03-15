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
peers="c62e0701155a690616fcd3a57fa2fda444840561@65.108.76.242:32095,bd2821b2dc8b928946026caf3e9bd1e7a0013a61@145.239.10.46:13656,da2673cf09dc2c124947827f4cf5e7c17114d504@142.132.202.98:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656,a7e7864f241db457f38d8e5b5b3c3de989dea2fe@66.94.126.62:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.169.213:26656,a7d96dc929824613315dcc1c90fee119f28cc51f@134.65.193.158:26656,471518432477e31ea348af246c0b54095d41352c@88.198.131.126:26656,3d150f6a71caca5607daff69c9049c04c37da64e@51.210.223.186:30095,b80cf7882c8cab4894d41ccd4f5a00406d8b5f7d@146.59.52.48:30095,0c2e37714b7922b160bce8579eeb444e59802efa@65.108.198.118:11856,c124ce0b508e8b9ed1c5b6957f362225659b5343@136.243.248.190:26656,177872437b2a31ebb0fb740ba5bd32b0be99e280@5.79.74.229:31095,4db916788d45d5454cfe7a68ca02c56996ee6b96@194.163.151.124:26656,01cf570d3b08fdb5fe2f307cb485de7a35a3af23@135.148.55.229:11856,d2247f7b919f0781c90ee61958d7044665a22d38@169.155.169.182:26656,1a781f294b8c30ab0b4e54494359263e9b389ebb@141.94.219.133:11756,ffac364ae5a9a730b49f02ba95b11878f76b7043@135.125.189.131:31095"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
