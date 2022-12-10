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
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:39656,986d2c87f1e01b23a18aef2c52f68a6dc51da21d@194.146.13.223:26656,2b551f4f0d14ff63ca1d374ad513949eb43faa29@178.208.86.44:26656,cadf119fa38b4b211f819072ef754ab07d8b1dfb@77.232.43.194:26656,d19f198aaca118db75502035395078d5557241bc@95.217.11.63:26656,afac65cfec4090e8af72f31bed047b56600a7702@45.85.146.252:26656,c3efbf90e5d85b989dd4abc7314d00cb29814e32@80.82.222.221:39656,bac6885714877eadea39a0395b0c666bbe01d0b7@141.94.73.93:36656,de147f2c8ddd0bbe8bbdf997015a2dc62ce4846d@185.135.137.238:26656,a1b90fca93a6ba4abf6d11691411c0245db63120@161.97.102.177:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.nibid/config/config.toml
```
