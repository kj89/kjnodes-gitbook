# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/kujira.png" width="150" alt=""><figcaption></figcaption></figure>

Kujira is a Layer 1 protocol built on Cosmos, which can be used for  hosting community-selected projects.

**Chain ID**: kaiyo-1 | **Latest Version Tag**: v0.6.4 | **Wasm**: ON

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
peers="f9509ef83ecce9433e3bc9de8a0abf6e00912b0e@173.212.247.202:26656,1048e73299d435b6598245d246562efc62df002d@65.108.128.201:11856,fa57c7c253be46ad9f696ee2f2c1d72cbc6a1591@146.59.52.135:31095,beb3329e969ae64d97c276f0ed0a1773ebdf61dc@146.19.24.142:26656,177872437b2a31ebb0fb740ba5bd32b0be99e280@5.79.74.229:31095,129771a48f43b83c6144c7d282ad1da62434cc07@15.204.197.12:26656,610b8e096b4d8f923b1f41f7bdf92d5b63e033dc@162.55.243.82:4060,3a7733d4b670a672db326bd6e5f8ae37e14a3dbd@138.201.226.227:26656,98a6a264d2f2f5093d317f09e71036e62aa73906@107.181.235.66:20656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.kujira/config/config.toml
```
