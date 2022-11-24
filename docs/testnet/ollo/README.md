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

**live-peers** (11)
```
peers="5c3866af45b659bb2585f9209f95ed362079aa3b@142.93.211.170:26656,83c109aacea2db21f46f9c4c5dbb5a7cbc81e6e1@178.62.62.90:26656,ad2b0a3dfdd52bb4de8624b6b378638815f8e64b@65.109.90.178:18156,a553ae4af55d127300dd707a46e715b47a82610a@65.21.131.215:26626,59fa5f6b273ea8ffb519f7bf71e329289dd2dbd7@161.97.122.177:26656,69d2c02f413bea1376f5398646f0c2ce0f82d62e@141.94.73.93:26656,74e60a35557efc793edb10667c3fff979ccbf49f@141.95.204.81:26656,b1fe199b7ac2a7714c5d21524bb87810a2be94fb@135.181.178.53:32656,88517ff0acf652ac8e8c76ee485da05d3ae35227@135.181.36.194:26656,2f5965450c9c831266959632fba2c1533b8f676d@38.242.248.2:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:32656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.ollo/config/config.toml
```
