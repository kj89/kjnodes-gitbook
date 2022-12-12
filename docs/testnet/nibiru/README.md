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
peers="509d6bfee12d4ff10f754fb7af4f0058f7c426b7@185.214.134.89:26656,211d8eb3e05a3398c68fa848ad15b96bb03cc7f6@109.123.242.208:26656,baea7ea41950cc4cdbce4a365e7fd391fc4b0666@65.109.70.4:56656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:39656,c9e812ef269d4b7307299bd03365a0dfdac03b11@88.99.59.53:26656,93137cb574b5d6bd6fdb60e6c8164a08c1516081@209.126.8.192:26656,64a7e8acdfb325c4fb2a9912db4e13fe378a0a41@188.34.202.151:26656,34b70090fcc8e1ebf6be10be6e314e8d66931371@185.239.208.90:26656,7bbe4afc59fbfff5e6c3189c8ef73a1c6ac3f067@80.82.215.23:26656,6aee086dc69deb1e2bcc79a654cff6e36b94c8ab@178.63.8.245:46656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.nibid/config/config.toml
```
