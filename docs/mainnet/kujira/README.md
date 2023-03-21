# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/kujira.png" width="150" alt=""><figcaption></figcaption></figure>

Kujira is a Layer 1 protocol built on Cosmos, which can be used for  hosting community-selected projects.

**Chain ID**: kaiyo-1 | **Latest Version Tag**: v0.8.4 | **Wasm**: ON

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

**live-peers** (20)
```bash
peers="66c551ebcb68fe343c7e2720593dc47426813a68@93.189.30.101:26656,d6d14f99ef25c8ffee6fa4afca40fece0c1ab9fe@107.181.229.154:20656,177872437b2a31ebb0fb740ba5bd32b0be99e280@5.79.74.229:31095,ecafd5cadaf3526a588550a7bc343ce2670c988d@185.16.39.231:26656,fa57c7c253be46ad9f696ee2f2c1d72cbc6a1591@146.59.52.135:31095,780ee91b43bcdced2daebee61996742f6b01b579@138.201.197.119:2000,b802fbfb83d6400639f17f2883f30a46ee6b05ad@51.210.223.185:32095,89757803f40da51678451735445ad40d5b15e059@169.155.45.187:26656,9dc8a19299064e8d5a414a1fc25dd0d12d9871c8@138.201.16.240:30095,e751b31b5444ed4a7489a456be805c736756eeb8@195.3.223.19:26656,8d59c2958dfb2f852b201cbaa60743c771ce338b@147.135.45.32:26656,a7e7864f241db457f38d8e5b5b3c3de989dea2fe@66.94.126.62:26656,129771a48f43b83c6144c7d282ad1da62434cc07@15.204.197.12:26656,413bd0410b649de5070b2fe8356cad356459dc37@65.108.235.165:26656,f2fe529a8d41ce4beffccb2e00342e74df9ebeca@78.31.71.246:26656,4ae125f9c9b8e2f1ac83749c2209e26056b97851@65.108.238.103:11856,b8e8c1738a49cd6143cf83287a5087c2618ebca0@141.95.47.82:30256,1cbc1bff7cdaeffd5a25583f9525f44fb55f7215@95.214.54.28:26156,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656,c62e0701155a690616fcd3a57fa2fda444840561@65.108.76.242:32095"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
