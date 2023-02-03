# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/lava.png" width="150" alt=""><figcaption></figcaption></figure>

Lava powers a trustless market for RPC data access. The protocol  governs over peer to peer and private Provider-Application pairings,  ensuring high quality RPC service while creating consensus around data served.

**Chain ID**: lava-testnet-1 | **Latest Version Tag**: v0.4.4 | **Wasm**: OFF

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

**live-peers** (31)
```bash
peers="14ae45e7f2ff7491cfa686a8fcac7cc095bc38ff@213.239.217.52:39656,74a979f0df53ef6f2ba9ab77c0c9fc5ba9c2bdc5@213.239.215.59:29456,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:44656,3c47fd1662bcb17a4713c23e41d7b25e34478b8e@103.19.25.157:26672,5c2a752c9b1952dbed075c56c600c3a79b58c395@185.16.39.172:27066,e593c7a9ca61f5616119d6beb5bd8ef5dd28d62d@34.246.190.1:26656,eb7832932626c1c636d16e0beb49e0e4498fbd5e@65.108.231.124:20656,f0758765ef0350d5cbbdeebf0b8e84f76e21c46d@54.221.204.97:26656,bebd03c6319c0930400dc564e9f5365068497322@95.217.41.15:26656,d3eb474a1f90d004e49638e384069c32d7dcc8a2@185.252.232.110:26656,24a2bb2d06343b0f74ed0a6dc1d409ce0d996451@188.40.98.169:27656,0c548b2704594c7929b713de4c6985b9d9f03b8a@194.163.184.46:27656,4fc42fdf634ef542094c7a44f22e031acea61162@91.77.165.172:27656,bd1e1f8df77e7b61200c490c9fabe6bbc4412d4e@91.223.3.144:26856,86cd808d9f4674b8810e4720ccff745d8c88ba3b@65.108.90.48:26656,3173b2d34ce415ee9a1bf08646d85688bf49e299@5.189.186.222:36656,8636a0d9276ee1b99c772e51904ea010862bc772@135.181.133.37:27656,433be6210ad6350bebebad68ec50d3e0d90cb305@217.13.223.167:60856,0735c5a841fe98ee0a74de7cef537c03b4c66a1b@45.89.54.153:26656,0a78dd75926983ba06de451480673487ffa1bcc1@199.175.98.106:26656,441fffc1478d480934d11d397384682ac42acd2f@95.217.9.227:26656,a5c1d2e86c2dc0eecb009dc71c92d6b5e193db6b@35.210.166.150:26656,18432dbb1238c416053bcbbc7b85b5f1258010a0@193.34.212.34:11134,3aef9d4925d9c299a77a4209db2be3fd7ded4ad0@94.103.91.148:26656,810bdfb3e88f4872995f9a05b6298c1bf3d20fe0@65.108.105.48:19956,f31c4dc121f37db1e0e24b49584bbbe4bbbba6c4@162.55.39.16:36656,3a445bfdbe2d0c8ee82461633aa3af31bc2b4dc0@3.252.219.158:26656,474e2436e097c28472a1fe269e1825762fa340d6@38.242.128.19:26656,e711b6631c3e5bb2f6c389cbc5d422912b05316b@213.239.216.252:33256,9a151159039fd8abce61ddb21e5342605787792b@5.75.228.39:26656,821c9347c927db52138dcd4bb54478fdf17f273e@81.0.218.53:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
