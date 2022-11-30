# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/kujira.png" width="150" alt=""><figcaption></figcaption></figure>

Kujira is a Layer 1 protocol built on Cosmos, which can be used for  hosting community-selected projects.

**Chain ID**: kaiyo-1 | **Latest Version Tag**: v0.7.1 | **Wasm**: ON

Website: [https://kujira.app](https://kujira.app)

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

**live-peers** (9)
```
peers="4c22af952c3af002136397d48f9933d0432ace7a@148.251.79.204:26656,d6f2eee997d108d4fde5683e31d678427376dfce@77.68.27.75:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656,eb9742d81b436b95e324816794229a9efdaf8ea8@142.132.155.170:26656,bbd504c2ab489671b948faab56f309c764fb23bb@65.108.108.179:9556,66778cba932969c95117cf720c1ad820fdc68ff5@65.108.235.34:26656,e751b31b5444ed4a7489a456be805c736756eeb8@195.3.223.19:26656,10b5feb3036147e31991964ddbf5610393716f6b@66.172.36.139:11256,2657f7bd2fd2a56ccebeb47f08754ff18e7860c6@176.9.125.13:5060"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.kujira/config/config.toml
```
