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
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:39656,6705a23ee032a75ddadd3c32ea3ab70feee64786@192.145.37.151:46656,afac65cfec4090e8af72f31bed047b56600a7702@45.85.146.252:26656,2b551f4f0d14ff63ca1d374ad513949eb43faa29@178.208.86.44:26656,ba98e0fdedf5e9e40fa3e07903160f228eeed876@194.163.172.82:26656,986d2c87f1e01b23a18aef2c52f68a6dc51da21d@194.146.13.223:26656,bbf891728d46b3df0702489aa0a3888c5e02843e@95.217.223.85:26656,ab26e57c27b608b7f5a4b30a6f6676dea50e80a5@95.217.218.125:26656,03de6cc7af9b236a28c319a7e792a681c7fe2205@95.217.211.58:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.nibid/config/config.toml
```
