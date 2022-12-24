# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/kujira.png" width="150" alt=""><figcaption></figcaption></figure>

Kujira is a Layer 1 protocol built on Cosmos, which can be used for  hosting community-selected projects.

**Chain ID**: kaiyo-1 | **Latest Version Tag**: v0.7.1 | **Wasm**: ON

[Website](https://kujira.app) | [Discord](https://discord.gg/teamkujira) | [Twitter](https://twitter.com/TeamKujira)

## Restake

[Restake with kjnodes](https://restake.app/kujira/kujiravaloper1tnuqj73jfn3724lqz34c27tuv80nv336sadqym) (every day at 08:00, 20:00)
## Public endpoints

* rpc: [https://kujira.rpc.kjnodes.com](https://kujira.rpc.kjnodes.com)
* api: [https://kujira.api.kjnodes.com](https://kujira.api.kjnodes.com)

## Peering

**state-sync**

```
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@kujira.rpc.kjnodes.com:13656
```

**seed-node**

```
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@kujira.rpc.kjnodes.com:13659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/kujira/addrbook.json > $HOME/.kujira/config/addrbook.json
```

**live-peers** (10)
```
peers="d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656,b29969a2384159db8f8052bc118066bd067157c4@85.215.105.19:15602,213dbb8301ce1c0f5662a9b723bd613f15e1dd4e@75.119.157.167:30656,6cf8b25d99bacca213c1d762e8d9ea21636fea41@178.211.139.222:26656,ffac364ae5a9a730b49f02ba95b11878f76b7043@135.125.189.131:31095,129771a48f43b83c6144c7d282ad1da62434cc07@15.204.197.12:26656,0cb9d54761ca14006daad4442378f2a1335de6ad@65.21.121.118:26656,0c7da38c54e1a7d8ab7d48601b51847564ce019e@5.161.91.34:45656,b80cf7882c8cab4894d41ccd4f5a00406d8b5f7d@146.59.52.48:30095,bd2821b2dc8b928946026caf3e9bd1e7a0013a61@145.239.10.46:13656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.kujira/config/config.toml
```
