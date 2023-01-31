# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/teritori.png" width="150" alt=""><figcaption></figcaption></figure>

Teritori is a multi-chain hub designed to allow IBC and non IBC communities  to connect, trade services & NFTs, launch new projects & build further existing ones.

**Chain ID**: teritori-1 | **Latest Version Tag**: v1.3.0 | **Wasm**: ON

[Website](https://teritori.com) | [Discord](https://discord.gg/teritori) | [Twitter](https://twitter.com/TeritoriNetwork)

[![Stake with kjnodes](https://i.ibb.co/cr44Q8j/button-stake-with-kjnodes.png)](https://restake.app/teritori/torivaloper184ln03hkpt75uhrrr26f66kvcqvf4yn4nc2xjm)

## Restake

[Restake with kjnodes](https://restake.app/teritori/torivaloper184ln03hkpt75uhrrr26f66kvcqvf4yn4nc2xjm) (every day at 08:00, 20:00)
## Chain explorer
[https://explorer.kjnodes.com/teritori](https://explorer.kjnodes.com/teritori)

## Public endpoints

* api: [https://teritori.api.kjnodes.com](https://teritori.api.kjnodes.com)
* rpc: [https://teritori.rpc.kjnodes.com](https://teritori.rpc.kjnodes.com)
* grpc: [https://teritori.grpc.kjnodes.com](https://teritori.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@teritori.rpc.kjnodes.com:19656
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@teritori.rpc.kjnodes.com:19659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/teritori/addrbook.json > $HOME/.teritorid/config/addrbook.json
```

**live-peers** (35)
```bash
peers="24b28cf013e6d7b5b88b6dba2701c5ddd2dd5ee1@65.109.58.225:28656,a043a97266360ff45781a9fc9392aedc16494c59@65.108.97.58:19656,ce3baba928ae06cd3ff0af20aec888a82ddffef7@54.37.129.171:26656,c124ce0b508e8b9ed1c5b6957f362225659b5343@169.155.168.57:26656,82ebb17ddac20928fb8107201dad9f5aea7f9132@198.244.200.3:26656,12101148702a99298a971b310286e64bc7bb6135@65.109.23.182:38026,ec4126b26336cd61b335345df4ff2a3fbb79338a@65.109.92.240:20026,0e189bbc6db606a14950a0e59641b798a255c3c8@65.109.37.154:3000,920f32f409bbb18b641cdc9513545e2e016c2c62@142.132.203.60:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:19656,88a407d4749e1ccbb630f98ca44f304744d97864@38.242.141.168:26656,e1b058e5cfa2b836ddaa496b10911da62dcf182e@138.201.8.248:26656,48980875839186e08e12ebf0d9a2803b45206833@65.109.92.241:38026,8ac41af54dfd91c41de71cde222a55670f2f405d@141.95.65.73:15956,4d6c820a7d426ad934a5e51f2e020836f0378919@116.202.143.91:26656,78815c81331c114cd508dae3a012f0d3e5e2b966@185.119.118.117:3000,d856120f262134ebf13e1d2632d778b69e704208@65.108.4.188:15956,46b7ae20e3cc4264076a91c3601f3894a021a80d@65.108.6.45:36656,a25a3a218a699e71e2a64edaa45f457dfd8507ba@65.21.148.206:26656,16f90d350de14a596ebdc683ce5e703c14e40bb3@75.119.146.181:19656,e726816f42831689eab9378d5d577f1d06d25716@176.9.188.21:26656,526d8c7c44f59be9a39d7463c576b68c0db23174@65.108.234.23:15956,856c165de82fbd0489df9ec6ffaa0958c620e073@198.244.179.127:26656,4b04b3d164dc6dd5bb555a7a106a8d314f30516f@65.21.136.170:53656,fd545a1e10bf9ef03a58bbdaf039df36d1115548@65.108.226.44:33656,4740ad44e58f4f4a0e2b9c4353500009eb73a05a@176.191.97.120:26656,1e08fefb7e8851490d40e804df76d1ac33cb1f0a@38.146.3.175:15956,0b27217386756577e1eadf00c4169dc8f041e522@51.210.7.219:26656,2b4f46e601fb4ede2a0c98976337e3afdaa50dac@65.108.238.102:15956,230ce8f6c8234593dcea673768c26cdcc4f91172@65.144.145.234:26656,b336b83d9bab0b8cf96a3833efcbc196fab63fdd@212.95.51.215:36656,ca0d6b49b304c5f1c629809795f50440d5710b40@159.89.40.188:26656,d956d6180e96c62315a777b1a3ed8f1ebf873e80@38.242.232.202:29656,ad347ea1ec920d12ccda2341348bcc89687739ef@88.99.164.158:38026,5a98d637a16b16bf425a4a785c9d11a7d1e5b8a0@65.21.131.215:26736"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.teritorid/config/config.toml
```
