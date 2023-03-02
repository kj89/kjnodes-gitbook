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

**live-peers** (19)
```bash
peers="82588f011491c6100d922d133f52fc23460b9231@95.217.91.238:26656,da2673cf09dc2c124947827f4cf5e7c17114d504@142.132.202.98:26656,15679999b404a9ee027dc9f5e795d6c4fddb6cee@51.91.152.102:20000,66c551ebcb68fe343c7e2720593dc47426813a68@93.189.30.101:26656,bd2821b2dc8b928946026caf3e9bd1e7a0013a61@145.239.10.46:13656,beb3329e969ae64d97c276f0ed0a1773ebdf61dc@146.19.24.142:26656,6f3129d01218b939511cccf7e0318bfe872d97c4@65.109.33.181:26656,b29969a2384159db8f8052bc118066bd067157c4@85.215.105.19:15602,a7d96dc929824613315dcc1c90fee119f28cc51f@134.65.193.158:26656,98a6a264d2f2f5093d317f09e71036e62aa73906@107.181.235.66:20656,4018be5af4189573366762fa168826b4408418db@135.125.188.17:32095,0c2e37714b7922b160bce8579eeb444e59802efa@65.108.198.118:11856,fa57c7c253be46ad9f696ee2f2c1d72cbc6a1591@146.59.52.135:31095,ecafd5cadaf3526a588550a7bc343ce2670c988d@185.16.39.231:26656,dd1f96b91053c8d89b1c65d92eebf7ad64c76add@65.21.200.164:26656,413bd0410b649de5070b2fe8356cad356459dc37@65.108.235.165:26656,bba10290da32f3cb41e15c3a192413666ce05cee@5.9.208.14:26656,780ee91b43bcdced2daebee61996742f6b01b579@138.201.197.119:2000,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
