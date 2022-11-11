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

**live-peers** (10)
```
peers="1048e73299d435b6598245d246562efc62df002d@65.108.128.201:11856,3a7733d4b670a672db326bd6e5f8ae37e14a3dbd@138.201.226.227:26656,610b8e096b4d8f923b1f41f7bdf92d5b63e033dc@162.55.243.82:4060,fa57c7c253be46ad9f696ee2f2c1d72cbc6a1591@146.59.52.135:31095,f9509ef83ecce9433e3bc9de8a0abf6e00912b0e@173.212.247.202:26656,213dbb8301ce1c0f5662a9b723bd613f15e1dd4e@75.119.157.167:30656,35629bef4cc1a0be69ebd053ff4e16de82970add@5.79.79.80:30095,5ef740383b8a490c1bee7f9e61bf03c43427b182@83.149.102.56:32095,eb9742d81b436b95e324816794229a9efdaf8ea8@142.132.155.170:26656,0f45ad954ac8a0674a73f1fbca5847650c245ba3@141.94.219.133:11756"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.kujira/config/config.toml
```
