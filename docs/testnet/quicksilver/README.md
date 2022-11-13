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
peers="433f85361545a434ad6b4202e2f373e4894ecf39@142.132.151.99:15619,0a3ac40a7a4ce35978c4da97be2eb6974bc3c58b@185.252.233.217:46656,66f9d8f52a4637dc9215cdaa8dc2977633e52bbf@95.217.144.121:26656,025e1a9ba7e536e1db47569b55081f7adf6d2f9e@95.217.83.28:26636,2096650d8586b858d3369205f3b46ac4c765bc8e@65.109.53.155:26656,711b97aa5956c6ce95c05895faa6c3ad3c04d440@135.181.59.162:11156,c4489720ba051c79f5bb16ae5d81341b0f248e19@54.194.109.230:26656,8a334ed2e728ca1164f8ef6ae58dd5fda31da5be@66.94.104.239:26641,e0f0703e9ce343c46e0ec01b19216715e817b358@65.109.85.170:28656,ba6c461874236d6dc95083886c8bd833d47d5c0a@195.3.221.13:46656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.quicksilverd/config/config.toml
```
