# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/teritori.png" width="150" alt=""><figcaption></figcaption></figure>

Teritori is a multi-chain hub designed to allow IBC and non IBC communities  to connect, trade services & NFTs, launch new projects & build further existing ones.

**Chain ID**: teritori-1 | **Latest Version Tag**: v1.3.0 | **Wasm**: ON

[Website](https://teritori.com) | [Discord](https://discord.gg/teritori) | [Twitter](https://twitter.com/TeritoriNetwork)

[![Stake with kjnodes](https://i.ibb.co/cr44Q8j/button-stake-with-kjnodes.png)](https://restake.app/teritori/torivaloper184ln03hkpt75uhrrr26f66kvcqvf4yn4nc2xjm)

## Restake

[Restake with kjnodes](https://restake.app/teritori/torivaloper184ln03hkpt75uhrrr26f66kvcqvf4yn4nc2xjm) (every 5 minutes)
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

**live-peers** (39)
```bash
peers="412afea7f33f6f91c85f8d149eff81acb6624bb3@195.201.63.87:42656,1f4e77295379ce0c928502d2b075157a8c8a9e64@51.83.96.150:26642,4b04b3d164dc6dd5bb555a7a106a8d314f30516f@65.21.136.170:53656,406fc7fe86ba396cb7fc8616c546f21a1d3c51cd@89.58.57.158:26656,12101148702a99298a971b310286e64bc7bb6135@65.109.23.182:38026,8ac41af54dfd91c41de71cde222a55670f2f405d@141.95.65.73:15956,920f32f409bbb18b641cdc9513545e2e016c2c62@142.132.203.60:26656,0b27217386756577e1eadf00c4169dc8f041e522@51.210.7.219:26656,ce3baba928ae06cd3ff0af20aec888a82ddffef7@54.37.129.171:26656,5057950d34b67a67325f02949703388c4a35c1dd@154.53.59.87:19656,5a98d637a16b16bf425a4a785c9d11a7d1e5b8a0@65.21.131.215:26736,48980875839186e08e12ebf0d9a2803b45206833@65.109.92.241:38026,6046cec27c36f0a7596cb9fa9f2c5decbd4e87cb@151.115.53.172:26656,856c165de82fbd0489df9ec6ffaa0958c620e073@198.244.179.127:26656,78815c81331c114cd508dae3a012f0d3e5e2b966@185.119.118.117:3000,46b7ae20e3cc4264076a91c3601f3894a021a80d@65.108.6.45:36656,2b4f46e601fb4ede2a0c98976337e3afdaa50dac@65.108.238.102:15956,b336b83d9bab0b8cf96a3833efcbc196fab63fdd@212.95.51.215:36656,82ebb17ddac20928fb8107201dad9f5aea7f9132@198.244.200.3:26656,e726816f42831689eab9378d5d577f1d06d25716@176.9.188.21:26656,c12c1ed98ab1f24266980c1f05ed0ca8812ca7aa@95.217.192.230:16656,e1b058e5cfa2b836ddaa496b10911da62dcf182e@138.201.8.248:26656,ec4126b26336cd61b335345df4ff2a3fbb79338a@65.109.92.240:20026,526d8c7c44f59be9a39d7463c576b68c0db23174@65.108.234.23:15956,35de81a10ed992e427e6eb1d0d9ec3622d0f37fe@193.70.47.90:15956,0e189bbc6db606a14950a0e59641b798a255c3c8@65.109.37.154:3000,3178ac8fffd269325500c95679d58d5e8ec61746@198.244.213.94:22956,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:19656,7ec495dc07533182ed7673f8aa68c03e05ffff44@51.79.27.21:28656,b3e9ad54d743ba8a465172f50b19cb52e77686c2@38.242.148.96:36656,40caa979c29a9930ea2b8a6249037924d308ae84@162.55.234.70:54256,e8cafb5a121c9fe322e554f5a7f489b2d25abd4c@51.159.153.113:26656,14fa46dbadd79647ebf3e5bc82326d2debc5fd52@51.159.176.185:26656,3594b73f909a9c4b87cfe6a361ef8b2b51124dd5@65.109.69.59:15956,d956d6180e96c62315a777b1a3ed8f1ebf873e80@38.242.232.202:29656,ad347ea1ec920d12ccda2341348bcc89687739ef@88.99.164.158:38026,20e1000e88125698264454a884812746c2eb4807@65.108.227.217:15956,ade4d8bc8cbe014af6ebdf3cb7b1e9ad36f412c0@135.181.5.219:15956,f97a75fb69d3a5fe893dca7c8d238ccc0bd66a8f@94.23.23.189:6969"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.teritorid/config/config.toml
```
