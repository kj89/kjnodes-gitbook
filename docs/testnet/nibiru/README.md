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
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:39656,8a367ad243ba21158e137f2598a4ab97d5252834@80.87.196.122:26656,68874e60acc2b864959ab97e651ff767db47a2ea@65.108.140.220:26656,ab26e57c27b608b7f5a4b30a6f6676dea50e80a5@95.217.218.125:26656,211d8eb3e05a3398c68fa848ad15b96bb03cc7f6@109.123.242.208:26656,1d3086e9de415e859fccaa426706220068c6065e@38.242.222.10:26656,7a462d07fbba56aa773a105aba232916395cd184@167.86.115.153:16656,fec2c643c922eaa9edf5988bd09c6d79f5542aa6@65.21.51.120:26656,dae1c8e4b46bba38d7903797fa63d266ae8188f8@150.158.90.74:26656,5631ef4078b98a299428e149c595a543b3f1efd9@194.163.135.104:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.nibid/config/config.toml
```
