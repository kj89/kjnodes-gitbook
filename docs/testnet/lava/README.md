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

**live-peers** (37)
```bash
peers="9d5802ec3e10fbac150850ffdfa50f324e804b95@95.214.55.62:35656,14ae45e7f2ff7491cfa686a8fcac7cc095bc38ff@213.239.217.52:39656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:44656,f68c57ca955420779773f9320a6b7710c2b29f73@188.191.36.222:26656,34271a6f82d755777a3db02be39e575bf4ebd415@65.109.30.197:28656,6ba3b6ec03839afffa64c83e18ff80a681f4968d@65.108.194.40:21756,d83043d1e14156d78722877b6f449e93b46ce871@142.132.152.46:44656,f9af0186eec9a88a5a657deb9a7deff34c05d99f@86.111.48.156:26656,4fc42fdf634ef542094c7a44f22e031acea61162@91.77.165.172:27656,5d55031717267b74a2d8110a6962d0fda48d583a@95.216.188.101:26656,10c4405d04b2a221959de97f69c9a6258676f55d@161.97.79.100:26656,5bdbd9a68d212ec341c781cc553043486ce5b8ee@31.220.76.135:26656,bc2e99e6004bb0b87c72ca10f20cd1617edf70fe@141.94.73.93:56656,e593c7a9ca61f5616119d6beb5bd8ef5dd28d62d@34.246.190.1:26656,3a445bfdbe2d0c8ee82461633aa3af31bc2b4dc0@3.252.219.158:26656,509eaf8341cca511c8a3127affaae2251593d514@161.97.148.146:56656,92b2e2f59cbbb11c601919f058575fbc50cb73c6@65.109.183.202:26656,e06519a36d7c780af9ad2be69616a98445112c7a@80.79.5.171:29656,d9703df8c0e5eef6c0766217d611a13ed6ee8d95@88.99.33.248:26656,bd1e1f8df77e7b61200c490c9fabe6bbc4412d4e@91.223.3.144:26856,112fba64a7e5e27b0cf8f02c634334c957891abf@75.119.146.244:28656,fcbe43af6ef40fca686af83e13a8b03d1a6046e6@135.181.178.53:56656,0314d53cc790860fb51f36ac656a19789800ce5c@176.103.222.20:26656,f642b376722d6ce104ffd4c204e78ffe811e16c3@5.75.230.221:26656,f6a3fcd1910ab808192c4c40a29fa0e85cd874cd@52.18.46.103:26656,0f9f0fb4b9371a65bdf1c883a2a7dc52d0023019@34.233.69.21:26656,433be6210ad6350bebebad68ec50d3e0d90cb305@217.13.223.167:60856,30da6072679c936f66c07ae022191e9541027d1d@116.203.186.209:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@185.16.39.172:27066,d6a116d2aed64bd2f383b894e38f2a62232e44b7@116.202.161.165:36656,eb7832932626c1c636d16e0beb49e0e4498fbd5e@65.108.231.124:20656,aadb410edcde075bbb449c25a9125c0b992e76ad@31.220.76.133:26656,5c744987d17199b2f07efd7bad9d9466d1a457a4@80.76.235.194:7054,0df9cc98fd8e88920efd02425292813108e14a45@185.202.238.214:26656,dd39aa607ab19d57a12fb71e7a5df36cef8d3405@185.48.24.106:26656,0925c475208d8e338907383ab87a094ad03c478e@65.109.55.186:40656,b62eb3baed171ab5654292e5e35d56a1287693c9@45.32.66.24:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
