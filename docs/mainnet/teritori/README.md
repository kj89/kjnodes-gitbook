# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/teritori.png" width="150" alt=""><figcaption></figcaption></figure>

Teritori is a multi-chain hub designed to allow IBC and non IBC communities  to connect, trade services & NFTs, launch new projects & build further existing ones.

**Chain ID**: teritori-1 | **Latest Version Tag**: v1.3.0 | **Wasm**: ON

[Website](https://teritori.com) | [Discord](https://discord.gg/teritori) | [Twitter](https://twitter.com/TeritoriNetwork)

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

**live-peers** (30)
```bash
peers="5a98d637a16b16bf425a4a785c9d11a7d1e5b8a0@65.21.131.215:26736,44b2bf9d970aece0531d3d939c5c546a7ac9201a@34.219.76.190:26656,8ac41af54dfd91c41de71cde222a55670f2f405d@141.95.65.73:15956,920f32f409bbb18b641cdc9513545e2e016c2c62@142.132.203.60:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:19656,a25a3a218a699e71e2a64edaa45f457dfd8507ba@65.21.148.206:26656,26175f13ada3d61c93bca342819fd5dc797bced0@65.109.58.226:28656,46b7ae20e3cc4264076a91c3601f3894a021a80d@65.108.6.45:36656,ce3baba928ae06cd3ff0af20aec888a82ddffef7@54.37.129.171:26656,526d8c7c44f59be9a39d7463c576b68c0db23174@65.108.234.23:15956,009e25e99e3f8fde86d283d4b8b0ce2f777cde53@138.201.8.248:53656,d856120f262134ebf13e1d2632d778b69e704208@65.108.4.188:15956,6ef7a8bc7a3cc0856594f12570e8f2282a099dcf@65.109.93.152:26796,856c165de82fbd0489df9ec6ffaa0958c620e073@198.244.179.127:26656,40caa979c29a9930ea2b8a6249037924d308ae84@162.55.234.70:54256,48980875839186e08e12ebf0d9a2803b45206833@65.109.92.241:38026,fec9760fec02405039ee0e90f80322b893e4ccef@65.144.145.234:26656,0b27217386756577e1eadf00c4169dc8f041e522@51.210.7.219:26656,3bd3a20d7c8a26a20927289a7a6bffecf71de53e@51.81.155.97:10856,2f93424bd346b857bd5164eaac0b2bfd5fd644c0@144.91.127.252:26656,24b28cf013e6d7b5b88b6dba2701c5ddd2dd5ee1@65.109.58.225:28656,593b8319d1d4b1958e7daba8c3bbb56795cb59ba@146.59.81.92:51656,703714c82c94fc1c74b6ee0d1fc3417b932be5f3@169.155.168.57:26656,51eaf493facf36754411baa4f7b89355bd9cb3e7@195.201.63.87:42666,94b63fddfc78230f51aeb7ac34b9fb86bd042a77@212.23.222.126:30552,3178ac8fffd269325500c95679d58d5e8ec61746@198.244.213.94:22956,ec4126b26336cd61b335345df4ff2a3fbb79338a@65.109.92.240:20026,ca0d6b49b304c5f1c629809795f50440d5710b40@159.89.40.188:26656,20e1000e88125698264454a884812746c2eb4807@65.108.227.217:15956,d956d6180e96c62315a777b1a3ed8f1ebf873e80@38.242.232.202:29656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.teritorid/config/config.toml
```
