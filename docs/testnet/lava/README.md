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

**live-peers** (39)
```bash
peers="24a2bb2d06343b0f74ed0a6dc1d409ce0d996451@188.40.98.169:27656,433be6210ad6350bebebad68ec50d3e0d90cb305@217.13.223.167:60856,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:44656,ce67e9671e7212695a0a7ba27fb0c723ea6ccff0@35.225.146.131:26656,3c47fd1662bcb17a4713c23e41d7b25e34478b8e@103.19.25.157:26672,4bfb0d4d945985d2cc92ea4ba3578459b80f1dab@190.2.155.67:33656,6dd9c6d619f9e6fc75f39bacd313f811ca64b2c6@65.108.224.180:26656,afc25b4b9f88c5af73c221475c47ba4c1cce4ae7@34.27.247.0:26656,72aabf4950afe5f2514cff8dc6c2c56600e7ed03@34.251.254.15:26656,2031e65ee8a13e57d922a14d28d67be0ada21a95@3.252.208.167:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@185.16.39.172:27066,d927303d07abf24b72f3eb8ae495ac02372e3908@91.195.101.78:26656,149f9f017344ce9cebb637baa7cab57a28f3a8c3@86.111.48.159:26656,18432dbb1238c416053bcbbc7b85b5f1258010a0@193.34.212.34:11134,eb7832932626c1c636d16e0beb49e0e4498fbd5e@65.108.231.124:20656,525696e557db51c4d5f5bca1d7152753c7426c2e@34.192.150.110:26656,b591ef22e0c2082eb76dcac5ead95be55d01b695@65.109.178.147:26656,ec8065014ed4814b12c884ed528b96f281104528@65.21.131.215:26686,0c548b2704594c7929b713de4c6985b9d9f03b8a@194.163.184.46:27656,c0d9684b2142d1269ec12d149c8bfc84d4880585@52.210.158.168:26656,e593c7a9ca61f5616119d6beb5bd8ef5dd28d62d@34.246.190.1:26656,3a445bfdbe2d0c8ee82461633aa3af31bc2b4dc0@3.252.219.158:26656,131227f65bbc8f5b86030124fa1610a3283ebcbd@135.181.176.109:26656,f0501090b870f7796dfdd1f1f5479aec2baecfe8@88.198.52.89:11656,13a9209a4d08803a3becac57de8eb02dd51f8f41@65.109.23.114:19956,377370216f2c003b9d00118ec5373ed21f13aab3@185.16.39.19:35656,9f4d521f5115b5c43af3e7866e8a6e54e9afefe0@209.182.238.30:26656,0adbe1e790b58d19cc53a9839059a95d7d5d7aba@65.109.70.23:19956,39fe8916ab25530cba837f501beb0f2535a35642@84.46.246.109:26656,1bc4ce6e77f871cbc20646742fa0675a8ed4e933@109.123.246.40:30656,a63dfe251af05653f237c1fcfcd6629bc7c8dcdc@64.225.79.209:26656,904ec45d55abe397e486579338225bd9b60e0d87@145.224.100.207:26656,27a9aebdcc1bd6a8eb8cbffdd689e565dca14bc2@5.189.149.159:27656,092593c7a93420af56a00341dfa0fe91a2afb1c8@149.28.123.156:26656,4b0b69e769d303412a5daaa6cc261165c9b92625@75.119.144.1:26656,97a7c2941a5875ce518f4775b841ff3b888c82d4@65.108.129.104:21656,47a18d7c304896a8afe245fa15920523c5b910a4@86.48.1.143:26656,632bfd3276ab33ed74cbb048a1de28183b927e9c@80.85.141.179:26656,821c9347c927db52138dcd4bb54478fdf17f273e@81.0.218.53:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
