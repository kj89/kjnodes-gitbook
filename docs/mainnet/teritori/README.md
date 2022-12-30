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

**live-peers** (22)
```
peers="d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:19656,d2247f7b919f0781c90ee61958d7044665a22d38@169.155.44.201:26656,0b27217386756577e1eadf00c4169dc8f041e522@51.210.7.219:26656,3178ac8fffd269325500c95679d58d5e8ec61746@198.244.213.94:22956,ff8f8c1b4cf70f38e1c370af05a40c1845022ae8@51.79.103.43:26656,4991cc04c48f96dec265464d5cf276e16f6b302c@188.217.162.92:26656,a7d96dc929824613315dcc1c90fee119f28cc51f@164.152.161.254:26656,a35dc0cd0efd7e04d3334d781112bae0698a8f57@164.92.131.1:26656,3594b73f909a9c4b87cfe6a361ef8b2b51124dd5@65.109.69.59:15956,82ebb17ddac20928fb8107201dad9f5aea7f9132@198.244.200.3:26656,26175f13ada3d61c93bca342819fd5dc797bced0@65.109.58.226:28656,2afdb9300c47e43e555fa572d033b2d68ac28506@65.109.70.68:26686,d956d6180e96c62315a777b1a3ed8f1ebf873e80@38.242.232.202:29656,51eaf493facf36754411baa4f7b89355bd9cb3e7@195.201.63.87:42666,808437b010f4663bf007b33433262d1495b0fbfe@35.90.134.158:28656,ed747c9e39fc04fdbc7ab5fc4a4a7f7a298ee329@65.144.145.234:26656,88a407d4749e1ccbb630f98ca44f304744d97864@38.242.141.168:26656,94b63fddfc78230f51aeb7ac34b9fb86bd042a77@176.9.98.24:30552,4740ad44e58f4f4a0e2b9c4353500009eb73a05a@176.191.97.120:26656,29b92a4020171c20fe70e5d60f9c5d07dc9f31f7@194.163.161.146:26656,46b7ae20e3cc4264076a91c3601f3894a021a80d@65.108.6.45:36656,ad347ea1ec920d12ccda2341348bcc89687739ef@88.99.164.158:38026"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.teritorid/config/config.toml
```
