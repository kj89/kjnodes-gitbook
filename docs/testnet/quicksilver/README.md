# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/quicksilver.png" width="150" alt=""><figcaption></figcaption></figure>

Quicksilver is a permissionless, sovereign Cosmos SDK zone providing liquid staking for the entire Cosmos Ecosystem.

**Chain ID**: innuendo-3 | **Latest Binary Version**: v0.10.4 | **Wasm**: OFF

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
peers="7d112277450f0a8ef1059e6b334c373a215726ea@23.88.0.170:15619,13564ca7ffcc8fa6bcc6d405c96fe8c724ec17da@88.99.213.25:11656,66f9d8f52a4637dc9215cdaa8dc2977633e52bbf@95.217.144.121:26656,8ff8a186fe9cbc70d0f34891fa051f87e561a48b@158.160.0.93:26656,125327a98d0e63adfb3f0be513947a96b24231fa@5.161.145.173:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:11656,0a3ac40a7a4ce35978c4da97be2eb6974bc3c58b@185.252.233.217:46656,c133c4c0c7034c8c345330f394984ad08092fc14@138.201.17.11:27656,433f85361545a434ad6b4202e2f373e4894ecf39@142.132.151.99:15619,025e1a9ba7e536e1db47569b55081f7adf6d2f9e@95.217.83.28:26636"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.quicksilverd/config/config.toml
```
