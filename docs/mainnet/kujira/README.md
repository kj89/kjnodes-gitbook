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
peers="15679999b404a9ee027dc9f5e795d6c4fddb6cee@51.91.152.102:20000,b802fbfb83d6400639f17f2883f30a46ee6b05ad@51.210.223.185:32095,94469c0d109e00e65d62a307f7ab3dc109c01055@65.108.238.104:11856,d6f2eee997d108d4fde5683e31d678427376dfce@77.68.27.75:26656,6212f700687500f96ef56af3488e99fc4b009e19@212.68.34.95:26656,ccffabe81f2de8a81e171f93fe1209392bf9993f@65.108.234.59:26656,b21f57d5054aaa4cf8e3599bbe13719a47cc02d4@141.94.193.12:14656,de08e6178779ff3b19a8b6d22a05664392cb2b35@185.216.179.205:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@144.76.163.233:13656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.kujira/config/config.toml
```
