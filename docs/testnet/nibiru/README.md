# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/nibiru.png" width="150" alt=""><figcaption></figcaption></figure>

Nibiru is a sovereign proof-of-stake blockchain, open-source platform,  and member of a family of interconnected blockchains that comprise the Cosmos Ecosystem.

**Chain ID**: nibiru-testnet-1 | **Latest Version Tag**: v0.15.0 | **Wasm**: OFF

Website: [https://nibiru.fi](https://nibiru.fi)


## Public endpoints

* rpc: [https://nibiru-testnet.rpc.kjnodes.com](https://nibiru-testnet.rpc.kjnodes.com)
* api: [https://nibiru-testnet.api.kjnodes.com](https://nibiru-testnet.api.kjnodes.com)

## Peering

**state-sync**

```
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@nibiru-testnet.rpc.kjnodes.com:39656
```

**seed-node**

```
3f472746f46493309650e5a033076689996c8881@nibiru-testnet.rpc.kjnodes.com:39659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/nibiru-testnet/addrbook.json > $HOME/.nibid/config/addrbook.json
```

**live-peers** (10)
```
peers="82abc5f988e0031409ffe1c0e437baee36d28695@65.108.100.53:35656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:39656,6b7c6b9519331f8c4a57e5f27c2c4fe291a09f19@14.29.132.178:26656,e43637dd28bb6674ddf40fab74c53f8a1e0829f4@95.111.254.87:26656,3dbaa4a9b957ac296e197083d120f94112c45607@161.97.115.131:26656,a545b2fd6575d64334a35919d16cd86c51251411@95.216.159.253:26656,afe1a8d392b2caaa02c51165dd2b37e0181dacf9@65.108.72.233:21656,911a6a9a932f21326e4947d492ff03c405e9039e@65.109.86.236:27656,ceb490476c68f9ac3bbcdd7c4803de24e8ccce2b@206.246.71.251:36656,742919810a3d1df3c6a08ca3995c628011a9cd99@92.63.192.144:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.nibid/config/config.toml
```
