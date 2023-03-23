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

**live-peers** (19)
```bash
peers="ccffabe81f2de8a81e171f93fe1209392bf9993f@65.108.234.59:26656,6f3129d01218b939511cccf7e0318bfe872d97c4@65.109.33.181:26656,8e4e1f1e087c76c71c64e477e95495833da82aa2@95.217.65.54:26656,4018be5af4189573366762fa168826b4408418db@135.125.188.17:32095,780ee91b43bcdced2daebee61996742f6b01b579@138.201.197.119:2000,3a7733d4b670a672db326bd6e5f8ae37e14a3dbd@138.201.226.227:26656,471518432477e31ea348af246c0b54095d41352c@88.198.131.126:26656,66c551ebcb68fe343c7e2720593dc47426813a68@93.189.30.101:26656,fa57c7c253be46ad9f696ee2f2c1d72cbc6a1591@146.59.52.135:31095,0c7da38c54e1a7d8ab7d48601b51847564ce019e@5.161.91.34:45656,de08e6178779ff3b19a8b6d22a05664392cb2b35@185.216.179.205:26656,b29969a2384159db8f8052bc118066bd067157c4@85.215.105.19:15602,a7e7864f241db457f38d8e5b5b3c3de989dea2fe@66.94.126.62:26656,177872437b2a31ebb0fb740ba5bd32b0be99e280@5.79.74.229:31095,89757803f40da51678451735445ad40d5b15e059@169.155.45.187:26656,d2247f7b919f0781c90ee61958d7044665a22d38@169.155.169.182:26656,79ace78a1fb98876c7bcbf8ec54864b740aa76ff@65.108.128.201:11856,7c26c34148779b1d0979eb069dbe354752a3644f@5.9.84.213:25656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
