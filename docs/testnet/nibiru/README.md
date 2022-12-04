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
peers="b664932b407486867350f2b3cbbdf57a1a43b0a2@185.173.39.253:26656,86c756af333d60326c5760fabf76f51c2c09ccbd@135.181.145.56:26656,873ae3863f2136820d81e89106b2210db7edbc67@65.108.238.217:11134,a20290d5f96accb99bb973a65aeecf92c68dcf47@195.2.80.83:26656,78bff95471439b1ba6d97432c5f8f855db33ed0b@185.245.183.192:46656,b135db9dc9d4b95bfae4f1ffbe095a91442dc3dc@167.235.145.49:26656,eae52d0dac43cd73e09e5ab2bd2ca2af6706dbca@178.79.133.241:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:39656,8e4993fe9be00b4cf58e329a2b600e4220e975ba@109.123.255.111:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.nibid/config/config.toml
```
