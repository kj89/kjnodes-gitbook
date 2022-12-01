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
peers="9c753f4e99433b79b0b7dce69fffa0a892491f95@65.108.234.154:26656,450e62f04093c283cc7dcf1257a9b2e4893ad545@148.251.85.115:26656,de08e6178779ff3b19a8b6d22a05664392cb2b35@185.216.179.205:26656,6212f700687500f96ef56af3488e99fc4b009e19@212.68.34.95:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656,eb9742d81b436b95e324816794229a9efdaf8ea8@142.132.155.170:26656,253d2293272a29057a27797a5703f5171c267da1@192.99.15.159:26656,62d62b1281dc8dd00ecb353722d26186a4cf678b@65.108.239.51:26656,1d85c9f16727584753db78b5b54eedf0ce8de3ed@51.159.16.49:5060,d02fc7c5db5e502bb78ceeb81067ddab5b0cf51a@89.39.104.128:13656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.kujira/config/config.toml
```
