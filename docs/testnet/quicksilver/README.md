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
peers="c133c4c0c7034c8c345330f394984ad08092fc14@138.201.17.11:27656,41f7d7004cace7bd1760a5f980a86123700c8f1d@185.146.148.116:26656,392a7ec2683e288866c353b7a8ac9ecc4e7b4bfc@142.165.207.19:16656,ba6c461874236d6dc95083886c8bd833d47d5c0a@195.3.221.13:46656,66f9d8f52a4637dc9215cdaa8dc2977633e52bbf@95.217.144.121:26656,433f85361545a434ad6b4202e2f373e4894ecf39@142.132.151.99:15619,a37474c1f254cd4b16d924327a755c914e8e7d86@65.109.30.53:26656,e0f0703e9ce343c46e0ec01b19216715e817b358@65.109.85.170:28656,7d112277450f0a8ef1059e6b334c373a215726ea@23.88.0.170:15619,20b6b3f6c0927c14a2348f5e378b98cb8596fc06@34.105.195.160:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.quicksilverd/config/config.toml
```
