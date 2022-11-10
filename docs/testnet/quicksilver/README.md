# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/quicksilver.png" width="150" alt=""><figcaption></figcaption></figure>

Quicksilver is a permissionless, sovereign Cosmos SDK zone providing liquid staking for the entire Cosmos Ecosystem.

**Chain ID**: innuendo-3 | **Latest Version Tag**: v0.10.0 | **Wasm**: OFF

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
peers="c896ef12812a82eea865111c49f226849ad077db@144.76.236.90:26656,41f7d7004cace7bd1760a5f980a86123700c8f1d@185.146.148.116:26656,ba6c461874236d6dc95083886c8bd833d47d5c0a@195.3.221.13:46656,7fe3007cba4de49584cbdad9489ffecfc9651c57@65.108.79.246:26673,433f85361545a434ad6b4202e2f373e4894ecf39@142.132.151.99:15619,0a3ac40a7a4ce35978c4da97be2eb6974bc3c58b@185.252.233.217:46656,19c724a6c0e00615b22fc307798fba9640259e45@135.181.137.120:47656,c133c4c0c7034c8c345330f394984ad08092fc14@138.201.17.11:27656,e0f0703e9ce343c46e0ec01b19216715e817b358@65.109.85.170:28656,2096650d8586b858d3369205f3b46ac4c765bc8e@65.109.53.155:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.quicksilverd/config/config.toml
```
