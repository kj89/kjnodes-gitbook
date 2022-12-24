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
peers="22d2b3587e2ce6ae750c189b12461e7315d08ae4@167.235.151.119:26656,2c0379f78b655e8a386cb477e3cf3cae700c4a7f@213.239.207.175:34656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:31656,bd2ae9f1c42183104719f7c44be078bb7d282a61@65.109.92.241:11056,5cd888a5c37474ca778277cfd9dee7d24fe96094@95.217.214.107:26656,1de2abae74a4c5fd7d96d9869ef02187f81498f0@134.209.238.66:26656,e7bb31c8fdd8d26a739bfd87cdf3ba7a8f90406e@65.21.145.228:31656,7d85caec437cc8c0a504d6ab3b18fd07c173b2fb@94.130.219.37:26001,cd13283cd646d71fae76aa2e54ac1c43ea478d58@5.161.41.237:26656,5b4482bfe02384184470070c3d3a4465cf0c18d4@144.91.82.61:31656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.hid-node/config/config.toml
```
