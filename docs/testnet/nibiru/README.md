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
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:39656,2a333d36aa9c5d7fa0a4b143d6d33ed7c0336ebc@141.95.20.183:26656,83fbb17df9dd448a12ae059947a6eb35a9520bea@185.161.208.88:26656,c0b22a7b64c287f8b0c4f4ac19001d195199d146@65.108.105.36:28656,6b463fa626f047c7fbdffe7715d89bde6d7c5d98@84.52.99.180:26656,de147f2c8ddd0bbe8bbdf997015a2dc62ce4846d@185.135.137.238:26656,74ac9089831532f9b4d13b7dee96503e109b7d5a@2.58.82.126:26651,e43637dd28bb6674ddf40fab74c53f8a1e0829f4@95.111.254.87:26656,eae52d0dac43cd73e09e5ab2bd2ca2af6706dbca@178.79.133.241:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.nibid/config/config.toml
```
