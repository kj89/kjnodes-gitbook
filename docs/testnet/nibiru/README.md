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
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:39656,f15e5a54a0288499b45e5d029b41c9ecde4c0a3d@46.228.199.183:26656,cb3c8df3e1d8942de9908bc1e5bb371a5671c404@89.163.231.30:36656,48e59e2e84e293fd6236341f76323ef6171b4b57@185.216.75.21:36656,f96e18b868fb6c517e9909293c528fa9d6b7236a@92.119.112.180:26656,5f35961c2c9aa0904f87b9563313593cf578cf52@194.5.152.17:26656,95514d97c9d0776478bee64353d986583a95c72e@185.135.137.193:26656,ba98e0fdedf5e9e40fa3e07903160f228eeed876@194.163.172.82:26656,2f32f43c17664253a5ab36538916cc08466ab26b@185.188.249.17:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.nibid/config/config.toml
```
