# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/quicksilver.png" width="150" alt=""><figcaption></figcaption></figure>

Quicksilver is a permissionless, sovereign Cosmos SDK zone providing liquid staking for the entire Cosmos Ecosystem.

**Chain ID**: innuendo-3 | **Latest Binary Version**: v0.10.3 | **Wasm**: OFF

Website: [https://quicksilver.zone](https://quicksilver.zone)


## Public endpoints

* rpc: [https://quicksilver-testnet.rpc.kjnodes.com](https://quicksilver-testnet.rpc.kjnodes.com)
* api: [https://quicksilver-testnet.api.kjnodes.com](https://quicksilver-testnet.api.kjnodes.com)

## Peering

**state-sync**

```
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@quicksilver-testnet.rpc.kjnodes.com:11656
```

**seed-node**

```
3f472746f46493309650e5a033076689996c8881@quicksilver-testnet.rpc.kjnodes.com:11659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/quicksilver-testnet/addrbook.json > $HOME/.quicksilverd/config/addrbook.json
```

**live-peers** (10)
```
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:11656,c896ef12812a82eea865111c49f226849ad077db@144.76.236.90:26656,7b21198feaf0882f09fcbb24060961f434d158a3@35.242.163.107:26656,af8cfa944802a9bd510fc3407950a15e8be86c31@213.239.217.52:30656,7d112277450f0a8ef1059e6b334c373a215726ea@23.88.0.170:15619,47a7fac621a79649519eadbb8deb92d33bb3259b@161.97.82.203:26256,66f9d8f52a4637dc9215cdaa8dc2977633e52bbf@95.217.144.121:26656,95a1126503bd644746b62bac1d57bd3913044149@144.76.45.59:22656,41f7d7004cace7bd1760a5f980a86123700c8f1d@185.146.148.116:26656,c133c4c0c7034c8c345330f394984ad08092fc14@138.201.17.11:27656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.quicksilverd/config/config.toml
```
