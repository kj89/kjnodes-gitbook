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

**live-peers** (9)
```
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:39656,2b93c4402a26adc73e043d9a35f3cedd4aea311b@149.102.129.200:26656,0fec0239dfc520a99c7bd80fbe6d2a7c6ee00aa3@188.40.204.217:26656,dc0bf3c87213890503648dd2b66b8badf9b9287f@195.201.197.4:38656,7cbdf8c9365b65353976e62cb3449a65ac973f1d@95.217.188.207:26656,64a7e8acdfb325c4fb2a9912db4e13fe378a0a41@188.34.202.151:26656,f28eb26fa495c874d267a34c5e35f1dedfbc6960@185.240.103.233:26656,95514d97c9d0776478bee64353d986583a95c72e@185.135.137.193:26656,fb9a2b9f5389030fb3a9673e3fe9c3eee9dca869@185.190.143.50:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.nibid/config/config.toml
```
