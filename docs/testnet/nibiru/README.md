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
peers="2a333d36aa9c5d7fa0a4b143d6d33ed7c0336ebc@141.95.20.183:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:39656,a20290d5f96accb99bb973a65aeecf92c68dcf47@195.2.80.83:26656,b664932b407486867350f2b3cbbdf57a1a43b0a2@185.173.39.253:26656,928f17440a93750eb882e9aa7f2376be088f2362@144.76.27.79:36656,b9c40a99f968b9ec4bb8678ca4f1a3e70a495673@38.242.199.178:39656,c9e812ef269d4b7307299bd03365a0dfdac03b11@88.99.59.53:26656,ef7d0cce1150c2f37b60621150b704a823593930@144.91.126.238:26656,742919810a3d1df3c6a08ca3995c628011a9cd99@92.63.192.144:26656,3dbaa4a9b957ac296e197083d120f94112c45607@161.97.115.131:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.nibid/config/config.toml
```
