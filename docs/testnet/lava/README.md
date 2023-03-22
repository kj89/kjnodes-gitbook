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

**live-peers** (35)
```bash
peers="24a2bb2d06343b0f74ed0a6dc1d409ce0d996451@188.40.98.169:27656,aebbf38433cc38ed3aad0bb5f2aa567797df78da@46.8.210.144:26756,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:44656,f9af0186eec9a88a5a657deb9a7deff34c05d99f@86.111.48.156:26656,71b55ea92787a99e766ee5f6177db0464421cff5@92.255.253.6:56656,eb7832932626c1c636d16e0beb49e0e4498fbd5e@65.108.231.124:20656,9057ee9d3d9b3c42c184dc89a7b2a07026b81a45@31.220.76.131:26656,14ae45e7f2ff7491cfa686a8fcac7cc095bc38ff@213.239.217.52:39656,9d5802ec3e10fbac150850ffdfa50f324e804b95@95.214.55.62:35656,dfa93668152cb6b3a822c987f9c22110a1c2f314@178.18.255.221:26656,f30d07170a092f82702e3c12334fa9fd828b71c6@168.119.124.130:47656,5a469a75fb05eddf2d79fb17063cc59e84d0821a@207.180.236.115:34656,3a445bfdbe2d0c8ee82461633aa3af31bc2b4dc0@3.252.219.158:26656,a7944b8f0953e703d301670a9aa5312f3edf8cf4@65.109.106.91:24656,e593c7a9ca61f5616119d6beb5bd8ef5dd28d62d@34.246.190.1:26656,799077b3a3b52094ab3ca19b6a7ecab89c50cb61@185.144.99.97:26657,e5f324d671e8bba44cd8eef2cb5b6e46ccf4f95a@65.108.199.120:60756,d796c20b5bdb8f1633c2a13afbf12314a77b668c@91.107.148.113:26656,4c86262ed00a1d42c6654967589ca57143f950d4@68.183.82.151:26656,10c4405d04b2a221959de97f69c9a6258676f55d@161.97.79.100:26656,4fc42fdf634ef542094c7a44f22e031acea61162@91.77.165.172:27656,64df498c92b9ccaf78012229d399aa34a014f087@65.109.122.105:56659,cb0d27cf52862191d9f2498f6f4ac808c76d2640@52.253.118.45:26656,35f045092f9c51ab743eec194438b91ecf8ce69e@65.109.116.22:11134,aef95e720e422b5bdf540fe90221fd5ba2e5e7e9@194.163.138.173:26656,bf7aef75c35725f89f31c12197100a1dd91b3174@146.190.47.103:26656,cb722cc36541920d3907cd67743db5444f53e80b@95.70.184.178:24656,d7c350f9b16111f04a5fe391ec8ccbed5faee56e@86.48.1.218:26656,e77870b8732c952f40813e4e622cc2f108fd0223@154.53.55.153:26656,bb8c8cea499a1fa7e97922b5a9882c2360c6575a@176.103.222.21:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@185.16.39.172:27066,433be6210ad6350bebebad68ec50d3e0d90cb305@217.13.223.167:60856,c13b120d588c86008dc4ea5e3633b93c01831124@80.79.5.171:31656,ab924e7944c332bd1b52c8733e262bbdd33cb5ac@116.202.165.53:26656,6b7bfa6f0297b231f40a9284d45282af93320315@65.109.116.50:28656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
