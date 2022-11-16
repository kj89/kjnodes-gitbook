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
peers="c133c4c0c7034c8c345330f394984ad08092fc14@138.201.17.11:27656,e0f0703e9ce343c46e0ec01b19216715e817b358@65.109.85.170:28656,66f9d8f52a4637dc9215cdaa8dc2977633e52bbf@95.217.144.121:26656,0a3ac40a7a4ce35978c4da97be2eb6974bc3c58b@185.252.233.217:46656,433f85361545a434ad6b4202e2f373e4894ecf39@142.132.151.99:15619,7fe3007cba4de49584cbdad9489ffecfc9651c57@65.108.79.246:26673,8ff8a186fe9cbc70d0f34891fa051f87e561a48b@158.160.0.93:26656,64c58848cae4f3f1cb5d7700d3c225aa21536d28@142.132.155.252:47656,7781c28c240e85474425040f744b501d99120d1d@195.201.108.152:11656,20b6b3f6c0927c14a2348f5e378b98cb8596fc06@34.105.195.160:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.quicksilverd/config/config.toml
```
