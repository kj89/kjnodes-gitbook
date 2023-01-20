# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/lava.png" width="150" alt=""><figcaption></figcaption></figure>

Lava powers a trustless market for RPC data access. The protocol  governs over peer to peer and private Provider-Application pairings,  ensuring high quality RPC service while creating consensus around data served.

**Chain ID**: lava-testnet-1 | **Latest Version Tag**: v0.4.3 | **Wasm**: OFF

[Website](https://lavanet.xyz) | [Discord](https://discord.com/invite/Tbk5NxTCdA) | [Twitter](https://twitter.com/lavanetxyz)


## Public endpoints

* api: [https://lava-testnet.api.kjnodes.com](https://lava-testnet.api.kjnodes.com)
* rpc: [https://lava-testnet.rpc.kjnodes.com](https://lava-testnet.rpc.kjnodes.com)
* grpc: [https://lava-testnet.grpc.kjnodes.com](https://lava-testnet.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@lava-testnet.rpc.kjnodes.com:44656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@lava-testnet.rpc.kjnodes.com:44659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/lava-testnet/addrbook.json > $HOME/.lava/config/addrbook.json
```

**live-peers** (32)
```bash
peers="24a2bb2d06343b0f74ed0a6dc1d409ce0d996451@188.40.98.169:27656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:44656,ce67e9671e7212695a0a7ba27fb0c723ea6ccff0@35.225.146.131:26656,0adbe1e790b58d19cc53a9839059a95d7d5d7aba@65.109.70.23:19956,72aabf4950afe5f2514cff8dc6c2c56600e7ed03@34.251.254.15:26656,2031e65ee8a13e57d922a14d28d67be0ada21a95@3.252.208.167:26656,eb7832932626c1c636d16e0beb49e0e4498fbd5e@65.108.231.124:20656,afc25b4b9f88c5af73c221475c47ba4c1cce4ae7@34.27.247.0:26656,e593c7a9ca61f5616119d6beb5bd8ef5dd28d62d@34.246.190.1:26656,18432dbb1238c416053bcbbc7b85b5f1258010a0@193.34.212.34:11134,15acccfd86840a2074c22027db107c1609182daa@185.244.181.109:36656,433be6210ad6350bebebad68ec50d3e0d90cb305@217.13.223.167:60856,3a445bfdbe2d0c8ee82461633aa3af31bc2b4dc0@3.252.219.158:26656,0a94c7f8451841f51bfaf86668edd212f181735f@95.214.55.155:21656,3031bcee46e31081eb6ecb90df2dad6fc757bebc@95.217.57.232:56656,b4c682261a1d6114e00a32bef17bd43398c7496c@164.92.241.245:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@185.16.39.172:27066,c0d9684b2142d1269ec12d149c8bfc84d4880585@52.210.158.168:26656,b591ef22e0c2082eb76dcac5ead95be55d01b695@65.109.178.147:26656,8cc0e66889c214d721e3fb34083da4c1edafa8ed@49.12.36.96:36656,377370216f2c003b9d00118ec5373ed21f13aab3@185.16.39.19:35656,4c86262ed00a1d42c6654967589ca57143f950d4@68.183.82.151:26656,f31c4dc121f37db1e0e24b49584bbbe4bbbba6c4@162.55.39.16:36656,6b209fb04491938b4d60b2847340799fbaced19f@38.242.153.36:44656,7e93260df1c1b6322b8ef229556264430cd83193@207.180.229.79:26656,988b396a3db1aa100a9489b7357612fd2d820e58@185.219.142.76:26656,0c32be34db35c25e3c034657abfbb22e93a06517@149.102.137.93:26656,0e9062ed560ce78eba346f1d73ae3ca9eeea5985@142.132.248.253:24656,3c47fd1662bcb17a4713c23e41d7b25e34478b8e@103.19.25.157:26672,e61d0d5eb484e778d842da903cc49dd74a802a57@5.180.151.155:26656,fb498cc17f301930cfd4d3b6e6261148c84e05e7@45.140.147.117:27656,a14b1484ad9b345e12fb6841ed48a5ce349af74b@65.108.63.58:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
