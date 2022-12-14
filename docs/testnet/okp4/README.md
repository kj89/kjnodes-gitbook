# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/okp4.png" width="150" alt=""><figcaption></figcaption></figure>

OKP4 is a revolutionary public blockchain protocol where communities are incentivized to  share data and services confidently. To maximize value from data, it needs to be processed  by complex algorithms and pooled with other datasets, to create valuable knowledge.

**Chain ID**: okp4-nemeton-1 | **Latest Version Tag**: v3.0.0 | **Wasm**: OFF

Website: [https://okp4.network](https://okp4.network)


## Public endpoints

* rpc: [https://okp4-testnet.rpc.kjnodes.com](https://okp4-testnet.rpc.kjnodes.com)
* api: [https://okp4-testnet.api.kjnodes.com](https://okp4-testnet.api.kjnodes.com)

## Peering

**state-sync**

```
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@okp4-testnet.rpc.kjnodes.com:36656
```

**seed-node**

```
3f472746f46493309650e5a033076689996c8881@okp4-testnet.rpc.kjnodes.com:36659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/okp4-testnet/addrbook.json > $HOME/.okp4d/config/addrbook.json
```

**live-peers** (5)
```
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:36656,540e0e9b33b2d87315fdf7089404671581d36e94@95.217.203.43:26656,ed52ad66f7c30b322c1e58d226791f1402883db3@23.88.72.246:36656,e755eb8016c2f6f5303b2f8d503d9126d235e80f@138.201.35.56:26656,82bb185819e5cf2bb6a9896447672efca27f28cb@65.109.15.202:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.okp4d/config/config.toml
```
