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
peers="98ea25336f87ebca4180c974e8b26aec55611ecb@173.212.226.128:32656,ea21f774b9a4c170a7fe4685074eef5fde7db193@116.202.236.115:22046,ee0e8fabb1b7d0511a2733b62ac68a7919896c5a@212.8.240.13:32656,ad204b3422acb2e9a364941e540c99203ec22c5c@212.23.222.93:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:32656,56bd2e7676dc6153c044701057977c6f0475b847@38.242.150.136:32656,ed38d885d068a963b0bc3986bb69680c34757a40@135.181.83.157:26656,b1fe199b7ac2a7714c5d21524bb87810a2be94fb@135.181.178.53:32656,59fa5f6b273ea8ffb519f7bf71e329289dd2dbd7@161.97.122.177:26656,c666b49c7a2b30d3c03152c9678b099247596f95@95.217.16.89:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.ollo/config/config.toml
```
