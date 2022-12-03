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
peers="94469c0d109e00e65d62a307f7ab3dc109c01055@65.108.238.104:11856,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656,bbd504c2ab489671b948faab56f309c764fb23bb@65.108.108.179:9556,e751b31b5444ed4a7489a456be805c736756eeb8@195.3.223.19:26656,177872437b2a31ebb0fb740ba5bd32b0be99e280@5.79.74.229:31095,0a03f5dfb5b995647808c4d100e7b98d0526302f@85.214.18.167:26656,935c1065ad23338a5e6a75f08fb650f9f46dbd3e@65.108.201.167:26656,9c753f4e99433b79b0b7dce69fffa0a892491f95@65.108.234.154:26656,10b5feb3036147e31991964ddbf5610393716f6b@66.172.36.139:11256"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.kujira/config/config.toml
```
