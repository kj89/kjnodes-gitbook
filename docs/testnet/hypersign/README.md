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
peers="23eff008c88dcc60ef9a71f2fb469c472679c35e@136.243.88.91:5040,610843eda2f0388cb8e75917e8c1f63350bd3bd1@154.26.131.130:16656,1de2abae74a4c5fd7d96d9869ef02187f81498f0@134.209.238.66:26656,c1b6d86f46eab9d0aa2e4399cddb9cf05d13621a@65.108.206.118:60556,1e3f0aeb6f2a2017b122af2461a75c9695790954@65.108.233.109:10956,1380864bb38481fef4b2358026a5ed53fc027679@95.214.52.206:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:31656,bd2ae9f1c42183104719f7c44be078bb7d282a61@65.109.92.241:11056,22d2b3587e2ce6ae750c189b12461e7315d08ae4@167.235.151.119:26656,2c0379f78b655e8a386cb477e3cf3cae700c4a7f@213.239.207.175:34656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.hid-node/config/config.toml
```
