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
peers="526d8c7c44f59be9a39d7463c576b68c0db23174@65.108.234.23:15956,920f32f409bbb18b641cdc9513545e2e016c2c62@142.132.203.60:26656,94b63fddfc78230f51aeb7ac34b9fb86bd042a77@212.23.222.126:30552,ce3baba928ae06cd3ff0af20aec888a82ddffef7@54.37.129.171:26656,ec4126b26336cd61b335345df4ff2a3fbb79338a@65.109.92.240:20026,0e189bbc6db606a14950a0e59641b798a255c3c8@65.109.37.154:3000,0b27217386756577e1eadf00c4169dc8f041e522@51.210.7.219:26656,e726816f42831689eab9378d5d577f1d06d25716@176.9.188.21:26656,c12c1ed98ab1f24266980c1f05ed0ca8812ca7aa@95.217.192.230:16656,5a98d637a16b16bf425a4a785c9d11a7d1e5b8a0@65.21.131.215:26736,78815c81331c114cd508dae3a012f0d3e5e2b966@185.119.118.117:3000,46b7ae20e3cc4264076a91c3601f3894a021a80d@65.108.6.45:36656,6085c32b26fb1baa4b16b426f5d56f2fff81cfc7@135.181.165.246:26656,3594b73f909a9c4b87cfe6a361ef8b2b51124dd5@65.109.69.59:15956,3178ac8fffd269325500c95679d58d5e8ec61746@198.244.213.94:22956,b3e9ad54d743ba8a465172f50b19cb52e77686c2@38.242.148.96:36656,48980875839186e08e12ebf0d9a2803b45206833@65.109.92.241:38026,12101148702a99298a971b310286e64bc7bb6135@65.109.23.182:38026,2b4f46e601fb4ede2a0c98976337e3afdaa50dac@65.108.238.102:15956,e1b058e5cfa2b836ddaa496b10911da62dcf182e@138.201.8.248:26656,5ab6437f73fe71f392d53566e037aa91087530ac@139.144.67.202:26656,106490318e51355bc6d72e7941a0080f8b8256b9@185.16.39.14:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:19656,8ac41af54dfd91c41de71cde222a55670f2f405d@141.95.65.73:15956,88a407d4749e1ccbb630f98ca44f304744d97864@38.242.141.168:26656,3bd3a20d7c8a26a20927289a7a6bffecf71de53e@51.81.155.97:10856,14fa46dbadd79647ebf3e5bc82326d2debc5fd52@51.159.176.185:26656,e3374c3d25a36f06662fa150043e5e6529d11570@88.198.32.17:31656,6ef7a8bc7a3cc0856594f12570e8f2282a099dcf@65.109.93.152:26796,82ebb17ddac20928fb8107201dad9f5aea7f9132@198.244.200.3:26656,c670830fdf60374f008fa4a4eb851deddcdaef5b@65.109.88.107:46656,35de81a10ed992e427e6eb1d0d9ec3622d0f37fe@193.70.47.90:15956,f813a00f52de54a49aea3211b89a65ae6133eac2@88.99.167.148:26686,4991cc04c48f96dec265464d5cf276e16f6b302c@5.95.112.194:26656,ad347ea1ec920d12ccda2341348bcc89687739ef@88.99.164.158:38026,669470aba9778ccccd07127115dcdc30e141d7ae@65.108.232.248:33656,1f858b8cc8e18ef05de79dd470ad29ba29ddbeb7@65.108.77.106:26889,d956d6180e96c62315a777b1a3ed8f1ebf873e80@38.242.232.202:29656,9755cab2585a2794453a5b396ef13b893393366f@65.108.212.224:46674"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.teritorid/config/config.toml
```
