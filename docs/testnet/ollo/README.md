# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/ollo.png" width="150" alt=""><figcaption></figcaption></figure>

OLLO is a sovereign L1 chain built on the Cosmos network providing  next-gen trading tools & sustainable tokenomics.

**Chain ID**: ollo-testnet-1 | **Latest Version Tag**: v0.0.1

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
peers="ea21f774b9a4c170a7fe4685074eef5fde7db193@116.202.236.115:22046,98ea25336f87ebca4180c974e8b26aec55611ecb@173.212.226.128:32656,5b2e5dbcfd31d4ed97ea6b4cda76155841bf47f1@185.209.228.174:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:32656,d4696aba0fbb58a31b2736819ddecf699d787edb@38.242.159.61:26656,b76de75c13b2e80febbf574df981a2bfd28a7de1@65.108.124.172:28656,0bd4dce54aad2d9b67b992fd69b51694b43d3272@149.102.147.59:32656,e5f7aed51914aa6a841535ee5760e0042524e297@188.166.181.125:26656,ee0e8fabb1b7d0511a2733b62ac68a7919896c5a@212.8.240.13:32656,c5ffaa34423e83bf2d63c8780ead6977a19fa64e@65.109.30.117:36656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.ollo/config/config.toml
```
