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
peers="9c538c7faa0881052ff1cb21c031372ab510e064@134.209.91.16:26656,ad2b0a3dfdd52bb4de8624b6b378638815f8e64b@65.109.90.178:18156,d6c5ff021b091a1fd93b9f811cf7fca0d31e8510@65.108.238.61:46656,23eb7907fc731a8492f74c3c3694d4c232ba3a21@139.162.10.122:26656,36899227ca3e8e225a188d71a5c582b183441641@87.248.157.28:26656,2a35b4ab40feb56dce051f955ae28b1fd8fbd5fb@80.65.211.249:26656,56bd2e7676dc6153c044701057977c6f0475b847@38.242.150.136:32656,c6ecf591a7a774ee8ef18cd67427e7fb813ab35d@95.217.84.248:32656,e3d1fbe11462a128f14ebc10f7e8bd59823f09e2@161.97.152.215:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:32656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.ollo/config/config.toml
```
