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
peers="47a7fac621a79649519eadbb8deb92d33bb3259b@161.97.82.203:26256,25410bff2fb7312d24c11b1e990507e5e3aa40b7@135.125.5.31:48656,66f9d8f52a4637dc9215cdaa8dc2977633e52bbf@95.217.144.121:26656,0a3ac40a7a4ce35978c4da97be2eb6974bc3c58b@185.252.233.217:46656,7d112277450f0a8ef1059e6b334c373a215726ea@23.88.0.170:15619,41f7d7004cace7bd1760a5f980a86123700c8f1d@185.146.148.116:26656,433f85361545a434ad6b4202e2f373e4894ecf39@142.132.151.99:15619,13564ca7ffcc8fa6bcc6d405c96fe8c724ec17da@88.99.213.25:11656,e0f0703e9ce343c46e0ec01b19216715e817b358@65.109.85.170:28656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:11656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.quicksilverd/config/config.toml
```
