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
peers="ad2b0a3dfdd52bb4de8624b6b378638815f8e64b@65.109.90.178:18156,69d2c02f413bea1376f5398646f0c2ce0f82d62e@141.94.73.93:26656,5c3866af45b659bb2585f9209f95ed362079aa3b@142.93.211.170:26656,ad204b3422acb2e9a364941e540c99203ec22c5c@212.23.222.93:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:32656,76035e4e4afa5d7e560c57f27bb147504cf33dac@35.228.89.235:26656,c5ffaa34423e83bf2d63c8780ead6977a19fa64e@65.109.30.117:36656,d6c5ff021b091a1fd93b9f811cf7fca0d31e8510@65.108.238.61:46656,7864a2e4b42e5af76a83a8b644b9172fa1e40fa5@52.8.174.235:26656,90ad9622ac54023fe4ee9824d77b5d3e3c25c245@162.55.234.70:54956"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.ollo/config/config.toml
```
