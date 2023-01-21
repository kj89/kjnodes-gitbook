# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/teritori.png" width="150" alt=""><figcaption></figcaption></figure>

Teritori is a multi-chain hub designed to allow IBC and non IBC communities  to connect, trade services & NFTs, launch new projects & build further existing ones.

**Chain ID**: teritori-1 | **Latest Version Tag**: v1.3.0 | **Wasm**: ON

[Website](https://teritori.com) | [Discord](https://discord.gg/teritori) | [Twitter](https://twitter.com/TeritoriNetwork)

[Explorer](https://explorer.kjnodes.com/teritori)

## Restake

[Restake with kjnodes](https://restake.app/teritori/torivaloper184ln03hkpt75uhrrr26f66kvcqvf4yn4nc2xjm) (every day at 08:00, 20:00)
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

**live-peers** (36)
```bash
peers="fffcd8c41a92e24d67b6d026f556c5afd49db092@45.77.41.21:26656,634a29ae2bd7ad8165d6ef66a6dea02d04c9bbed@65.108.77.250:26641,8480ce1f929a9410567d315a5b3fc2709c2807a7@93.115.25.106:51656,1e08fefb7e8851490d40e804df76d1ac33cb1f0a@38.146.3.175:15956,920f32f409bbb18b641cdc9513545e2e016c2c62@142.132.203.60:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:19656,2f93424bd346b857bd5164eaac0b2bfd5fd644c0@144.91.127.252:26656,526d8c7c44f59be9a39d7463c576b68c0db23174@65.108.234.23:15956,48980875839186e08e12ebf0d9a2803b45206833@65.109.92.241:38026,0b27217386756577e1eadf00c4169dc8f041e522@51.210.7.219:26656,fec9760fec02405039ee0e90f80322b893e4ccef@65.144.145.234:26656,856c165de82fbd0489df9ec6ffaa0958c620e073@198.244.179.127:26656,5a98d637a16b16bf425a4a785c9d11a7d1e5b8a0@65.21.131.215:26736,8ac41af54dfd91c41de71cde222a55670f2f405d@141.95.65.73:15956,46b7ae20e3cc4264076a91c3601f3894a021a80d@65.108.6.45:36656,a25a3a218a699e71e2a64edaa45f457dfd8507ba@65.21.148.206:26656,26d6ee4138c7533c5541722c6e1ecc6d60d47a86@104.193.254.42:26656,ec4126b26336cd61b335345df4ff2a3fbb79338a@65.109.92.240:20026,0e189bbc6db606a14950a0e59641b798a255c3c8@65.109.37.154:3000,bbc594f0a8424368b869fef47a18d6e35965db2e@176.9.188.21:26656,d856120f262134ebf13e1d2632d778b69e704208@65.108.4.188:15956,5057950d34b67a67325f02949703388c4a35c1dd@154.53.59.87:19656,e1b058e5cfa2b836ddaa496b10911da62dcf182e@138.201.8.248:26656,78815c81331c114cd508dae3a012f0d3e5e2b966@185.119.118.117:3000,a043a97266360ff45781a9fc9392aedc16494c59@65.108.97.58:19656,3594b73f909a9c4b87cfe6a361ef8b2b51124dd5@65.109.69.59:15956,a35dc0cd0efd7e04d3334d781112bae0698a8f57@164.92.131.1:26656,4b04b3d164dc6dd5bb555a7a106a8d314f30516f@65.21.136.170:53656,6ef7a8bc7a3cc0856594f12570e8f2282a099dcf@65.109.93.152:26796,d29bed885306037dbe219278415025a2ea8880a4@51.159.160.140:26656,ce3baba928ae06cd3ff0af20aec888a82ddffef7@54.37.129.171:26656,44b2bf9d970aece0531d3d939c5c546a7ac9201a@34.219.76.190:26656,2b4f46e601fb4ede2a0c98976337e3afdaa50dac@65.108.238.102:15956,51eaf493facf36754411baa4f7b89355bd9cb3e7@195.201.63.87:42666,20e1000e88125698264454a884812746c2eb4807@65.108.227.217:15956,d956d6180e96c62315a777b1a3ed8f1ebf873e80@38.242.232.202:29656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.teritorid/config/config.toml
```
