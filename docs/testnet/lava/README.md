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

**live-peers** (38)
```bash
peers="24a2bb2d06343b0f74ed0a6dc1d409ce0d996451@188.40.98.169:27656,14ae45e7f2ff7491cfa686a8fcac7cc095bc38ff@213.239.217.52:39656,fe1998168f5336811a79fbcaf2d5d5a69f2f9f63@65.108.81.145:26656,ddafabd9760011a797952ab62c50b758f83ea7ca@65.109.112.20:11144,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:44656,5c2a752c9b1952dbed075c56c600c3a79b58c395@185.16.39.172:27066,3c47fd1662bcb17a4713c23e41d7b25e34478b8e@103.19.25.157:26672,3a445bfdbe2d0c8ee82461633aa3af31bc2b4dc0@3.252.219.158:26656,7c1b4625e9be15151bd4c977140aa3fe601f0456@65.108.97.58:2996,eb7832932626c1c636d16e0beb49e0e4498fbd5e@65.108.231.124:20656,0c548b2704594c7929b713de4c6985b9d9f03b8a@194.163.184.46:27656,e593c7a9ca61f5616119d6beb5bd8ef5dd28d62d@34.246.190.1:26656,18432dbb1238c416053bcbbc7b85b5f1258010a0@193.34.212.34:11134,b591ef22e0c2082eb76dcac5ead95be55d01b695@65.109.178.147:26656,a5c1d2e86c2dc0eecb009dc71c92d6b5e193db6b@35.210.166.150:26656,fb2b9d41678f3d1c9c0bdef1a87f2037b6b0088a@146.19.24.252:26666,bebd03c6319c0930400dc564e9f5365068497322@95.217.41.15:26656,d3eb474a1f90d004e49638e384069c32d7dcc8a2@185.252.232.110:26656,f31c4dc121f37db1e0e24b49584bbbe4bbbba6c4@162.55.39.16:36656,dfa93668152cb6b3a822c987f9c22110a1c2f314@178.18.255.221:26656,0a528da95ca8025ef4043b6e73f1e789f4102940@176.103.222.22:26656,ba028c47672824bc64e1c66f0d8217c3d7426115@77.91.123.187:26656,4373d820675ffcad758892bbd8e442d545cb1f4b@86.111.48.155:26656,f30d07170a092f82702e3c12334fa9fd828b71c6@168.119.124.130:47656,fd72e2c2418ea30da3771d6a66893cb4c7ac4263@5.189.137.33:26656,0a78dd75926983ba06de451480673487ffa1bcc1@199.175.98.106:26656,4fc42fdf634ef542094c7a44f22e031acea61162@91.77.165.172:27656,0adbe1e790b58d19cc53a9839059a95d7d5d7aba@65.109.70.23:19956,160000efb6293c89e411ac81b086f8a9fe0c770a@161.97.144.208:26656,2ba64fe3a65f6b22f6e9c63e63ef3af20e813100@5.161.178.136:26656,e84082d8c5273ffb92baeb7da9ef78e05b0e2d5d@109.123.255.86:26656,54dcc266dc66a79866f55aac1f2ae33a3f4d7f9e@65.109.224.188:26656,e6703109f87389aea6b1ca9b8335a6eddbce50d6@185.182.186.85:26656,3a0f10539eb8e0f46432564edaf6303bd67c18f3@23.88.71.247:26656,e711b6631c3e5bb2f6c389cbc5d422912b05316b@213.239.216.252:33256,c5c98017339ce6d4d5d2a4fd0fb1aaeb966ef0f7@65.108.124.57:36656,d60e577b6dbdac7a7cd620f71a6bff71f9f82c2e@146.19.24.242:26656,4634ca7cefe997035440df1095915ed255e81296@49.12.189.98:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
