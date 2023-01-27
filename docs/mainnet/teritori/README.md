# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/teritori.png" width="150" alt=""><figcaption></figcaption></figure>

Teritori is a multi-chain hub designed to allow IBC and non IBC communities  to connect, trade services & NFTs, launch new projects & build further existing ones.

**Chain ID**: teritori-1 | **Latest Version Tag**: v1.3.0 | **Wasm**: ON

[Website](https://teritori.com) | [Discord](https://discord.gg/teritori) | [Twitter](https://twitter.com/TeritoriNetwork)

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

**live-peers** (34)
```bash
peers="43da931d00da102c002e0a227de7258b8fb1871a@144.126.135.53:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:19656,920f32f409bbb18b641cdc9513545e2e016c2c62@142.132.203.60:26656,d40face481bc00a617d9a29c39be412a776e28c2@116.202.36.240:10656,ec4126b26336cd61b335345df4ff2a3fbb79338a@65.109.92.240:20026,e726816f42831689eab9378d5d577f1d06d25716@176.9.188.21:26656,526d8c7c44f59be9a39d7463c576b68c0db23174@65.108.234.23:15956,82ebb17ddac20928fb8107201dad9f5aea7f9132@198.244.200.3:26656,46b7ae20e3cc4264076a91c3601f3894a021a80d@65.108.6.45:36656,e1b058e5cfa2b836ddaa496b10911da62dcf182e@138.201.8.248:26656,856c165de82fbd0489df9ec6ffaa0958c620e073@198.244.179.127:26656,78815c81331c114cd508dae3a012f0d3e5e2b966@185.119.118.117:3000,5a98d637a16b16bf425a4a785c9d11a7d1e5b8a0@65.21.131.215:26736,ce3baba928ae06cd3ff0af20aec888a82ddffef7@54.37.129.171:26656,6060a7c4f09dd7315f2c59b0c516f71e6e719a76@51.89.7.234:26642,48980875839186e08e12ebf0d9a2803b45206833@65.109.92.241:38026,0b27217386756577e1eadf00c4169dc8f041e522@51.210.7.219:26656,d856120f262134ebf13e1d2632d778b69e704208@65.108.4.188:15956,0e189bbc6db606a14950a0e59641b798a255c3c8@65.109.37.154:3000,3594b73f909a9c4b87cfe6a361ef8b2b51124dd5@65.109.69.59:15956,3178ac8fffd269325500c95679d58d5e8ec61746@198.244.213.94:22956,88a407d4749e1ccbb630f98ca44f304744d97864@38.242.141.168:26656,3bd3a20d7c8a26a20927289a7a6bffecf71de53e@51.81.155.97:10856,a25a3a218a699e71e2a64edaa45f457dfd8507ba@65.21.148.206:26656,1e08fefb7e8851490d40e804df76d1ac33cb1f0a@38.146.3.175:15956,5057950d34b67a67325f02949703388c4a35c1dd@154.53.59.87:19656,8ac41af54dfd91c41de71cde222a55670f2f405d@141.95.65.73:15956,1f9293a286df733dac6303aad3c39240ad3b3796@178.211.139.24:46656,2b4f46e601fb4ede2a0c98976337e3afdaa50dac@65.108.238.102:15956,b78dd48a9d34146f04801f479a82348a19a69ab7@51.159.185.141:26656,106490318e51355bc6d72e7941a0080f8b8256b9@185.16.39.14:26656,5ab6437f73fe71f392d53566e037aa91087530ac@139.144.67.202:26656,4740ad44e58f4f4a0e2b9c4353500009eb73a05a@176.191.97.120:26656,ed747c9e39fc04fdbc7ab5fc4a4a7f7a298ee329@65.144.145.234:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.teritorid/config/config.toml
```
