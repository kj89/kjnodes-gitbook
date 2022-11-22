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
peers="90ad9622ac54023fe4ee9824d77b5d3e3c25c245@162.55.234.70:54956,74e60a35557efc793edb10667c3fff979ccbf49f@141.95.204.81:26656,98ea25336f87ebca4180c974e8b26aec55611ecb@173.212.226.128:32656,7349272f712e713a957bf5349930e3439e98b518@167.235.27.69:20656,a553ae4af55d127300dd707a46e715b47a82610a@65.21.131.215:26626,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:32656,76035e4e4afa5d7e560c57f27bb147504cf33dac@35.228.89.235:26656,d6c5ff021b091a1fd93b9f811cf7fca0d31e8510@65.108.238.61:46656,46cd4ab1a4fd92ee0ab510d05dce3cd00e639a05@3.235.146.125:26656,4a1dce5e59374f85d45fdb49478658b03e3d2ef3@65.21.134.202:26626"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.ollo/config/config.toml
```
