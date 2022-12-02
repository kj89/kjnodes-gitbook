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
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:39656,a85243341f413c07ec778f3a6dfb30f2cfc9d942@144.126.135.86:29656,d9d716ad1d94a662f1e4c646619da14d6cf3aa35@88.210.3.200:26656,cd827f8fb58627d503e2972f8d0cc3e05f38caf2@62.171.159.134:26656,713956378a1afc4f53fda1734141ead7619c8f99@144.126.143.183:29656,83fbb17df9dd448a12ae059947a6eb35a9520bea@185.161.208.88:26656,27c1bfd195aab3d98f7d7194942abcc125212696@167.235.145.80:26656,a20290d5f96accb99bb973a65aeecf92c68dcf47@195.2.80.83:26656,714dd5d212a642bd20d931a0764303acf75d8f88@154.53.32.169:29656,c9dcc45a1c3183f0df5751da6f5f7ae6f08138fd@188.134.69.27:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.nibid/config/config.toml
```
