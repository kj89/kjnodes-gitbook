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
peers="7cbdf8c9365b65353976e62cb3449a65ac973f1d@95.217.188.207:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:39656,238cb61559295fdafe10366a8e70b5369e4fb3c7@173.212.213.112:26656,ac19b924f4f549483c0833ff7ad262cc3b04973e@5.182.39.82:26656,3f48d1d7427e226ed930bb05a40b5885db10a8ed@194.5.152.244:26656,92e93ba4593eeed74988bab604df3fbc5426fc32@167.235.27.69:26656,49ee8e65e47d86799d26f54937304da04c2cc2b6@144.91.85.204:46656,d0a88020e735f9816d913990d163b344675d4f06@45.142.214.127:26656,9b6b62540afaabd7b75b80e641bf3b12dfd65bed@185.135.137.237:26656,f15e5a54a0288499b45e5d029b41c9ecde4c0a3d@46.228.199.183:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.nibid/config/config.toml
```
