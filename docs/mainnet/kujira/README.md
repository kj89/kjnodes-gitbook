# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/kujira.png" width="150" alt=""><figcaption></figcaption></figure>

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
peers="4ae125f9c9b8e2f1ac83749c2209e26056b97851@65.108.238.103:11856,7c26c34148779b1d0979eb069dbe354752a3644f@5.9.84.213:25656,bd2821b2dc8b928946026caf3e9bd1e7a0013a61@145.239.10.46:13656,ecafd5cadaf3526a588550a7bc343ce2670c988d@185.16.39.231:26656,9dc8a19299064e8d5a414a1fc25dd0d12d9871c8@138.201.16.240:30095,780ee91b43bcdced2daebee61996742f6b01b579@138.201.197.119:2000,1d85c9f16727584753db78b5b54eedf0ce8de3ed@51.159.16.49:5060,a9ed3a9256cbabe889b2989ad99a3e7e173c3ffe@108.165.178.242:26655,b29969a2384159db8f8052bc118066bd067157c4@85.215.105.19:15602,fc593f5f9fcf7f88790bd8274ebc791f612d3efe@65.21.89.54:26655,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656,beb3329e969ae64d97c276f0ed0a1773ebdf61dc@146.19.24.142:26656,fa57c7c253be46ad9f696ee2f2c1d72cbc6a1591@146.59.52.135:31095,177872437b2a31ebb0fb740ba5bd32b0be99e280@5.79.74.229:31095,2544287899424decd29c659445578a579a500ab2@85.10.200.231:31095,66c551ebcb68fe343c7e2720593dc47426813a68@93.189.30.101:26656,129771a48f43b83c6144c7d282ad1da62434cc07@15.204.197.12:26656,3d150f6a71caca5607daff69c9049c04c37da64e@51.210.223.186:30095"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
