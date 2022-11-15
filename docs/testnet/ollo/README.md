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
peers="ea21f774b9a4c170a7fe4685074eef5fde7db193@116.202.236.115:22046,ad204b3422acb2e9a364941e540c99203ec22c5c@212.23.222.93:26656,ad2b0a3dfdd52bb4de8624b6b378638815f8e64b@65.109.90.178:18156,c5ffaa34423e83bf2d63c8780ead6977a19fa64e@65.109.30.117:36656,5c3866af45b659bb2585f9209f95ed362079aa3b@142.93.211.170:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:32656,125b0e30f00df3ff2ee7b29b7992ed888998ad31@65.109.28.177:47656,70ba32724461c7ed4ec8d6ddc8b5e0b1cfb9e237@54.219.57.63:26656,9865c6e15faced6643adc228e3a59744e1b4e277@116.203.29.162:46656,42beefd08b5f8580177d1506220db3a548090262@65.108.195.29:26116"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.ollo/config/config.toml
```
