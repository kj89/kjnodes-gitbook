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

**live-peers** (33)
```bash
peers="d856120f262134ebf13e1d2632d778b69e704208@65.108.4.188:15956,3178ac8fffd269325500c95679d58d5e8ec61746@198.244.213.94:22956,88a407d4749e1ccbb630f98ca44f304744d97864@38.242.141.168:26656,920f32f409bbb18b641cdc9513545e2e016c2c62@142.132.203.60:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:19656,ce3baba928ae06cd3ff0af20aec888a82ddffef7@54.37.129.171:26656,12101148702a99298a971b310286e64bc7bb6135@65.109.23.182:38026,a25a3a218a699e71e2a64edaa45f457dfd8507ba@65.21.148.206:26656,593b8319d1d4b1958e7daba8c3bbb56795cb59ba@146.59.81.92:51656,48980875839186e08e12ebf0d9a2803b45206833@65.109.92.241:38026,24b28cf013e6d7b5b88b6dba2701c5ddd2dd5ee1@65.109.58.225:28656,89757803f40da51678451735445ad40d5b15e059@134.65.192.221:26656,26d6ee4138c7533c5541722c6e1ecc6d60d47a86@104.193.254.42:26656,5a98d637a16b16bf425a4a785c9d11a7d1e5b8a0@65.21.131.215:26736,856c165de82fbd0489df9ec6ffaa0958c620e073@198.244.179.127:26656,40caa979c29a9930ea2b8a6249037924d308ae84@162.55.234.70:54256,1f858b8cc8e18ef05de79dd470ad29ba29ddbeb7@65.108.77.106:26889,0e189bbc6db606a14950a0e59641b798a255c3c8@65.109.37.154:3000,3594b73f909a9c4b87cfe6a361ef8b2b51124dd5@65.109.69.59:15956,526d8c7c44f59be9a39d7463c576b68c0db23174@65.108.234.23:15956,78815c81331c114cd508dae3a012f0d3e5e2b966@185.119.118.117:3000,ec4126b26336cd61b335345df4ff2a3fbb79338a@65.109.92.240:20026,e1b058e5cfa2b836ddaa496b10911da62dcf182e@138.201.8.248:26656,8ac41af54dfd91c41de71cde222a55670f2f405d@141.95.65.73:15956,46b7ae20e3cc4264076a91c3601f3894a021a80d@65.108.6.45:36656,e726816f42831689eab9378d5d577f1d06d25716@176.9.188.21:26656,ad347ea1ec920d12ccda2341348bcc89687739ef@88.99.164.158:38026,2b4f46e601fb4ede2a0c98976337e3afdaa50dac@65.108.238.102:15956,d29bed885306037dbe219278415025a2ea8880a4@51.159.160.140:26656,0b27217386756577e1eadf00c4169dc8f041e522@51.210.7.219:26656,5057950d34b67a67325f02949703388c4a35c1dd@154.53.59.87:19656,d956d6180e96c62315a777b1a3ed8f1ebf873e80@38.242.232.202:29656,4b04b3d164dc6dd5bb555a7a106a8d314f30516f@65.21.136.170:53656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.teritorid/config/config.toml
```
