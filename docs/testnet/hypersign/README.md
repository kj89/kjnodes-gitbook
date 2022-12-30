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
peers="5e4fc955b23ab00f6a07cb6d56e89aafac0c85ff@167.86.85.122:26656,5b4482bfe02384184470070c3d3a4465cf0c18d4@144.91.82.61:31656,1e3f0aeb6f2a2017b122af2461a75c9695790954@65.108.233.109:10956,bd2ae9f1c42183104719f7c44be078bb7d282a61@65.109.92.241:11056,b946e1722d17420f911dd58d716964b43dfd12a9@65.108.238.217:11204,ce6686036f6554deb0490103dcc201172e7c3f2f@81.0.220.131:26656,1de2abae74a4c5fd7d96d9869ef02187f81498f0@134.209.238.66:26656,4aa182ce191cd089929544fe0612d33a02a2cde9@46.17.250.145:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:31656,22d2b3587e2ce6ae750c189b12461e7315d08ae4@167.235.151.119:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.hid-node/config/config.toml
```
