# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/lava.png" width="150" alt=""><figcaption></figcaption></figure>

Lava powers a trustless market for RPC data access. The protocol  governs over peer to peer and private Provider-Application pairings,  ensuring high quality RPC service while creating consensus around data served.

**Chain ID**: lava-testnet-1 | **Latest Version Tag**: v0.7.0 | **Wasm**: OFF

[Website](https://lavanet.xyz) | [Discord](https://discord.com/invite/Tbk5NxTCdA) | [Twitter](https://twitter.com/lavanetxyz)




## Chain explorer
[https://explorer.kjnodes.com/lava-testnet](https://explorer.kjnodes.com/lava-testnet)

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

**live-peers** (42)
```bash
peers="9d571b0658acf791b2d5ce1a2d82f7820a279a38@135.181.146.148:12656,e593c7a9ca61f5616119d6beb5bd8ef5dd28d62d@34.246.190.1:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:44656,6ba3b6ec03839afffa64c83e18ff80a681f4968d@65.108.194.40:21756,14ae45e7f2ff7491cfa686a8fcac7cc095bc38ff@213.239.217.52:39656,5a469a75fb05eddf2d79fb17063cc59e84d0821a@207.180.236.115:34656,13a9209a4d08803a3becac57de8eb02dd51f8f41@65.109.23.114:19956,112fba64a7e5e27b0cf8f02c634334c957891abf@75.119.146.244:28656,3a445bfdbe2d0c8ee82461633aa3af31bc2b4dc0@3.252.219.158:26656,d6a116d2aed64bd2f383b894e38f2a62232e44b7@116.202.161.165:36656,5c2a752c9b1952dbed075c56c600c3a79b58c395@185.16.39.172:27066,9d5802ec3e10fbac150850ffdfa50f324e804b95@95.214.55.62:35656,bd1e1f8df77e7b61200c490c9fabe6bbc4412d4e@91.223.3.144:26856,6bc4f7c26faad2e87d005f8934108f7bcb1b9543@162.55.95.144:26656,51aeaa2c757989f720c904023c2dbedfc720f75e@23.88.5.169:27656,d1730b774b7c1d52dd9f6ae874a56de958aa147e@65.109.15.19:26656,f68c57ca955420779773f9320a6b7710c2b29f73@188.191.36.222:26656,f0758765ef0350d5cbbdeebf0b8e84f76e21c46d@54.221.204.97:26656,7adc61737172235479b405f61477a02be635fb21@62.171.188.69:26656,fb2b9d41678f3d1c9c0bdef1a87f2037b6b0088a@146.19.24.252:26666,c19965fe8a1ea3391d61d09cf589bca0781d29fd@162.19.217.52:26656,07c557b393b235a7b004a4a32831e54092dc24a0@91.107.147.250:26656,550d7467d6a442da11d9772b804252a8dfdca27e@91.107.243.149:26656,7fb838681ff9855a634c7823de605fb4a5d22eba@65.108.144.202:26656,5bdbd9a68d212ec341c781cc553043486ce5b8ee@31.220.76.135:26656,0c548b2704594c7929b713de4c6985b9d9f03b8a@194.163.184.46:27656,013f0163d37428ed99eacd8ee84059da5c243981@5.161.132.217:26656,cc5b61248a30c7e34ff4a7dfee3d470000b0de2d@194.50.0.178:26656,9057ee9d3d9b3c42c184dc89a7b2a07026b81a45@31.220.76.131:26656,0adbe1e790b58d19cc53a9839059a95d7d5d7aba@65.109.70.23:19956,b043a968059a60026988045fdd543c10b2756d6d@79.137.206.77:26656,b62eb3baed171ab5654292e5e35d56a1287693c9@45.32.66.24:26656,d6c9a48634b9e1277d587fdb76d58421a23903a4@65.109.90.171:34656,eb7832932626c1c636d16e0beb49e0e4498fbd5e@65.108.231.124:20656,c13b120d588c86008dc4ea5e3633b93c01831124@80.79.5.171:31656,d8900913c64c2d7894d13ba35fe6c3e7c346015a@95.31.224.15:36656,b495744cfa1883935fe641eaade6aa0dc91be689@134.209.243.127:26656,0925c475208d8e338907383ab87a094ad03c478e@65.109.55.186:40656,1dcafa53e66c0b8470b96db4b532a658c26fa026@167.235.84.123:26656,6b7bfa6f0297b231f40a9284d45282af93320315@65.109.116.50:28656,a20e24a251c9e6325a7c1e05d6a479bcd9c721ac@168.119.52.60:26656,4e96723af8feb8a515573a7b9391e7bf7d562480@194.163.162.155:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
