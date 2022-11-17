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
peers="d14b740968d24aa5c31ade7dbda2b1204c40f24c@65.109.52.156:46656,b1fe199b7ac2a7714c5d21524bb87810a2be94fb@135.181.178.53:32656,76035e4e4afa5d7e560c57f27bb147504cf33dac@35.228.89.235:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:32656,0bd4dce54aad2d9b67b992fd69b51694b43d3272@149.102.147.59:32656,d6c5ff021b091a1fd93b9f811cf7fca0d31e8510@65.108.238.61:46656,a553ae4af55d127300dd707a46e715b47a82610a@65.21.131.215:26626,e5f7aed51914aa6a841535ee5760e0042524e297@188.166.181.125:26656,c5ffaa34423e83bf2d63c8780ead6977a19fa64e@65.109.30.117:36656,d4696aba0fbb58a31b2736819ddecf699d787edb@38.242.159.61:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.ollo/config/config.toml
```
