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

**live-peers** (16)
```bash
peers="bd2821b2dc8b928946026caf3e9bd1e7a0013a61@145.239.10.46:13656,b80cf7882c8cab4894d41ccd4f5a00406d8b5f7d@146.59.52.48:30095,9dc8a19299064e8d5a414a1fc25dd0d12d9871c8@138.201.16.240:30095,ecafd5cadaf3526a588550a7bc343ce2670c988d@185.16.39.231:26656,89757803f40da51678451735445ad40d5b15e059@169.155.45.187:26656,b12591db8b67f7a78b2834b5c122299fdb6c8deb@65.108.201.154:2060,129771a48f43b83c6144c7d282ad1da62434cc07@15.204.197.12:26656,ffac364ae5a9a730b49f02ba95b11878f76b7043@135.125.189.131:31095,d3427d444b6909529d73025fe32a73dfea7b90d1@148.251.85.115:26656,3457c7c0ff7c368c35f0d574a289d5ef77b504b7@65.108.9.164:10656,63e9da22c656da3e80f12e586c058da40521f424@172.176.188.81:26656,fdde823fb8c9ef908d4b229f177c5f8b18e90274@54.235.174.123:26656,8362a432d50cc800618de6a76cc92d532baa8fa4@173.212.247.202:26656,52739251216bd8e7d17ac69810f83bf58a7b1b10@47.144.5.20:26656,75cd9d2f96a352eb429e166e69b45cb1dfb99d06@65.108.200.49:9556,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
