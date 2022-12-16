# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/teritori.png" width="150" alt=""><figcaption></figcaption></figure>

Teritori is a multi-chain hub designed to allow IBC and non IBC communities  to connect, trade services & NFTs, launch new projects & build further existing ones.

**Chain ID**: teritori-1 | **Latest Version Tag**: v1.3.0 | **Wasm**: ON

Website: [https://teritori.com](https://teritori.com)

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

**live-peers** (27)
```
peers="3bd3a20d7c8a26a20927289a7a6bffecf71de53e@51.81.155.97:10856,2b4f46e601fb4ede2a0c98976337e3afdaa50dac@65.108.238.102:15956,3594b73f909a9c4b87cfe6a361ef8b2b51124dd5@65.109.69.59:15956,6ef7a8bc7a3cc0856594f12570e8f2282a099dcf@65.109.93.152:26796,574479abf5b0ed001519c60042bd88a97ce80a48@18.236.38.205:26656,5a98d637a16b16bf425a4a785c9d11a7d1e5b8a0@65.21.131.215:26736,1e08fefb7e8851490d40e804df76d1ac33cb1f0a@38.146.3.175:15956,2f93424bd346b857bd5164eaac0b2bfd5fd644c0@144.91.127.252:26656,106490318e51355bc6d72e7941a0080f8b8256b9@185.16.39.14:26656,8e1e342208f400bb10677617d4f08b31a3b48877@138.201.61.159:26656,b336b83d9bab0b8cf96a3833efcbc196fab63fdd@212.95.51.215:36656,6fb98b9e316b2900fce2fd331621460a932f4d7d@65.108.15.183:51656,26175f13ada3d61c93bca342819fd5dc797bced0@65.109.58.226:28656,1ae3e0eafc14a3626a9cd43de867958526fd851a@176.9.98.24:30589,14fa46dbadd79647ebf3e5bc82326d2debc5fd52@51.159.176.185:26656,a191006e50d3af40fd253c23dae715a45fdd7415@95.179.217.1:26656,8ac41af54dfd91c41de71cde222a55670f2f405d@141.95.65.73:15956,b0dcd078a40b8bca35f0cf873951b27e5dd45793@188.217.162.92:26656,28456ac1dded17760432c3f1d759c7d50ab6ed3e@51.250.83.54:26656,51eaf493facf36754411baa4f7b89355bd9cb3e7@195.201.63.87:42666,29b92a4020171c20fe70e5d60f9c5d07dc9f31f7@194.163.161.146:26656,8480ce1f929a9410567d315a5b3fc2709c2807a7@93.115.25.106:51656,b906f0fdace24fb415254213644b51d4d6806d28@91.226.253.197:28756,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:19656,ed747c9e39fc04fdbc7ab5fc4a4a7f7a298ee329@65.144.145.234:26656,44b2bf9d970aece0531d3d939c5c546a7ac9201a@34.219.76.190:26656,46b7ae20e3cc4264076a91c3601f3894a021a80d@65.108.6.45:36656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.teritorid/config/config.toml
```
