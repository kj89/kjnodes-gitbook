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

**live-peers** (33)
```bash
peers="24a2bb2d06343b0f74ed0a6dc1d409ce0d996451@188.40.98.169:27656,3f6d9698d9a5d9fe17afa5968ea652fae478b32f@185.250.37.239:32656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:44656,0c548b2704594c7929b713de4c6985b9d9f03b8a@194.163.184.46:27656,6ba3b6ec03839afffa64c83e18ff80a681f4968d@65.108.194.40:21756,f30d07170a092f82702e3c12334fa9fd828b71c6@168.119.124.130:47656,e593c7a9ca61f5616119d6beb5bd8ef5dd28d62d@34.246.190.1:26656,d796c20b5bdb8f1633c2a13afbf12314a77b668c@91.107.148.113:26656,31478ee0c0521c7cfb3312b86ef490936b5ceb80@65.109.92.240:197,0a78dd75926983ba06de451480673487ffa1bcc1@199.175.98.106:26656,60be50fae1525143ea9226eff17830c4a474af6c@154.53.39.80:26656,14ae45e7f2ff7491cfa686a8fcac7cc095bc38ff@213.239.217.52:39656,9057ee9d3d9b3c42c184dc89a7b2a07026b81a45@31.220.76.131:26656,f9af0186eec9a88a5a657deb9a7deff34c05d99f@86.111.48.156:26656,3a445bfdbe2d0c8ee82461633aa3af31bc2b4dc0@3.252.219.158:26656,397056c8cd7e2fce451d4f8e34ef24c0c9ffacba@176.9.44.113:26676,32d0eaa31ab8f9c2779ce9272b7a68f3d15a8e6e@213.239.207.175:40656,5c2a752c9b1952dbed075c56c600c3a79b58c395@185.16.39.172:27066,112fba64a7e5e27b0cf8f02c634334c957891abf@75.119.146.244:28656,9d5802ec3e10fbac150850ffdfa50f324e804b95@95.214.55.62:35656,5ab0449599aabcf90f664003c2ef1510ecd33b1b@65.21.203.204:11656,eb7832932626c1c636d16e0beb49e0e4498fbd5e@65.108.231.124:20656,b4d53b1e7a2fee2192a30e411ba83136c07ab595@161.97.147.107:26656,5e068fccd370b2f2e5ab4240a304323af6385f1f@172.93.110.154:27656,abbad4acf9360b250764ef660b5a25a4ec58245f@172.104.159.69:55676,433be6210ad6350bebebad68ec50d3e0d90cb305@217.13.223.167:60856,db959c7c05b9d5b5441b4964ab40dd679e7e6627@95.216.29.100:26656,5d55031717267b74a2d8110a6962d0fda48d583a@95.216.188.101:26656,14110234a060fc0d9568fb43a32c8b6b0f0f8cc2@65.108.240.151:26656,bc2e99e6004bb0b87c72ca10f20cd1617edf70fe@141.94.73.93:56656,6b7bfa6f0297b231f40a9284d45282af93320315@65.109.116.50:28656,fcd5a8f4aebc4c7100573914b7974a35cd389963@5.9.69.253:20656,a2afdc48785be73f208af349e78d632b5556cc01@5.75.226.151:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
