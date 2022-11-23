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
peers="2a35b4ab40feb56dce051f955ae28b1fd8fbd5fb@80.65.211.249:26656,d4696aba0fbb58a31b2736819ddecf699d787edb@38.242.159.61:26656,42beefd08b5f8580177d1506220db3a548090262@65.108.195.29:26116,ad204b3422acb2e9a364941e540c99203ec22c5c@212.23.222.93:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:32656,59fa5f6b273ea8ffb519f7bf71e329289dd2dbd7@161.97.122.177:26656,ed38d885d068a963b0bc3986bb69680c34757a40@135.181.83.157:26656,392a64d15d8e1e318e7639cc20f36ed6a4a31703@5.75.169.25:26656,d6c305ccde3e850ac34228e41952508e48bfa86c@65.21.62.84:26656,861d8791ee3912589a825278b28170f8c523dab0@45.147.199.129:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.ollo/config/config.toml
```
