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
peers="0a3ac40a7a4ce35978c4da97be2eb6974bc3c58b@185.252.233.217:46656,025e1a9ba7e536e1db47569b55081f7adf6d2f9e@95.217.83.28:26636,8ff8a186fe9cbc70d0f34891fa051f87e561a48b@158.160.0.93:26656,41f7d7004cace7bd1760a5f980a86123700c8f1d@185.146.148.116:26656,433f85361545a434ad6b4202e2f373e4894ecf39@142.132.151.99:15619,2096650d8586b858d3369205f3b46ac4c765bc8e@65.109.53.155:26656,ba6c461874236d6dc95083886c8bd833d47d5c0a@195.3.221.13:46656,66f9d8f52a4637dc9215cdaa8dc2977633e52bbf@95.217.144.121:26656,47a7fac621a79649519eadbb8deb92d33bb3259b@161.97.82.203:26256,392a7ec2683e288866c353b7a8ac9ecc4e7b4bfc@142.165.207.19:16656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.quicksilverd/config/config.toml
```
