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
* grpc: https://teritori.grpc.kjnodes.com:443

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
peers="1f4e77295379ce0c928502d2b075157a8c8a9e64@51.83.96.150:26642,82ebb17ddac20928fb8107201dad9f5aea7f9132@198.244.200.3:26656,920f32f409bbb18b641cdc9513545e2e016c2c62@142.132.203.60:26656,26d6ee4138c7533c5541722c6e1ecc6d60d47a86@104.193.254.42:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:19656,46b7ae20e3cc4264076a91c3601f3894a021a80d@65.108.6.45:36656,856c165de82fbd0489df9ec6ffaa0958c620e073@198.244.179.127:26656,a25a3a218a699e71e2a64edaa45f457dfd8507ba@65.21.148.206:26656,8206037aba2622c284b8b229583a18c909709266@195.3.223.204:10656,0b27217386756577e1eadf00c4169dc8f041e522@51.210.7.219:26656,634a29ae2bd7ad8165d6ef66a6dea02d04c9bbed@65.108.77.250:26641,5a98d637a16b16bf425a4a785c9d11a7d1e5b8a0@65.21.131.215:26736,9c5393bb5611f8c3aaa0abde1ce753284c1428d0@141.95.34.175:27656,34b87bdfc1f0b6a11724cf45dda3ee66c9a4691c@38.146.3.176:15956,d956d6180e96c62315a777b1a3ed8f1ebf873e80@38.242.232.202:29656,d856120f262134ebf13e1d2632d778b69e704208@65.108.4.188:15956,88a407d4749e1ccbb630f98ca44f304744d97864@38.242.141.168:26656,8ac41af54dfd91c41de71cde222a55670f2f405d@141.95.65.73:15956,fffcd8c41a92e24d67b6d026f556c5afd49db092@45.77.41.21:26656,2afdb9300c47e43e555fa572d033b2d68ac28506@65.109.70.68:26686,7d47faa64cef3eca57ed3f4eaf21f7a3981d512b@57.128.65.115:28656,3594b73f909a9c4b87cfe6a361ef8b2b51124dd5@65.109.69.59:15956,526d8c7c44f59be9a39d7463c576b68c0db23174@65.108.234.23:15956,40caa979c29a9930ea2b8a6249037924d308ae84@162.55.234.70:54256,26175f13ada3d61c93bca342819fd5dc797bced0@65.109.58.226:28656,d2247f7b919f0781c90ee61958d7044665a22d38@169.155.44.201:26656,1f9293a286df733dac6303aad3c39240ad3b3796@178.211.139.24:46656,28ffbde471fa1c1bb848ab3c8ea4ecbf5833529a@81.196.253.241:17656,4740ad44e58f4f4a0e2b9c4353500009eb73a05a@176.191.97.120:26656,ca0d6b49b304c5f1c629809795f50440d5710b40@159.89.40.188:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.teritorid/config/config.toml
```
