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
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:39656,5be20d8aba9971860e455257508803785679faef@135.181.208.213:26656,fe4e8a0688820808981aefda5c12fe41bba8e54a@78.47.141.222:26656,83fbb17df9dd448a12ae059947a6eb35a9520bea@185.161.208.88:26656,bac6885714877eadea39a0395b0c666bbe01d0b7@141.94.73.93:36656,bc6a9f58cf8abcb3d98848042a1f10720505321e@95.216.191.59:26656,211d8eb3e05a3398c68fa848ad15b96bb03cc7f6@109.123.242.208:26656,adcc42512f7d86e294f4f1e148e961361c098d57@185.135.137.245:26656,6b7c6b9519331f8c4a57e5f27c2c4fe291a09f19@14.29.132.178:26656,a20290d5f96accb99bb973a65aeecf92c68dcf47@195.2.80.83:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.nibid/config/config.toml
```
