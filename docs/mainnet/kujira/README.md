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
peers="177872437b2a31ebb0fb740ba5bd32b0be99e280@5.79.74.229:31095,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656,a586bb5aeb2b3492c5a5f68b7cf96f2440ef5deb@139.162.153.235:26656,de08e6178779ff3b19a8b6d22a05664392cb2b35@185.216.179.205:26656,3d150f6a71caca5607daff69c9049c04c37da64e@51.210.223.186:30095,fa57c7c253be46ad9f696ee2f2c1d72cbc6a1591@146.59.52.135:31095,fc593f5f9fcf7f88790bd8274ebc791f612d3efe@65.21.89.54:26655,6f3129d01218b939511cccf7e0318bfe872d97c4@65.109.33.181:26656,b80cf7882c8cab4894d41ccd4f5a00406d8b5f7d@146.59.52.48:30095,01cf570d3b08fdb5fe2f307cb485de7a35a3af23@135.148.55.229:11856"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.kujira/config/config.toml
```
