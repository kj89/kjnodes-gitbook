# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/quicksilver.png" width="150" alt=""><figcaption></figcaption></figure>

Quicksilver is a permissionless, sovereign Cosmos SDK zone providing liquid staking for the entire Cosmos Ecosystem.

**Chain ID**: innuendo-3 | **Latest Version Tag**: v0.10.1 | **Wasm**: OFF

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
peers="7d112277450f0a8ef1059e6b334c373a215726ea@23.88.0.170:15619,c133c4c0c7034c8c345330f394984ad08092fc14@138.201.17.11:27656,7781c28c240e85474425040f744b501d99120d1d@195.201.108.152:11656,a37474c1f254cd4b16d924327a755c914e8e7d86@65.109.30.53:26656,5844010472bac487748336616d450bc9f0cbc57c@65.108.72.175:29656,7fe3007cba4de49584cbdad9489ffecfc9651c57@65.108.79.246:26673,025e1a9ba7e536e1db47569b55081f7adf6d2f9e@95.217.83.28:26636,0a3ac40a7a4ce35978c4da97be2eb6974bc3c58b@185.252.233.217:46656,c896ef12812a82eea865111c49f226849ad077db@144.76.236.90:26656,1c1ca90d704c22844570d57039ccf2e8f58e475d@80.64.208.123:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.quicksilverd/config/config.toml
```
