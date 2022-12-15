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

**live-peers** (11)
```
peers="e755eb8016c2f6f5303b2f8d503d9126d235e80f@138.201.35.56:26656,ed52ad66f7c30b322c1e58d226791f1402883db3@23.88.72.246:36656,a4a96019d2fbc1b5df07940cd971585311166acd@65.108.206.118:61356,6bc178290d0773e244cf04598a3919d7a9391bf1@65.109.131.71:36656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:36656,15fdc722cd49ef7676205b6ad3120a84728d948c@65.108.225.158:17656,2bfd405e8f0f176428e2127f98b5ec53164ae1f0@142.132.149.118:26656,11d2d5cab53f3e10bc8d91c76601d68cce33c82b@144.76.28.163:26656,cd2e7d49cc2f911d7df7c7951d72c96727d1db1d@212.8.240.13:36656,8af258bbe73f4c66127a7b3e8b1ec23fde2950a6@65.108.192.123:19656,5a343f58402802a83ac546a22f66b1a799480dec@95.216.2.232:33656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.okp4d/config/config.toml
```
