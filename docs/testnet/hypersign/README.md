# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/hypersign.png" width="150" alt=""><figcaption></figcaption></figure>

Hypersign is a decentralized identity layer for the internet, giving  users control of their personal data and identity whilst digital  enabling trust for businesses.

**Chain ID**: jagrat | **Latest Version Tag**: v0.1.5 | **Wasm**: OFF

[Website](https://hypersign.id) | [Discord](https://discord.gg/DmuUjMrHVw) | [Twitter](https://twitter.com/hypersignchain)


## Public endpoints

* rpc: [https://hypersign-testnet.rpc.kjnodes.com](https://hypersign-testnet.rpc.kjnodes.com)
* api: [https://hypersign-testnet.api.kjnodes.com](https://hypersign-testnet.api.kjnodes.com)

## Peering

**state-sync**

```
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@hypersign-testnet.rpc.kjnodes.com:31656
```

**seed-node**

```
3f472746f46493309650e5a033076689996c8881@hypersign-testnet.rpc.kjnodes.com:31659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/hypersign-testnet/addrbook.json > $HOME/.hid-node/config/addrbook.json
```

**live-peers** (10)
```
peers="a275d8018f683f279bf5167a72d294bfacafa839@178.63.102.172:41656,7d85caec437cc8c0a504d6ab3b18fd07c173b2fb@94.130.219.37:26001,22d2b3587e2ce6ae750c189b12461e7315d08ae4@167.235.151.119:26656,5e4fc955b23ab00f6a07cb6d56e89aafac0c85ff@167.86.85.122:26656,5b4482bfe02384184470070c3d3a4465cf0c18d4@144.91.82.61:31656,1e3f0aeb6f2a2017b122af2461a75c9695790954@65.108.233.109:10956,5cd888a5c37474ca778277cfd9dee7d24fe96094@95.217.214.107:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:31656,52eee2c34150d621312087e49f118969472ba55f@149.102.137.192:26656,c1b6d86f46eab9d0aa2e4399cddb9cf05d13621a@65.108.206.118:60556"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.hid-node/config/config.toml
```
