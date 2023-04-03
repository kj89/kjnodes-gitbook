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

**live-peers** (14)
```bash
peers="01d708d4124f30700c05c97947ae10231d8755f7@95.217.197.100:26655,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.169.213:26656,c55d35ef908b74c2ddec2f47dbdb4032d7dfbcd4@23.88.69.22:27266,471518432477e31ea348af246c0b54095d41352c@88.198.131.126:26656,ecafd5cadaf3526a588550a7bc343ce2670c988d@185.16.39.231:26656,8a210f1bcfc9015a7bc18dcc5add29c0dce3f2dc@95.217.70.62:26656,3457c7c0ff7c368c35f0d574a289d5ef77b504b7@65.108.9.164:10656,4a87e847c8fc15812e4d8ce57c43581ab0e7a4dd@95.214.55.100:26256,fdde823fb8c9ef908d4b229f177c5f8b18e90274@54.235.174.123:26656,177872437b2a31ebb0fb740ba5bd32b0be99e280@5.79.74.229:31095,09076c7908db88316498cf4cd4702a8d269e0da9@15.235.114.85:26656,a9ed3a9256cbabe889b2989ad99a3e7e173c3ffe@108.165.178.242:26655,dd1f96b91053c8d89b1c65d92eebf7ad64c76add@65.21.200.164:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
