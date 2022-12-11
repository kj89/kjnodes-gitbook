# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/quicksilver.png" width="150" alt=""><figcaption></figcaption></figure>

Quicksilver is a permissionless, sovereign Cosmos SDK zone providing liquid staking for the entire Cosmos Ecosystem.

**Chain ID**: innuendo-3 | **Latest Binary Version**: v0.10.5 | **Wasm**: OFF

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
peers="433f85361545a434ad6b4202e2f373e4894ecf39@142.132.151.99:15619,a37474c1f254cd4b16d924327a755c914e8e7d86@65.109.30.53:26656,f337087c08a4965e6ba6b7fc8813c6abcdafaf88@178.128.228.78:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:11656,c133c4c0c7034c8c345330f394984ad08092fc14@138.201.17.11:27656,64c58848cae4f3f1cb5d7700d3c225aa21536d28@142.132.155.252:47656,95a1126503bd644746b62bac1d57bd3913044149@144.76.45.59:22656,0a3ac40a7a4ce35978c4da97be2eb6974bc3c58b@185.252.233.217:46656,7d112277450f0a8ef1059e6b334c373a215726ea@23.88.0.170:15619,fe4ef62f5d26dbe7674549cc9fac591f5cca5bbc@148.72.153.180:11656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.quicksilverd/config/config.toml
```
