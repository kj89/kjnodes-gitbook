# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/nibiru.png" width="150" alt=""><figcaption></figcaption></figure>

Nibiru is a sovereign proof-of-stake blockchain, open-source platform,  and member of a family of interconnected blockchains that comprise the Cosmos Ecosystem.

**Chain ID**: nibiru-testnet-1 | **Latest Version Tag**: v0.15.0 | **Wasm**: OFF

Website: [https://nibiru.fi](https://nibiru.fi)


## Public endpoints

* rpc: [https://nibiru-testnet.rpc.kjnodes.com](https://nibiru-testnet.rpc.kjnodes.com)
* api: [https://nibiru-testnet.api.kjnodes.com](https://nibiru-testnet.api.kjnodes.com)

## Peering

**state-sync**

```
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@nibiru-testnet.rpc.kjnodes.com:39656
```

**seed-node**

```
3f472746f46493309650e5a033076689996c8881@nibiru-testnet.rpc.kjnodes.com:39659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/nibiru-testnet/addrbook.json > $HOME/.nibid/config/addrbook.json
```

**live-peers** (9)
```
peers="ba98e0fdedf5e9e40fa3e07903160f228eeed876@194.163.172.82:26656,c880147e0f0980772010a97b8cbf949f12c0eb7c@178.18.247.78:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:39656,2f32f43c17664253a5ab36538916cc08466ab26b@185.188.249.17:26656,2b93c4402a26adc73e043d9a35f3cedd4aea311b@149.102.129.200:26656,6692cf5cc5ad3568d3195a5b009f5d6b05ccfc82@135.181.178.53:28656,afac65cfec4090e8af72f31bed047b56600a7702@45.85.146.252:26656,3f4fb67220c37be0b5dc15a0945b6e79406dc558@194.163.176.105:33656,fffb7c1c3cc14ef52428bdfb01e28a373525e2f4@185.188.249.103:39656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.nibid/config/config.toml
```
