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

**live-peers** (36)
```bash
peers="24a2bb2d06343b0f74ed0a6dc1d409ce0d996451@188.40.98.169:27656,14ae45e7f2ff7491cfa686a8fcac7cc095bc38ff@213.239.217.52:39656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:44656,5c2a752c9b1952dbed075c56c600c3a79b58c395@185.16.39.172:27066,e593c7a9ca61f5616119d6beb5bd8ef5dd28d62d@34.246.190.1:26656,6ba3b6ec03839afffa64c83e18ff80a681f4968d@65.108.194.40:21756,f8b7dbce90a7cd73f008ce65218caad40c0f56c6@167.86.115.153:32656,7ec0007e3c24012db9d5596745db5cb7c8321b50@95.216.7.169:60956,d9abc551547563e9a45160adc070b8bb42fc7d62@75.119.134.69:29656,3a445bfdbe2d0c8ee82461633aa3af31bc2b4dc0@3.252.219.158:26656,5bdbd9a68d212ec341c781cc553043486ce5b8ee@31.220.76.135:26656,112fba64a7e5e27b0cf8f02c634334c957891abf@75.119.146.244:28656,bfe21dd5af98aa42d213cd5bd943162a36b0505f@92.243.165.98:26656,34271a6f82d755777a3db02be39e575bf4ebd415@65.109.30.197:28656,dfa93668152cb6b3a822c987f9c22110a1c2f314@178.18.255.221:26656,eb7832932626c1c636d16e0beb49e0e4498fbd5e@65.108.231.124:20656,9057ee9d3d9b3c42c184dc89a7b2a07026b81a45@31.220.76.131:26656,f642b376722d6ce104ffd4c204e78ffe811e16c3@5.75.230.221:26656,0adbe1e790b58d19cc53a9839059a95d7d5d7aba@65.109.70.23:19956,80922095c0766aabdaf9e93e9c38c45321347ac0@85.239.237.85:26656,4f97a7b7d386dc6cc4b4a7239cf76be3c507a1c8@173.212.243.149:26656,9d5802ec3e10fbac150850ffdfa50f324e804b95@95.214.55.62:35656,5ed48f1abdd16d62f2179af31af3789ac5a42ecc@34.124.167.73:37656,ac99b8d7f3d863baa09cf6378057b78c4f02d029@91.233.173.45:26656,c44a02dba51e23ac06b006fb1285988c89051ce7@85.10.198.171:26556,f30d07170a092f82702e3c12334fa9fd828b71c6@168.119.124.130:47656,6b7bfa6f0297b231f40a9284d45282af93320315@65.109.116.50:28656,433be6210ad6350bebebad68ec50d3e0d90cb305@217.13.223.167:60856,a7944b8f0953e703d301670a9aa5312f3edf8cf4@65.109.106.91:24656,4fc42fdf634ef542094c7a44f22e031acea61162@91.77.165.172:27656,d8900913c64c2d7894d13ba35fe6c3e7c346015a@95.31.224.15:36656,0925c475208d8e338907383ab87a094ad03c478e@65.109.55.186:40656,0c548b2704594c7929b713de4c6985b9d9f03b8a@194.163.184.46:27656,f4223c735207cbf38a1d053d7a33531f82d12fc9@185.249.225.230:26656,c851e54d8d43ecd7524299c658e80222c7ee3af4@84.54.23.244:26656,8b774eabd1b4fbffdf9d14fba3d4a1690c69d0ad@65.109.24.227:30656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
