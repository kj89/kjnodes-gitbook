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

**live-peers** (39)
```bash
peers="14ae45e7f2ff7491cfa686a8fcac7cc095bc38ff@213.239.217.52:39656,9057ee9d3d9b3c42c184dc89a7b2a07026b81a45@31.220.76.131:26656,9d5802ec3e10fbac150850ffdfa50f324e804b95@95.214.55.62:35656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:44656,e0f25590f8074b4ea70f069f9be332b19f81f344@23.88.70.109:15656,e593c7a9ca61f5616119d6beb5bd8ef5dd28d62d@34.246.190.1:26656,6ba3b6ec03839afffa64c83e18ff80a681f4968d@65.108.194.40:21756,38093a87129f828125be65e8969bb7ede682b26c@38.242.197.134:26656,3177033dfc8a88c0b1a4500e2812c74f41e9a32b@94.130.236.21:26656,3a445bfdbe2d0c8ee82461633aa3af31bc2b4dc0@3.252.219.158:26656,d6a116d2aed64bd2f383b894e38f2a62232e44b7@116.202.161.165:36656,7adc61737172235479b405f61477a02be635fb21@62.171.188.69:26656,51aeaa2c757989f720c904023c2dbedfc720f75e@23.88.5.169:27656,f0758765ef0350d5cbbdeebf0b8e84f76e21c46d@54.221.204.97:26656,df06418afe0c3d6ebbe8cd233dc9bed02b87cc62@65.108.107.241:26656,b591ef22e0c2082eb76dcac5ead95be55d01b695@65.109.178.147:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@185.16.39.172:27066,75ed1e87b48d6e1ab341e3568708c9fb81743ffa@65.109.88.251:11036,f30d07170a092f82702e3c12334fa9fd828b71c6@168.119.124.130:47656,64df498c92b9ccaf78012229d399aa34a014f087@65.109.122.105:56659,0adbe1e790b58d19cc53a9839059a95d7d5d7aba@65.109.70.23:19956,194ad0ab2f1003e123085300b0ca16d57e223be8@94.190.90.38:7060,704db28ae8082ed936675e8eea9b5a71ba946241@18.212.181.61:26656,509eaf8341cca511c8a3127affaae2251593d514@161.97.148.146:56656,aebbf38433cc38ed3aad0bb5f2aa567797df78da@46.8.210.144:26756,eb7832932626c1c636d16e0beb49e0e4498fbd5e@65.108.231.124:20656,5e068fccd370b2f2e5ab4240a304323af6385f1f@172.93.110.154:27656,c19965fe8a1ea3391d61d09cf589bca0781d29fd@162.19.217.52:26656,0925c475208d8e338907383ab87a094ad03c478e@65.109.55.186:40656,35f045092f9c51ab743eec194438b91ecf8ce69e@65.109.116.22:11134,f4d6605ea7a9a88d2afaf6c2c13f00b77eb3239f@185.241.227.182:26656,d8900913c64c2d7894d13ba35fe6c3e7c346015a@95.31.224.15:36656,b62eb3baed171ab5654292e5e35d56a1287693c9@45.32.66.24:26656,f005d7d08cbd68237e320388c314bdc0e78280b3@38.242.153.231:26656,6b7bfa6f0297b231f40a9284d45282af93320315@65.109.116.50:28656,bc2e99e6004bb0b87c72ca10f20cd1617edf70fe@141.94.73.93:56656,f137232fd25d5c3adc6d3f6cffa879beafe17768@89.250.150.241:26656,0df9cc98fd8e88920efd02425292813108e14a45@185.202.238.214:26656,4634ca7cefe997035440df1095915ed255e81296@49.12.189.98:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
