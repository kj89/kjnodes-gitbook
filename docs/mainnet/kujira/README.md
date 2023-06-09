# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/kujira.png" alt=""><figcaption></figcaption></figure>

Kujira is a Layer 1 protocol built on Cosmos, which can be used for  hosting community-selected projects.

**Chain ID**: kaiyo-1 | **Latest Version Tag**: v0.8.7 | **Wasm**: ON

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

**live-peers** (10)
```bash
peers="1d85c9f16727584753db78b5b54eedf0ce8de3ed@51.159.16.49:5060,1cbc1bff7cdaeffd5a25583f9525f44fb55f7215@95.214.54.28:26156,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:11356,ab587b4bf216c348657ed3dde85d1f48c5ad279c@15.235.115.155:10004,012b9888db14d1c4cc8f08320ce1921e22fcc329@65.109.33.48:18656,d02fc7c5db5e502bb78ceeb81067ddab5b0cf51a@89.39.104.128:13656,4fb4e8c78692a7ed9b4d76f0f50129f17358484a@51.81.66.123:11856,a430d40d7c4272a649b8309abed412f562057539@3.37.223.124:26656,e8f53eab61a5cb9f2c3460c739080ee86f2b80cc@13.40.82.236:26656,b802fbfb83d6400639f17f2883f30a46ee6b05ad@51.210.223.185:32095"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
