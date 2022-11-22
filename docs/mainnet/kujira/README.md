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
peers="7ce3988ad06172aa22856e1c3ec7940dd01c2592@95.217.144.25:15602,b80cf7882c8cab4894d41ccd4f5a00406d8b5f7d@146.59.52.48:30095,d3cbe679ef7e491d3b34f6557bde23077f28e21f@77.22.195.34:26656,15679999b404a9ee027dc9f5e795d6c4fddb6cee@51.91.152.102:20000,01cf570d3b08fdb5fe2f307cb485de7a35a3af23@135.148.55.229:11856,5ef740383b8a490c1bee7f9e61bf03c43427b182@83.149.102.56:32095,4c1f4d9358118cb8917567702c12ca4f31714b32@65.108.132.107:26656,129771a48f43b83c6144c7d282ad1da62434cc07@15.204.197.12:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@144.76.163.233:13656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.kujira/config/config.toml
```
