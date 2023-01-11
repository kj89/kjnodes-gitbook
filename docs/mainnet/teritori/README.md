# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/teritori.png" width="150" alt=""><figcaption></figcaption></figure>

Teritori is a multi-chain hub designed to allow IBC and non IBC communities  to connect, trade services & NFTs, launch new projects & build further existing ones.

**Chain ID**: teritori-1 | **Latest Version Tag**: v1.3.0 | **Wasm**: ON

[Website](https://teritori.com) | [Discord](https://discord.gg/teritori) | [Twitter](https://twitter.com/TeritoriNetwork)

## Restake

[Restake with kjnodes](https://restake.app/teritori/torivaloper184ln03hkpt75uhrrr26f66kvcqvf4yn4nc2xjm) (every day at 08:00, 20:00)
## Public endpoints

* rpc: [https://teritori.rpc.kjnodes.com](https://teritori.rpc.kjnodes.com)
* api: [https://teritori.api.kjnodes.com](https://teritori.api.kjnodes.com)

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

**live-peers** (28)
```bash
peers="75d41a5ab4f826b7ba468a6c4912dbd8f4541428@65.108.200.142:26646,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:19656,7fb5a1a53f481f037487920ed08b0495158e2041@148.251.53.202:26796,efe721a953196d8c5f2375b86dcd54285aec565c@51.158.231.48:26656,920f32f409bbb18b641cdc9513545e2e016c2c62@142.132.203.60:26656,0b27217386756577e1eadf00c4169dc8f041e522@51.210.7.219:26656,26175f13ada3d61c93bca342819fd5dc797bced0@65.109.58.226:28656,406fc7fe86ba396cb7fc8616c546f21a1d3c51cd@89.58.57.158:26656,3594b73f909a9c4b87cfe6a361ef8b2b51124dd5@65.109.69.59:15956,856c165de82fbd0489df9ec6ffaa0958c620e073@198.244.179.127:26656,5a98d637a16b16bf425a4a785c9d11a7d1e5b8a0@65.21.131.215:26736,a25a3a218a699e71e2a64edaa45f457dfd8507ba@65.21.148.206:26656,46b7ae20e3cc4264076a91c3601f3894a021a80d@65.108.6.45:36656,b212d5740b2e11e54f56b072dc13b6134650cfb5@134.65.192.81:26656,722b63e6c65628b929f22013dcbcde980210cb44@176.9.127.54:26656,d856120f262134ebf13e1d2632d778b69e704208@65.108.4.188:15956,5057950d34b67a67325f02949703388c4a35c1dd@154.53.59.87:19656,d956d6180e96c62315a777b1a3ed8f1ebf873e80@38.242.232.202:29656,4b04b3d164dc6dd5bb555a7a106a8d314f30516f@65.21.136.170:53656,8ac41af54dfd91c41de71cde222a55670f2f405d@141.95.65.73:15956,8f28518afd31a42ea81bb3232a50ab0cec4dcdf7@51.158.236.131:26656,fffcd8c41a92e24d67b6d026f556c5afd49db092@45.77.41.21:26656,526d8c7c44f59be9a39d7463c576b68c0db23174@65.108.234.23:15956,94b63fddfc78230f51aeb7ac34b9fb86bd042a77@212.23.222.126:30552,1e08fefb7e8851490d40e804df76d1ac33cb1f0a@38.146.3.175:15956,34b87bdfc1f0b6a11724cf45dda3ee66c9a4691c@38.146.3.176:15956,6ef7a8bc7a3cc0856594f12570e8f2282a099dcf@65.109.93.152:26796,942c99cb9ff717552f884639dda9f52ab66f9726@65.108.134.12:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.teritorid/config/config.toml
```
