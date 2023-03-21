# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/lava.png" width="150" alt=""><figcaption></figcaption></figure>

Lava powers a trustless market for RPC data access. The protocol  governs over peer to peer and private Provider-Application pairings,  ensuring high quality RPC service while creating consensus around data served.

**Chain ID**: lava-testnet-1 | **Latest Version Tag**: v0.7.0 | **Wasm**: OFF

[Website](https://lavanet.xyz) | [Discord](https://discord.com/invite/Tbk5NxTCdA) | [Twitter](https://twitter.com/lavanetxyz)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/lava-testnet](https://explorer.kjnodes.com/lava-testnet)

## Public endpoints

* api: [https://lava-testnet.api.kjnodes.com](https://lava-testnet.api.kjnodes.com)
* rpc: [https://lava-testnet.rpc.kjnodes.com](https://lava-testnet.rpc.kjnodes.com)
* grpc: lava-testnet.grpc.kjnodes.com:44090

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

**live-peers** (34)
```bash
peers="24a2bb2d06343b0f74ed0a6dc1d409ce0d996451@188.40.98.169:27656,14ae45e7f2ff7491cfa686a8fcac7cc095bc38ff@213.239.217.52:39656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:44656,0eb2dba8e99f29941edaf58974f469635479562f@154.12.245.39:28656,194ad0ab2f1003e123085300b0ca16d57e223be8@94.190.90.38:7060,3a445bfdbe2d0c8ee82461633aa3af31bc2b4dc0@3.252.219.158:26656,9d5802ec3e10fbac150850ffdfa50f324e804b95@95.214.55.62:35656,e593c7a9ca61f5616119d6beb5bd8ef5dd28d62d@34.246.190.1:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@185.16.39.172:27066,a20e24a251c9e6325a7c1e05d6a479bcd9c721ac@168.119.52.60:26656,ac99b8d7f3d863baa09cf6378057b78c4f02d029@91.233.173.45:26656,13a9209a4d08803a3becac57de8eb02dd51f8f41@65.109.23.114:19956,799077b3a3b52094ab3ca19b6a7ecab89c50cb61@185.144.99.97:26657,7aa9d96f0a3f162385b743ef92a2c6e03a4a1d84@65.108.48.77:20656,a7944b8f0953e703d301670a9aa5312f3edf8cf4@65.109.106.91:24656,d6a116d2aed64bd2f383b894e38f2a62232e44b7@116.202.161.165:36656,f7c1a998b8ef7cae7e38b0eff64d96206924e957@45.84.138.167:26656,a70a5c81f820ba95049f8bc4e9bd98450ba78bf5@142.93.36.176:44656,f68c57ca955420779773f9320a6b7710c2b29f73@188.191.36.222:26656,3f6d9698d9a5d9fe17afa5968ea652fae478b32f@185.250.37.239:32656,f642b376722d6ce104ffd4c204e78ffe811e16c3@5.75.230.221:26656,82c3a20fbc0d18b0982b183fb535eee7e03a72c9@207.180.248.217:28656,e77870b8732c952f40813e4e622cc2f108fd0223@154.53.55.153:26656,f30d07170a092f82702e3c12334fa9fd828b71c6@168.119.124.130:47656,64df498c92b9ccaf78012229d399aa34a014f087@65.109.122.105:56659,4e96723af8feb8a515573a7b9391e7bf7d562480@194.163.162.155:26656,eb7832932626c1c636d16e0beb49e0e4498fbd5e@65.108.231.124:20656,b7274e1274815e898fd52e4724c934820571fb5e@142.132.191.94:16656,b6e23ec5fbdf386fd65e1f195a205b00851f64c1@90.188.248.131:12656,6b7bfa6f0297b231f40a9284d45282af93320315@65.109.116.50:28656,8b774eabd1b4fbffdf9d14fba3d4a1690c69d0ad@65.109.24.227:30656,bc2e99e6004bb0b87c72ca10f20cd1617edf70fe@141.94.73.93:56656,ab924e7944c332bd1b52c8733e262bbdd33cb5ac@116.202.165.53:26656,c13b120d588c86008dc4ea5e3633b93c01831124@80.79.5.171:31656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
