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

**live-peers** (20)
```bash
peers="9c753f4e99433b79b0b7dce69fffa0a892491f95@65.108.234.154:26656,780ee91b43bcdced2daebee61996742f6b01b579@138.201.197.119:2000,9dc8a19299064e8d5a414a1fc25dd0d12d9871c8@138.201.16.240:30095,bd2821b2dc8b928946026caf3e9bd1e7a0013a61@145.239.10.46:13656,177872437b2a31ebb0fb740ba5bd32b0be99e280@5.79.74.229:31095,b29969a2384159db8f8052bc118066bd067157c4@85.215.105.19:15602,8d59c2958dfb2f852b201cbaa60743c771ce338b@147.135.45.32:26656,129771a48f43b83c6144c7d282ad1da62434cc07@15.204.197.12:26656,8a210f1bcfc9015a7bc18dcc5add29c0dce3f2dc@95.217.70.62:26656,b12591db8b67f7a78b2834b5c122299fdb6c8deb@65.108.201.154:2060,ff7a1787ea93a49ece2ee92f601a4c52951278c4@185.119.118.112:2000,97e4468ac589eac505a800411c635b14511a61bb@5.9.239.238:26656,b80cf7882c8cab4894d41ccd4f5a00406d8b5f7d@146.59.52.48:30095,d3427d444b6909529d73025fe32a73dfea7b90d1@148.251.85.115:26656,471518432477e31ea348af246c0b54095d41352c@88.198.131.126:26656,fa57c7c253be46ad9f696ee2f2c1d72cbc6a1591@146.59.52.135:31095,3a7733d4b670a672db326bd6e5f8ae37e14a3dbd@138.201.226.227:26656,d02fc7c5db5e502bb78ceeb81067ddab5b0cf51a@89.39.104.128:13656,2544287899424decd29c659445578a579a500ab2@85.10.200.231:31095,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
