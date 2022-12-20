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

**live-peers** (10)
```
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:39656,d19f198aaca118db75502035395078d5557241bc@95.217.11.63:26656,42a0e7d08b912bea8ed1f114bc3def40b33183bc@135.181.96.116:26656,2a333d36aa9c5d7fa0a4b143d6d33ed7c0336ebc@141.95.20.183:26656,66173b39d0cd4cae67786c02bb9f5924b259fa51@173.249.14.172:26656,f96e18b868fb6c517e9909293c528fa9d6b7236a@92.119.112.180:26656,58ef403bb25b4d473816632bfe7dfe0360c1cc24@65.108.231.238:36656,14400308576815f96bdec78848a570e07c14f412@91.195.101.99:26656,eb3cefa339eea87f2b7ce6f64b1ebff273d10903@193.46.243.254:26656,a1b90fca93a6ba4abf6d11691411c0245db63120@161.97.102.177:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.nibid/config/config.toml
```
