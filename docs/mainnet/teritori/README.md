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

```
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@teritori.rpc.kjnodes.com:19656
```

**seed-node**

```
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@teritori.rpc.kjnodes.com:19659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/teritori/addrbook.json > $HOME/.teritorid/config/addrbook.json
```

**live-peers** (30)
```
peers="5a98d637a16b16bf425a4a785c9d11a7d1e5b8a0@65.21.131.215:26736,4b04b3d164dc6dd5bb555a7a106a8d314f30516f@65.21.136.170:53656,d856120f262134ebf13e1d2632d778b69e704208@65.108.4.188:15956,88a407d4749e1ccbb630f98ca44f304744d97864@38.242.141.168:26656,526d8c7c44f59be9a39d7463c576b68c0db23174@65.108.234.23:15956,51eaf493facf36754411baa4f7b89355bd9cb3e7@195.201.63.87:42666,920f32f409bbb18b641cdc9513545e2e016c2c62@142.132.203.60:26656,8ac41af54dfd91c41de71cde222a55670f2f405d@141.95.65.73:15956,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:19656,0b27217386756577e1eadf00c4169dc8f041e522@51.210.7.219:26656,6ef7a8bc7a3cc0856594f12570e8f2282a099dcf@65.109.93.152:26796,a25a3a218a699e71e2a64edaa45f457dfd8507ba@65.21.148.206:26656,26175f13ada3d61c93bca342819fd5dc797bced0@65.109.58.226:28656,3178ac8fffd269325500c95679d58d5e8ec61746@198.244.213.94:22956,40caa979c29a9930ea2b8a6249037924d308ae84@162.55.234.70:54256,d956d6180e96c62315a777b1a3ed8f1ebf873e80@38.242.232.202:29656,3594b73f909a9c4b87cfe6a361ef8b2b51124dd5@65.109.69.59:15956,a7d96dc929824613315dcc1c90fee119f28cc51f@164.152.161.254:26656,89757803f40da51678451735445ad40d5b15e059@134.65.192.221:26656,2b4f46e601fb4ede2a0c98976337e3afdaa50dac@65.108.238.102:15956,703714c82c94fc1c74b6ee0d1fc3417b932be5f3@169.155.168.57:26656,35cdec21668ac214c74a6e45d444f6933f094bc4@144.202.72.17:26646,24b28cf013e6d7b5b88b6dba2701c5ddd2dd5ee1@65.109.58.225:28656,82ebb17ddac20928fb8107201dad9f5aea7f9132@198.244.200.3:26656,406fc7fe86ba396cb7fc8616c546f21a1d3c51cd@89.58.57.158:26656,5ab6437f73fe71f392d53566e037aa91087530ac@139.144.67.202:26656,370bf5f5b9ce655403d05753c355798288c1f120@89.245.24.81:23356,942c99cb9ff717552f884639dda9f52ab66f9726@65.108.134.12:26656,d29bed885306037dbe219278415025a2ea8880a4@51.159.160.140:26656,46b7ae20e3cc4264076a91c3601f3894a021a80d@65.108.6.45:36656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.teritorid/config/config.toml
```
