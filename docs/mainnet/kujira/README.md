# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/kujira.png" alt=""><figcaption></figcaption></figure>

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
* grpc: kujira.grpc.kjnodes.com:11390

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@kujira.rpc.kjnodes.com:11356
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@kujira.rpc.kjnodes.com:11359
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/kujira/addrbook.json > $HOME/.kujira/config/addrbook.json
```

**live-peers** (11)
```bash
peers="a7d96dc929824613315dcc1c90fee119f28cc51f@134.65.193.158:26656,b29969a2384159db8f8052bc118066bd067157c4@85.215.105.19:15602,94da43cae2bc6e9d16decfe3d78c64603f5ad9e2@192.118.76.122:26616,c8b74590ce04f0f7c32b1c668290e00ec7ec275e@148.113.8.63:11856,6212f700687500f96ef56af3488e99fc4b009e19@212.68.34.95:26656,d6f2eee997d108d4fde5683e31d678427376dfce@77.68.27.75:26656,58fc044463399f5c2d94a39e3474ea6196dab0bd@65.108.198.118:11856,2e3c72b0b6f3007a109e78864e22661dd7071c06@38.242.130.118:26656,a76e18bffe05fb1332dcd4340fc6e2b482ed38fb@195.3.222.246:26656,b12591db8b67f7a78b2834b5c122299fdb6c8deb@65.108.201.154:2060,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:11356"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
