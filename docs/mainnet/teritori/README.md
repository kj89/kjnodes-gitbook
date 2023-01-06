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

**live-peers** (26)
```bash
peers="26175f13ada3d61c93bca342819fd5dc797bced0@65.109.58.226:28656,b212d5740b2e11e54f56b072dc13b6134650cfb5@134.65.192.81:26656,703714c82c94fc1c74b6ee0d1fc3417b932be5f3@169.155.168.57:26656,3178ac8fffd269325500c95679d58d5e8ec61746@198.244.213.94:22956,4d6c820a7d426ad934a5e51f2e020836f0378919@116.202.143.91:26656,e3b906fefa58783395fcf72086c698707908a558@141.95.65.26:27736,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:19656,8ac41af54dfd91c41de71cde222a55670f2f405d@141.95.65.73:15956,920f32f409bbb18b641cdc9513545e2e016c2c62@142.132.203.60:26656,0b27217386756577e1eadf00c4169dc8f041e522@51.210.7.219:26656,5a98d637a16b16bf425a4a785c9d11a7d1e5b8a0@65.21.131.215:26736,a7d96dc929824613315dcc1c90fee119f28cc51f@164.152.161.254:26656,d856120f262134ebf13e1d2632d778b69e704208@65.108.4.188:15956,a25a3a218a699e71e2a64edaa45f457dfd8507ba@65.21.148.206:26656,3594b73f909a9c4b87cfe6a361ef8b2b51124dd5@65.109.69.59:15956,6ef7a8bc7a3cc0856594f12570e8f2282a099dcf@65.109.93.152:26796,2afdb9300c47e43e555fa572d033b2d68ac28506@65.109.70.68:26686,526d8c7c44f59be9a39d7463c576b68c0db23174@65.108.234.23:15956,1f4e77295379ce0c928502d2b075157a8c8a9e64@51.83.96.150:26642,d956d6180e96c62315a777b1a3ed8f1ebf873e80@38.242.232.202:29656,942c99cb9ff717552f884639dda9f52ab66f9726@65.108.134.12:26656,89757803f40da51678451735445ad40d5b15e059@134.65.192.221:26656,5ab6437f73fe71f392d53566e037aa91087530ac@139.144.67.202:26656,46b7ae20e3cc4264076a91c3601f3894a021a80d@65.108.6.45:36656,ad347ea1ec920d12ccda2341348bcc89687739ef@88.99.164.158:38026,8f75bd347c90fbaa2c96eb187a413bb3751b3a7e@51.81.208.70:15956"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.teritorid/config/config.toml
```
