# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/ollo.png" width="150" alt=""><figcaption></figcaption></figure>

OLLO is a sovereign L1 chain built on the Cosmos network providing  next-gen trading tools & sustainable tokenomics.

**Chain ID**: ollo-testnet-1 | **Latest Version Tag**: v0.0.1 | **Wasm**: OFF

Website: [https://www.ollostation.zone](https://www.ollostation.zone)


## Public endpoints

* rpc: [https://ollo-testnet.rpc.kjnodes.com](https://ollo-testnet.rpc.kjnodes.com)
* api: [https://ollo-testnet.api.kjnodes.com](https://ollo-testnet.api.kjnodes.com)

## Peering

**state-sync**

```
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@ollo-testnet.rpc.kjnodes.com:32656
```

**seed-node**

```
3f472746f46493309650e5a033076689996c8881@ollo-testnet.rpc.kjnodes.com:32659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/ollo-testnet/addrbook.json > $HOME/.ollo/config/addrbook.json
```

**live-peers** (10)
```
peers="c5ffaa34423e83bf2d63c8780ead6977a19fa64e@65.109.30.117:36656,56bd2e7676dc6153c044701057977c6f0475b847@38.242.150.136:32656,e5f7aed51914aa6a841535ee5760e0042524e297@188.166.181.125:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:32656,ea21f774b9a4c170a7fe4685074eef5fde7db193@116.202.236.115:22046,90ad9622ac54023fe4ee9824d77b5d3e3c25c245@162.55.234.70:54956,b1fe199b7ac2a7714c5d21524bb87810a2be94fb@135.181.178.53:32656,69d2c02f413bea1376f5398646f0c2ce0f82d62e@141.94.73.93:26656,7349272f712e713a957bf5349930e3439e98b518@167.235.27.69:20656,74e60a35557efc793edb10667c3fff979ccbf49f@141.95.204.81:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.ollo/config/config.toml
```
