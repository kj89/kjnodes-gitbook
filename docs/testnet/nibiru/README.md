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
peers="5be20d8aba9971860e455257508803785679faef@135.181.208.213:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:39656,a20290d5f96accb99bb973a65aeecf92c68dcf47@195.2.80.83:26656,2ec6cb2a83c178fb490a992a3bd6a5c142c3fc61@135.181.20.30:26656,44a06bbdeb3d45ff356cc44d74494453a243f047@65.108.53.27:39656,c0b22a7b64c287f8b0c4f4ac19001d195199d146@65.108.105.36:28656,3f4fb67220c37be0b5dc15a0945b6e79406dc558@194.163.176.105:33656,ecb2711272cb62fccf2d96e8df1133491cfdda01@185.213.25.243:26656,7007d1150613015fcf55d65800f981cb1b0f624d@65.108.2.41:60556,e4e48a142f87f2918acb3ec032a27cb61dc15657@167.86.71.232:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.nibid/config/config.toml
```
