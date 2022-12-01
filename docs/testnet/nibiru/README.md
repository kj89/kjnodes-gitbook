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
peers="a2162bd42fdb011eb821d62fcaed3276142cf4d4@142.132.139.101:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:39656,b502caa5e8071c14179c562a328bb2a096f6b44a@141.94.139.233:30656,4dbb35256838e39da9237294f6a3c2820b02dd2d@65.108.82.135:26656,86c756af333d60326c5760fabf76f51c2c09ccbd@135.181.145.56:26656,a20290d5f96accb99bb973a65aeecf92c68dcf47@195.2.80.83:26656,afe1a8d392b2caaa02c51165dd2b37e0181dacf9@65.108.72.233:21656,4333fc79b0616c524a495313bf1b025870cedae3@190.2.155.67:31656,4860946be65b6738122f71202fbfaec6f149662e@2.58.82.148:26651"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.nibid/config/config.toml
```
