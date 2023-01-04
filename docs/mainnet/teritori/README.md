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

**live-peers** (32)
```
peers="317d9a102d4a04337c65571c18df0e98269dce87@141.94.193.12:13656,406fc7fe86ba396cb7fc8616c546f21a1d3c51cd@89.58.57.158:26656,b336b83d9bab0b8cf96a3833efcbc196fab63fdd@212.95.51.215:36656,1e08fefb7e8851490d40e804df76d1ac33cb1f0a@38.146.3.175:15956,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:19656,26175f13ada3d61c93bca342819fd5dc797bced0@65.109.58.226:28656,942c99cb9ff717552f884639dda9f52ab66f9726@65.108.134.12:26656,8ac41af54dfd91c41de71cde222a55670f2f405d@141.95.65.73:15956,0b27217386756577e1eadf00c4169dc8f041e522@51.210.7.219:26656,5a98d637a16b16bf425a4a785c9d11a7d1e5b8a0@65.21.131.215:26736,bbc594f0a8424368b869fef47a18d6e35965db2e@176.9.188.21:53656,d856120f262134ebf13e1d2632d778b69e704208@65.108.4.188:15956,24b28cf013e6d7b5b88b6dba2701c5ddd2dd5ee1@65.109.58.225:28656,d2247f7b919f0781c90ee61958d7044665a22d38@169.155.44.201:26656,6ef7a8bc7a3cc0856594f12570e8f2282a099dcf@65.109.93.152:26796,a25a3a218a699e71e2a64edaa45f457dfd8507ba@65.21.148.206:26656,787a6b318ebc4167fefb1d5ef9f88af6cb5a8b29@173.212.222.167:35656,97838a0c8a5035398f696dd29f28fe66b20b6a8d@46.4.81.204:44656,89757803f40da51678451735445ad40d5b15e059@134.65.192.221:26656,526d8c7c44f59be9a39d7463c576b68c0db23174@65.108.234.23:15956,a7d96dc929824613315dcc1c90fee119f28cc51f@164.152.161.254:26656,51eaf493facf36754411baa4f7b89355bd9cb3e7@195.201.63.87:42666,fefd8ffb33a5d6ae194f082a39c4bb713da3a06b@167.86.86.197:36656,e8cafb5a121c9fe322e554f5a7f489b2d25abd4c@51.159.153.113:26656,b78dd48a9d34146f04801f479a82348a19a69ab7@51.159.185.141:26656,3594b73f909a9c4b87cfe6a361ef8b2b51124dd5@65.109.69.59:15956,4991cc04c48f96dec265464d5cf276e16f6b302c@188.217.162.92:26656,eac081c2d27e17b49ac988bca5ff1366b4507638@185.163.64.143:26656,ad347ea1ec920d12ccda2341348bcc89687739ef@88.99.164.158:38026,46b7ae20e3cc4264076a91c3601f3894a021a80d@65.108.6.45:36656,703714c82c94fc1c74b6ee0d1fc3417b932be5f3@169.155.168.57:26656,20e1000e88125698264454a884812746c2eb4807@65.108.227.217:15956"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.teritorid/config/config.toml
```
