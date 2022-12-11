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
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:39656,d19f198aaca118db75502035395078d5557241bc@95.217.11.63:26656,afac65cfec4090e8af72f31bed047b56600a7702@45.85.146.252:26656,211d8eb3e05a3398c68fa848ad15b96bb03cc7f6@109.123.242.208:26656,c9e812ef269d4b7307299bd03365a0dfdac03b11@88.99.59.53:26656,5be20d8aba9971860e455257508803785679faef@135.181.208.213:26656,509d6bfee12d4ff10f754fb7af4f0058f7c426b7@185.214.134.89:26656,8a367ad243ba21158e137f2598a4ab97d5252834@80.87.196.122:26656,66363f55c128ce60bb4c5ebfbc070ec464bcd532@80.82.215.220:26656,41c0720bd041ed4effc52a03c60cc821452ceb47@185.245.182.141:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.nibid/config/config.toml
```
