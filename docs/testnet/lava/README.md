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

**live-peers** (38)
```bash
peers="24a2bb2d06343b0f74ed0a6dc1d409ce0d996451@188.40.98.169:27656,e593c7a9ca61f5616119d6beb5bd8ef5dd28d62d@34.246.190.1:26656,5ab0449599aabcf90f664003c2ef1510ecd33b1b@65.21.203.204:11656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:44656,6ba3b6ec03839afffa64c83e18ff80a681f4968d@65.108.194.40:21756,5c2a752c9b1952dbed075c56c600c3a79b58c395@185.16.39.172:27066,a724b94c593241890022e204e0065d8baa67168c@116.202.227.117:44656,5a469a75fb05eddf2d79fb17063cc59e84d0821a@207.180.236.115:34656,0a78dd75926983ba06de451480673487ffa1bcc1@199.175.98.106:26656,3a445bfdbe2d0c8ee82461633aa3af31bc2b4dc0@3.252.219.158:26656,5e068fccd370b2f2e5ab4240a304323af6385f1f@172.93.110.154:27656,14ae45e7f2ff7491cfa686a8fcac7cc095bc38ff@213.239.217.52:39656,fb2b9d41678f3d1c9c0bdef1a87f2037b6b0088a@146.19.24.252:26666,99327e5cf0f31ac3bb1ca8e39cc9f17c823b7ec1@109.236.88.8:26656,9057ee9d3d9b3c42c184dc89a7b2a07026b81a45@31.220.76.131:26656,112fba64a7e5e27b0cf8f02c634334c957891abf@75.119.146.244:28656,e06519a36d7c780af9ad2be69616a98445112c7a@80.79.5.171:29656,c44a02dba51e23ac06b006fb1285988c89051ce7@85.10.198.171:26556,92b2e2f59cbbb11c601919f058575fbc50cb73c6@65.109.183.202:26656,f9af0186eec9a88a5a657deb9a7deff34c05d99f@86.111.48.156:26656,32d0eaa31ab8f9c2779ce9272b7a68f3d15a8e6e@213.239.207.175:40656,74a979f0df53ef6f2ba9ab77c0c9fc5ba9c2bdc5@213.239.215.59:29456,d9703df8c0e5eef6c0766217d611a13ed6ee8d95@88.99.33.248:26656,4f9120f706512162fbe4f39aac78b9924efbec58@65.109.92.235:11036,86868b056de4225ac7c1470e9d7ba2385b59a8bc@67.217.61.134:26656,4e96723af8feb8a515573a7b9391e7bf7d562480@194.163.162.155:26656,bb8c8cea499a1fa7e97922b5a9882c2360c6575a@176.103.222.21:26656,194ad0ab2f1003e123085300b0ca16d57e223be8@94.190.90.38:7060,0d08a1b452e6d7ccdfbc9b54658b5f9ed24eff7b@135.181.138.160:29956,84712b4b59bfdfb4d5818c6baa37ed5b5a8e87f8@85.239.243.211:26656,0adbe1e790b58d19cc53a9839059a95d7d5d7aba@65.109.70.23:19956,67dae0d05a857065afd0286d134cbed1c8e9de40@38.242.231.22:29656,bc2e99e6004bb0b87c72ca10f20cd1617edf70fe@141.94.73.93:56656,eb7832932626c1c636d16e0beb49e0e4498fbd5e@65.108.231.124:20656,e711b6631c3e5bb2f6c389cbc5d422912b05316b@213.239.216.252:33256,0df9cc98fd8e88920efd02425292813108e14a45@185.202.238.214:26656,8d949ac905cf8aa6902a72c8c1fb6bda5a7c4d69@65.108.200.60:21656,4732ed188fbe7603f81d9f4c825397277bb72217@5.75.235.195:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
