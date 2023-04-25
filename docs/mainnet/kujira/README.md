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

**live-peers** (30)
```bash
peers="177872437b2a31ebb0fb740ba5bd32b0be99e280@5.79.74.229:31095,3d150f6a71caca5607daff69c9049c04c37da64e@51.210.223.186:30095,b29969a2384159db8f8052bc118066bd067157c4@85.215.105.19:15602,ff7a1787ea93a49ece2ee92f601a4c52951278c4@185.119.118.112:2000,c62e0701155a690616fcd3a57fa2fda444840561@65.108.76.242:32095,da2673cf09dc2c124947827f4cf5e7c17114d504@142.132.202.98:26656,94da43cae2bc6e9d16decfe3d78c64603f5ad9e2@192.118.76.122:26616,89757803f40da51678451735445ad40d5b15e059@169.155.45.187:26656,d6f2eee997d108d4fde5683e31d678427376dfce@77.68.27.75:26656,66c551ebcb68fe343c7e2720593dc47426813a68@93.189.30.101:26656,ccb4fffc9caa2f0d8da833f3cad906b833320bab@51.222.254.98:26656,c8b74590ce04f0f7c32b1c668290e00ec7ec275e@148.113.8.63:11856,79ace78a1fb98876c7bcbf8ec54864b740aa76ff@65.108.128.201:11856,3a15fa46fe0a27d4ee60497a470a8c91911a9e5e@15.235.66.89:11756,0cd7caa189ab5e3fb19b4d32516027b578ab7838@45.79.118.43:26656,1cbc1bff7cdaeffd5a25583f9525f44fb55f7215@95.214.54.28:26156,cedf10f69de7d77b358964a1b802a15ad79a7c97@74.80.183.130:26655,55d5419822feeab727b2be57e834534cbd91d6a4@65.108.69.91:26656,4c54a10004045c74ae65e57de7ed7126d8481549@95.216.46.251:26656,b8d3a5e5d43d8e18c4ecfd56a8ca46dc3b91bc32@107.181.231.178:26656,030f65339defb01b0e3ddaeaa54cbeac00dd0c74@185.182.193.89:26656,a9ed3a9256cbabe889b2989ad99a3e7e173c3ffe@108.165.178.242:26655,9dc8a19299064e8d5a414a1fc25dd0d12d9871c8@138.201.16.240:30095,fa925ef53799d2cf30b317ac52759871909b151c@44.206.174.98:26656,ecafd5cadaf3526a588550a7bc343ce2670c988d@185.16.39.231:26656,52739251216bd8e7d17ac69810f83bf58a7b1b10@47.144.18.69:26656,f62a0842be95a33b191879c977eed2072e37926b@57.128.20.147:30256,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656,ffac364ae5a9a730b49f02ba95b11878f76b7043@135.125.189.131:31095,ab587b4bf216c348657ed3dde85d1f48c5ad279c@15.235.115.155:10004"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
