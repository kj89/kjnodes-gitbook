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

**live-peers** (10)
```
peers="ccffabe81f2de8a81e171f93fe1209392bf9993f@65.108.234.59:26656,c55d35ef908b74c2ddec2f47dbdb4032d7dfbcd4@23.88.69.22:27266,eb9742d81b436b95e324816794229a9efdaf8ea8@142.132.155.170:26656,1d85c9f16727584753db78b5b54eedf0ce8de3ed@51.159.16.49:5060,01cf570d3b08fdb5fe2f307cb485de7a35a3af23@135.148.55.229:11856,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656,3533d12b4dcacec1ab74183fad9cc65cb9e71ac7@198.244.167.22:5060,0c7da38c54e1a7d8ab7d48601b51847564ce019e@5.161.91.34:45656,e751b31b5444ed4a7489a456be805c736756eeb8@195.3.223.19:26656,15679999b404a9ee027dc9f5e795d6c4fddb6cee@51.91.152.102:20000"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.kujira/config/config.toml
```
