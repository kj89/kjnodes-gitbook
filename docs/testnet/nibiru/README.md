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
peers="2f32f43c17664253a5ab36538916cc08466ab26b@185.188.249.17:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:39656,2a333d36aa9c5d7fa0a4b143d6d33ed7c0336ebc@141.95.20.183:26656,ad28f301beed76a28f324331df8cf3a012a654e1@144.91.81.78:28656,03010515fbba01893754eabe0f309866f3d68edf@85.114.132.101:26656,baea7ea41950cc4cdbce4a365e7fd391fc4b0666@65.109.70.4:56656,f0e61ae1e14644d1a64c9464874583f0be74400b@51.79.142.184:26656,87a6d552d11fd025e739fd9d577a929c5f9f775e@38.242.252.157:26656,23a18fe03c6c1b0ccc7eb0d53716ef2ba5887fd3@194.5.152.200:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.nibid/config/config.toml
```
